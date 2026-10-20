# Startbetrieb "Getraenkegruppe" – Plan 2027. Werte in T€, sofern nicht anders angegeben. Alle Werte sind Annahmen.
import datetime as dt
from collections import OrderedDict as OD
CHECKS=[]
def chk(name, cond, detail=""):
    CHECKS.append((name, bool(cond), detail))
    if not cond: raise AssertionError(f"{name}: {detail}")
def eq(a,b,tol=0.01): return abs(a-b)<=tol
# ---------- 1 Kalender ----------
HOL=[dt.date(2027,m,d) for m,d in [(1,1),(3,26),(3,29),(5,1),(5,6),(5,17),(5,27),(10,3),(11,1),(12,25),(12,26)]]
d=dt.date(2027,1,1); LIEFERTAGE=0; OEFFTAGE=0
while d.year==2027:
    if d.weekday()<5 and d not in HOL: LIEFERTAGE+=1
    if d.weekday()<6 and d not in HOL: OEFFTAGE+=1
    d+=dt.timedelta(1)
chk("Liefertage NRW 2027 (Mo–Fr ohne Feiertage) = 254", LIEFERTAGE==254, LIEFERTAGE)
chk("Öffnungstage NRW 2027 (Mo–Sa ohne Feiertage) = 304 (06 F1)", OEFFTAGE==304, OEFFTAGE)
LKW_TAGE=250; FAHRER_TAGE=210; DIESEL=2.00
# ---------- 2 Fuhrpark ----------
FZ=OD([("18-t-Lkw (Verteilung)",(9,2300,30000,28,0.50,0.25,11.0)),("7,5-t-Lkw (Innenstadt)",(1,1300,22000,18,0.50,0.177,6.5)),
       ("Sattelzug (Abholung, Leergut)",(1,3200,70000,31,0.85,0.348,16.0)),("Transporter < 3,5 t (Objekt, Heimdienst, Feste)",(4,650,25000,10,0.0,0.0,3.3))])
fz=OD()
for k,(n,leas,km,l100,ma,ms,so) in FZ.items():
    liter=km*l100/100; e=dict(n=n,leas_m=leas,km=km,l100=l100,mant=ma,msatz=ms,leasing=leas*12/1000,diesel=liter*DIESEL/1000,maut=km*ma*ms/1000,sonst=so,liter=liter)
    e['summe']=e['leasing']+e['diesel']+e['maut']+e['sonst']; fz[k]=e
FUHRPARK=sum(e['summe']*e['n'] for e in fz.values()); LITER=sum(e['liter']*e['n'] for e in fz.values())
MAUT=sum(e['maut']*e['n'] for e in fz.values()); LEASING_FZ=sum(e['leasing']*e['n'] for e in fz.values())
LKW_JAHR=fz["18-t-Lkw (Verteilung)"]['summe']; LKW75=fz["7,5-t-Lkw (Innenstadt)"]['summe']
SATTEL=fz["Sattelzug (Abholung, Leergut)"]['summe']; TRANSP=fz["Transporter < 3,5 t (Objekt, Heimdienst, Feste)"]['summe']
CO2_T=LITER*2.65/1000
# ---------- 3 KG-Segmente ----------
SEG=OD([
 ('A',dict(name='Gastronomie',ware=9500.0,neben=0.0,req=0.33,kunden=600,auftr=27000,kolli=526500,kgew=1.0,spt=17,dso=25,kund_txt='600 (60 A, 200 B, 340 C)')),
 ('B',dict(name='Wiederverkäufer',ware=3000.0,neben=0.0,req=0.15,kunden=150,auftr=3000,kolli=250000,kgew=0.6,spt=6,dso=20,kund_txt='150 Fremdmärkte, Kioske, Tankstellen')),
 ('C',dict(name='Strecke (LEH, Großkunden)',ware=2500.0,neben=0.0,req=0.045,kunden=25,auftr=1500,kolli=0,kgew=0,spt=None,dso=30,kund_txt='25')),
 ('D',dict(name='Objekt/Heimdienst',ware=1440.0,neben=60.0,req=0.31,kunden=1200,auftr=21000,kolli=160000,kgew=1.0,spt=None,dso=21,kund_txt='300 Objekte + 900 Haushalte')),
 ('E',dict(name='Veranstaltungen',ware=800.0,neben=200.0,req=0.28,kunden=180,auftr=350,kolli=57000,kgew=1.0,spt=None,dso=14,kund_txt='≈ 180 Auftraggeber, 350 Feste')),
])
for s in SEG.values():
    s['umsatz']=s['ware']+s['neben']; s['reI']=s['ware']*s['req']+s['neben']; s['we']=s['ware']*(1-s['req'])
GASTRO=[("A-Kunden (Brauhaus, Hotel)",60,50.0,104,24),("B-Kunden (Restaurant, Kneipe)",200,20.0,52,12),("C-Kunden (Eckkneipe, Verein)",340,2500/340,30,2)]
G_UM=sum(n*u for _,n,u,_,_ in GASTRO); G_ST=sum(n*st for _,n,_,st,_ in GASTRO); BESUCHE=sum(n*b for _,n,_,_,b in GASTRO)
chk("Gastro-Kundenstruktur ergibt 9.500 T€", eq(G_UM,9500,0.01), G_UM)
chk("Gastro-Kundenstruktur ergibt ≈ 27.000 Stopps (±200)", abs(G_ST-27000)<=200, G_ST)
# ---------- 4 Maerkte ----------
EK_FAKTOR=0.94; VP_Z=0.03
M=OD([('M1',dict(name='Markt 1 (Referenzmarkt 02)',vk=900,flaeche=1350,umsatz=2150.0,bons=100000,re_ext=575.985/2150,oeff='Mo–Sa 8–20 (72 h)')),
      ('M2',dict(name='Markt 2',vk=600,flaeche=900,umsatz=1350.0,bons=67500,re_ext=0.275,oeff='Mo–Fr 9–19, Sa 8–18 (60 h)')),
      ('M3',dict(name='Markt 3',vk=450,flaeche=700,umsatz=1000.0,bons=52600,re_ext=0.27,oeff='Mo–Fr 9–19, Sa 9–16 (57 h)'))])
def lohn_std(std,satz,sonder,f=1.245): return (std*52*satz+sonder)*f/1000
MJ=lambda n:(f"{n} Minijobber à 600 €", n*600/14.60*12/52/40, n*600*12*1.32/1000, n*600/14.60*12/52)
SA=lambda txt,brutto:(txt, brutto/14.8/52/40, brutto*1.10/1000, brutto/14.8/52)
ROSTER={
 'M1':[("Marktleitung (angestellt, statt Inhaber)",1.0,(3600*12+1200)*1.245/1000,40),("Stellv. Marktleitung",1.0,(3100*12+1000)*1.245/1000,40),
       ("Verkauf/Lager Vollzeit (2)",2.0,2*lohn_std(40,15.5,500),80),("Kasse Teilzeit 25 h",0.625,lohn_std(25,15.0,0),25),("Verkauf Teilzeit 20 h (neu, 06 F6)",0.5,lohn_std(20,15.0,0),20),
       ("Azubi 2. Lj. (50 % im Markt)",0.5,1100*12*1.22/1000,20),MJ(5),SA("Saison Mai–Aug (2), Faktor 1,10 (06 F16)",11500)],
 'M2':[("Marktleitung",1.0,(3300*12+1000)*1.245/1000,40),("Verkauf/Lager Vollzeit",1.0,lohn_std(40,15.5,500),40),("Kasse Teilzeit 25 h",0.625,lohn_std(25,15.0,0),25),
       ("Verkauf Teilzeit 20 h (2)",1.0,2*lohn_std(20,15.0,0),40),MJ(5),SA("Saison (1)",6000)],
 'M3':[("Marktleitung",1.0,(3100*12+1000)*1.245/1000,40),("Verkauf/Lager Vollzeit",1.0,lohn_std(40,15.5,500),40),("Kasse Teilzeit 25 h",0.625,lohn_std(25,15.0,0),25),
       MJ(5),SA("Saison (1)",6000)]}
