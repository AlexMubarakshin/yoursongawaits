"""Unit-economics model for the AI song-gift service (canonical, 2026-11-05).

Inputs: appendix/economics-demand.md §8 (funnel, CAC, AOV), appendix/economics-costs.md §b (generation cost),
Polar fees (polar.sh/docs/merchant-of-record/fees, Starter plan, checked 2026-11-05), decisions in 05-decisions.md.
Q18 block (2026-11-06, bottom of file): group gift, subscription, RU contour for MVP scope v0.2 (06-prd).
Run: python3 models/unit_economics.py
"""

# --- Scenarios (paid-acquisition scale; NOT the launch plan, see PLAN_05 below) ---
SC = {
    'bear': dict(aov_gross=27.0, refunds=.08, conv=.12, orders24=1.10, cac=95, k=.01, aff_share=.05, aff_comm=.20, orders_y2=16000),
    'base': dict(aov_gross=35.5, refunds=.04, conv=.15, orders24=1.25, cac=30, k=.06, aff_share=.10, aff_comm=.15, orders_y2=55000),
    'bull': dict(aov_gross=52.0, refunds=.02, conv=.20, orders24=1.45, cac=8,  k=.25, aff_share=.20, aff_comm=.10, orders_y2=115000),
}
# AOV base $35.5 = base song $29 + ~25% of buyers take the $49-59 bundle.
# Bear $27 / bull $52 assume base price $24 / $39 and bundle take 15% / ~43% (price-sensitivity scenarios; decision D2 = $29).

# --- Generation stacks: cost of one attempt = LLM lyrics ($0.025) + 2 tracks. Pay-per-use only (05-decisions). ---
STACK = {
    'A  ACE-Step 1.5, serverless GPU': 0.035,
    'A2 ACE-Step 1.5 on fal':          0.097,
    'A3 MiniMax 2.0 on fal':           0.085,
    'L  Google Lyria 3.5':             0.185,
}
ATTEMPTS_PER_PREVIEW_USER = 1.5   # avg attempts per user who reaches preview
REGEN_PER_PAID = 0.3              # extra attempts by payers
EXTRAS = 0.017                    # cover image, storage/CDN, email
REACTION_VIDEO = 0.05             # recipient reaction capture + storage + render (MVP feature), per paid order [E]
SUPPORT = 0.50                    # support time per order [E]

# --- Payments: Polar Starter (MoR): 5% + $0.50; +1.5% non-US cards; $15 per dispute; Stripe payout cross-border 1% ---
INTL_SHARE = 0.40                 # share of non-US cards (GB/CA/AU/EU)
DISPUTE_RATE = 0.005
def payment_fee(aov):
    return 0.05 * aov + 0.50 + 0.015 * INTL_SHARE * aov + DISPUTE_RATE * 15 + 0.01 * aov  # last term: payout cross-border


def cogs_per_paid(p, attempt):
    gen = ATTEMPTS_PER_PREVIEW_USER * attempt / p['conv'] + REGEN_PER_PAID * attempt
    aff = p['aff_share'] * p['aff_comm'] * p['aov_gross']
    return gen, gen + EXTRAS + REACTION_VIDEO + SUPPORT + payment_fee(p['aov_gross']) + aff


def fixed_month(orders_m):  # infra + tools (economics-costs.md §d), excl. legal/accounting
    if orders_m <= 100:
        return 75
    if orders_m <= 1000:
        return 75 + (orders_m - 100) / 900 * 75
    if orders_m <= 10000:
        return 150 + (orders_m - 1000) / 9000 * 2350
    return 2500 + (orders_m - 10000) / 40000 * 5500


def scenarios():
    print(f"{'scen':5}|{'stack':34}|{'netAOV':>7}|{'gen':>5}|{'COGS':>6}|{'CM1':>6}|{'CM1%':>5}|{'LTV24':>6}|{'CAC':>6}|{'LTV/CAC':>7}|{'Rev Y2':>10}|{'Profit Y2':>11}")
    for s, p in SC.items():
        for st, att in STACK.items():
            net = p['aov_gross'] * (1 - p['refunds'])
            gen, cogs = cogs_per_paid(p, att)
            cm1 = net - cogs
            ltv = cm1 * p['orders24']
            cac = p['cac'] / (1 + p['k'])
            cust_y = p['orders_y2'] / p['orders24']
            profit_y = p['orders_y2'] * cm1 - cust_y * cac - fixed_month(p['orders_y2'] / 12) * 12
            print(f"{s:5}|{st:34}|{net:7.2f}|{gen:5.2f}|{cogs:6.2f}|{cm1:6.2f}|{cm1/net:5.0%}|{ltv:6.2f}|{cac:6.2f}|{ltv/cac:7.2f}|{p['orders_y2']*net:10,.0f}|{profit_y:11,.0f}")


