# Konzept-final: alle neuen Zahlen der Getraenkegruppe (Variante ohne Kelterei + Hausmarke Limonade in Lohnabfuellung)
# Alle Parameter sind Annahmen [Vermutung]; Basis = Modell 08 (Variante ohne Kelterei).
from base import g, r
P=print
CK=[]
def chk(n,c,d=""):
    CK.append(n)
    if not c: raise AssertionError(f"{n}: {d}")
KZ=g['KZ_OHNE']; KB=g['KB_OHNE']; END=g['END_OHNE']; CF=g['CF_OHNE']; M=g['M']
UST=1.19
P("=== 0 Basis 08 ohne Kelterei ===")
P("EBIT",r(KZ['ebit']),"EBITDA",r(KZ['ebitda']),"EBT",r(KZ['ebt']),"Erg",r(KZ['erg']))

# ---------------- 1 Markt 1: Ueberleitung Einzelmarkt 02 -> Filiale ----------------
P("\n=== 1 Ueberleitung Markt 1 (02 -> Filiale 2027) ===")
E02=dict(umsatz=2500.0, reII=749.318, pers=355.430, sach=317.360, afa=26.0)
E02['ebit']=E02['reII']-E02['pers']-E02['sach']-E02['afa']
m1=M['M1']
fil=dict(umsatz=m1['umsatz'], re=m1['reI']-m1['invdiff'], pers=m1['pers'], sach=m1['sach'], umlage=m1['umlage'], afa=m1['afa'])
fil['ebit']=fil['re']-fil['pers']-fil['sach']-fil['umlage']-fil['afa']
chk("Filiale EBIT = Modell", abs(fil['ebit']-m1['ebit'])<1e-6)
P("02 EBIT",r(E02['ebit'],1)," Filiale",r(fil['ebit'],1))
br=[('Rohertrag (RE II 02 -> RE I auf VP nach Invdiff)',fil['re']-E02['reII']),('Personal',E02['pers']-fil['pers']),('Sachkosten',E02['sach']-fil['sach']),('Umlage Zentrale',-fil['umlage']),('AfA',E02['afa']-fil['afa'])]
for n,v in br: P(" ",n,r(v,1))
chk("Bruecke schliesst", abs(E02['ebit']+sum(v for _,v in br)-fil['ebit'])<1e-6)
# Zerlegung Rohertrag: Laden 02 RE I 575,985 + NV/Inv anteilig; Einkaufsvorteil 6 %, VP +3 %
we02_laden=2150-575.985
P(" Laden-RE I 02:",575.985," WE 02 Laden",r(we02_laden,1)," Einkaufsvorteil 6 % =",r(0.06*we02_laden,1)," VP-Aufschlag 3 % =",r(-0.03*0.94*we02_laden,1))
P(" Heimdienst+Fest RE I 02:",91.6+47.5," NV+Inv 02:",r(46.733-12.5,1))
x= 575.985 + 0.06*we02_laden - 0.03*0.94*we02_laden - m1['invdiff']
P(" Pruefung RE Filiale aus 02-Laden:",r(x,2),"Modell",r(fil['re'],2))
bri=[('EBIT 02',E02['ebit']),('HD/Fest-RE in KG',-139.1),('NV in KG',-46.733),('Invdiff',12.5-m1['invdiff']),('Einkaufsvorteil',0.06*we02_laden),('VP',-0.03*0.94*we02_laden),('Personal',E02['pers']-fil['pers']),('Sach',E02['sach']-fil['sach']),('Umlage',-fil['umlage']),('AfA',E02['afa']-fil['afa'])]
P(" Bruecke:",[(n,r(v,1)) for n,v in bri],"=",r(sum(v for _,v in bri),2))

# ---------------- 2 L01-Kaskade, Aktion Februar 2027 ----------------
P("\n=== 2 Aktion L01 (Kapitel 1) ===")
vk_n=17.49/UST; vk_a=9.99/UST; ek_n=12.40; ek_a=8.20
ein_n=0.94*ek_n; ein_a=0.94*ek_a; vp_n=ein_n*1.03; vp_a=ein_a*1.03
dbm_n=vk_n-vp_n; dbm_a=vk_a-vp_a; dbg_n=vk_n-ein_n; dbg_a=vk_a-ein_a
P("VK netto",r(vk_n,3),r(vk_a,3),"Einstand",r(ein_n,3),r(ein_a,3),"VP",r(vp_n,3),r(vp_a,3))
P("db Markt n/a",r(dbm_n,3),r(dbm_a,3),"Gruppe n/a",r(dbg_n,3),r(dbg_a,3), "Markt-RE% normal", r(dbm_n/vk_n*100,1))
base=120; x=480; mehr=x-base; kann=0.6*mehr; nach=48; bons=150
net_extra=mehr-kann-nach
comp_m=[x*dbm_a,-base*dbm_n,-kann*2.80,-nach*dbm_n,bons*3.40,0.0,-net_extra*0.25]
comp_g=[x*dbg_a,-base*dbg_n,-kann*3.10,-nach*dbg_n,bons*3.60,400.0,-net_extra*(0.25+0.35)]
P("Markt",[r(c,1) for c in comp_m],"=",r(sum(comp_m),1))
P("Gruppe",[r(c,1) for c in comp_g],"=",r(sum(comp_g),1), "net extra",net_extra)
AKT_M=sum(comp_m); AKT_G=sum(comp_g)
# Gegenangebot 10,99 / Aktions-EK 8,60, gleicher Lift (optimistisch)
vk_a2=10.99/UST; ein_a2=0.94*8.60; vp_a2=ein_a2*1.03
m2=x*(vk_a2-vp_a2)+sum(comp_m[1:]); g2=x*(vk_a2-ein_a2)+sum(comp_g[1:])
P("Gegenangebot Markt",r(m2,1),"Gruppe",r(g2,1))
P("Umsatzplus netto (Fehler D10)", r(x*vk_a-base*vk_n,1))
P("Nachbelastung 300 Kaesten", r(300*(ein_n-ein_a),2), "je Kasten", r(ein_n-ein_a,3))
P("L01 Kaskade 14,20 -> 12,40 -> NN 11,78; Gruppen-Einstand", r(ein_n,3), "VP", r(vp_n,3), "Konzern-RE je Kasten", r(dbg_n,2))