BEDARF={'M1':[("Kasse 72 h + Zweitkasse Fr 4 / Sa 8",84),("Fläche/Leergut 72 h + Fr 6 / Sa 10",88),("Warenannahme/Verräumen",24),("Marktleitung Büro/Dispo",20),("Reinigung, MHD, Inventur",10)],
        'M2':[("Kasse 60 h + 6",66),("Fläche/Leergut 60 h + 6",66),("Warenannahme",12),("Marktleitung Büro",12),("Sonstiges",6)],
        'M3':[("Kasse 57 h + 4",61),("Fläche/Leergut",44),("Warenannahme",10),("Marktleitung Büro",10),("Sonstiges",5)]}
PROD=0.815
SACH_M={
 'M1':OD(Miete=1350*7.0*12/1000,Nebenkosten=1350*1.8*12/1000,Energie=26.6,Stapler=5.0,Marketing=18.0,IT_Kasse=7.0,Leergutautomaten=10.8,Kartengebühren=8.4,Versicherung=4.0,Entsorgung=4.2,Instandhaltung=6.0,Büro=1.0,Sonstiges=6.0,Pfanddifferenzen=3.0),
 'M2':OD(Miete=900*5.5*12/1000,Nebenkosten=900*1.7*12/1000,Energie=18.0,Stapler=4.0,Marketing=14.0,IT_Kasse=5.5,Leergutautomaten=7.2,Kartengebühren=5.3,Versicherung=3.0,Entsorgung=3.0,Instandhaltung=5.0,Büro=1.0,Sonstiges=4.0,Pfanddifferenzen=2.0),
 'M3':OD(Miete=700*5.0*12/1000,Nebenkosten=700*1.6*12/1000,Energie=14.0,Stapler=3.0,Marketing=10.0,IT_Kasse=4.5,Leergutautomaten=6.0,Kartengebühren=3.9,Versicherung=2.5,Entsorgung=2.5,Instandhaltung=4.0,Büro=1.0,Sonstiges=3.0,Pfanddifferenzen=1.5)}
AFA_M={'M1':24/6+96/6+20/72,'M2':14.0,'M3':10.0}
UMLAGE_Q=0.015; LIEF_WOCHE={'M1':3,'M2':2,'M3':2}; LEERGUT_M={'M1':160000,'M2':100000,'M3':75000}; EK_KOLLI=8.50/1000
for k,m in M.items():
    m['we_ext']=m['umsatz']*(1-m['re_ext']); m['einstand']=m['we_ext']*EK_FAKTOR; m['vp']=m['einstand']*(1+VP_Z)
    m['reI']=m['umsatz']-m['vp']; m['re_einst']=m['umsatz']-m['einstand']; m['invdiff']=0.005*m['umsatz']
    m['pers']=sum(r[2] for r in ROSTER[k]); m['vzae']=sum(r[1] for r in ROSTER[k]); m['std_bez']=sum(r[3] for r in ROSTER[k])
    m['bedarf']=sum(b for _,b in BEDARF[k]); m['std_prod']=m['std_bez']*PROD
    m['sach']=sum(SACH_M[k].values()); m['umlage']=UMLAGE_Q*m['umsatz']; m['afa']=AFA_M[k]
    m['ebitda']=m['reI']-m['invdiff']-m['pers']-m['sach']-m['umlage']; m['ebit']=m['ebitda']-m['afa']; m['ebt']=m['ebit']
    m['kolli']=m['we_ext']/EK_KOLLI; m['lief']=LIEF_WOCHE[k]*52; m['leergut']=LEERGUT_M[k]
    chk(f"{k}: produktive Personalstunden ≥ Bedarf je Woche", m['std_prod']>=m['bedarf'], (round(m['std_prod'],1),m['bedarf']))
MS={x:sum(m[x] for m in M.values()) for x in ['umsatz','we_ext','einstand','vp','reI','re_einst','invdiff','pers','vzae','sach','umlage','afa','ebitda','ebit','ebt','kolli','lief','leergut','bons','vk']}
# ---------- 5 Kelterei ----------
DICHTE=1.048
K=dict(obst_eigen=800,obst_lohn=400,ausbeute=0.72,obstpreis=150.0)
K['saft_eigen_l']=K['obst_eigen']*K['ausbeute']/DICHTE*1000; K['saft_lohn_l']=K['obst_lohn']*K['ausbeute']/DICHTE*1000
K['trester_t']=(K['obst_eigen']+K['obst_lohn'])*(1-K['ausbeute'])
GLAS1=350000; GLAS02=100000; BIB_E=K['saft_eigen_l']-GLAS1-GLAS02
K_ABSATZ=OD([('Glas 1,0 l',(280000,GLAS1-280000,0.88,0.90)),('Glas 0,2 l (Gastro)',(GLAS02,0,1.50,1.50)),('BiB 5 l (eigen)',(60000,BIB_E-60000,0.95,1.20))])
K_LOHN_PREIS=0.55; TRESTER_ERL=15.0; TRESTER_ABH=8.0
K['umsatz_int']=sum(a*pi for a,_,pi,_ in K_ABSATZ.values())/1000
K['umsatz_saft_ext']=sum(b*pe for _,b,_,pe in K_ABSATZ.values())/1000
K['umsatz_lohn']=K['saft_lohn_l']*K_LOHN_PREIS/1000; K['umsatz_trester']=K['trester_t']*TRESTER_ERL/1000
K['umsatz_ext']=K['umsatz_saft_ext']+K['umsatz_lohn']+K['umsatz_trester']; K['umsatz']=K['umsatz_int']+K['umsatz_ext']
FLASCHEN=GLAS1/1.0+GLAS02/0.2; BIB_E_ST=BIB_E/5; BIB_L_ST=K['saft_lohn_l']/5
EINZEL=OD([('Obst (800 t × 150 €/t)',K['obst_eigen']*K['obstpreis']/1000),('Verschlüsse, Etiketten (0,04 €/Fl.)',FLASCHEN*0.04/1000),('Glasersatz 2 % (0,30 €/Fl.)',FLASCHEN*0.02*0.30/1000),
           ('BiB-Beutel/Karton eigen (0,85 €/5 l)',BIB_E_ST*0.85/1000),('BiB-Beutel/Karton Lohnmost',BIB_L_ST*0.85/1000)])
KST=OD([('H1 Annahme/Waschen/Pressen',OD(Personal=46,Energie=6,Instandhaltung=5,Entsorgung=K['trester_t']*TRESTER_ABH/1000+6.0,AfA=25,Miete=10)),
        ('H2 Pasteurisieren/Tank/Lager',OD(Personal=32,Energie=16.8,Instandhaltung=5,Hilfsstoffe=12,Labor=8,AfA=28,Miete=12,Versicherung=6)),
        ('H3 Abfüllung Glas',OD(Personal=70,Energie=14,Instandhaltung=10,AfA=45,Miete=10)),
        ('H4 Abfüllung BiB',OD(Personal=34,Energie=4,Instandhaltung=2,AfA=6,Miete=4)),
        ('VV Verwaltung/Vertrieb/Hofladen',OD(Personal=18,Versicherung=2,Sonstiges=10,Umlage_KG=15))])
KST_SUM=OD((k,sum(v.values())) for k,v in KST.items())
K_KA=OD()
for v in KST.values():
    for a,b in v.items(): K_KA[a]=K_KA.get(a,0)+b
