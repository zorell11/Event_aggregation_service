# Služba sdružování událostí

## Projekt structure
#### projekt name:
- event_portal

#### applications:
- events
- users
- cart

#### Main menu:
- Domov(Hlavna stranka)
- Divadlo
- Hudba
- Festival
- Sport
- Zabava
- Ostatne


### Ideas:
- [ ] login via FB or google account 
- [ ] komentar na ktory odpove oranizator 
- [ ] organizatorovi sa po prihlaseni zobrazi notifikacia o novom komentari k eventu, aj pri kupe listka
- [ ] viacjazykova stranka
- [ ] create event wathclist for user


## Stručný popis systému
Součástí tohoto projektu je vytvoření webové stránky, která organizátorům akcí umožní přidávat akce a vybírat na ně vstupné. Přihlásit se může jakýkoliv registrovaný uživatel. Web by měl mít také vyhledávač událostí (s několika kritérii) a API, které umožní prezentaci na jiných stránkách / službách
## Hlavní funkce systému
- [x] Registrace a přihlašování uživatele.
- [ ] Vytváření a úprava událostí organizátorem (uživatel se speciální rolí).
- [x] Komentování událostí přihlášenými uživateli.
- [x] Přihlašování na akce.
- [x] Vyhledávač událostí.
- [ ] API pro ostatní webové stránky / služby, kde budou akce prezentovány.
## Obecné pokyny
Vývoj webové stránky za použití Django a Django REST Framework jako API.
Zavedení rozdělení na modely, zobrazení a ovladače v aplikaci a pro každý z nich využití vhodné logiky.
Zabezpečení přístupu k aplikaci a jejím funkcím pomocí django.contrib.auth.
## Funkcionality
Domovská stránka
vytvoření prvního ovladače a náhledu souboru
vytvoření souborů s definovaným stylem / scriptem (bootstrap + případný vlastní), který bude připojen ke každé následující stránce (včetně)
stránka by měla mít název a v horní části by měla obsahovat tlačítko pro přihlašování a registraci
## Registrace uživatele 
- [ ] registrační formulář by měl obsahovat:
  - [x] přihlašovací údaje (email) – s kontrolou správnosti emailu,
  - [x] heslo - musí sestávat nejméně z 8 znaků (ne však z více než 30 znaků),
  - [x]  zobrazované jméno – toto pole nemůže zůstat prázdné nebo obsahovat pouze mezery, maximální délka je 50 znaků.
  - [X]  email použitý k registraci může být použit pouze jednou.
  - [X]  uživatel by měl mít přiřazené systémové role, které budou pokrývat alespoň dva případy: organizátor a běžný uživatel. 
  - [X] Každá registrovaná osoba automaticky získává roli „standardního uživatele“.
  - [x]  heslo je uloženo v databázi ve formě, která zabraňuje jeho záměrnému prolomení / obnovení
## Přihlášení uživatele
- [x] přihlašovací formulář obsahuje přihlašovací <s>jméno</s> email a heslo.
- [X] přihlašování pomocí django.contrib.auth (pro vytvoření příslušné konfigurace).
- [X] po úspěšném přihlášení by měl být uživatel přesměrován na domovskou stránku, kde se místo tlačítek Přihlášení / Zaregistrovat se zobrazí informace: "Přihlášen jako: email
## Přidání nové události
### Událost musí obsahovat minimálně následující body:
- [x] název – pole nemůže zůstat prázdné nebo obsahovat pouze mezery,
- [X] datum od/do – povinné (volitelné zaškrtnutí, zda jde o budoucí datum),
- [x] popis – minimálně 20 znaků.
- [x] událost musí být spojena s uživatelem, který ji přidal
## Seznam událostí
- [x] na úvodní stránce v centrální části by měl být umístěn seznam všech aktuálních akcí
- [x] každý prvek seznamu by měl obsahovat:
  - [x] zvýrazněný titulek s názvem události,
  - [x] datum akce od/do,
  - [x] prvních 50 znaků popisu.
