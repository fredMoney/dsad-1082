Tema 4.1
În fișierul Etnicity.csv se află date privind populația pe etnii la nivelul localităților conform
Recensământului Populației și Locuințelor din 2011. În fișierele Coduri_Localiatati.csv,
Coduri_Judete.csv și Coduri_Regiuni.csv sunt codificările localităților, județelor, regiunilor și
macroregiunilor României.
1. Să se calculeze și să se salveze populația pe etnii la nivelul județelor, regiunilor și
macroregiunilor
2. Să se calculeze și să se salveze indicii de segregare etnică la nivelul județelor. Vor fi utilizați
următorii indici:
Indicele de disimilaritate, D = 1/
2
∑ |
𝑥𝑖/
𝑇𝑥
−
𝑟𝑖/
𝑇𝑟
|
𝑛
𝑖=1
Shannon-Weaver, H = − ∑ 𝑝𝑖
log2 𝑝𝑖
𝑛
𝑖=1
unde n este numărul de unități administrativ-teritoriale, xi
este populația de o anumită etnie, ri
este
restul populației, Tx
este totalul populației de etnia respectivă, Tr
este totalul restului populației, pi
este ponderea etniei la nivelul unității administrativ-teritoriale i față de totalul etniei.