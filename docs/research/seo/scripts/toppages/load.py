import csv,glob,os,re
S=os.path.dirname(os.path.abspath(__file__))
def num(x):
    try: return float(x) if x not in ('',None) else 0.0
    except: return 0.0
def load():
    D={}
    for f in sorted(glob.glob(S+'/csv/*.csv')):
        dom=os.path.basename(f).split('-top-pages')[0]
        rows=list(csv.DictReader(open(f,encoding='utf-8'),delimiter='\t'))
        for r in rows:
            for k in list(r):
                if k.startswith('AI responses') or k in('UR','Previous traffic','Current traffic','Traffic change','Previous traffic value','Current traffic value','Traffic value change','Current referring domains','Previous # of keywords','Current # of keywords','Previous top keyword: Volume','Current top keyword: Volume','Previous top keyword: Position','Current top keyword: Position'):
                    r[k+'#']=num(r[k])
        D[dom]=rows
    return D