K_AFA=K_KA['AfA']; K_MIETE=K_KA['Miete']; K_PERS=K_KA['Personal']
K_MAT=sum(EINZEL.values())+K_KA['Hilfsstoffe']
K_SONST=sum(KST_SUM.values())-K_PERS-K_AFA-K_KA['Hilfsstoffe']
LITER_H12=K['saft_eigen_l']+K['saft_lohn_l']
R_H12=(KST_SUM['H1 Annahme/Waschen/Pressen']+KST_SUM['H2 Pasteurisieren/Tank/Lager']-K['umsatz_trester'])/LITER_H12*1000
OBST_L=EINZEL['Obst (800 t × 150 €/t)']/K['saft_eigen_l']*1000
AEZ=OD([('Glas 1,0 l',1.0),('Glas 0,2 l (Gastro)',2.5)]); AEZ_UNITS=GLAS1*1.0+GLAS02*2.5
R_H3=KST_SUM['H3 Abfüllung Glas']/AEZ_UNITS*1000
LITER_BIB=BIB_E+K['saft_lohn_l']; R_H4=KST_SUM['H4 Abfüllung BiB']/LITER_BIB*1000
PACK_FL=0.04+0.02*0.30
HK=OD([('Glas 1,0 l',OBST_L+R_H12+R_H3*1.0+PACK_FL/1.0),('Glas 0,2 l (Gastro)',OBST_L+R_H12+R_H3*2.5+PACK_FL/0.2),
       ('BiB 5 l (eigen)',OBST_L+R_H12+R_H4+0.85/5),('Lohnmost (BiB)',R_H12+R_H4+0.85/5)])
VOL=OD([('Glas 1,0 l',GLAS1),('Glas 0,2 l (Gastro)',GLAS02),('BiB 5 l (eigen)',BIB_E),('Lohnmost (BiB)',K['saft_lohn_l'])])
HK_TOTAL=sum(HK[p]*VOL[p] for p in HK)/1000
PROD_KOSTEN=sum(EINZEL.values())+sum(v for k,v in KST_SUM.items() if not k.startswith('VV'))-K['umsatz_trester']
chk("Kelterei: Σ Herstellkosten × Menge = Produktionskosten (ohne VV, Trester gutgeschrieben)", eq(HK_TOTAL,PROD_KOSTEN,0.01),(HK_TOTAL,PROD_KOSTEN))
K['ebitda']=K['umsatz']-K_MAT-K_PERS-K_SONST; K['ebit']=K['ebitda']-K_AFA
K_DARL=150.0; K_ZINS=(150+100)/2*0.045+250*0.08; K['ebt']=K['ebit']-K_ZINS; K_VZAE=4.5
chk("Kelterei-GuV: Kostenarten = Kostenstellen + Einzelkosten", eq(K_MAT+K_PERS+K_SONST+K_AFA,sum(EINZEL.values())+sum(KST_SUM.values())))
MSS=OD([('kalk. AfA (WBW 540 / 12 J.)',540/12),('kalk. Zins (6 % × AHK/2 = 240)',0.06*480/2),('Raum (Miete-Anteil)',10.0),('Instandhaltung',10.0),('Energie',14.0)]); MSS_H=1200
MSS_MASCH=sum(MSS.values())/MSS_H*1000; MSS_PERS=70.0/MSS_H*1000
H3_FIX=KST_SUM['H3 Abfüllung Glas']-14.0
BESCH_ABW=H3_FIX*(1-700/1200)
LOHN_VAR=0.85/5+ (6+16.8+4)/ (LITER_H12/1000) /1000*1000 if False else None
# Lohnmost: variable Kosten = BiB-Material + Energie anteilig + Saison-Personal anteilig (Annahme)
LOHN_KV=0.85/5+(6+16.8+4)/(LITER_H12/1000)/1000+26/LITER_H12  # €/l
LOHN_DB=K_LOHN_PREIS-LOHN_KV
MISS_OBST=280.0; MISS_EFFEKT=K['obst_eigen']*(MISS_OBST-K['obstpreis'])/1000
# Kelterei-Bezug der KG nach Zielsegment (T€, zu Kelterei-VP)
KB_SEG=OD(A=GLAS02*1.50/1000+55000*0.88/1000,B=24000*0.88/1000,D=33000*0.88/1000+20000*0.95/1000,E=6000*0.88/1000,F=162000*0.88/1000+40000*0.95/1000)
chk("Kelterei-Bezug nach Segmenten = interner Kelterei-Umsatz", eq(sum(KB_SEG.values()),K['umsatz_int'],1e-6),(sum(KB_SEG.values()),K['umsatz_int']))
chk("Kelterei: 1-l-Glas intern = Σ Segmentmengen", 55000+24000+33000+6000+162000==280000)
chk("Kelterei: BiB intern = Σ Segmentmengen", 20000+40000==60000)
# ---------- 6 Leergut ----------
PFAND_BR=OD(BK=3.10,WK=3.30,SK=2.40,Fass=30.0)
PFAND=OD((k,v/1.19) for k,v in PFAND_BR.items()); PFAND['Palette']=10.0
GEB=['BK','WK','SK','Fass','Palette']
GEBNAME={'BK':'Bierkasten 20 × 0,5 (3,10 €)','WK':'Wasser-/AfG-Kasten (3,30 €)','SK':'Saftkasten Kelterei (2,40 €)','Fass':'Fass 30/50 l (30 €)','Palette':'Palette (10 € netto)'}
BEST=OD([('Kunden extern (Kundenkonten)',OD(BK=90000,WK=60000,SK=12000,Fass=3600,Palette=2000)),
         ('KG-Lager Vollgut',OD(BK=35000,WK=25000,SK=4000,Fass=1500,Palette=2500)),
         ('KG-Lager Leergut (Silvester-Rückstau)',OD(BK=30000,WK=22000,SK=3000,Fass=800,Palette=1500)),
         ('Unterwegs / Gutschrift offen',OD(BK=8000,WK=4000,SK=1000,Fass=200,Palette=500)),
         ('Märkte Vollgut',OD(BK=9500,WK=6500,SK=1800,Fass=50,Palette=300)),
         ('Märkte Leergut',OD(BK=3200,WK=2000,SK=700,Fass=0,Palette=0))])
LEER_NORMAL=OD(BK=14000,WK=10000,SK=1000)
def W(ort,g): return BEST[ort][g]*PFAND[g]/1000
PF_ABF=sum(W(o,g) for o in BEST for g in GEB if g!='SK')
PF_KELT=sum(W(o,'SK') for o in BEST)
PF_KUNDEN=sum(W('Kunden extern (Kundenkonten)',g) for g in GEB)
PF_MAERKTE=sum(W(o,g) for o in ['Märkte Vollgut','Märkte Leergut'] for g in GEB)
LEER_UEBERHANG=sum((BEST['KG-Lager Leergut (Silvester-Rückstau)'][g]-LEER_NORMAL[g])*PFAND[g] for g in LEER_NORMAL)/1000
DURCH=OD([('A',OD(BK=220000,WK=150000,SK=30000,Fass=10400)),('B',OD(BK=120000,WK=75000,SK=4000,Fass=0)),('D',OD(BK=30000,WK=75000,SK=5500,Fass=0)),
          ('E',OD(BK=25000,WK=9000,SK=1000,Fass=600)),('F',OD(BK=170000,WK=138000,SK=27000,Fass=0))])
KAESTEN={s:sum(DURCH[s][g] for g in ['BK','WK','SK']) for s in DURCH}; KAESTEN_SUM=sum(KAESTEN.values())
chk("Leergut Segment F = Σ Rücknahme der Märkte", KAESTEN['F']==MS['leergut'],(KAESTEN['F'],MS['leergut']))
SK_SOLL=280000/6+GLAS02/4.8; SK_DURCH=sum(DURCH[s]['SK'] for s in DURCH)
chk("Saftkästen-Durchlauf = Kelterei-Glasabsatz an KG (6 × 1,0 l bzw. 24 × 0,2 l)", abs(SK_DURCH-SK_SOLL)<1,(SK_DURCH,SK_SOLL))
FREMD_Q=0.04; FREMD_NICHT=0.15
DIFF=OD([('Fremdleergut nicht rückführbar (4 % × 15 % × 2,70 €)',KAESTEN_SUM*FREMD_Q*FREMD_NICHT*2.70/1000),('Fehlflaschen, Bruch (0,3 % × 1,00 €)',KAESTEN_SUM*0.003*1.0/1000),
         ('Palettenschwund (1.200 × 10 €)',12.0),('Fässer verloren (30 × 25,21 €)',30*PFAND['Fass']/1000),('Zähl- und Erfassungsdifferenzen',15.0)])
