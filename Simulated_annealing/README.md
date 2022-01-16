
# Projekt: Nieklasyczne metody optymalizacji


Realizacja projektu, ktory ma na celu wyjasnienie oraz demonstracje algorytmu sluzacemu do optymalizacji: simulating annealing. 
Autor projektu zdecydowal sie na zastosowanie pewnych konwencji aby rozszerzyc merytorycznie projekt. 

Na samym pocztaku zostanie przedstawiony program pipenv oraz terminal PowerShell w celu ulatwienia pracy osobom ktore beda chcialy zainsralowac i pobrac folder z tym projektem.

Ponadto aby dobrze zademonstrowac zagadnienie jakim jest optymalizacja w dziedzinie Machine Learningu zostanie zawarty wstep teoretyczny.


Autor: Mikołaj Maślanka
Numer albumu
Email:
Telefon:

Uczelnia: SGH - Szkola Glowna Handlowa
Kierunek studiow: Metody Ilosciowe
Tryb studiow: Zaoczne: sobotnio-niedzielne



# Spis tresci

1. [Wystepne wymagania](#Wystepne-wymagania)

1.1. [Srodowisko wirtualne](#Srodowisko-wirtualne)

1.2. [Srodowisko wirtualne](#Srodowisko-wirtualne)

1.3. [Terminal](#Terminal)

1.4. [Plik gitignore](#Plik-gitignore)


# Wystepne wymagania

Wymagania dotyczace uzywanych zasobow systemowych oraz jezykow programowania plus wersji bibliotek i pakietow.
Dodatkowe informacje na temat zainstalowanych bibliotek zjanduja sie w pliku `pipfile`.


* System operacyjny: **Windows 11**

* Jezyk Python: **wersja jezyka Python: 3.10.0**

* Program pip: **Wersja uzyta do instalacji globalnych: 21.3.1**

* Program PowerShell: **Wersja uzyta do pracy nad projektem: 7.2.1**



## Srodowisko wirtualne


Na samym początku od strony technicznej zoatalo stworzone srodowisko wirtualne tak aby projekt byl replikowalny na komputerze odbircy / osoby replikujacej.
W tym celu zostal wykorzystany program do zarzadzania srodowiskiem wirtualny `pipenv`. Wygodny interfesj oraz latwosc obslugi byly tu przewazajacymi argumentami.

Aby zainstalować `pipenv` na lokalnym komputerze lub serwerze tudziez klastrze nalezy wykonac (dla systemu Windows):

> `pip install pipenv`

Powyzszy program instaluje sie w globalnym interpreterze jezyka Python dlatego nie powinnismy znajdowac sie w zadnym srodowisku wirtualnym.

Ponadto `pipenv` stworzy automatycznie dwa pliki: `pipfile.lock` oraz `pipfile` - w tych dwoch plikach znajduja sie wszytkie wykorzystane biblioteki oraz wersja jezyka Python.

Dzięki temu że pliki te automatycznie sie aktualizuja zyskujemy mozliwosc kontrolowania zaleznosci deweloperskich oraz produkcyjnych.


Aby stworzyc wirtualne srodowisko nalezy w danym folderze wykonac w terminalu komende:

> `pipenv install`

Wszystkie komendy oraz wymaania zostaly opisane w dokumentacji tego programu i mozna je znalezc pod ponizszym linkiem:

[Link to pipenv doc](https://pipenv.pypa.io/en/latest/)


Warto jeszcze na samym początku zwrocic uwage na zaleznosci deweloperskie, gdyz domyslnie `pipenv` zainstaluje biblioteke / pakiet jako zaleznosc produkcyjna.

W celu instalacji zalenosci deweloperskiej nalezy:

> `pipenv install --dev --pre NAZWA_BIBLIOTEKI`

Dosc wazna komenda jest tez wyjscie ze srodowiska wirtualnego, w tym celu nalezy wykonac:

> `deactivate`

Aby usunac srodowisko wirtualne nalezy:

> `pipenv -rm`


## Terminal

Podczas realizacji projektu byl wykorzystywany system Windows i to na nim odbywaly sie wszytkie obliczenia zwiazane z kodem Python. 
Dodatkowo wszytkie profilowania kodu byly rowniez wykonywane z pomoca komend ktore sa tozsame dla systemu Windows.

Jako zintegrowany terminal systemowy zostal wykorzystany PowerShell  w wersji 7.2.1

Aby sprawdzić jakiej wersji używa się aktualnie na swoim komputerze należy wykonać w terminalu:

> `$PSVersionTable`


## Plik gitignore

Jako, że projekt wykonuje z uzycie narzedzia Visual Studio Code oraz dodatkowo wykorzystuje kontrole wersji - program Git - oraz projekt jezt napisany w jezyku Pytho, to konieczne wydaje sie byc zalaczenie pliku .gitignore.

Docelowo bedzie napisana wersja anglojezyczna niniejszego projektu a w dalszej kolejnosci bedzie stworzone repozytorium na GitHubie.

Plik .gitignore zawiera zakres typowych plikow ktore sa ignorowane w przypadku pracy projektowe w jezyku Python.
