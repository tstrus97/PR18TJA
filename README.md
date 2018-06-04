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

<<<<<<< HEAD
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
=======
 --- TU JE POROČILO ---
![Alt text](assets/country.png?raw=true)
![Alt text](assets/nameDistribution.png?raw=true)
>>>>>>> b31e20648f605f224dff233952e233994ef06429
![Alt text](assets/boughtGames.png?raw=true)
![Alt text](assets/mostPlayed.png?raw=true )


![Alt text](assets/hardestGames.png?raw=true )
![Alt text](assets/easyAchievents.png?raw=true )
 
![Alt text](assets/nameDistribution.png?raw=true)