- [ ] události by měly být seřazeny od těch, které se budou konat nejdříve.
## Vyhledávač událostí
#### V horní části domovské stránky by měl být formulář, který bude obsahovat:
  - [x] textové pole pro zadání fráze,
  - [ ] volitelné (rozbalovací seznam): 
    - [ ] budoucí, 
    - [ ] probíhající 
    - [ ] budoucí, 
    - [ ] vše,
    - [ ] tlačítko "hledat".
  - [x] zadaná fráze se má hledat v názvu.
  - [x] výsledky vyhledávání by měly být na samostatné stránce ve stejném rozložení jako na domovské stránce.
  - [ ] stránka s výsledky vyhledávání by také měla obsahovat vyhledávací formulář jako na domovské stránce a jeho pole by měla být nastavena podle aktuálně zvolených kritérií.
## Detail zobrazení události
#### Samostatná stránka, na které budou viditelné všechny podrobnosti události: 
- [ ] název, 
- [ ] data od / do, 
- [ ] úplný popis.
- [ ] název je propojen na domovské stránce a na stránce s výsledky vyhledávání, takže po kliknutí je uživatel přesměrován na stránku konkrétní události.
## Přidávání komentářů k události
- [x] pod obecnými informacemi o události přidejte formulář pro vložení komentáře.
- [x] komentář může mít až 500 znaků.
- [x] pouze přihlášený uživatel může přidat komentář.
- [x] komentáře by měly být seřazeny od těch nejnovějších.
## Přihlašování na událost
- [ ] na stránce události by měla být přidána možnost (tlačítko) přihlásit se k odběru, pouze však pro přihlášené uživatele.
- [ ] pokud je aktuální uživatel již zaregistrován, místo tlačítka uvidí příslušné informace a volitelně tlačítko pro odhlášení z události.
- [ ] vedle obecných informací o akci uveďte seznam všech aktuálně registrovaných uživatelů.
## API pro jiné weby - seznam událostí
#### API by mělo splňovat doporučení REST.
- [ ] metoda by měla vrátit seznam všech budoucích událostí.
- [ ] volitelně může dodatečně povolit filtrování vrácených událostí na časové období.
## Aplikace zobrazující události stažené z API
- [ ] je nutné sestavit druhou aplikaci (Django), která bude využívat API události a zobrazovat seznam v některých zobrazeních
- [ ] volitelné: přidání možnosti filtrování událostí v aplikaci podle zvoleného časového období pomocí filtrování na straně API
## Další úkoly a rozšíření:
### Možnost přidat obrázek k události
- [x] umožnit přidání grafického souboru v sekci přidat / editovat formulář události.
- [ ] uložení nahraného souboru na disk nebo do externího cloudového úložiště přes API nebo skrze vlastní API (pokročilá verze)
- [x] poskytnutí souborů pro zobrazení v detailech události (a případně i na jiných místech)
### Úprava události
- [ ] dodatečná stránka, která vám umožní upravit vytvořenou událost.
- [ ] událost může upravovat pouze vlastník nebo administrátor (nová role pro uživatele).
- [ ] editace by se měla objevit alespoň na stránce podrobností události.
### Moje události
- [ ] sekce pro přihlášené uživatele, kde vidí všechny akce (založené uživatelem i ty, kterých se sám účastní)
vlastněné by měly mít možnost přepnutí na editaci (mechanismus z předchozí úlohy).
seznam by měl umožňovat filtrování:
##### role:
- [ ] vše
- [ ] organizátor
- [ ] účastník
##### datum konání:
- [ ] budoucí
- [ ] právě probíhající nebo budoucí
- [ ] proběhlé
- [ ] vše
##### daatum (volitelné):
- [ ] pole od
- [ ] pole do
### Dodatečné požadavky
- [ ] je nutné, aby byly splněny estetické i funkční požadavky projektu
- [ ] data získávaná od uživatelů by měla být předem ověřena