LEERGUT_DIFF=sum(DIFF.values())
SORTIERVERG=0.09*KAESTEN_SUM/1000; ABHOLVERG=12000*5/1000; DEPOTVERG=40.0
PFAND_VOL=sum(DURCH[s][g]*PFAND[g] for s in DURCH for g in ['BK','WK','SK','Fass'])/1000
# ---------- 7 KG Personal, Sachkosten, AfA ----------
PERS_KG=[("Fahrer CE (Lkw, Sattelzug)",12.5,48.0),("Fahrer B (Transporter)",5.0,40.0),("Beifahrer Gastro",1.5,34.0),("Lager, Kommissionierung, Leergut",11.0,43.0),
 ("Innendienst/Disposition",5.0,45.0),("Außendienst Gastro",3.0,70.0),("Schanktechnik",1.5,55.0),("Veranstaltungsservice (Leitung)",1.0,42.0),("Saisonkräfte (Feste, Silvester)",1.0,40.0),
 ("Verwaltung (Buchhaltung 2,5, Lohn 1, IT 1)",4.5,50.0),("Controller",1.0,75.0),("Logistikleiter",1.0,95.0),("Geschäftsführer (Kommanditist)",1.0,140.0)]
KG_PERS=sum(v*c for _,v,c in PERS_KG); KG_VZAE=sum(v for _,v,_ in PERS_KG)
def pers(name): return [v*c for n,v,c in PERS_KG if n.startswith(name)][0]
GF_VERG=pers("Geschäftsführer")
FAHRT=OD(A=SEG['A']['auftr']/SEG['A']['spt'],B=SEG['B']['auftr']/SEG['B']['spt'],F=MS['lief']*0.5,E=100.0)
TOURTAGE=sum(FAHRT.values()); LKW_VERT=10
chk("Verteiler-Lkw: Tourtage ≤ 97 % der Kapazität", TOURTAGE<=LKW_VERT*LKW_TAGE*0.97,(TOURTAGE,LKW_VERT*LKW_TAGE))
CE_BEDARF=(TOURTAGE+LKW_TAGE)/FAHRER_TAGE
chk("CE-Fahrer (12,5 VZÄ) decken Bedarf Verteilung + Sattelzug", 12.5>=CE_BEDARF,(CE_BEDARF,))
chk("B-Fahrer (5 VZÄ) decken 4 Transporter", 5.0>=4*LKW_TAGE/FAHRER_TAGE,(4*LKW_TAGE/FAHRER_TAGE,))
SACH_KG=OD([('Fuhrpark (Leasing, Diesel, Maut, Unterhalt)',FUHRPARK),('Lagermiete (Besitzgesellschaft)',330.0),('Lager-Nebenkosten/Energie',100.0),('Lagertechnik (Stapler, Wartung)',65.0),
 ('Schankmaterial/CO₂',40.0),('Marketing',100.0),('IT (ERP, Telematik, Tourenplanung, mobile Erfassung)',140.0),('Versicherungen',80.0),('Beratung/Abschlussprüfung',75.0),
 ('Büro/Kommunikation',50.0),('Entsorgung',50.0),('Verbundbeitrag',35.0),('Leergut-/Palettendifferenzen',LEERGUT_DIFF),('Forderungs- und Darlehensausfälle',78.0),
 ('Veranstaltungsbedarf',30.0),('Sonstiges',70.0)])
KG_SACH=sum(SACH_KG.values())
AFA_KG=OD([('Leihinventar bei Wirten',220.0),('Sortieranlage',60.0),('Lager-/Betriebsausstattung',40.0),('IT und Software',20.0),('Veranstaltungsinventar',46.0),('Anhänger/Kühlanhänger',15.0)])
KG_AFA=sum(AFA_KG.values())
# ---------- 8 KG-Erloese, NV, GuV ----------
KG_UMS_EXT=sum(s['umsatz'] for s in SEG.values()); KG_UMS_F=MS['vp']; KG_UMS=KG_UMS_EXT+KG_UMS_F
KG_REI=sum(s['reI'] for s in SEG.values())+(MS['vp']-MS['einstand'])
KG_WE=sum(s['we'] for s in SEG.values())+MS['einstand']
KG_WE_EXT=KG_WE-K['umsatz_int']
KUNDENBONI=0.015*SEG['A']['ware']; NV_Q=0.03; NV_STR=0.01; INV_Q=0.0035
NVS=OD(); INVS=OD()
for x in ['A','B','C','D','E','F']:
    we=SEG[x]['we'] if x!='F' else MS['einstand']
    NVS[x]=we*NV_STR if x=='C' else (we-KB_SEG.get(x,0.0))*NV_Q
    INVS[x]=0.0 if x=='C' else we*INV_Q
NV=sum(NVS.values()); INVDIFF_KG=sum(INVS.values())
KG_REII=KG_REI-KUNDENBONI+NV-INVDIFF_KG
UMLAGE_ERL_M=MS['umlage']; UMLAGE_ERL_K=KST['VV Verwaltung/Vertrieb/Hofladen']['Umlage_KG']
KG_SO_ERL=SORTIERVERG+ABHOLVERG+DEPOTVERG+UMLAGE_ERL_M+UMLAGE_ERL_K
KG_EBITDA=KG_REII+KG_SO_ERL-KG_PERS-KG_SACH; KG_EBIT=KG_EBITDA-KG_AFA
# ---------- 9 Prozesskosten und Segmentrechnung KG ----------
W_LAGER_F=0.7; W_LEER_F=0.8
KOL_L=OD((x,SEG[x]['kolli']) for x in 'ABDE'); KOL_L['F']=MS['kolli']*W_LAGER_F
KOL_G=OD((x,SEG[x]['kolli']*SEG[x]['kgew']) for x in 'ABDE'); KOL_G['F']=MS['kolli']*0.35
P_LAGER=pers("Lager"); MIETE_NK=430.0
POOL=OD([('Wareneingang/Lagerung',0.25*P_LAGER+0.45*MIETE_NK+0.40*65+0.5*40+0.4*50),
         ('Kommissionierung',0.45*P_LAGER+0.20*MIETE_NK+0.35*65+0.3*40),
         ('Leergut (brutto, inkl. Differenzen)',0.30*P_LAGER+0.35*MIETE_NK+0.25*65+60+0.2*40+0.6*50+LEERGUT_DIFF)])