# ---------------- 3 Hausmarke Limonade 2027 ----------------
P("\n=== 3 Hausmarke 2027 ===")
G={ # Flaschen/Kasten, l/Fl, Kaesten 2027, Lohn/Fl, Flaschenpreis, Kanaele [(Kanal, Kaesten, Preis netto)], Fremdreferenz (Preis-Kanaele, Einstand)
 'H33':dict(n=24,l=0.33,K=14000,lohn=0.19,flp=0.28,kan=[('Gastro',14000,12.90)],fr=[('Gastro',14000,14.90)],fr_ein=10.15),
 'H50':dict(n=20,l=0.50,K=9000,lohn=0.21,flp=0.32,kan=[('Heimdienst/Objekt',9000,10.40)],fr=[('Heimdienst/Objekt',9000,11.97)],fr_ein=8.80),
 'H100':dict(n=12,l=1.00,K=16000,lohn=0.25,flp=0.42,kan=[('Wiederverkaeufer',10000,7.14),('Heimdienst/Objekt',6000,7.83)],fr=[('Wiederverkaeufer',10000,7.55),('Heimdienst/Objekt',6000,8.26)],fr_ein=5.966),
}
ZUCKER_GL=75; ZUCKERPREIS=0.80; GRUNDSTOFF=0.13
ROH_L=ZUCKER_GL/1000*ZUCKERPREIS+GRUNDSTOFF
VERS=0.03; SCHW_FL=0.03; KASTEN=4.20; SCHW_K=0.01; FRACHT=0.15
P("Rohstoff je l", r(ROH_L,3))
T=dict(K=0,fl=0,l=0,U=0,E=0,RE=0,lohn=0,Uf=0,REf=0,NVf=0,roh=0)
for k,d in G.items():
    n=d['n']; l=d['l']
    roh=n*l*ROH_L; v=n*VERS; lo=n*d['lohn']; lg=n*SCHW_FL*d['flp']+SCHW_K*KASTEN
    ein=roh+v+lo+lg+FRACHT; d['ein']=ein
    U=sum(kk*p for _,kk,p in d['kan']); pavg=U/d['K']; d['pavg']=pavg
    Uf=sum(kk*p for _,kk,p in d['fr']); pf=Uf/d['K']; d['pf']=pf
    d['db']=pavg-ein; d['dbf']=pf-d['fr_ein']; d['nvf']=0.03*d['fr_ein']
    chk(f"{k} Kanalmengen", sum(kk for _,kk,_ in d['kan'])==d['K'])
    P(k,"roh",r(roh,3),"vers",r(v,2),"lohn",r(lo,2),"leergut",r(lg,3),"fracht",FRACHT,"Einstand",r(ein,2),"Preis avg",r(pavg,3),"DB I",r(d['db'],2),r(d['db']/pavg*100,1),"% | Fremd Preis",r(pf,3),"Ein",d['fr_ein'],"RE",r(d['dbf'],2),"NV",r(d['nvf'],3),"RE II",r(d['dbf']+d['nvf'],2))
    for kan,kk,p in d['kan']: P("   Kanal",kan,kk,"Preis netto",r(p,3),"brutto",r(p*UST,2) if kan=='Maerkte' else '', "Markt-db (VP)" , r(p-ein*1.03,3) if kan=='Maerkte' else '', "Gruppen-db", r(p-ein,3))
    for kan,kk,p in d['fr']: 
        if kan=='Maerkte': P("   Fremd Markt: VK",r(p*UST,2),"netto",r(p,3),"Markt-db",r(p-d['fr_ein']*1.03,3),r((p-d['fr_ein']*1.03)/p*100,1),"% | HM Markt-db %", r((d['kan'][0][2]-ein*1.03)/d['kan'][0][2]*100,1))
    T['K']+=d['K']; T['fl']+=n*d['K']; T['l']+=n*l*d['K']; T['U']+=U; T['E']+=ein*d['K']; T['RE']+=d['db']*d['K']; T['lohn']+=lo*d['K']; T['roh']+=roh*d['K']
    T['Uf']+=Uf; T['REf']+=d['dbf']*d['K']; T['NVf']+=d['nvf']*d['K']
