# Engeto_p3

Jedná se o třetí projekt v rámci kurzu Engeto. Election Scraper. 

## Popis projektu

Election Scraper slouží k získání dat z výsledků parlamentních voleb v roce 2017. Odkaz je [zde.](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

## Instalace knihoven

Knihovny použité v kódu jsou uloženy v souboru requirements.txt. Pro instalaci doporučujipoužít nové virtuální prostředí a s naistalovaným manažerem použít tyto příkazy:

- pip3 --version
- pip3 install -r requirements.txt

## Spuštění projektu

Pro správný běh je potřeba zadat dva argumenty:
- odkaz na "Výsledky hlasování za územní celky – výběr obce"
- jméno souboru do kterého budou data uložena

## Ukázka projektu

Výsledky hlasování pro okres Ostrava - Město:

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106
2. argument: vysledky_ostrava.csv

Spuštění programu:

    python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106" "vysledky_ostrava.csv"

Průběh stahování:

    Získávám data z https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106
    Zapisuji data do souboru vysledky_ostrava.csv
    Ukončuji Elections Scraper

Částečný výstup:

    code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,....
    569119,Čavisov,419,318,316,29,0,0,22,0,16,34,4,2,2,0,0,36,0,0,5,103,0,0,27,0,1,2,0,29,4
    506711,Dolní Lhota,1 202,904,899,95,2,0,69,0,31,41,9,3,2,1,1,90,0,0,25,356,0,2,65,0,6,7,0,91,3
    569500,Horní Lhota,691,480,474,49,0,0,39,1,17,52,5,4,1,0,0,38,0,0,8,152,0,0,19,0,2,5,0,82,0
    599549,Klimkovice,3 652,2 449,2 434,230,0,0,166,1,56,200,32,16,34,3,6,292,0,4,97,835,2,0,156,2,22,8,7,256,9