R_WE=POOL['Wareneingang/Lagerung']/sum(KOL_L.values())*1000
R_KOMM=POOL['Kommissionierung']/sum(KOL_G.values())*1000
KAESTEN_GEW=KAESTEN_SUM-KAESTEN['F']*(1-W_LEER_F)
R_LEER_BR=POOL['Leergut (brutto, inkl. Differenzen)']/KAESTEN_GEW*1000
R_LEER=(POOL['Leergut (brutto, inkl. Differenzen)']-SORTIERVERG)/KAESTEN_GEW*1000
FAHRER_CE=pers("Fahrer CE"); CE_SATTEL=LKW_TAGE/FAHRER_TAGE*48.0
LKW_POOL=9*LKW_JAHR+LKW75; R_LKW_TAG=LKW_POOL/(LKW_VERT*LKW_TAGE)*1000; R_FAHRER_TAG=48.0/FAHRER_TAGE*1000
R_TOURTAG=R_LKW_TAG+R_FAHRER_TAG
LEERKOSTEN_LKW=LKW_POOL-R_LKW_TAG*TOURTAGE/1000; FAHRER_LEER=(FAHRER_CE-CE_SATTEL)-R_FAHRER_TAG*TOURTAGE/1000
BEIFAHRER=pers("Beifahrer"); R_STOPP_A=R_TOURTAG/SEG['A']['spt']+BEIFAHRER/SEG['A']['auftr']*1000
AUFTR=OD((x,SEG[x]['auftr']) for x in 'ABCDE'); AUFTR['F']=MS['lief']
INNEN=pers("Innendienst")+0.5*140.0; R_AUFTR=INNEN/sum(AUFTR.values())*1000
SATTEL_POOL=SATTEL+CE_SATTEL-ABHOLVERG; R_SATTEL=SATTEL_POOL/sum(KOL_L.values())*1000
TRANSP_POOL=4*TRANSP+pers("Fahrer B")
AUSSEN=pers("Außendienst"); R_BESUCH=0.9*AUSSEN/BESUCHE*1000
SCHANK=pers("Schanktechnik")+40.0
VERANST=pers("Veranstaltungsservice")+pers("Saisonkräfte")+30.0+AFA_KG['Veranstaltungsinventar']+AFA_KG['Anhänger/Kühlanhänger']
MARKETING=OD(A=40.0,B=10.0,C=0.0,D=25.0,E=15.0,F=10.0); AUSFALL=OD(A=71.5,B=3.0,C=2.5,D=1.0,E=0.0,F=0.0)
Z_ERTRAG=36.0
SD=OD()
for x in ['A','B','C','D','E','F']:
    if x=='F': u=MS['vp']; we=MS['einstand']; reI=u-we; boni=0.0
    else: u=SEG[x]['umsatz']; we=SEG[x]['we']; reI=SEG[x]['reI']; boni=KUNDENBONI if x=='A' else 0.0
    d=OD(umsatz=u,we=we,reI=reI,boni=boni,nv=NVS[x],inv=INVS[x]); d['reII']=reI-boni+NVS[x]-INVS[x]
    kol=KOL_L.get(x,0); kgw=KOL_G.get(x,0)
    d['lager']=kol*R_WE/1000; d['komm']=kgw*R_KOMM/1000; d['leergut']=KAESTEN.get(x,0)*(W_LEER_F if x=='F' else 1.0)*R_LEER/1000; d['sattel']=kol*R_SATTEL/1000; d['auftrag']=AUFTR[x]*R_AUFTR/1000
    d['tour']={'A':FAHRT['A']*R_TOURTAG/1000+BEIFAHRER,'B':FAHRT['B']*R_TOURTAG/1000,'F':FAHRT['F']*R_TOURTAG/1000,'E':FAHRT['E']*R_TOURTAG/1000+0.25*TRANSP_POOL,'D':0.75*TRANSP_POOL,'C':0.0}[x]
    d['logistik']=d['lager']+d['komm']+d['leergut']+d['sattel']+d['auftrag']+d['tour']; d['dbII']=d['reII']-d['logistik']
    d['aussen']={'A':0.9*AUSSEN,'B':0.1*AUSSEN}.get(x,0.0); d['schank']={'A':0.9*SCHANK,'E':0.1*SCHANK}.get(x,0.0)
    d['veranst']=VERANST if x=='E' else 0.0; d['leihinv']=AFA_KG['Leihinventar bei Wirten'] if x=='A' else 0.0
    d['ausfall']=AUSFALL[x]; d['marketing']=MARKETING[x]; d['zinsertrag']=Z_ERTRAG if x=='A' else 0.0
    d['dbIII']=d['dbII']-d['aussen']-d['schank']-d['veranst']-d['leihinv']-d['ausfall']-d['marketing']+d['zinsertrag']
    SD[x]=d
OVH=OD([('Verwaltung (Buchhaltung, Lohn, IT)',pers("Verwaltung")),('Controller',pers("Controller")),('Logistikleiter',pers("Logistikleiter")),('Geschäftsführer',GF_VERG),
 ('IT (50 %)',70.0),('Versicherungen',80.0),('Beratung/Prüfung',75.0),('Büro',50.0),('Verbund',35.0),('Sonstiges',70.0),('AfA IT/Software',20.0),
 ('Leerkosten Lkw (ungenutzte Kapazität)',LEERKOSTEN_LKW),('Leerkosten Fahrer',FAHRER_LEER)])
OVERHEAD=sum(OVH.values()); SO_ERL_REST=DEPOTVERG+UMLAGE_ERL_M+UMLAGE_ERL_K
KG_EBIT_SEG=sum(SD[x]['dbIII'] for x in SD)-OVERHEAD+SO_ERL_REST-Z_ERTRAG
chk("Segmentrechnung KG: Σ DB III − Overhead + Umlage/Depot − Zinsertrag = KG-EBIT", eq(KG_EBIT_SEG,KG_EBIT,0.01),(KG_EBIT_SEG,KG_EBIT))
ALLOC=sum(POOL.values())+LKW_POOL+FAHRER_CE+BEIFAHRER+INNEN+SATTEL+TRANSP_POOL+AUSSEN+SCHANK+VERANST+AFA_KG['Leihinventar bei Wirten']+78.0+sum(MARKETING.values())+OVERHEAD-LEERKOSTEN_LKW-FAHRER_LEER
chk("Kostenverteilung KG vollständig: verteilte Kosten = Personal + Sachkosten + AfA", eq(ALLOC,KG_PERS+KG_SACH+KG_AFA,0.01),(ALLOC,KG_PERS+KG_SACH+KG_AFA))
chk("Σ Segment-NV = NV der GuV", eq(sum(SD[x]['nv'] for x in SD),NV))
ILOG=OD()
for k,m in M.items():
    il=OD(lager=m['kolli']*W_LAGER_F*R_WE/1000,komm=m['kolli']*0.35*R_KOMM/1000,leergut=m['leergut']*W_LEER_F*R_LEER/1000,sattel=m['kolli']*W_LAGER_F*R_SATTEL/1000,tour=m['lief']*0.5*R_TOURTAG/1000,auftrag=m['lief']*R_AUFTR/1000)
    il['summe']=sum(il.values()); ILOG[k]=il
ILOG_SUM=sum(ILOG[k]['summe'] for k in M)
chk("interne Logistik Σ Märkte = Logistikkosten Segment F", eq(ILOG_SUM,SD['F']['logistik'],0.01))
def vp_var(f):
    r=OD()
    for k,m in M.items():
        vp=f(m,k); mk=m['umsatz']-vp-m['invdiff']-m['pers']-m['sach']-m['umlage']-m['afa']
        kg=(vp-m['einstand'])+(m['einstand']-KB_SEG['F']*m['einstand']/MS['einstand'])*NV_Q-m['einstand']*INV_Q-ILOG[k]['summe']-MARKETING['F']*m['umsatz']/MS['umsatz']
        r[k]=(vp,mk,kg,mk+kg)
    return r
VPV=OD([('a) Einstand',vp_var(lambda m,k:m['einstand'])),('b) Einstand + 3 % (Startregel)',vp_var(lambda m,k:m['einstand']*(1+VP_Z))),
        ('c) Einstand + interne Logistik (Vollkosten)',vp_var(lambda m,k:m['einstand']+ILOG[k]['summe'])),('d) Marktpreis wie Wiederverkäufer (RE 15 %)',vp_var(lambda m,k:m['einstand']/(1-SEG['B']['req'])))])
for nm,v in VPV.items():
    for k in M: chk(f"VP-Variante {nm[:2]} {k}: Gesamtergebnis unverändert", eq(v[k][3],VPV['a) Einstand'][k][3],1e-6))
chk("Startregel b) reproduziert Märkte-EBIT der GuV", all(eq(VPV['b) Einstand + 3 % (Startregel)'][k][1],M[k]['ebit'],1e-6) for k in M))
chk("Σ Segment F (DB III) = Σ KG-Anteil Variante b)", eq(SD['F']['dbIII'],sum(VPV['b) Einstand + 3 % (Startregel)'][k][2] for k in M),0.01),(SD['F']['dbIII'],))
def schliessung(k,abbau=0.5):
    m=M[k]; il=ILOG[k]; nvb=(m['einstand']-KB_SEG['F']*m['einstand']/MS['einstand'])*NV_Q
    verlust=m['umsatz']-m['einstand']+nvb-m['einstand']*INV_Q-m['invdiff']
    ersp_direkt=m['pers']+m['sach']; ersp_log=(il['komm']+il['leergut']+il['tour']+il['auftrag'])*abbau
    ersp_mkt=MARKETING['F']*m['umsatz']/MS['umsatz']
    return OD(verlust=verlust,direkt=ersp_direkt,log=ersp_log,mkt=ersp_mkt,wirkung=ersp_direkt+ersp_log+ersp_mkt-verlust)
