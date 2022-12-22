# **Budget-app**
Käyttäjät voivat sovelluksella budjetoida omia kulujaan. Sovelluksessa jokainen käyttäjä rekistöröityy sovellukseen, jolloin jokainen käyttäjä voi seurata omia tulojaan ja menojaan.
## Dokumentaatio
#### Määrittelydokumentti 
[vaatimusmaarittely.md](https://github.com/sannituomisto/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/vaatimusmaarittely.md)
#### Käyttöohje
[kayttoohje.md](https://github.com/sannituomisto/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/kayttoohje.md)
#### Työaikakirjanpito
[tyoaikakirjanpito.md](https://github.com/sannituomisto/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/tyoaikakirjanpito.md)
#### Changelog
[changelog.md](https://github.com/sannituomisto/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/changelog.md)
#### Arkkitehtuuri
[arkkitehtuuri.md](https://github.com/sannituomisto/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/arkkitehtuuri.md)
#### Testaus
[testaus.md](https://github.com/sannituomisto/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/testausdok.md)
#### Releases
- [viikko5 release](https://github.com/sannituomisto/ot-harjoitustyo/releases/tag/viikko5)
- [viikko6 release](https://github.com/sannituomisto/ot-harjoitustyo/releases/tag/viikko6)
- [loppupalautus](https://github.com/sannituomisto/ot-harjoitustyo/releases/tag/Loppupalautus)

## Asennus
1. Riippuvuudet asennetaan komennolla:
```bash
poetry install
```
2. Aloitustoimenpiteet suoritetaan komennolla:
```bash
poetry run invoke build
```
3. Sovellus käynnistetään komennolla:
```bash
poetry run invoke start
```
## Testaus
Testit suoritetaan komennolla:

```bash
poetry run invoke test
```
## Testikattavuus
Testikattavuusraportin saa komennolla:
```bash
poetry run invoke coverage-report
```
Testikattavuusraportin löytää htmlcov-hakemistosta index.html-tiedostosta.

## Pylint-tarkistukset
Pylint-tarkistukset suoritetaan komennolla:
```bash
poetry run invoke lint
```