P({k:r(v,1) for k,v in T.items()}, "DB-Quote", r(T['RE']/T['U']*100,1))
HM_U=T['U']/1000; HM_RE=T['RE']/1000
KANN=0.70; FIX_HM=37.0
disp_U=KANN*T['Uf']/1000; disp_RE=KANN*(T['REf']+T['NVf'])/1000
SORT_LOST=KANN*T['K']*0.09/1000
INKR_K=(1-KANN)*T['K']; VAR_LOG=INKR_K*0.05/1000
PK_LANG=INKR_K*(0.30+0.32+0.45)/1000
# Option Listung in den Maerkten (Kapitel 1): Markt-db bei VP und Gruppen-db
for k,vk,fvk in (('H50',11.99,13.99),('H100',8.99,9.49)):
    d=G[k]; p=vk/UST; pf=fvk/UST
    P("Listung",k,"VK",vk,"Markt-db HM",r(p-d['ein']*1.03,3),r((p-d['ein']*1.03)/p*100,1),"% | Fremd VK",fvk,"Markt-db",r(pf-d['fr_ein']*1.03,3),r((pf-d['fr_ein']*1.03)/pf*100,1),"% | Gruppen-db HM",r(p-d['ein'],3),"Fremd inkl NV",r(pf-d['fr_ein']+d['nvf'],3))
# Pool
uml={'H33':6,'H50':4,'H100':4}; res=1.25
pool_fl=sum(G[k]['n']*G[k]['K']/uml[k]*res for k in G); pool_k=sum(G[k]['K']/uml[k]*res for k in G)
pool_w=(sum(G[k]['n']*G[k]['K']/uml[k]*res*G[k]['flp'] for k in G)+pool_k*KASTEN)/1000
pfand_umlauf=0.5*(pool_fl*0.15+pool_k*1.50)/UST/1000
pool_netto=pool_w-pfand_umlauf
P("Pool Flaschen",r(pool_fl),"Kaesten",r(pool_k),"Wert T€",r(pool_w,1),"Kundenpfand netto (50 % im Umlauf)",r(pfand_umlauf,1),"Nettobindung",r(pool_netto,1))
dEBITDA=HM_RE-disp_RE-FIX_HM-SORT_LOST-VAR_LOG
dU=HM_U-disp_U
P("HM Umsatz",r(HM_U,1),"RE I",r(HM_RE,1),"| verdraengt Umsatz",r(disp_U,1),"RE II",r(disp_RE,1),"| Markenfix",FIX_HM,"Sortierverg weg",r(SORT_LOST,2),"var Log",r(VAR_LOG,2))
P("Delta Umsatz",r(dU,1),"Delta EBITDA=EBIT (kurzfristig)",r(dEBITDA,2),"Prozesskosten langfristig Mehrmenge",r(PK_LANG,1),"Delta EBIT langfristig",r(dEBITDA-PK_LANG+VAR_LOG,2))
# Break-even-Absatz gegenueber Fremdware (langfristig): je zusaetzlicher Kasten Mix
# Zuckersteuer
ZS=0.26
for k,d in G.items(): P("Zuckersteuer je Kasten",k,r(d['n']*d['l']*ZS,2))
P("Zuckersteuer 2027-Menge",r(T['l']*ZS/1000,1),"T€; Liter",r(T['l']))
K28={'H33':20000,'H50':10000,'H100':17000}; K29={'H33':26000,'H50':11000,'H100':18000}
L28=sum(G[k]['n']*G[k]['l']*K28[k] for k in G); L29=sum(G[k]['n']*G[k]['l']*K29[k] for k in G)
P("Liter 2028",r(L28),"Steuer",r(L28*ZS/1000,1)," Liter 2029",r(L29),"Steuer",r(L29*ZS/1000,1), "Fl 2029", sum(G[k]['n']*K29[k] for k in G))
RE28=sum(G[k]['db']*K28[k] for k in G)/1000
P("RE I 2028 bei Preisen 2027",r(RE28,1))
# Target Costing H33 Gastro
alw=12.90*0.60; drift_st=G['H33']['ein']+24*0.33*ZS
ROH_NEU=45/1000*ZUCKERPREIS+0.03+GRUNDSTOFF
drift_ref=G['H33']['ein']+24*0.33*(ROH_NEU-ROH_L)
P("TC H33: Allowable",r(alw,2),"Drifting mit Steuer",r(drift_st,2),"Luecke",r(drift_st-alw,2),"| Rezeptur <5 g: Rohstoff/l",r(ROH_NEU,3),"Drifting",r(drift_ref,2),"Luecke",r(drift_ref-alw,2))
comp={'Rezeptur':24*0.33*ROH_NEU,'Lohnabfuellung':24*0.19,'Verschluss/Etikett':24*VERS,'Leergut-Ersatz':24*SCHW_FL*0.28+SCHW_K*KASTEN,'Fracht':FRACHT}
tot=sum(comp.values())
w={'Geschmack':0.40,'Frische/Kohlensaeure':0.20,'Optik/Auftritt':0.15,'Mehrweg-Handling':0.10,'Lieferfaehigkeit':0.15}
c={'Geschmack':{'Rezeptur':0.85,'Lohnabfuellung':0.15},
   'Frische/Kohlensaeure':{'Lohnabfuellung':0.60,'Rezeptur':0.20,'Verschluss/Etikett':0.20},
   'Optik/Auftritt':{'Verschluss/Etikett':0.60,'Lohnabfuellung':0.20,'Leergut-Ersatz':0.20},
   'Mehrweg-Handling':{'Leergut-Ersatz':0.50,'Lohnabfuellung':0.30,'Fracht':0.20},
   'Lieferfaehigkeit':{'Fracht':0.40,'Lohnabfuellung':0.60}}