SCHL=OD((k,schliessung(k)) for k in M)
def kunden_db(u,re,bq,st,kol,bes,darl,afa,aq):
    d=OD(umsatz=u,re=u*re,bonus=u*bq); d['db1']=d['re']-d['bonus']
    d['lager']=kol*(R_WE+R_SATTEL); d['komm']=kol*R_KOMM; d['leer']=kol*0.85*R_LEER; d['stopps']=st*(R_STOPP_A+R_AUFTR)
    d['db2']=d['db1']-d['lager']-d['komm']-d['leer']-d['stopps']
    d['aussen']=bes*R_BESUCH; d['zins']=darl*(0.06-0.03); d['afa']=afa; d['ausf']=u*aq; d['db3']=d['db2']-d['aussen']-d['zins']-d['afa']-d['ausf']; return d
KDB=OD([('Brauhaus (A-Kunde)',kunden_db(60000,0.30,0.02,104,2750,24,30000,4000,0.005)),('Eckkneipe (C-Kunde)',kunden_db(12000,0.35,0.0,52,670,12,0,1500,0.02)),
        ('Eckkneipe, 14-tägig beliefert',kunden_db(12000,0.35,0.0,26,670,12,0,1500,0.02))])
KOLLIWERT_A=SEG['A']['ware']*1000/SEG['A']['kolli']
KV_KOLLI_A=R_KOMM+0.85*R_LEER+R_WE+R_SATTEL
MBW=(R_STOPP_A+R_AUFTR)/(SEG['A']['req']-KV_KOLLI_A/KOLLIWERT_A)
LOG_KOLLI_A=SD['A']['logistik']*1000/SEG['A']['kolli']; STOPP_A=R_STOPP_A+R_AUFTR
# ---------- 10 Zinsen, Steuern, Konzern-GuV ----------
TILG=OD(BMD=250.0,AKQ=50.0,KELT=50.0)
Z_BMD=(2000+1750)/2*0.05; Z_AKQ=(300+250)/2*0.045
KK_SAISON=100.0; KK_SATZ=0.08
def zins_kg(kk_avg): return Z_BMD+Z_AKQ+kk_avg*KK_SATZ-Z_ERTRAG
def hinz(z,mi,le): b=z+0.5*mi+0.2*le; return max(0,b-200)*0.25,b
STAPLER_LEAS=29.4; HEBESATZ=4.0
def rechne(kk_avg_kg):
    R=OD()
    R['kg_zins']=zins_kg(kk_avg_kg); R['kg_ebt']=KG_EBIT-R['kg_zins']
    R['h_kg'],R['hb_kg']=hinz(Z_BMD+Z_AKQ+kk_avg_kg*KK_SATZ,330.0,LEASING_FZ+STAPLER_LEAS)
    R['h_m'],R['hb_m']=hinz(0.0,sum(SACH_M[k]['Miete'] for k in M),sum(SACH_M[k]['Stapler'] for k in M)+0.7*sum(SACH_M[k]['Leergutautomaten'] for k in M))
    R['h_k'],R['hb_k']=hinz(K_ZINS,K_MIETE,0.0)
    R['ge_mit']=R['kg_ebt']+GF_VERG+R['h_kg']+MS['ebt']+R['h_m']+K['ebt']+R['h_k']-24.5
    # ohne Kelterei: KG ohne Umlage Kelterei, ohne Akquisitionsdarlehen
    R['kg_ebt_ohne']=KG_EBIT-UMLAGE_ERL_K-(R['kg_zins']-Z_AKQ)
    h2,_=hinz(Z_BMD+kk_avg_kg*KK_SATZ,330.0,LEASING_FZ+STAPLER_LEAS)
    R['h_kg_ohne']=h2
    R['ge_ohne']=R['kg_ebt_ohne']+GF_VERG+h2+MS['ebt']+R['h_m']-24.5
    R['gst_mit']=max(0,R['ge_mit'])*0.035*HEBESATZ; R['gst_ohne']=max(0,R['ge_ohne'])*0.035*HEBESATZ
    return R
GOF0=30.0; GOF_AFA=3.0; GOF_RBW=GOF0-2*GOF_AFA
def konzern(R,mit):
    ums=KG_UMS+MS['umsatz']+(K['umsatz'] if mit else 0); innen=KG_UMS_F+(K['umsatz_int'] if mit else 0)
    umlage=UMLAGE_ERL_M+(UMLAGE_ERL_K if mit else 0)
    we=KG_WE+MS['vp']+(K_MAT if mit else 0)-innen
    pers_=KG_PERS+MS['pers']+(K_PERS if mit else 0)
    so_erl=SORTIERVERG+ABHOLVERG+DEPOTVERG
    sach=KG_SACH+MS['sach']+(K_SONST-UMLAGE_ERL_K if mit else 0)  # Umlage Kelterei eliminiert
    inv=INVDIFF_KG+MS['invdiff']
    ebitda=ums-innen-we-KUNDENBONI+NV-inv+so_erl-pers_-sach
    afa=KG_AFA+MS['afa']+(K_AFA+GOF_AFA if mit else 0)
    ebit=ebitda-afa
    zins=(R['kg_zins']+K_ZINS) if mit else (R['kg_zins']-Z_AKQ)
    ebt=ebit-zins; gst=R['gst_mit'] if mit else R['gst_ohne']
    return OD(umsatz_summe=ums,innen=innen,umsatz=ums-innen,we=we,boni=KUNDENBONI,nv=NV,inv=inv,so_erl=so_erl,pers=pers_,sach=sach,ebitda=ebitda,afa=afa,ebit=ebit,zins=zins,ebt=ebt,gewst=gst,erg=ebt-gst)
# ---------- 11 Bilanzen 01.01.2027 ----------
FORD_EXT=sum(SEG[x]['umsatz']*1.19*SEG[x]['dso']/365 for x in SEG)+40.0
VERB_WARE=KG_WE_EXT*1.19*26/365; VERB_SACH=(KG_SACH-330.0)*1.19/12; VERB_PFAND=180.0; VERB_LL_KG=VERB_WARE+VERB_SACH+VERB_PFAND
IC_WARE_M=MS['vp']*1.19*14/365; IC_WARE_K=K['umsatz_int']*1.19/12
TANK_L=200000; FERTIG=OD([('Glas 1,0 l',80000),('Glas 0,2 l (Gastro)',25000),('BiB 5 l (eigen)',30000)])
K_VORR=TANK_L*(OBST_L+R_H12)/1000+sum(FERTIG[p]*HK[p] for p in FERTIG)/1000+15.0
K_IN_KG=OD([('Glas 1,0 l',12000),('Glas 0,2 l (Gastro)',5000),('BiB 5 l (eigen)',3000)]); K_IN_M=OD([('Glas 1,0 l',6000),('BiB 5 l (eigen)',2000)])
VPK=OD((p,v[2]) for p,v in K_ABSATZ.items())
ZG_K=(sum(q*(VPK[p]-HK[p]) for p,q in K_IN_KG.items())+sum(q*(VPK[p]-HK[p]) for p,q in K_IN_M.items()))/1000
M_VORR=OD(M1=125.0,M2=80.0,M3=58.0); M_VORR_SUM=sum(M_VORR.values()); ZG_M=M_VORR_SUM*VP_Z/(1+VP_Z)
EAV26_M=MS['ebt']; EAV26_K=K['ebt']
KG_EK_KAP=600.0; KG_EK_RL=1500.0; CASHPOOL_M=150.0
def bil_kg(mit=True):
    A=OD([('Immaterielle VG (ERP-Software)',40.0),('Sachanlagen (Sortieranlage 420, Lager-BGA 200, IT 40, Veranstaltungsinventar 196, Anhänger 60)',916.0),
          ('Leihinventar bei Wirten',900.0),('Beteiligung Märkte GmbH',250.0)])
    if mit: A['Beteiligung Kelterei GmbH']=330.0
    A['Ausleihungen (Gastro-Darlehen)']=1200.0; A['Vorräte (Lagerware)']=700.0
    A['Pfand-Erstattungsansprüche gg. Abfüller']=PF_ABF+(0 if mit else PF_KELT)
    A['Forderungen L+L extern (inkl. Pfandsaldo 40, brutto)']=FORD_EXT
    A['Ford. gg. Märkte: Warenlieferungen']=IC_WARE_M; A['Ford. gg. Märkte: Cash-Pool']=CASHPOOL_M; A['Ford. gg. Märkte: EAV 2026']=EAV26_M
    if mit: A['Ford. gg. Kelterei: Pfand Saftkästen']=PF_KELT; A['Ford. gg. Kelterei: EAV 2026']=EAV26_K
    A['Bonus-/WKZ-Forderungen (Nachvergütungen 2026)']=290.0; A['Sonstige VG']=60.0; A['Bank']=150.0; A['RAP']=30.0
    P=OD([('EK: Kommanditkapital',KG_EK_KAP),('EK: Rücklagen',KG_EK_RL),('Rückstellungen (Kundenboni 142,5, Urlaub 60, Prüfung 35, GewSt 25, Sonst. 20)',282.5),
          ('Bankdarlehen Betriebsmittel (5 %, Tilgung 250/J.)',2000.0)])
    if mit: P['Akquisitionsdarlehen Kelterei (4,5 %, Tilgung 50/J.)']=300.0
    P['Verbindlichkeiten L+L extern (inkl. Pfandsaldo 180)']=VERB_LL_KG+(0 if mit else IC_WARE_K)
    P['Pfandverbindlichkeiten gg. Kunden']=PF_KUNDEN; P['Pfandverbindlichkeit gg. Märkte (intern)']=PF_MAERKTE
    if mit: P['Verb. gg. Kelterei: Lieferungen']=IC_WARE_K
    P['Sonstige Verbindlichkeiten (USt, LSt, SV)']=220.0
    P['Kontokorrent (Rahmen 1.300)']=sum(A.values())-sum(P.values())
    return A,P
