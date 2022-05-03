# Käyttöohje
Projektin uusimman releasen lähdekoodi ladataan valitsemalla Assests-osiosta Source code.

## Ohjelman käynnistäminen
1. Ensin asenna riippuvuudet komennolla:
```bash
poetry install
```
2. Seuraavaksi täytyy suorittaa aloitustoimenpiteet komennolla:
```bash
poetry run invoke build
```
3. Nyt sovellus on valmiina käytettäväksi ja voit käynnistää sen komennolla:
```bash
poetry run invoke start
```
## Sovellukseen kirjautuminen
Sisäänkirjautuminen tapahtuu alla olevassa näkymässä:

![login.png](./pictures/kayttoohje-kirjautuminen.png)

Voit kirjautua sisään sovellukseen omalla käyttäjätunnuksella ja salasanalla. Syötä käyttäjätunnus ja salasana omiin syötekenttiinsä ja paina _LOG IN_- painiketta. Jos sinulla ei ole vielä käyttäjää, voit luoda sen painamalla _Create a new user_-painiketta, jolloin siirryt käyttäjän luomisnäkymään.

## Uuden käyttäjän luominen
Uuden käyttäjän luominen tapahtuu alla olevassa näkymässä:

Voit luoda uuden käyttäjän keksimällä itsellesi käyttäjätunnuksen ja salasanan ja kirjaittamalla ne omiin syötekenttiinsä. Painamalla _CREATE USER_- painiketta uusi käyttäjä luodaan ja siirryt auytomaattisesti takaisin kirjautumissivulle, jossa voi kirjautua sisään aikaisemman ohjeen mukaan.

## Kotinäkymän toiminnot
Voit siirtyä kirjaamaan tuloja ja menoja sekä kirjautua ulos alla olevassa näkymässä:

Painamalla _Eneter new expense or income_- painiketta pääset kirjaamaan tuloja ja menoja. Painamalla _LOG OUT_- painiketta voit kirjautua ulos sovelluksesta.

## Tulojen ja menojen kirjaaminen
Tulojen ja menojen kirjaaminen tapahtuu alla olevassa näkymässä:

Voit kirjata uusia menoja _New expense_- otsikon alla. Valitse ensin valikosta sopiva kategoria ja kirjoita syötekenttään menon määrä. Sen jälkeen paina punaista _Enter_- painiketta. 

Voit kirjata uusia tuloja _New income_- otsikon alla. Kirjoita syötekenttään tulon määrä ja paina sen jälkeen vihreää _Enter_- painiketta.

Pääset takaisin katselemaan kotinäkymään katselemaan yhteenvetoa tuloista ja menoista painamalla koti- kuvaketta.





