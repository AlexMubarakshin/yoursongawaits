# Черновой расчёт COGS на заказ из сессии 2026-11-05 (до решений 05: Stripe, ElevenLabs, Suno).
# Справочный. Канонический расчёт: models/unit_economics.py.

llm=0.025
att=1.5
paid_regen=0.3
extras=0.01+0.005+0.002  # cover, storage/cdn, email
pay_stripe=0.6*(0.029*35+0.30)+0.4*(0.054*35+0.30)+0.005*35  # blended + Stripe Tax
pay_paddle=0.05*35+0.50
disp=0.005*15
sc={
 'A1 ACE-Step self-host (serverless L40S)':0.01,
 'A2 ACE-Step on fal':0.072,
 'A3 MiniMax 2.0 on fal':0.06,
 'L Lyria 3.5':0.16,
 'S Suno reseller (Apiframe)':0.11,
 'E ElevenLabs full 2x3min':0.90,
 'Ef ElevenLabs via fal':3.60,
}
print('stripe blended',round(pay_stripe,2),'paddle',pay_paddle)
for n,m in sc.items():
  a=m+llm
  for c in (0.05,0.10,0.20):
    gen=att*a/c + paid_regen*a + extras
    print(f"{n:45s} c={c:.0%} attempt={a:.3f} gen/paid={gen:.2f} +stripe={gen+pay_stripe+disp:.2f} +paddle={gen+pay_paddle+disp:.2f}")
# ElevenLabs preview-first: 2x45s previews = 0.225; payer gets full chosen 3min 0.45 (+second 0.45 optional)
pv=0.225+llm
for c in (0.05,0.10,0.20):
  gen=att*pv/c + 0.45 + paid_regen*pv + extras
  print(f"E' preview-first c={c:.0%} gen/paid={gen:.2f} +stripe={gen+pay_stripe+disp:.2f}")