def bil_m():
    A=OD([('Sachanlagen (Markt 1: 120, Markt 2: 65, Markt 3: 45)',230.0),('Vorräte zu VP (M1 125, M2 80, M3 58)',M_VORR_SUM),('Pfand-Erstattungsanspruch gg. KG (intern)',PF_MAERKTE),
          ('Einweg-Pfandforderungen (DPG-Clearing)',6.0),('Forderungen (Kartenzahlungen unterwegs)',15.0),('Kasse',18.0),('RAP',3.0)])
    P=OD([('EK: Stammkapital',100.0),('EK: Kapitalrücklage',150.0),('Rückstellungen',20.0),('Verb. gg. KG: Warenlieferungen',IC_WARE_M),('Verb. gg. KG: Cash-Pool (zinslos)',CASHPOOL_M),
          ('Verb. gg. KG: EAV 2026',EAV26_M),('Sonstige Verbindlichkeiten (USt, LSt)',45.0),('Verbindlichkeiten L+L extern',25.0)])
    A['Bank']=sum(P.values())-sum(A.values()); return A,P
def bil_k():
    A=OD([('Sachanlagen (Glaslinie 160, Presse 50, Tanks 72, BiB 24, Leergut-Pool 30, BGA 20)',356.0),('Vorräte (Tankware, Fertigware zu HK, Hilfsstoffe)',K_VORR),
          ('Ford. gg. KG: Lieferungen',IC_WARE_K),('Forderungen L+L extern',12.0),('Bank',5.0)])
    P=OD([('EK: Stammkapital',100.0),('EK: Kapitalrücklage',200.0),('Bankdarlehen (4,5 %, Tilgung 50/J.)',K_DARL),('Pfandverbindlichkeit gg. KG (Saftkästen im Umlauf)',PF_KELT),
          ('Verb. gg. KG: EAV 2026',EAV26_K),('Verbindlichkeiten L+L',28.0),('Rückstellungen',12.0),('Sonstige Verbindlichkeiten',10.0)])
    P['Saison-Kontokorrent (Rahmen 400)']=sum(A.values())-sum(P.values()); return A,P
KG_A,KG_P=bil_kg(True); M_A,M_P=bil_m(); K_A,K_P=bil_k()
for nm,(a,p) in {'KG':(KG_A,KG_P),'Märkte GmbH':(M_A,M_P),'Kelterei GmbH':(K_A,K_P)}.items(): chk(f"Eröffnungsbilanz {nm}: Aktiva = Passiva", eq(sum(a.values()),sum(p.values()),1e-9))
KK0_KG=KG_P['Kontokorrent (Rahmen 1.300)']; KK0_K=K_P['Saison-Kontokorrent (Rahmen 400)']
chk("KG-Kontokorrent 01.01. zwischen 0 und Rahmen 1.300", 0<=KK0_KG<=1300, KK0_KG)
chk("Märkte-Bank 01.01. ≥ 0", M_A['Bank']>=0, M_A['Bank'])
chk("Kelterei-Kontokorrent 01.01. zwischen 0 und Rahmen 400", 0<=KK0_K<=400, KK0_K)
def konsolidiere(mit=True):
    a_kg,p_kg=bil_kg(mit)
    E=OD()
    E['Kapitalkonsolidierung Märkte: Beteiligung 250 ↔ EK 250']=(-250.0,-250.0)
    if mit: E['Kapitalkonsolidierung Kelterei: Beteiligung 330 ↔ EK 300, GoF 30 abzgl. AfA 2025/26']=(-330.0+GOF_RBW,-300.0-(GOF0-GOF_RBW))
    E['Schulden: Warenlieferungen KG → Märkte']=(-IC_WARE_M,-IC_WARE_M); E['Schulden: Cash-Pool KG → Märkte']=(-CASHPOOL_M,-CASHPOOL_M)
    E['Schulden: Pfand Märkte ↔ KG']=(-PF_MAERKTE,-PF_MAERKTE); E['Schulden: EAV 2026 Märkte']=(-EAV26_M,-EAV26_M)
    if mit:
        E['Schulden: Lieferungen Kelterei → KG']=(-IC_WARE_K,-IC_WARE_K); E['Schulden: Pfand Saftkästen KG ↔ Kelterei']=(-PF_KELT,-PF_KELT); E['Schulden: EAV 2026 Kelterei']=(-EAV26_K,-EAV26_K)
    E['Zwischengewinn KG in Märkte-Vorräten (3/103)']=(-ZG_M,-ZG_M)
    if mit: E['Zwischengewinn Kelterei in KG- und Märkte-Vorräten']=(-ZG_K,-ZG_K)
    for kk,(da,dp) in E.items(): chk(f"Konsolidierungsbuchung beidseitig gleich ({'mit' if mit else 'ohne'} K): {kk[:40]}", eq(da,dp,1e-9))
    sumA=sum(a_kg.values())+sum(M_A.values())+(sum(K_A.values()) if mit else 0); sumP=sum(p_kg.values())+sum(M_P.values())+(sum(K_P.values()) if mit else 0)
    bils=sumA+sum(v[0] for v in E.values()); totP=sumP+sum(v[1] for v in E.values())
    ek=KG_EK_KAP+KG_EK_RL-(GOF0-GOF_RBW if mit else 0)-ZG_M-(ZG_K if mit else 0)
    ek_einzel=KG_EK_KAP+KG_EK_RL+250.0+(300.0 if mit else 0)
    chk(f"Konzern-EK ({'mit' if mit else 'ohne'} K) = Σ Einzel-EK − Beteiligungen − GoF-AfA − Zwischengewinne", eq(ek_einzel-250-(300+GOF0-GOF_RBW if mit else 0)-ZG_M-(ZG_K if mit else 0),ek,1e-9))
    kk=p_kg['Kontokorrent (Rahmen 1.300)']+(K_P['Saison-Kontokorrent (Rahmen 400)'] if mit else 0)
    bank=a_kg['Bank']+M_A['Bank']+M_A['Kasse']+(K_A['Bank'] if mit else 0)
    darl=2000.0+(300.0+K_DARL if mit else 0)
    R=OD(E=E,sumA=sumA,sumP=sumP,bilsum=bils,totP=totP,ek=ek,kk=kk,bank=bank,darl=darl,pf_ford=a_kg['Pfand-Erstattungsansprüche gg. Abfüller'],pf_verb=PF_KUNDEN,a_kg=a_kg,p_kg=p_kg)
    chk(f"Konzernbilanz ({'mit' if mit else 'ohne'} Kelterei): Aktiva = Passiva", eq(bils,totP,1e-9))
    R['ekq']=ek/bils; R['ekq_netto']=ek/(bils-PF_KUNDEN); R['netdebt']=darl+kk-bank
    return R
