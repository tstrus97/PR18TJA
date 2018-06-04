Sodelujoči
- Tomaž Štrus
- Anže Košir
- Jan Harej

O projektu:
Iz platforme Steam, namenjenu predvsem za distrubicijo video iger, bomo zbrali podatke igrah več ljudi, ter analizirali stvari kot so npr. koliko iger, ki jih kupijo dejansko preigrajo, kolika časa bo nekdo zapravil za neko igro, kakšno igro bo kupil naslednjo, glede na svoje igre ipd.

Podatki:
Uporabili bomo API, ki ga ponuja Steam: https://developer.valvesoftware.com/wiki/Steam_Web_API#JSON
Tu lahko dobimo podatko o čisto vsemu kar potrebujemo npr. o uporabniku, njegove igre, prijatelji, koliko ur je igral neko igro, ...
Dobili bomo podatke za npr. 100.000+ uporabnikov (prijatelji naših prijateljev, in njihov prijateljev itd.).

PROJEKTNI PODATKI:
  - posamezen uporabnik ( odprt/zaprt profil, št. prijateljev, št. iger, statistika posamezne igre)
  - posamezne igre ( splošni podatki in statistike igre )
  - nakupi uporabnikov ( kdaj je kupil neko igro )
  - dosežki v igrah za posameznega uporabnika
  - "ban" posameznih igralcev v neki igri ( vsak uporabnik ima nabor "banov" za posamezno igro )
  - "family share" iger za posameznega uporabnika 
  
TRENUTNA VPRAŠANJA:
- [x] Nojbolj kupljena in najbolj igrana igra
- [ ] Povprečno dokončanje igre
- [ ] Število in vrsta Bannov v povezavi z javnimi/privatnimi profili
- [ ] Najmanjkrat odklenjeni dosežki za igrane igre
- [ ] Število prijateljev glede na "starost" računa
- [ ] Nakupi iger v posameznih obdobji (steam sale)
- [ ] Delitev igralcev glede na državo
- [ ] Ali lahko ugotovimo, kakšno igro moramo izdelati za komercialni uspeh? Najbrž lahko preko dosežkov ugotovimo, ali je igra pretežka ali prelahka.
 ISKANJE OSAMELCEV:
  - Hipoteza: igralci glede na dosežke se delijo na tiste, ki jih ne zanimajo, tiste ki jih nekaj dobijo in "achievement hunterje",   tu bomo poskušali najti te igralce.

 # TU JE POROČILO

# Steam web api data mining
## Data
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
Pri najlažjih igrah opazimo, da imajo zelo veliko dosežkov. Ampak pri večina teh iger, je mogoče igro končati v približno uri in dobiti vse dosežke... le zakaj
 
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

## Analiza prepovedi igranja (Ban)
Najprej nas zanima, je razlika med uporabniki z privatnim in odprtim profilom?
### VAC ban
![Alt text](assets/vac_bans_vis.png?raw=true)
### Economy ban
![Alt text](assets/economy_bans_vis.png?raw=true)
### Game ban
![Alt text](assets/bame_bans_vis.png?raw=true)

Vidimo, da je malenkostna razlike med procenti banov privatnih in javnih profilov, še posebaj pri VAC banih. Torej mit, da če imaš privatni profil, si heker imalo nekaj resnice. Kakšna pa je razlika med banim v različnih državah? 
![Alt text](assets/bans_country.png?raw=true)