for f in c: chk("Spalte 100 %",abs(sum(c[f].values())-1)<1e-9,f)
nutz={k:sum(w[f]*c[f].get(k,0) for f in w) for k in comp}
P("TC Komponenten (Kosten, Kostenanteil, Nutzenanteil, ZKI=Nutzen/Kosten, Zielkosten):")
for k in comp: P("  ",k,r(comp[k],2),r(comp[k]/tot*100,1),r(nutz[k]*100,1),r(nutz[k]/(comp[k]/tot),2),r(alw*nutz[k],2))
P("  Summe",r(tot,2))

# ---------------- 4 Konzern mit Hausmarke ----------------
P("\n=== 4 Konzern mit Hausmarke ===")
dZins=pool_netto*0.08
dEBT=dEBITDA-dZins
dGewSt=0.14*(dEBT+0.25*dZins)
dErg=dEBT-dGewSt
dEntn=0.45*dEBT-dGewSt
KZH=dict(umsatz=KZ['umsatz']+dU, ebitda=KZ['ebitda']+dEBITDA, afa=KZ['afa'], ebit=KZ['ebit']+dEBITDA, zins=KZ['zins']+dZins)
KZH['ebt']=KZH['ebit']-KZH['zins']; KZH['gewst']=KZ['gewst']+dGewSt; KZH['erg']=KZH['ebt']-KZH['gewst']
P({k:r(v,1) for k,v in KZH.items()}, "dZins",r(dZins,2),"dGewSt",r(dGewSt,2),"dEntn",r(dEntn,2))
entn=g['P']['ohne']['entn']+dEntn
BS0=KB['bilsum']+pool_w; EK0=KB['ek']; KK0=KB['kk']+pool_netto; PFV=g['PF_KUNDEN']+pfand_umlauf; ND0=KB['netdebt']+pool_netto
P("01.01.: BS",r(BS0,1),"EK",r(EK0,1),"EKQ",r(EK0/BS0*100,2),"EKQ Pfand saldiert",r(EK0/(BS0-PFV)*100,2),"KK",r(KK0,1),"ND",r(ND0,1),"ND/EBITDA",r(ND0/KZH['ebitda'],2))
dcash=dErg-dEntn
BS1=END['bilsum']+pool_w; EK1=END['ek']+dErg-dEntn; KK1=END['kk']+pool_netto-dcash; ND1=END['netdebt']+pool_netto-dcash
P("31.12. Plan: BS",r(BS1,1),"EK",r(EK1,1),"EKQ",r(EK1/BS1*100,2),"EKQ saldiert",r(EK1/(BS1-PFV)*100,2),"KK",r(KK1,1),"ND",r(ND1,1),"ND/EBITDA",r(ND1/KZH['ebitda'],2), "KK-Anstieg ggü 01.01", r(KK1-KK0,1))
KDF=(KZH['erg']+KZH['afa']+KZH['zins'])/(KZH['zins']+250)
P("KDF",r(KDF,2),"Controller/EBIT",r(75/KZH['ebit']*100,1),"Float inkl HM (Abfueller-Anspr - Kundenpfand - L+L-Saldo)",r(g['PF_ABF']+g['PF_KELT']-PFV-180,1))
chk("Covenants Plan", EK1/BS1>=0.25 and ND1/KZH['ebitda']<=3.5 and KDF>=1.2)

# ---------------- 5 Eckkneipe mit angezeigten Saetzen ----------------
P("\n=== 5 Eckkneipe (angezeigte Saetze) ===")
S=dict(LB=0.39,KOM=0.32,LG=0.35,STOPP=34.16,BES=41.81)
def kneipe(st):
    d={}; d['re']=4200.0; d['lb']=670*S['LB']; d['kom']=670*S['KOM']; d['lg']=670*0.85*S['LG']; d['st']=st*S['STOPP']
    d['db2']=d['re']-d['lb']-d['kom']-d['lg']-d['st']; d['ad']=12*S['BES']; d['afa']=1500.0; d['aus']=240.0
    d['db3']=d['db2']-d['ad']-d['afa']-d['aus']; return d
