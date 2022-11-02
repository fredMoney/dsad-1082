link csv: https://drive.google.com/drive/folders/18AakZ7l8thAQOFPjXa92e1Vzj-FJ-mpZ

În fișierul IndustriaAlimentara.csv se află informații privind numărul de angajați în industria
alimentară la nivel de localitate. Informațiile sunt următoarele:
Siruta - Codul Siruta al localității;
Localitate - Denumirea localității;
Carne, Peste, LegumeFructe, Uleiuri, Lactate, Morarit, Panificatie - Valorile reprezentând
numărul de angajați pe principalele activități din industria alimentară.
În fișierul PopulatieLocalitati.csv se află populația pe localități și indicativele de județ pentru
fiecare localitate.
Cerințe:
1. Să se salveze în fișierul Cerinta1.csv datele privind numărul de angajați pe activitățile din
industria alimentară, pentru localitățile în care numărul de angajați este mai mare decât 0. Fișierul
Cerinta1.csv va avea aceleași coloane ca fișierul IndustriaAlimentara.csv.
2. Să se salveze în fișierul Cerinta2.csv numărul mediu de angajați pe fiecare activitate la nivel de
județ. Se va calcula media ponderată, folosind ca pondere populația localităților.
3. Să se calculeze și să se afișeze în fișierul Cerinta3.csv indicii de localizare la nivel de județ
pentru fiecare activitate. Un indice de localizare se calculează ca raport între ponderea județului i
în activitatea j la nivel național și ponderea populației din județul i în totalul populației.
De exemplu dacă pentru județul x numărul de angajați în industria cărnii este de 3000 de persoane
și populația este de 200000 de locuitori, iar la nivel național numărul de angajați în industria cărnii
este de 100000 de persoane iar populația țării este de 20000000 locuitori, indicele de localizare
pentru industria cărnii în județul x este: (3000/100000)/(200000/20000000) = 3.
4. Să se determine matricea de corelații pentru activitățile din industria alimentară la nivel de județ
și să se traseze corelograma
5. Să se traseze graficele linie după indicii de localizare la nivel de județ
6. Să se traseze hărțile după indicii de localizare la nivel de județ

Observație
Media ponderată pentru o serie de observații xi
, i = ̅1̅̅,̅𝑛̅ și ponderi pi
, i = 1̅̅̅,̅𝑛̅ se calculează după
relația: 𝑥̅= ∑ 𝑥𝑖𝑝𝑖
𝑛
𝑖=1
.