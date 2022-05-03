# Arkkitehtuuri

## Rakenne
Ui sisältää tiedostot, jossa ovat kirjautumissivu, uuden käyttäjän luontiin tarkoitettu sivu, tulojen ja menojen kirjaamissivu sekä sivu, jossa on yhteenveto tuloista ja menoista eli ui vastaa käyttöliittymästä. Services vastaa sovelluslogiikasta ja repositories vastaa koodista, jolla tallennetaan tietoja tietokantaan. Entities sisältää tiedostot, joissa oleva koodi kuvastaa käyttäjän sekä tulojen ja menojen muotoa.

![rakenne](./pictures/rakenne.png)

## Sovelluslogiikka
Sovelluksen luokka User kuvaa käyttäjiä, Expense menoja ja Income tuloja. Nämä luokat kertovat, mitä tietoja sovelluksessa tallennetaan tietokantaan. Sovelluksen tietomalli näyttää siis seuraavalta:

Itse sovelluksen toiminnot ovat `BudgetServices`-luokassa, jossa on eri metodit jokaiselle toiminnolle. UserRepository ja BudgetRepository vastaavat tietojen tallentamisesta tietokantaan niiden omiin alustettuihin tietokantatauluihin. `BudgetServices` taas saa käyttäjiin sekä tuloihin ja menoihin liittyvät tiedot UserRepositoryn ja BudgetRepositoryn avulla.
Sovelluksen eri osien suhdetta voidaan kuvata seuraavalla pakkauskaaviolla:


## Toimintalogiikka

### Luodaan uusi käyttäjä
Sovellus toimii alla olevan sekvenssikaavion mukaan, kun uuden käyttäjän luomisikkunassa käyttäjä syöttää oikeanlaisen käyttäjätunnuksen ja salasanan ja painaa *CREATE USER* -nappia.

![create_user_sek](./pictures/create_user_sek.png)

*CREATE USER* -napin painaminen kutsuu `BudgetServices` luokan `create_user` metodia ja parametreiksi ottaa käyttäjän syöttämät tiedot. `UserRepositoryn` avulla selvitetään onko käyttäjänimi käytössä ja jos ei ole, luodaan käyttäjä `User`-oliona ja tallettaa sen tietokantaan `UserReporitoryn` metodilla `create`. Seuraavaksi käyttöliittymä vaihtaa näkymäksi kirjautumisikkunan ja käyttäjä voi kirjautua sovellukseen luomallaan käyttäjätunnuksella ja salasanalla.

### Kirjaudutaan sovellukseen
Sovellus toimii alla olevan sekvenssikaavion mukaan, kun kirjautumisikkunassa käyttäjä syöttää käyttäjätunnuksensa ja salasanansa ja painaa *LOG IN* -nappia.

![login_sek](./pictures/login_sek.png)

*LOG IN* -napin painaminen kutsuu `BudgetServices` luokan `login` metodia ja parametreiksi ottaa käyttäjän syöttämät käyttäjätunnuksen ja salasanan. `UserRepositoryn` avulla selvitetään onko käyttäjänimi olemassa ja täsmääkö salasanat. Jos käyttäjä löytyy ja salasana on oikein, käyttäjä kirjataan sisään ja käyttöliittymä vaihtaa näkymäksi budget-appin aloitus- eli kotisivun.