k52=kneipe(52); k26=kneipe(26)
P("52 Stopps",{k:r(v,1) for k,v in k52.items()})
P("26 Stopps",{k:r(v,1) for k,v in k26.items()})
var_td=(9*(g['fz']["18-t-Lkw (Verteilung)"]['diesel']+g['fz']["18-t-Lkw (Verteilung)"]['maut'])+(g['fz']["7,5-t-Lkw (Innenstadt)"]['diesel']+g['fz']["7,5-t-Lkw (Innenstadt)"]['maut']))/g['TOURTAGE']*1000
var_stopp=var_td/17
P("var je Tourtag",r(var_td,2),"var je Stopp",r(var_stopp,2))
kurz=-4200+52*var_stopp+240
P("Kuendigung kurzfristig (RE weg, Diesel/Maut + Ausfall gespart):",r(kurz,0))
lang=k52['db2']-k52['ad']-k52['aus']
P("langfristig relevanter Beitrag (DB II - AD - Ausfall, AfA versunken):",r(lang,1)," 14-taegig:",r(k26['db2']-k26['ad']-k26['aus'],1))
mbw=34.16/(0.33-0.0567)
P("MBW 34,16/(33 %-5,67 %)",r(mbw,1),"Ø Bestellwert",r(12000/52,2),r(12000/26,2))
# Rhythmusprogramm 120 Kunden
stops=120*26; td=stops/17
P("Rhythmus: Stopps",stops,"Tourtage",r(td,1),"PK-Ersparnis T€",r(stops*34.16/1000,1),"kurzfristig",r(td*var_td/1000,1),r(td*var_td/(stops*34.16)*100,1),"% Fahrer",r(td*228.57/1000,1),"Lkw fix",r(g['fz']["18-t-Lkw (Verteilung)"]['leasing']+g['fz']["18-t-Lkw (Verteilung)"]['sonst'],1),"Auslastung 9 Lkw",r((g['TOURTAGE']-td)/(9*250)*100,1))

# ---------------- 6 Januar 2028: Salden, Bonus, KK ----------------
P("\n=== 6 Januar-Abschluss 2028 ===")
P("Saldo Differenz",62480-61200,"=",880+300+100,"| Werte",r(880*3.10/UST,2),r(300*3.10/UST,2),r(100*3.10/UST,2))
P("Bonus 1 %",r(198400*11.90*0.01,0),"2 %",r(200000*11.90*0.02,0),"Preisrunde 1600x0,60",1600*0.60,"Zins 23,2 T€ 6 Wo 8 %",r(23216*0.08*6/52,0))
kk_ist=KK1+116.7
ues=[12000*78.99/30000, 1600*(11.90+3.10/UST)/1000, 9500*UST*2/365]
P("KK-Ueberleitung",[r(x,1) for x in ues],"=",r(sum(ues),1),"| Plan KK",r(KK1,1),"Ist",r(KK1+sum(ues),1), "Ueberhang je Kasten", r(78.99/30000*1000,3))
EKQ_ist=EK1/(BS1+sum(ues)); ND_ist=ND1+sum(ues)
P("Covenant-Tacho Ist: EKQ",r(EKQ_ist*100,1),"(Plan",r(EK1/BS1*100,1),") ND/EBITDA",r(ND_ist/KZH['ebitda'],2),"(Plan",r(ND1/KZH['ebitda'],2),")")
# Bistro Muehlentor
ford=7.4; quote=0.05
v_ford=ford/UST*(1-quote); v_darl=18.0*(1-quote); v_inv=8.0*0.70
P("Bistro: Forderung netto Ausfall",r(v_ford,2),"USt-Korrektur",r(ford/UST*0.19*(1-quote),2),"Darlehen",r(v_darl,1),"Inventar",r(v_inv,1),"Summe",r(v_ford+v_darl+v_inv,1))
# mit Pruefauftrag im Oktober: Barzahlung ab Nov -> Forderung 2,6 brutto; Inventar gesichert (Verwertung 60 %)
v2=2.6/UST*(1-quote)+18.0*0.60+8.0*0.40
P("Bistro mit Pruefauftrag (Barzahlung ab Nov, Buergschaft 40 %, Inventar frueh zurueck 60 %):",r(v2,1))

# ---------------- 7 Make or Buy (Plan 2029) ----------------
P("\n=== 7 Make or Buy ===")
AEZ={'H33':1.00,'H50':1.15,'H100':1.60}
hm_fl={k:G[k]['n']*K29[k] for k in G}
hm_l={k:hm_fl[k]*G[k]['l'] for k in G}
fr_fl=1_000_000; fr_l=fr_fl*0.5; fr_k=fr_fl/20
aez_hm=sum(hm_fl[k]*AEZ[k] for k in G); aez_fr=fr_fl*AEZ['H50']; aez=aez_hm+aez_fr
rate=4000*0.65; h=aez/rate; h_hm=aez_hm/rate
P("Fl HM",sum(hm_fl.values()),"AEZ",aez_hm,aez_fr,aez,"Stunden",r(h,1),"HM",r(h_hm,1),"Auslastung 1 Schicht",r(h/(225*7.5)*100,1),r(h_hm/(225*7.5)*100,1))
S7=['H1','H2','H3','F1','F2','F3','F4']
WBW={'H1':120,'H2':0,'H3':0,'F1':80,'F2':300,'F3':450,'F4':100}; AHKf=950/1050
qm={'H1':60,'H2':40,'H3':20,'F1':60,'F2':200,'F3':180,'F4':240}
pers={'H1':0,'H2':0,'H3':25,'F1':10.5,'F2':18.25,'F3':31+36.5,'F4':0}
wasser=0.008*aez/1000
prim={s:WBW[s]/10+0.06*WBW[s]*AHKf/2+qm[s]*5*12/1000+pers[s] for s in S7}
prim['H1']+=40.0; prim['H2']+=40.5; prim['F2']+=wasser; prim['H3']+=6.0; prim['F3']+=6.0; prim['F4']+=4.0
k1={'H2':0.03,'H3':0.02,'F1':0.05,'F2':0.55,'F3':0.25,'F4':0.10}
k2={'H3':0.02,'F1':0.08,'F2':0.35,'F3':0.45,'F4':0.10}
k3={'F1':0.40,'F2':0.10,'F3':0.50}
end=dict(prim); ums={}
for hs,kk in (('H1',k1),('H2',k2),('H3',k3)):
    u=end[hs]; end[hs]=0; ums[hs]={s:u*w_ for s,w_ in kk.items()}
    for s_,w_ in kk.items(): end[s_]+=u*w_