def sensitivity():
    p = SC['base']; att = STACK['A  ACE-Step 1.5, serverless GPU']
    print('\nBase / stack A: preview->pay conversion vs CAC (Meta CPC $1.13, visit->start 30%, start->preview 60%)')
    for conv in (.08, .10, .12, .15, .20):
        q = dict(p, conv=conv)
        net = p['aov_gross'] * (1 - p['refunds']); _, cogs = cogs_per_paid(q, att)
        ltv = (net - cogs) * p['orders24']
        cac_meta = 1.13 / (.30 * .60 * conv)
        print(f"  conv {conv:.0%}: LTV24 ${ltv:.1f} | paid Meta CAC ${cac_meta:.0f} | blended (30% free, k=0.06) ${cac_meta*.7/1.06:.0f}")
    print('\nBase / stack A: AOV sensitivity (conv 15%)')
    for aov in (24, 29, 35.5, 45, 59):
        q = dict(p, aov_gross=aov)
        net = aov * (1 - p['refunds']); _, cogs = cogs_per_paid(q, att)
        print(f"  AOV ${aov}: CM1 ${net-cogs:.1f}, LTV24 ${(net-cogs)*p['orders24']:.1f}")


def plan_05():
    """Launch plan from 05-decisions: $300 one-off test, organic growth, goal >= $300/month net (before personal tax)."""
    p = SC['base']; att = STACK['A  ACE-Step 1.5, serverless GPU']
    net = p['aov_gross'] * (1 - p['refunds']); _, cogs = cogs_per_paid(p, att)
    cm1 = net - cogs
    fixed = fixed_month(15) + 10  # infra + domain/email tools; legal/accounting see 05-decisions
    need = (300 + fixed) / cm1
    print(f"\nPLAN 05: CM1/order ${cm1:.2f}, fixed ${fixed:.0f}/mo -> orders/month for $300 net: {need:.1f}")
    print(f"  visits/month needed at visit->pay 2.7%: {need/0.027:.0f}")
    test_visits = 300 / 1.13
    print(f"  $300 Meta test: ~{test_visits:.0f} visits -> ~{test_visits*.30:.0f} starts -> ~{test_visits*.30*.60:.0f} previews -> ~{test_visits*.30*.60*.15:.1f} paid orders")


# =====================================================================================================
# Q18 (2026-11-06): MVP scope v0.2 — group gift, subscription "Календарь поводов", RU contour.
# Prices: 06-prd P1 ($55 bundle), P13 (EN subscriptions), P14 (RU), P17 (group gift).
# Everything below is [E] unless a source is named. Canonical EN numbers above are unchanged.
# =====================================================================================================
BASE = SC['base']
ATT_A = STACK['A  ACE-Step 1.5, serverless GPU']
EN_BASE_PRICE, EN_BUNDLE_PRICE = 29.0, 55.0
EN_FIXED = fixed_month(15) + 10            # $85, as in plan_05
TARGET = 300.0
VISIT_TO_PAY = 0.027


def aov_mix(base, bundle, take):
    return base * (1 - take) + bundle * take   # 29/55 at 25% -> 35.5 = canonical base AOV


def en_cm1(aov, att=ATT_A):
    q = dict(BASE, aov_gross=aov)
    net = aov * (1 - BASE['refunds']); _, cogs = cogs_per_paid(q, att)
    return net - cogs


# --- Group gift (organizer pays, same prices as solo, P17) ---
GROUP = {   # share of paid orders | bundle take | participants besides organizer | participant -> buyer within 12 mo
    'bear': dict(share=.05, bundle=.30, participants=3,  p_conv=.01),
    'base': dict(share=.10, bundle=.40, participants=6,  p_conv=.03),
    'bull': dict(share=.20, bundle=.50, participants=10, p_conv=.06),
}
# economics-demand §5.2: 5-15 participants per group gift (Tribute, Kudoboard). Participants are invited by a friend,
# wrote a memory and saw the result, so their conversion is higher than a gift-page viewer's.
GROUP_EXTRA_COGS = 0.60   # longer lyrics prompt + moderation per contribution + photo storage + participant emails + extra support


