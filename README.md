# **Budjet-app**
Käyttäjät voivat sovelluksella budjetoida omia kulujaan. Sovelluksessa jokainen käyttäjä rekistöröityy sovellukseen, jolloin jokainen käyttäjä voi seurata omia tulojaan ja menojaan.
## Dokumentaatio
#### Määrittelydokumentti 
[vaatimusmaarittely.md](https://github.com/sannituomisto/ot-harjoitustyo/blob/master/budjet-app/dokumentaatio/vaatimusmaarittely.md)
#### Työaikakirjanpito
[tyoaikakirjanpito.md](https://github.com/sannituomisto/ot-harjoitustyo/blob/master/budjet-app/dokumentaatio/tyoaikakirjanpito.md)
#### Changelog
[changelog.md](https://github.com/sannituomisto/ot-harjoitustyo/blob/master/budjet-app/dokumentaatio/changelog.md)
## Asennus
1. Asenna riippuvuudet komennolla:
```bash
poetry install
```
2. Suorita vaadittavat alustustoimenpiteet komennolla:
```bash
poetry run invoke build
```
3. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```