P("prim",{s:r(prim[s],1) for s in S7},"Summe",r(sum(prim.values()),1))
for hs in ums: P(" Umlage",hs,{s:r(v,1) for s,v in ums[hs].items()})
P("Endkosten",{s:r(end[s],1) for s in S7 if s.startswith('F')},"Summe",r(sum(end.values()),1))
line=end['F2']+end['F3']; pers_line=pers['F2']+pers['F3']
MSS_o=(line-pers_line)/h*1000; MSS_m=line/h*1000
P("Linie",r(line,1),"MSS ohne Bedienung",r(MSS_o,2),"mit",r(MSS_m,2))
# korrigierte Kalkulation: F1 je Liter, F2+F3 je AEZ (Maschinenzeit), F4 je Kasten
liter_ges=sum(hm_l.values())+fr_l; kaesten_ges=sum(K29.values())+fr_k
s_F1=end['F1']*1000/liter_ges; s_lin=line*1000/aez; s_F4=end['F4']*1000/kaesten_ges
hk={}
for k in G:
    hk[k]=s_F1*G[k]['l']+s_lin*AEZ[k]+s_F4/G[k]['n']
hk_fr=s_F1*0.5+s_lin*1.15+s_F4/20
chk("Kalkulation verteilt alle Fertigungskosten", abs(sum(hk[k]*hm_fl[k] for k in G)+hk_fr*fr_fl-sum(end[s] for s in S7 if s.startswith('F'))*1000)<1)
alt_aez=sum(end[s] for s in S7 if s.startswith('F'))*1000/aez
P("Saetze: F1 €/l",r(s_F1,4),"Linie €/AEZ-Fl",r(s_lin,4),"F4 €/Kasten",r(s_F4,4))
P("HK korrekt je Fl",{k:r(v,4) for k,v in hk.items()},"Kessler 0,5",r(hk_fr,4)," | alles nach AEZ:",{k:r(alt_aez*AEZ[k],4) for k in G})
P("HK je Kasten korrekt",{k:r(hk[k]*G[k]['n'],2) for k in G})
# variable/fixe Kosten
var=32.0+12.0+wasser+54.75; fert=sum(end[s] for s in S7 if s.startswith('F')); fix=fert-var; kv=var*1000/aez
P("fix",r(fix,1),"var",r(var,1),"kv je AEZ",r(kv,4),"kv 0,5 l",r(kv*1.15,4))
lohn27={'H33':0.19,'H50':0.21,'H100':0.25}
def buy(inc,f=1.0): return sum(hm_fl[k]*lohn27[k]*(1+inc) for k in G)/1000*f+40*0.38+7.0
cash_fix=fix-105-28.5
def make_kalk(frq=1.0): fr=fr_fl*frq; return fix+kv*aez_hm/1000+kv*fr*1.15/1000-fr*0.16/1000
def make_cash(frq=1.0,f=1.0): fr=fr_fl*frq; return cash_fix+kv*aez_hm*f/1000+kv*fr*1.15/1000-fr*0.16/1000
for inc in (0.18,0.09,0.0):
    P(f"Buy +{inc*100:.0f}%",r(buy(inc),1),"| Make kalk mit/ohne Kessler",r(make_kalk(1),1),r(make_kalk(0),1),"| Lohn je Fl",{k:r(lohn27[k]*(1+inc),4) for k in G})
for inc in (0.18,0.09):
    lohn_aez=sum(hm_fl[k]*lohn27[k]*(1+inc) for k in G)/aez_hm
    km=fix*1000/(lohn_aez-kv); P(f"krit Menge (+{inc*100:.0f}%) AEZ",r(km),"Fl",r(km/(aez_hm/sum(hm_fl.values()))))
I0=950.0
def rbf(i,n): return (1-(1+i)**-n)/i
def kw(inc,fy,i=0.06,growth=0.0,frq=1.0):
    tot=-I0
    for t in range(1,11):
        f=(1+growth)**(t-1)
        b=buy(inc,f) if f==1.0 else (sum(hm_fl[k]*lohn27[k]*(1+inc) for k in G)/1000*f+15.2+7.0)
        m=make_cash(frq if t<=fy else 0.0,f)
        tot+=(b-m)/(1+i)**t
    return tot