def group():
    print('\nQ18 / GROUP GIFT (EN, stack A)')
    print(f"{'scen':5}|{'share':>6}|{'AOV grp':>8}|{'CM1 grp':>8}|{'CM1 avg':>8}|{'k grp':>6}|{'k blend':>8}")
    out = {}
    for s, g in GROUP.items():
        k_single = SC[s]['k']
        aov_g = aov_mix(EN_BASE_PRICE, EN_BUNDLE_PRICE, g['bundle'])
        cm_g = en_cm1(aov_g) - GROUP_EXTRA_COGS
        cm_solo = en_cm1(BASE['aov_gross'])
        cm_avg = (1 - g['share']) * cm_solo + g['share'] * cm_g
        k_g = k_single + g['participants'] * g['p_conv']
        k_b = (1 - g['share']) * k_single + g['share'] * k_g
        out[s] = dict(cm_avg=cm_avg, k=k_b)
        print(f"{s:5}|{g['share']:6.0%}|{aov_g:8.2f}|{cm_g:8.2f}|{cm_avg:8.2f}|{k_g:6.2f}|{k_b:8.3f}")
    return out


# --- Subscription "Календарь поводов" ---
SONG_COGS_SUB = 1.8 * ATT_A + EXTRAS + REACTION_VIDEO + SUPPORT   # a credit song: no unpaid-preview overhead
SUB_EN = dict(
    annual=dict(price=59.0, credits=4),
    monthly=dict(price=9.99, months_per_credit=1),   # P13 as written: a credit at every renewal
)
SUB_BEHAVIOUR = dict(            # base [E]
    take=.03,                    # payers who subscribe (economics-demand §5.1: 1/3/5%)
    annual_share=.6,
    annual_used=2.2,             # credits used of 4 within 12 months (breakage ~45%)
    monthly_churn=.12,           # per month -> ~6.5 paid months in the first year
    monthly_used_per_credit=.8,
    member_songs=.2,             # extra songs at member price per year
    would_buy=0.8,               # songs this person would have bought at base price anyway in 12 months
    bundle_take=.25,
)


def cheapest_one_song(base, annual, monthly, member, months_per_credit):
    """Cheapest way for a non-subscriber to get exactly one song (gift date known 1-3 months ahead)."""
    paths = {'base': base, 'annual': annual, 'monthly + member price': monthly + member,
             f'monthly x{months_per_credit} for 1 credit': monthly * (months_per_credit + (1 if months_per_credit == 1 else 0))}
    # P13/P14: "first credit at the first renewal" -> with 1 month/credit you pay 2 months; with N>1 you pay N months
    return paths


def sub_value(months_per_credit, fee=payment_fee, cm_repeat=None, song_cogs=SONG_COGS_SUB,
              plan=SUB_EN, member=19.0, bundle_diff=EN_BUNDLE_PRICE - EN_BASE_PRICE, refunds=.04):
    """12-month contribution of one subscriber vs the counterfactual (buys `would_buy` songs at base, CM1 each)."""
    b = SUB_BEHAVIOUR
    cm_repeat = cm_repeat if cm_repeat is not None else en_cm1(BASE['aov_gross'])
    upgrade = b['bundle_take'] * (bundle_diff - fee(bundle_diff))           # bundle surcharge on credit songs
    member_cm = b['member_songs'] * ((member + b['bundle_take'] * bundle_diff) * (1 - refunds) - fee(member) - song_cogs)
    a = plan['annual']
    annual = a['price'] * (1 - refunds) - fee(a['price']) - b['annual_used'] * (song_cogs - upgrade) + member_cm
    months = sum((1 - b['monthly_churn']) ** m for m in range(12))
    m = plan['monthly']
    credits = max(0, (months - (1 if months_per_credit == 1 else 0))) / months_per_credit
    used = credits * b['monthly_used_per_credit']
    monthly = months * (m['price'] * (1 - refunds) - fee(m['price'])) - used * (song_cogs - upgrade) + member_cm
    counter = b['would_buy'] * cm_repeat
    blend = b['annual_share'] * annual + (1 - b['annual_share']) * monthly
    return dict(annual=annual, monthly=monthly, months=months, used_monthly=used, counter=counter,
                inc=blend - counter, inc_annual=annual - counter, inc_monthly=monthly - counter)


