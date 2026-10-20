# Laedt das 08-Modell (94 Pruefungen) und gibt die Kennzahlen der Variante OHNE Kelterei aus
import os
NS={}
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'model08.py')).read()
exec(compile(src,'model08','exec'),NS)
g=NS
r=lambda x,n=1: round(x,n)
if __name__=='__main__':
    print("Checks bestanden:", len(g['CHECKS']))
    KZ=g['KZ_OHNE']; KB=g['KB_OHNE']; END=g['END_OHNE']; CF=g['CF_OHNE']
    for k in ['umsatz','ebitda','afa','ebit','zins','ebt','gewst','erg']: print('KZ_ohne',k,r(KZ[k]))
    print('Bilanz 01.01 ohne: BS',r(KB['bilsum']),'EK',r(KB['ek']),'EKQ',r(KB['ekq']*100,2),'EKQ netto',r(KB['ekq_netto']*100,2),'ND',r(KB['netdebt']),'ND/EBITDA',r(KB['netdebt']/KZ['ebitda'],3),'KK',r(KB['kk']),'Bank',r(KB['bank']))
    print('Plan 31.12 ohne: BS',r(END['bilsum']),'EK',r(END['ek']),'EKQ',r(END['ekq']*100,2),'EKQ netto',r(END['ekq_netto']*100,2),'ND',r(END['netdebt']),'ND/EBITDA',r(END['netdebt']/KZ['ebitda'],3),'KK',r(END['kk']))
    print('CF ohne', {k:r(v) for k,v in CF.items()})
    print('KDF ohne', r(g['kdf'](KZ,g['P']['ohne']['tilg']),3), 'Tilg', g['P']['ohne']['tilg'], 'Entn', r(g['P']['ohne']['entn'],2))
    print('Float ohne K: PF_ABF+PF_KELT-PF_KUNDEN-180 =', r(g['PF_ABF']+g['PF_KELT']-g['PF_KUNDEN']-g['VERB_PFAND']))
    print('Ueberhang', r(g['LEER_UEBERHANG'],2))
    M=g['M']
    for k,m in M.items(): print(k,{x:r(m[x],2) for x in ['umsatz','einstand','vp','reI','invdiff','pers','sach','umlage','afa','ebit','vzae']})
    print('MS', {x:r(g['MS'][x],2) for x in ['umsatz','einstand','vp','reI','ebit','pers','sach']})
    print('KG_EBIT',r(g['KG_EBIT']),'UMLAGE_K',g['UMLAGE_ERL_K'])
    print('Rates WE',r(g['R_WE'],4),'KOMM',r(g['R_KOMM'],4),'LEER_BR',r(g['R_LEER_BR'],4),'LEER',r(g['R_LEER'],4),'SATTEL',r(g['R_SATTEL'],4),'TOURTAG',r(g['R_TOURTAG'],2),'STOPP_A',r(g['R_STOPP_A'],2),'AUFTR',r(g['R_AUFTR'],3),'BESUCH',r(g['R_BESUCH'],2),'MBW',r(g['MBW'],1))
    print('LKW_TAG',r(g['R_LKW_TAG'],2),'FAHRER_TAG',r(g['R_FAHRER_TAG'],2),'TOURTAGE',r(g['TOURTAGE'],1),'Leerkosten',r(g['LEERKOSTEN_LKW'],1))
    for k,d in g['KDB'].items(): print(k,{x:r(v,1) for x,v in d.items()})
    for x,d in g['SD'].items(): print('SEG',x,r(d['umsatz']),r(d['dbII']),r(d['dbIII']),r(d['dbIII']/d['umsatz']*100,1))
    for nm,v in g['VPV'].items(): print(nm,[ (k,r(v[k][1]),r(v[k][2]),r(v[k][3])) for k in v], 'sum', r(sum(v[k][3] for k in v)), 'Maerkte',r(sum(v[k][1] for k in v)))
    for k,s in g['SCHL'].items(): print('Schliessung',k,r(s['wirkung']), 'bei 100%', r(s['wirkung']+s['log'],1))
    print('ILOG', {k:r(g['ILOG'][k]['summe'],1) for k in M}, r(g['ILOG_SUM'],1))
    print('Fuhrpark',r(g['FUHRPARK'],1),'Liter',r(g['LITER']),'Maut',r(g['MAUT'],1),'CO2',r(g['CO2_T']))
    print('NV',r(g['NV'],1),'Sortierverg',r(g['SORTIERVERG'],1),'Kaesten',g['KAESTEN_SUM'])
    print('ZG_M',r(g['ZG_M'],2),'IC_WARE_M',r(g['IC_WARE_M'],1),'PF_MAERKTE',r(g['PF_MAERKTE'],1),'EAV26_M',r(g['EAV26_M'],1))
    print('Konzern VZAE ohne K', r(g['KG_VZAE']+g['MS']['vzae'],1))
    print('GewSt ohne', r(g['Ro']['gst_ohne'],2), 'ge', r(g['Ro']['ge_ohne'],2))