for inc in (0.09,0.18):
    P(f"KW +{inc*100:.0f}%:",{fy:r(kw(inc,fy),1) for fy in (10,9,8,7,5,3,0)})
P("KW +9% K10 HM +5 %/J",r(kw(0.09,10,growth=0.05),1)," K3 HM+5%",r(kw(0.09,3,growth=0.05),1))
def irr(inc,fy):
    lo,hi=-0.3,0.3
    for _ in range(200):
        mid=(lo+hi)/2
        if kw(inc,fy,i=mid)>0: lo=mid
        else: hi=mid
    return mid
P("IZF +9% K10",r(irr(0.09,10)*100,2),"%")
# kritische Laufzeit (stetig)
for inc in (0.09,):
    for fy in range(1,11):
        if kw(inc,fy)>0: P("erste positive Laufzeit",fy); break
s_mit=buy(0.09)-make_cash(1); s_ohne=buy(0.09)-make_cash(0)
P("Ersparnis/Jahr +9%: mit",r(s_mit,1),"ohne",r(s_ohne,1))
# Bruchteil-Jahr fuer KW=0 linear zwischen 9 und 10
a9=kw(0.09,9); a10=kw(0.09,10); P("KW 9J",r(a9,1),"10J",r(a10,1),"Break-even-Laufzeit ≈",r(9+(-a9)/(a10-a9),1),"J")
P("Kessler 0,16 vs HK 0,5 l",r(hk_fr,4),"kv 0,5 l",r(kv*1.15,4))
# Covenants pro forma (Basis Plan 31.12.2027 mit HM, Kredit 950)
for nm,s in (("mit",s_mit),("ohne",s_ohne)):
    P("Covenant",nm,"ND/EBITDA",r((ND1+950)/(KZH['ebitda']+s),2),"EKQ",r(EK1/(BS1+950)*100,1))
P("Erst-probieren: Lohn 2029 +18 % gesamt",r(buy(0.18),1),"Amortisation naiv",r(950/buy(0.18),1),"J")
# Plankosten Juli 2029
fix_line=line-(54.75+wasser+0.80*32+0.80*12); kvh=(54.75+wasser+0.80*32+0.80*12)/h*1000
plan_h=95.0; ist_h=52.0+0.6*43.0; ist_k=30.40
pk=fix_line/12+plan_h*kvh/1000; sk=fix_line/12+ist_h*kvh/1000; vpk=pk/plan_h*ist_h
P("Linie fix/Monat",r(fix_line/12,2),"kv €/h",r(kvh,1),"Ist h",r(ist_h,1),"Plan",r(pk,2),"Soll",r(sk,2),"verr",r(vpk,2),"VA",r(ist_k-sk,2),"BA",r(sk-vpk,2),"Ges",r(ist_k-vpk,2))
P("Normal-MSS Jahr",r(MSS_m,2),"verrechnet Juli",r(MSS_m*ist_h/1000,2),"Unterdeckung",r(ist_k-MSS_m*ist_h/1000,2))
# Hollmann (IHK-Schema)
mk=418.5/4; fl_=176/4; en=16.0*1.40; rein=9.5
hkH=mk+fl_+en+rein; sk_=hkH*1.15; pr=sk_*1.08
P("Hollmann HK",r(hkH,2),"VwGK10",r(hkH*0.10,2),"VtGK5",r(hkH*0.05,2),"SK",r(sk_,2),"Gewinn",r(sk_*0.08,2),"Preis",r(pr,2),"vs 190:",r((pr/190-1)*100,1))
eA=35/4*1.15*1.08; eB=16*0.28*1.15*1.08
pr_k=pr-eA-eB; eC=((383.5+176)/4000*1000-(383.5+176)/4200*1000)*1.242
P("A",r(eA,2),"B",r(eB,2),"korr",r(pr_k,2),r((pr_k/190-1)*100,1),"C",r(eC,2),"->",r(pr_k-eC,2),r(((pr_k-eC)/190-1)*100,1))
# Vorlage 2: Zuschlagskalkulation (Lohnabfueller B, je 1.000 Fl 0,5 l)
def zk(mat,mgk,lohn,fgk_satz,energie_extra,sekf):
    MK=mat*(1+mgk); FK=lohn+lohn*fgk_satz+energie_extra+sekf; HK=MK+FK; SK=HK*1.15; return dict(MK=MK,FGK=lohn*fgk_satz,FK=FK,HK=HK,SK=SK,P=SK*1.08)
a=zk(15.0,0.10,40.0,1.75,0.0,6.0)
f=zk(16.5,0.10,42.4,1.95,18.0*0.25,6.0)
# berechtigt: FGK = Energie 18 x 1,25 + Rest 52 unveraendert
bb=dict(MK=16.5*1.1); bb['FK']=42.4+18*1.25+52.0+6.0; bb['HK']=bb['MK']+bb['FK']; bb['P']=bb['HK']*1.15*1.08
P("ZK 2027",{k:r(v,2) for k,v in a.items()},"| Forderung",r(f['P'],2),r((f['P']/a['P']-1)*100,1),"% | berechtigt",r(bb['P'],2),r((bb['P']/a['P']-1)*100,1),"% FGK-Satz berechtigt",r((18*1.25+52)/42.4*100,1))