def subscription():
    print('\nQ18 / SUBSCRIPTION (EN, P13)')
    for mpc in (1, 3):
        paths = cheapest_one_song(EN_BASE_PRICE, 59, 9.99, 19, mpc)
        print(f"  monthly credit every {mpc} paid month(s): cheapest single song -> " +
              ', '.join(f"{k} ${v:.2f}" for k, v in paths.items()))
    print(f"  Polar fee per charge: monthly $9.99 -> ${payment_fee(9.99):.2f} ({payment_fee(9.99)/9.99:.0%}); "
          f"annual $59 -> ${payment_fee(59):.2f} ({payment_fee(59)/59:.0%})")
    print(f"  credit song COGS ${SONG_COGS_SUB:.2f}")
    for mpc in (1, 3):
        v = sub_value(mpc)
        print(f"  [{mpc} mo/credit] 12-mo CM per subscriber: annual ${v['annual']:.1f}, monthly ${v['monthly']:.1f} "
              f"({v['months']:.1f} paid months, {v['used_monthly']:.1f} credits used); counterfactual ${v['counter']:.1f} "
              f"-> incremental annual ${v['inc_annual']:+.1f}, monthly ${v['inc_monthly']:+.1f}, blended ${v['inc']:+.1f}")
    v = sub_value(3)
    for take in (.01, .03, .05):
        per_month = 13 * take * v['inc']
        print(f"  take {take:.0%} of 13 orders/mo -> {13*take:.2f} new subscribers/mo -> steady-state +${per_month:.1f}/mo to the $300 goal")
    # worst case: heavy gifters who would have bought all their songs anyway
    w = SUB_BEHAVIOUR['would_buy']
    for wb in (2.0, 3.0):
        SUB_BEHAVIOUR['would_buy'] = wb
        v = sub_value(3)
        print(f"  cannibalisation: subscriber would have bought {wb:.0f} songs/yr anyway -> incremental ${v['inc']:+.1f}/yr")
    SUB_BEHAVIOUR['would_buy'] = w


# --- RU contour (D7, P14) ---
FX = 80.5   # RUB per USD, ЦБ РФ 02.11.2026 (80.5573) [S]
RU = dict(base=790, bundle=1490, bundle_take=.25, refunds=.04, conv=.15,
          card_share=.5, card_fee=.038, sbp_fee=.007, vat_on_fee=.22,   # economics-costs §c; VAT 22% on acquiring fee from 2026
          llm_attempt=3.2,   # YandexGPT 5.1 Pro ~0.80 ₽/1k tokens [S] x ~4k tokens (lyrics + moderation) [E]
          extras=5, support=40)
RU_GPU = {   # ₽ per attempt (2 tracks ~3 min) and fixed ₽/month
    'R1 serverless GPU (Cloud.ru ML Inference, scale-to-zero) [S/E]': dict(gpu_attempt=11, fixed=0),
    'R2 dedicated RTX 4090-class GPU ~30k ₽/mo [S/E]':                  dict(gpu_attempt=0,  fixed=30000),
}
RU_FIXED = dict(infra_rf=3500, email=500, cloud_kassa_ofd=1500, bank=500, domain=50)   # ₽/month [E]
IP_CONTRIB_Y = 57390   # ИП fixed insurance contributions 2026 [S]; +1% of income over 300k ₽


def ru_fee(gross):
    r = RU
    return gross * (r['card_share'] * r['card_fee'] + (1 - r['card_share']) * r['sbp_fee']) * (1 + r['vat_on_fee'])


def ru_cm1(gpu):
    r = RU
    aov = aov_mix(r['base'], r['bundle'], r['bundle_take'])
    net = aov * (1 - r['refunds'])
    attempts = ATTEMPTS_PER_PREVIEW_USER / r['conv'] + REGEN_PER_PAID
    gen = attempts * (gpu['gpu_attempt'] + r['llm_attempt'])
    cm = net - ru_fee(aov) - gen - r['extras'] - r['support']
    return aov, net, gen, cm


def ru_tax_month(net_month):
    """ИП on УСН 'доходы' without employees: 6% tax is reduced by all contributions -> total = max(contrib, 6% income)."""
    inc_y = net_month * 12
    contrib = IP_CONTRIB_Y + 0.01 * max(0, inc_y - 300000)
    return max(contrib, 0.06 * inc_y) / 12


def ru_profit(n, gpu):
    aov, net, gen, cm = ru_cm1(gpu)
    fixed = sum(RU_FIXED.values()) + gpu['fixed']
    return n * cm - fixed - ru_tax_month(n * net)


