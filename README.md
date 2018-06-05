
# Steam web api data mining
## Sodelujoči
- Tomaž Štrus
- Anže Košir
- Jan Harej

## Data
Uporabili bomo API, ki ga ponuja Steam: https://developer.valvesoftware.com/wiki/Steam_Web_API#JSON , ven smo dobili naslednje:
* 100k Users (name, username, country, game library, playtime, bans)
* 61k Games (name, achievements, achievements completion)

## Uporabniki razdeljeni po državah
Kot vidimo v spodnjem grafu, nimamo toliko problema, da bi imeli preveč slovenskih uporabnikov, ampak jih imamo porazdeljenih po celem svetu.
![Alt text](assets/country.png?raw=true)

## Kupljene igre uporabnikov  (samo za naše prijatelje)
V naslednjih grafim bomo naredili analizo knjižnjice iger, žal smo lahko dobili podatke za samo 600 uporabnikov, ki so bili naši prijatelji, tako da se podatki zelo prilagajajo tudi igram, ki jih imamo mi sami.
![Alt text](assets/boughtGames.png?raw=true)
![Alt text](assets/mostPlayed.png?raw=true )

## Podatki iger
Tukaj poskušam najti najtežje in najlažje igre. Za vsak dosežek vsake igre vemo koliko procentov ljudi so ga naredili. Torej najtežja igra, sem predpostavil da je tista, ki ima povprečno najmanjše procente dokončanje dosežkov po igralcih.
![Alt text](assets/hardestGames.png?raw=true )
![Alt text](assets/easyAchievents.png?raw=true )
Tukaj vidimo, da so med najlažjimi igrami same take, ki imajo zelo veliko dosežkov. Poglej koliko je največ teh dosežkov v igri.
![Alt text](assets/numOfAchievemnts.png?raw=true )
Če pogledamo te igre bližje, vidimo, da se jih večina konča v manj kot uri. Poglejmo kakšne imajo dejansko dosežke:


Dosežki igre z največ dosežki:  
![Alt text](assets/ach2.png?raw=true )  


Dosežki igre z drugim največjim dosežkim:  
![Alt text](assets/ach1.png?raw=true )  


Vidimo, da  sta to igre, kjer lahko "farmamo" dosežke, ker nekateri uporabniki to radi počnejo. Ampak niso vse igre take, četrta najboljša igra ima dejansko veliko dosežkov, njen čas dokončanja pa je kar 400 urni.  
![Alt text](assets/ach3.png?raw=true )  

## Podobnost med vzdevkom in imenom uporabnika
Tukaj bomo po Jaro indeksu razdalje pogledali razliko med vzdevkom in imenom uporabnika. Tukaj vidimo porazdelitev
![Alt text](assets/nameDistribution.png?raw=true)  


Vidimo, da ima od vradnost indeksa od 0.7 do 1 samo 10% uporabnikobv. Ti imajo izpeljanke imen, kot so nasledni:
VZDEVEK, IME
* 'Thorvald', 'Thorvald ter Meer'
* 'Berra', 'Bernardo'
* 'Robingg', 'Robin B'
* 'KentKennedy #Akk!', 'Kent Kennedy'
* 'Bostjan88', 'Bostjan'
* 'AnzeDragar', 'Anze Dragar'
* 'Nikkoff', 'Nikko'
* 'ninos10', 'nino'
* 'NinaFin', 'Nina Fininis'
* 'Justin500 DE', 'Justin'
* 'JacobofGames', 'Jacob'
* 'Robertbtw', 'Robert'
* 'xXxBen_DoverxXx', 'Ben Dover'  

Skoraj 35% uporabnikov ima ime čisto drugačno kot vzdevek, torej jih na internetu nočejo povezovati. Za ostale uporabnike pa ne moramo točno vedeti ali so izpeljanke ali ne, ker nam to indeks ne omogoča.  
## Analiza prepovedi igranja (Ban)
Najprej nas zanima, je razlika med uporabniki z privatnim in odprtim profilom?
### VAC ban
![Alt text](assets/vac_bans_vis.png?raw=true)
### Economy ban
![Alt text](assets/economy_bans_vis.png?raw=true)
### Game ban
![Alt text](assets/bame_bans_vis.png?raw=true)

Vidimo, da je malenkostna razlike med procenti banov privatnih in javnih profilov, še posebaj pri VAC banih. Torej mit, da če imaš privatni profil, si heker imalo nekaj resnice.  
Kakšna pa je razlika med banim v različnih državah? 
![Alt text](assets/bans_country.png?raw=true)  
Tukaj je precejšna razlika med Romuni in Rusi. Med Romuni in Slovenci je kar 15% razlika v številu banov uporabnikov.