KB_MIT=konsolidiere(True); KB_OHNE=konsolidiere(False)
# ---------- 12 Cashflow, Planbilanz, Iteration Kontokorrentzins ----------
EST_SATZ=0.45
CAPEX=OD([('Leihinventar (Ersatz, neue Wirte)',200.0),('KG übrige (Lager, IT, Veranstaltung)',110.0),('Märkte (inkl. Kühlmöbel Markt 1 im Dezember)',45.0),('Kelterei (Pumpen, Filter)',60.0)])
AUSL_NEU=300.0; AUSL_RUECK=250.0
def plan(kk_avg,kk_avg_o):
    R=rechne(kk_avg); Ro=rechne(kk_avg_o); KZm=konzern(R,True); KZo=konzern(Ro,False)
    est_basis=R['kg_ebt']+MS['ebt']+K['ebt']
    entn=max(0,EST_SATZ*est_basis-min(R['gst_mit'],4.0*0.035*max(0,R['ge_mit'])))
    entn_o=max(0,EST_SATZ*(Ro['kg_ebt_ohne']+MS['ebt'])-min(Ro['gst_ohne'],4.0*0.035*max(0,Ro['ge_ohne'])))
    out=OD()
    for mit,KZ,KB,en in [(True,KZm,KB_MIT,entn),(False,KZo,KB_OHNE,entn_o)]:
        tilg=TILG['BMD']+(TILG['AKQ']+TILG['KELT'] if mit else 0)
        capex=sum(CAPEX.values())-(0 if mit else CAPEX['Kelterei (Pumpen, Filter)'])
        cf=OD(); cf['Konzernergebnis nach GewSt']=KZ['erg']; cf['+ Abschreibungen (inkl. GoF)']=KZ['afa']; cf['− Entnahmen für ESt der Kommanditisten']=-en
        cf['= Cashflow nach Entnahmen']=KZ['erg']+KZ['afa']-en; cf['− Investitionen']=-capex; cf['− neue Gastro-Darlehen']=-AUSL_NEU; cf['+ Rückflüsse Gastro-Darlehen']=AUSL_RUECK
        cf['− Tilgung Bankdarlehen']=-tilg; cf['± Working Capital (Stichtag wie Vorjahr)']=0.0
        dkk=-(cf['= Cashflow nach Entnahmen']-capex-AUSL_NEU+AUSL_RUECK-tilg); cf['= Anstieg Kontokorrent']=dkk
        end=OD(ek=KB['ek']+KZ['erg']-en,darl=KB['darl']-tilg,kk=KB['kk']+dkk,bilsum=KB['bilsum']+capex-KZ['afa']+AUSL_NEU-AUSL_RUECK)
        end['check']=(end['ek']-KB['ek'])+(end['darl']-KB['darl'])+(end['kk']-KB['kk'])-(end['bilsum']-KB['bilsum'])
        end['ekq']=end['ek']/end['bilsum']; end['ekq_netto']=end['ek']/(end['bilsum']-PF_KUNDEN)
        end['netdebt']=end['darl']+end['kk']-KB['bank']
        out['mit' if mit else 'ohne']=OD(KZ=KZ,KB=KB,cf=cf,end=end,entn=en,tilg=tilg,capex=capex)
    return R,Ro,out
KK0_KG_O=KB_OHNE['p_kg']['Kontokorrent (Rahmen 1.300)']
kk_avg=600.0; kk_avg_o=600.0
for i in range(60):
    R,Ro,P=plan(kk_avg,kk_avg_o)
    kk_kg_end=KK0_KG+P['mit']['cf']['= Anstieg Kontokorrent']   # Kelterei-KK konstant (Annahme), Veraenderung trifft die KG
    kk_kg_end_o=KK0_KG_O+P['ohne']['cf']['= Anstieg Kontokorrent']
    new=(KK0_KG+kk_kg_end)/2+KK_SAISON; new_o=(KK0_KG_O+kk_kg_end_o)/2+KK_SAISON
    if abs(new-kk_avg)<1e-10 and abs(new_o-kk_avg_o)<1e-10: break
    kk_avg=new; kk_avg_o=new_o
KK_AVG=kk_avg; KK_AVG_O=kk_avg_o; KK_KG_END=kk_kg_end
chk("Kontokorrentzins-Iteration konvergiert (Ø-Saldo = (Anfang + Ende) ÷ 2 + 100 Saison, beide Varianten)", abs(new-kk_avg)<1e-6 and abs(new_o-kk_avg_o)<1e-6, i)
KZ_MIT=P['mit']['KZ']; KZ_OHNE=P['ohne']['KZ']; END_MIT=P['mit']['end']; END_OHNE=P['ohne']['end']; CF_MIT=P['mit']['cf']; CF_OHNE=P['ohne']['cf']
KG_ZINS=R['kg_zins']; KG_EBT=R['kg_ebt']
for nm in ['mit','ohne']: chk(f"Planbilanz 31.12.2027 ({nm} Kelterei): Aktiva = Passiva", eq(P[nm]['end']['check'],0,1e-9))
chk("Konzern-EBT (mit K) = Σ Einzel-EBT vor EAV − GoF-AfA", eq(KZ_MIT['ebt'],KG_EBT+MS['ebt']+K['ebt']-GOF_AFA,1e-6))
chk("Konzern-EBIT (mit K) = Σ Einzel-EBIT − GoF-AfA", eq(KZ_MIT['ebit'],KG_EBIT+MS['ebit']+K['ebit']-GOF_AFA,1e-6))
chk("Konzern-EBIT (ohne K) = KG-EBIT − Umlage Kelterei + Märkte-EBIT", eq(KZ_OHNE['ebit'],KG_EBIT-UMLAGE_ERL_K+MS['ebit'],1e-6))
chk("Konzernumsatz (mit K) = externe Umsätze aller Gesellschaften", eq(KZ_MIT['umsatz'],KG_UMS_EXT+MS['umsatz']+K['umsatz_ext'],1e-6))
chk("KK 31.12.2027 im Gesamtrahmen 1.700", END_MIT['kk']<=1700, END_MIT['kk'])
def kdf(KZ,tilg): return (KZ['erg']+KZ['afa']+KZ['zins'])/(KZ['zins']+tilg)
COV=OD(ekq0=KB_MIT['ekq'],ekq1=END_MIT['ekq'],ekq0_n=KB_MIT['ekq_netto'],nd0=KB_MIT['netdebt']/KZ_MIT['ebitda'],nd1=END_MIT['netdebt']/KZ_MIT['ebitda'],kdf=kdf(KZ_MIT,P['mit']['tilg']))
chk("Covenant Konzern-EK-Quote ≥ 25 % am 01.01.2027", COV['ekq0']>=0.25, COV['ekq0'])
chk("Covenant Konzern-EK-Quote ≥ 25 % am 31.12.2027 (Plan)", COV['ekq1']>=0.25, COV['ekq1'])
chk("Covenant Nettoverschuldung/EBITDA ≤ 3,5 (31.12.2027)", COV['nd1']<=3.5, COV['nd1'])
chk("Covenant Kapitaldienstfähigkeit ≥ 1,2 (Formel M50)", COV['kdf']>=1.2, COV['kdf'])
FLOAT_KONZERN=PF_ABF-PF_KUNDEN-VERB_PFAND
KONZERN_VZAE=KG_VZAE+MS['vzae']+K_VZAE