def ru():
    global IP_CONTRIB_Y
    print(f"\nQ18 / RU CONTOUR (FX {FX} ₽/$; fixed w/o GPU {sum(RU_FIXED.values())} ₽/mo; ИП contributions {IP_CONTRIB_Y} ₽/yr)")
    print(f"  payment fee {ru_fee(1):.2%} of gross (50% card 3.8% / 50% СБП 0.7%, +VAT 22% on fee)")
    for name, gpu in RU_GPU.items():
        aov, net, gen, cm = ru_cm1(gpu)
        be = next(n for n in range(0, 2000) if ru_profit(n, gpu) >= 0)
        tgt = next(n for n in range(0, 5000) if ru_profit(n, gpu) >= TARGET * FX)
        print(f"  {name}\n    AOV {aov:.0f} ₽ (${aov/FX:.2f}), net {net:.0f} ₽, gen/order {gen:.0f} ₽, CM1 {cm:.0f} ₽ (${cm/FX:.2f}) before tax"
              f"\n    break-even {be} orders/mo (~{be/VISIT_TO_PAY:.0f} visits); $300 from RU alone: {tgt} orders/mo (~{tgt/VISIT_TO_PAY:.0f} visits)")
        print('    orders/mo -> profit ₽ (USD): ' + ', '.join(f"{n}: {ru_profit(n, gpu):,.0f} (${ru_profit(n, gpu)/FX:,.0f})" for n in (0, 10, 20, 40, 80)))
    print('  Stars (bot) instead of ЮKassa would leave ~380 ₽ of 790 (facts §8) -> not used (D15)')
    gpu = RU_GPU['R1 serverless GPU (Cloud.ru ML Inference, scale-to-zero) [S/E]']
    print('  R1 sensitivity (break-even orders/mo | orders for $300 from RU alone):')
    for label, base, bundle, contrib in (('P14 prices, ИП only for RU', 790, 1490, 57390),
                                         ('P14 prices, ИП exists anyway (contrib. not incremental)', 790, 1490, 0),
                                         ('base 590 / bundle 1190', 590, 1190, 57390),
                                         ('base 990 / bundle 1790', 990, 1790, 57390)):
        RU['base'], RU['bundle'], IP_CONTRIB_Y = base, bundle, contrib
        be = next(n for n in range(0, 2000) if ru_profit(n, gpu) >= 0)
        tgt = next(n for n in range(0, 5000) if ru_profit(n, gpu) >= TARGET * FX)
        print(f"    {label:58}: CM1 {ru_cm1(gpu)[3]:4.0f} ₽ | {be:3} | {tgt:3}")
    RU['base'], RU['bundle'], IP_CONTRIB_Y = 790, 1490, 57390


# --- Combined: what the $300/month goal needs with the MVP v0.2 scope (base) ---
def plan_q18(grp):
    cm_solo = en_cm1(BASE['aov_gross'])
    v = sub_value(3)
    sub_per_order = SUB_BEHAVIOUR['take'] * v['inc']
    print('\nQ18 / PLAN: orders and visits per month for $300 net (base)')
    rows = [('EN only (canonical, plan_05)', cm_solo, SC['base']['k']),
            ('EN + group gift', grp['base']['cm_avg'], grp['base']['k']),
            ('EN + group gift + subscription', grp['base']['cm_avg'] + sub_per_order, grp['base']['k'])]
    for name, cm, k in rows:
        n = (TARGET + EN_FIXED) / cm
        ext = n / (1 + k)
        print(f"  {name:34}: CM/order ${cm:5.2f} -> {n:4.1f} orders, {n/VISIT_TO_PAY:4.0f} visits; "
              f"of them via gift pages/participants {n-ext:.1f} orders -> {ext/VISIT_TO_PAY:4.0f} external visits")
    gpu = RU_GPU['R1 serverless GPU (Cloud.ru ML Inference, scale-to-zero) [S/E]']
    cm = grp['base']['cm_avg'] + sub_per_order
    print('  + RU contour (R1): RU orders/mo -> RU profit -> EN orders needed for $300 total')
    for n_ru in (0, 10, 20, 30, 50, 80):
        p = ru_profit(n_ru, gpu) / FX
        n_en = max(0, (TARGET + EN_FIXED - p) / cm)
        print(f"    RU {n_ru:3}: RU {p:+7.0f}$ -> EN {n_en:4.1f} orders (~{n_en/VISIT_TO_PAY:4.0f} visits)")


if __name__ == '__main__':
    scenarios(); sensitivity(); plan_05()
    g = group(); subscription(); ru(); plan_q18(g)