# ---------------- 8 Uebezeit ----------------
# Hausmarke 2029 langfristig (Volumen 2029, Buy +9 %), Break-even Lohnsenkung 2027
lohn_HM27=T['lohn']/1000
dEBT_lang=dEBITDA-PK_LANG+VAR_LOG-dZins
P("HM 2027 Delta EBT kurzfristig",r(dEBITDA-dZins,1),"langfristig",r(dEBT_lang,1),"Lohnsenkung fuer Delta=0 langfristig",r(-dEBT_lang/lohn_HM27*100,1),"%")
def hm_delta(Kd,lohnfak,fixhm=37.0):
    Tl=dict(RE=0,REf=0,K=0,l=0)
    for k,d in G.items():
        ein=d['ein']+d['n']*d['lohn']*(lohnfak-1)
        Tl['RE']+=(d['pavg']-ein)*Kd[k]; Tl['REf']+=(d['dbf']+d['nvf'])*Kd[k]; Tl['K']+=Kd[k]
    pool=pool_netto*Tl['K']/T['K']
    return (Tl['RE']-KANN*Tl['REf'])/1000-fixhm-KANN*Tl['K']*0.09/1000-(1-KANN)*Tl['K']*1.07/1000-pool*0.08
P("HM 2029 Delta EBT langfristig: Buy+9%",r(hm_delta(K29,1.09),1),"Lohn 2027",r(hm_delta(K29,1.0),1))
P("\n=== 8 Uebezeit ===")
skills=190; reviews=9; total=skills*reviews; frueh=total*0.5
P("Abrufe",total,"davon Fruehschicht",frueh,"h bei 0,8 min",r(frueh*0.8/60,1))
P("Checks:",len(CK))

# ---------------- 9 HB3-Kennzahlen Konzern mit Hausmarke (01.01.2027 / Plan) ----------------
P("\n=== 9 HB3-Kennzahlen ===")
AV=40+1146+pool_w+900+1200
FK=BS0-EK0
zins_brutto=KZH['zins']+36.0
rGK=(KZH['erg']+zins_brutto)/BS0; iFK=zins_brutto/FK; rEK=KZH['erg']/EK0
P("AV",r(AV,1),"Anlagendeckung II",r((EK0+1750)/AV*100,1),"%  ROI DuPont",r(KZH['ebit']/KZH['umsatz']*100,2),"x",r(KZH['umsatz']/BS0,2),"=",r(KZH['ebit']/BS0*100,2),"%")
P("rGK",r(rGK*100,2),"Ø i FK",r(iFK*100,2),"rEK",r(rEK*100,2),"Leverage-Check",r((rGK+(rGK-iFK)*FK/EK0)*100,2),"| verzinsl. FK-Zins",r(zins_brutto/(2000+KK0)*100,2))
kurzV=KK0+1733.7+PFV+265.0+250+302.5
liq2=206.2+1417.8+290+93+6.0+1057.5
P("Liquiditaet 2. Grades brutto",r(liq2/kurzV*100,1),"% ohne Pfand beidseitig",r((liq2-1057.5)/(kurzV-PFV)*100,1),"%")
cfo=KZH['erg']+KZH['afa']; cfi=-355.0-300+250; cff=-250-entn
P("KFR indirekt: CFO",r(cfo,1),"CFI",r(cfi,1),"CFF",r(cff,1),"Delta Fonds",r(cfo+cfi+cff,1),"Entnahmen",r(entn,1))
# Markt 1 Januar
m1=M['M1']; uj=2150*0.065; rej=uj*m1['reI']/m1['umsatz']
saison=[rr for rr in g['ROSTER']['M1'] if rr[0].startswith('Saison')][0][2]
pj=(m1['pers']-saison)/12; sj=m1['sach']/12; ebitj=rej-0.005*uj-pj-sj-m1['umlage']/12*0+(-0.015*uj)-m1['afa']/12
P("Markt 1 Januar: Umsatz",r(uj,2),"RE",r(rej,2),r(rej/uj*100,1),"Pers",r(pj,1),"Sach",r(sj,1),"Umlage",r(0.015*uj,1),"AfA",r(m1['afa']/12,1),"EBIT",r(ebitj,1), "WE", r(uj-rej,1))
# Gastro-Darlehen Barwert Zinsnachteil
pv=sum(0.03*(30-5*(t-1))/1.06**t for t in range(1,7)); P("Darlehen 30 T€ PV Zinsnachteil",r(pv,2))
# Newsvendor L09 Markt 1
from statistics import NormalDist
vp09=3.50*0.94*1.03; cu=5.99/UST-vp09+0.50; co=0.11; cr=cu/(cu+co); z=NormalDist().inv_cdf(cr)
P("Newsvendor: VP",r(vp09,3),"Cu",r(cu,3),"CR",r(cr,3),"z",r(z,3),"Q",r(600+z*120,0))
P("Checks:",len(CK))
