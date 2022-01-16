


# Spis tresci

1. [Wstepne wyjasnienie](#Wstepne-wyjasnienie)

2. [ Co to jest optymalizacja funkcji?](#Co-to-jest-optymalizacja-funkcji?)

2.1. [Optymalizacja funkcji](#Optymalizacja-funkcji)

2.2. [Rozwiązania dla kandydatów](#Rozwiązania-dla-kandydatów)

2.3. [Funkcje celu](#Funkcje-celu)

2.4. [Koszty oceny](#Koszty-oceny)

3. [Optymalizacja i uczenie maszynowe](#Optymalizacja-i-uczenie-maszynowe)










# Wstepne wyjasnienie

Poniewaz zakres teoretyczny jaki jest zwiazany z optymalizacja w projektach Machine Learningowych jest ogromny a same algogytmy potrafia byc w ciekawy sposob skomplikowane zdecydowalem sie zalaczyc wstepny opis teoretyczny.

Pozwoli to odseparowac czesc czystego kodu i obliczen od czesci teoretycznej, ktora moim zdaniem jest niezbedna.

Projekt zaklada pokazanie i wyjasnienie algorytmu simulating annealing, dlatego znaczna czesc teorii bedzie dotyczyc wlasnie tego algorytmu, niemniej jednak spojrzenie z szerszej perspektywy wciaz jest dobry pomyslem.


# Co to jest optymalizacja funkcji?

Optymalizacja funkcji jest podstawowym obszarem badań, a techniki są wykorzystywane prawie
każde pole ilościowe. Co ważne, optymalizacja funkcji ma kluczowe znaczenie dla prawie wszystkich maszyn algorytmy uczenia się i projekty modelowania predykcyjnego. W związku z tym ważne jest, aby zrozumieć, co optymalizacji funkcji, terminologii stosowanej w tej dziedzinie oraz elementów, które składają się na problem optymalizacji funkcji. W tym samouczku odkryjesz delikatne wprowadzenie do optymalizacja funkcji. Po ukończeniu tego samouczka będziesz wiedzieć:

* Trzy elementy optymalizacji funkcji jako rozwiązania kandydujące, funkcje celu,
i koszt.

* Konceptualizacja optymalizacji funkcji jako nawigowania w przestrzeni poszukiwań i odpowiedzi
powierzchnia.

* Różnica między optyma globalną a lokalną przy rozwiązywaniu problemu optymalizacji funkcji.

## Optymalizacja funkcji

Optymalizacja funkcji jest poddziedziną matematyki, a w dzisiejszych czasach jest adresowana za pomocą metody obliczeń numerycznych. Optymalizacja funkcji ciągłej (w skrócie „optymalizacja funkcji”) należy do szerszej dziedziny nauki zwanej optymalizacją matematyczną. To jest
odróżnia się od innych rodzajów optymalizacji, ponieważ polega na znalezieniu optymalnych rozwiązań kandydujących składa się z liczbowych zmiennych wejściowych, w przeciwieństwie do kandydujących rozwiązań złożonych z sekwencji
lub kombinacje (np. optymalizacja kombinatoryczna). Optymalizacja funkcji jest szeroko stosowanym narzędziem
zestaw technik stosowanych praktycznie we wszystkich dyscyplinach naukowych i inżynierskich.


Odgrywa kluczową rolę w uczeniu maszynowym, z którego korzystają prawie wszystkie algorytmy uczenia maszynowego optymalizacja funkcji w celu dopasowania modelu do uczącego zestawu danych. Na przykład dopasowanie linii do a zebranie punktów wymaga rozwiązania problemu optymalizacyjnego. Podobnie jak dopasowanie regresji liniowej
lub model sieci neuronowej na uczącym zbiorze danych. W ten sposób optymalizacja zapewnia narzędzie do:
dostosować ogólny model do konkretnej sytuacji. Nauka jest traktowana jako optymalizacja lub wyszukiwanie
problem. W praktyce optymalizacja funkcji opisuje klasę problemów związanych ze znalezieniem danych wejściowych
do danej funkcji, która powoduje minimalne lub maksymalne wyjście z funkcji.

Optymalizacja funkcji obejmuje trzy elementy: dane wejściowe funkcji (np. x),
samą funkcję celu (np. f(x)) i wyjście z funkcji (np. koszt, y).

* Dane wejściowe x: Dane wejściowe ocenianej funkcji, tj. potencjalne rozwiązanie.

* Funkcja f(): Funkcja celu lub funkcja docelowa, która ocenia dane wejściowe.

* Koszt y: Wynik oceny kandydata na rozwiązanie z funkcją celu, zminimalizowane lub zmaksymalizowane.


## Rozwiązania dla kandydatów

Kandydujące rozwiązanie jest pojedynczym wejściem do funkcji celu. Forma rozwiązania kandydata
zależy od specyfiki funkcji celu. Może to być pojedyncza liczba zmiennoprzecinkowa,
wektor liczb, macierz liczb lub tak złożona, jak jest to konieczne dla konkretnego problemu
domena. Najczęściej wektory liczb. W przypadku problemu testowego wektor reprezentuje
określonych wartości każdej zmiennej wejściowej do funkcji (x = [x1, x2, x3, .. . , xn]). Do maszyny
model uczenia się, wektor może reprezentować współczynniki lub wagi modelu.

Mogą istnieć ograniczenia nałożone przez dziedzinę problemu lub funkcję celu na
rozwiązania kandydatów. Może to obejmować takie aspekty, jak:

* Liczba zmiennych (1, 20, 1 000 000 itd.)

* Typ danych zmiennych (całkowite, binarne, o wartościach rzeczywistych itp.)

* Zakres akceptowanych wartości (od 0 do 1 itd.)

Co ważne, rozwiązania kandydackie są dyskretne i jest ich wiele. Wszechświat
potencjalne rozwiązania mogą być rozległe, zbyt duże, by je wymienić. Zamiast tego najlepsze, co możemy zrobić, to próbować
rozwiązania kandydatów w przestrzeni poszukiwań. Jako praktyk poszukujemy algorytmu optymalizacji
który najlepiej wykorzystuje dostępne informacje o problemie do efektywnego próbkowania
przestrzeni wyszukiwania i zlokalizuj dobre lub najlepsze rozwiązanie kandydata.

* Przestrzeń wyszukiwania: Wszechświat proponowanych rozwiązań zdefiniowanych przez liczbę, typ i zakres przyjętych danych wejściowych do funkcji celu.

Wreszcie, kandydujące rozwiązania można uszeregować w kolejności na podstawie ich oceny według celu funkcja, co oznacza, że ​​niektóre są lepsze od innych.

## Funkcje celu

Funkcja celu jest specyficzna dla dziedziny problemowej. Może to być funkcja testowa, np. a
znane równanie z określoną liczbą zmiennych wejściowych, których wyliczenie zwraca
koszt wkładu. Optima funkcji testowych są znane, dzięki czemu algorytmy są:
w porównaniu na podstawie ich zdolności do sprawnego poruszania się w przestrzeni wyszukiwania.
W uczeniu maszynowym funkcja celu może obejmować podłączenie potencjalnego rozwiązania
do modelu i oceniając go w odniesieniu do części treningowego zestawu danych, a koszt może być
ocena błędu, często nazywana utratą modelu. Funkcja celu jest łatwa do zdefiniowania, chociaż
drogie do oceny. Efektywność optymalizacji funkcji odnosi się do minimalizacji liczby całkowitej
ewaluacji funkcji.
Chociaż funkcja celu jest łatwa do zdefiniowania, jej optymalizacja może być trudna. ten
trudność funkcji celu może obejmować możliwość analitycznego rozwiązania funkcji
bezpośrednio za pomocą rachunku różniczkowego lub algebry liniowej (łatwe), do lokalnego algorytmu wyszukiwania (umiarkowane),
do korzystania z globalnego algorytmu wyszukiwania (trudne). Trudność funkcji celu opiera się na:
ile wiadomo o funkcji. Często nie można tego określić po prostu przeglądając
równanie lub kod do oceny rozwiązań kandydujących. Zamiast tego odnosi się do struktury
powierzchnia odpowiedzi. Powierzchnia odpowiedzi (lub krajobraz poszukiwań) to struktura geometryczna
koszt w stosunku do przestrzeni poszukiwań rozwiązań kandydatów. Na przykład płynna odpowiedź
powierzchnia sugeruje, że małe zmiany w danych wejściowych (rozwiązania kandydackie) skutkują małymi zmianami w
wynik (koszt) z funkcji celu.

Powierzchnię odpowiedzi można zwizualizować w niewielkich wymiarach, m.in. dla rozwiązań kandydackich z jednym
lub dwie zmienne wejściowe. Jednowymiarowe dane wejściowe można wykreślić jako wykres punktowy 2D z danymi wejściowymi
wartości na osi x i koszt na osi y. Dane wejściowe dwuwymiarowe można wykreślić jako 3D
wykres powierzchni ze zmiennymi wejściowymi na osi x i y oraz wysokością powierzchni reprezentującą
koszt.
W przypadku problemu minimalizacji słabe rozwiązania byłyby przedstawiane jako wzgórza w odpowiedzi
powierzchnię i dobre rozwiązania reprezentowałyby doliny. Byłoby to odwrócone dla
maksymalizacja problemów. Struktura i kształt tej powierzchni odpowiedzi określają trudność
algorytm będzie miał nawigację w przestrzeni wyszukiwania do rozwiązania. Złożoność rzeczywistości
funkcje celu oznaczają, że nie możemy analitycznie analizować powierzchni, a wysoka wymiarowość
danych wejściowych i kosztów obliczeniowych ewaluacji funkcji sprawia, że mapowanie i wykreślanie staje się realne
funkcje obiektywne niewykonalne.


## Koszty oceny

Koszt rozwiązania kandydata to prawie zawsze jedna wartość rzeczywista. Skala
wartości kosztów będą się różnić w zależności od specyfiki funkcji celu. Ogólnie jedyny
sensowne porównanie wartości kosztów jest z innymi wartościami kosztów obliczonymi dla tego samego celu
funkcjonować. Minimalna lub maksymalna wydajność funkcji nazywana jest optymizmem
funkcja, zazwyczaj uproszczona do minimum. Każda funkcja, którą chcemy zmaksymalizować, może być
konwertowane na minimalizowanie poprzez dodanie znaku minusa na początku kosztu zwracanego z
funkcjonować.



Oprócz optymów globalnych funkcja może mieć optyma lokalne, które są dobrym kandydatem
rozwiązania, które mogą być stosunkowo łatwe do zlokalizowania, ale nie tak dobre jak globalne optima. Lokalny
optima może wydawać się globalnym optima dla algorytmu wyszukiwania, np. może być w dolinie
powierzchni odpowiedzi, w takim przypadku moglibyśmy nazwać je tak zwodniczymi, jak algorytm łatwo
zlokalizuj je i utknij, nie znajdując globalnego optima.


Względny charakter wartości kosztów oznacza, że ​​punkt odniesienia w wydajności rozwiązywania trudnych problemów
można ustalić za pomocą algorytmu wyszukiwania naiwnego (np. losowego) i „dobroci” optymalnego
rozwiązania znalezione przez bardziej wyrafinowane algorytmy wyszukiwania można porównać w stosunku do punktu odniesienia.
Rozwiązania kandydackie są często bardzo proste do opisania i bardzo łatwe do skonstruowania. Wyzwanie
częścią optymalizacji funkcji jest ocena rozwiązań kandydatów.
Rozwiązanie problemu optymalizacji funkcji lub funkcji celu odnosi się do znalezienia optima.
Całym celem projektu jest znalezienie konkretnego rozwiązania kandydata o dobrym lub najlepszym koszcie,
daj czas i dostępne zasoby. W prostych i umiarkowanych problemach możemy być w stanie:
dokładnie zlokalizować optymalne rozwiązanie kandydata i mieć pewność, że to zrobiliśmy.


# Optymalizacja i uczenie maszynowe

Uczenie maszynowe polega na wykorzystaniu algorytmu do uczenia się i uogólniania danych historycznych w
aby dokonywać prognoz na nowych danych. Ten problem można opisać jako przybliżenie a
funkcja odwzorowująca przykłady wejść na przykłady wyjść. Przybliżenie funkcji może
być rozwiązany poprzez sformułowanie problemu jako optymalizacji funkcji. To tutaj uczenie maszynowe
algorytm definiuje sparametryzowaną funkcję odwzorowania (np. ważoną sumę wejść) oraz
algorytm optymalizacji służy do finansowania wartości parametrów (np. współczynników modelu), które
zminimalizować błąd funkcji, gdy jest używany do mapowania wejść do wyjść. Oznacza to, że każdy
gdy dopasowujemy algorytm uczenia maszynowego do treningowego zbioru danych, rozwiązujemy optymalizację
problem. W tym samouczku odkryjesz centralną rolę optymalizacji w uczeniu maszynowym.


Optymalizacja funkcji to problem znalezienia zbioru danych wejściowych do docelowej funkcji celu
które skutkują minimum lub maksimum funkcji. Może to być trudny problem, ponieważ
funkcja może mieć dziesiątki, setki, tysiące, a nawet miliony wejść, a strukturę
funkcja jest nieznana, często niemożliwa do rozróżnienia i głośna.



Uczenie maszynowe można opisać jako aproksymację funkcji. To znaczy przybliżając
nieznana podstawowa funkcja, która mapuje przykłady wejść na wyjścia w celu wykonania
prognozy dotyczące nowych danych. Może to być trudne, ponieważ często istnieje ograniczona liczba przykładów
z którego możemy aproksymować funkcję i strukturę funkcji, która jest
przybliżony jest często nieliniowy, zaszumiony, a nawet może zawierać sprzeczności.


Optymalizacja funkcji jest często prostsza niż aproksymacja funkcji. Co ważne, w maszynie
ucząc się, często rozwiązujemy problem aproksymacji funkcji za pomocą optymalizacji funkcji. Na
rdzeniem prawie wszystkich algorytmów uczenia maszynowego jest algorytm optymalizacji. Ponadto
proces pracy nad problemem modelowania predykcyjnego obejmuje optymalizację na wielu
kroki oprócz nauki modelu, w tym:


* Wybór hiperparametrów modelu.

* Wybór przekształceń do zastosowania do danych przed modelowaniem

* Wybór potoku modelowania do użycia jako model ostateczny.

## Nauka jako optymalizacja

Problemy z modelowaniem predykcyjnym obejmują prognozowanie na przykładzie danych wejściowych. Numeryczny
ilość musi być przewidziana w przypadku problemu regresji, podczas gdy etykieta klasy musi
należy przewidzieć w przypadku problemu z klasyfikacją. Problemem modelowania predykcyjnego jest:
wystarczająco trudne, że nie możemy napisać kodu, aby przewidywać. Zamiast tego musimy użyć
algorytm uczenia zastosowany do danych historycznych w celu uczenia się „programu” zwanego modelem predykcyjnym
które możemy wykorzystać do przewidywania nowych danych.

W uczeniu statystycznym, statystycznym spojrzeniu na uczenie maszynowe, problem jest sformułowany
jako uczenie funkcji odwzorowania (f) podane przykłady danych wejściowych (X) i powiązane
dane wyjściowe (y).

$$
y = f(X)
$$

Wyuczone mapowanie będzie niedoskonałe. Żaden model nie jest doskonały, a pewien błąd przewidywania to
oczekiwane, biorąc pod uwagę trudność problemu, szum w obserwowanych danych i wybór
algorytm uczenia się. Matematycznie algorytmy uczące rozwiązują problem aproksymacji
mapowanie funkcji przez rozwiązanie problemu optymalizacji funkcji. W szczególności podane przykłady
wejścia i wyjścia, znajdź zestaw wejść do funkcji mapowania, który daje minimum
strata, minimalny koszt lub minimalny błąd przewidywania. Im bardziej tendencyjny lub ograniczony wybór
funkcja mapowania, tym łatwiej jest rozwiązać optymalizację.
Spójrzmy na kilka przykładów, aby to wyjaśnić.
Regresja liniowa (dla problemów z regresją) jest modelem silnie ograniczonym i może być
rozwiązany analitycznie przy użyciu algebry liniowej. Danymi wejściowymi funkcji mapowania są współczynniki
modelu. Możemy użyć algorytmu optymalizacji, takiego jak lokalny algorytm wyszukiwania quasi-Newtona,
ale prawie zawsze będzie mniej wydajne niż rozwiązanie analityczne.



* Regresja liniowa: dane wejściowe funkcji to współczynniki modelu, problemy optymalizacji
które można rozwiązać analitycznie.

Regresja logistyczna (dla problemów klasyfikacyjnych) jest nieco mniej ograniczona i musi zostać rozwiązana
jako problem optymalizacji, chociaż coś o strukturze funkcji optymalizacji
rozwiązywanie jest znane, biorąc pod uwagę ograniczenia nałożone przez model. Oznacza to wyszukiwanie lokalne
można zastosować algorytm podobny do metody quasi-Newtona. Moglibyśmy użyć globalnego wyszukiwania, takiego jak stochastic
zejście gradientowe, ale prawie zawsze będzie mniej wydajne.

* Regresja logistyczna: dane wejściowe funkcji to współczynniki modelu, problemy optymalizacji
które wymagają iteracyjnego algorytmu wyszukiwania lokalnego.
Model sieci neuronowej to bardzo elastyczny algorytm uczenia się, który nakłada niewiele ograniczeń.

Dane wejściowe funkcji mapowania to wagi sieciowe. Lokalny algorytm wyszukiwania nie może
być używane, biorąc pod uwagę, że przestrzeń poszukiwań jest multimodalna i wysoce nieliniowa; zamiast tego globalne wyszukiwanie
należy zastosować algorytm.
Powszechnie stosowany jest globalny algorytm optymalizacji, w szczególności stochastyczne opadanie gradientu,
a aktualizacje są dokonywane w sposób świadomy struktury modelu (propagacja wsteczna)
i zasada łańcucha). Moglibyśmy użyć globalnego algorytmu wyszukiwania, który jest nieświadomy struktury
model, jak algorytm genetyczny, ale prawie zawsze będzie mniej wydajny.

* Sieć neuronowa: dane wejściowe funkcji to wagi modelu, problemy optymalizacji, które
wymagają iteracyjnego globalnego algorytmu wyszukiwania.


Widzimy, że każdy algorytm przyjmuje inne założenia dotyczące formy odwzorowania
funkcji, która wpływa na rodzaj problemu optymalizacyjnego do rozwiązania. Możemy też to zobaczyć
domyślny algorytm optymalizacji używany dla każdego algorytmu uczenia maszynowego nie jest arbitralny; to
reprezentuje najbardziej wydajny algorytm rozwiązywania określonego problemu optymalizacyjnego w ramach
algorytm, m.in. gradient stochastyczny dla sieci neuronowych zamiast algorytmu genetycznego.
Odejście od tych wartości domyślnych wymaga ważnego powodu.



Nie wszystkie algorytmy uczenia maszynowego rozwiązują problem optymalizacji. Godnym uwagi przykładem jest
algorytm k-najbliższych sąsiadów, który przechowuje uczący zbiór danych i wyszukuje k
najlepsze dopasowania do każdego nowego przykładu w celu dokonania prognozy.
Teraz, gdy znamy uczenie się w algorytmach uczenia maszynowego jako optymalizację,
spójrzmy na kilka powiązanych przykładów optymalizacji w projekcie uczenia maszynowego.

## Optymalizacja w projekcie uczenia maszynowego

Optymalizacja odgrywa ważną rolę w projekcie uczenia maszynowego, oprócz dopasowania
algorytm uczenia się na uczącym zbiorze danych. Etap przygotowania danych przed dopasowaniem
model i etap strojenia wybranego modelu również można sformułować jako problem optymalizacyjny. w
w rzeczywistości cały projekt modelowania predykcyjnego można traktować jako jeden duży problem optymalizacyjny.

Przygotowanie danych polega na przekształceniu surowych danych do postaci, która jest najbardziej odpowiednia dla
algorytmy uczenia się. Może to obejmować skalowanie wartości, obsługę brakujących wartości i zmianę
rozkład prawdopodobieństwa zmiennych. Można dokonać przekształceń, aby zmienić reprezentację
dane historyczne w celu spełnienia oczekiwań lub wymagań określonych algorytmów uczenia się. Już,
czasami dobre lub najlepsze wyniki można osiągnąć, gdy naruszone zostaną oczekiwania lub gdy
wykonywana jest niepowiązana transformacja danych. Możemy pomyśleć o wyborze przekształceń do zastosowania
dane treningowe jako problem wyszukiwania lub optymalizacji najlepszego ujawnienia nieznanego podłoża
struktura danych do algorytmu uczenia.

Ten problem optymalizacji jest często wykonywany ręcznie za pomocą prób i błędów opartych na ludziach.
Niemniej jednak możliwe jest zautomatyzowanie tego zadania za pomocą globalnego algorytmu optymalizacji, gdzie
dane wejściowe funkcji to typy i kolejność przekształceń zastosowanych do danych uczących.
Liczba i permutacje przekształceń danych są zazwyczaj dość ograniczone i może być
możliwość przeprowadzenia wyszukiwania wyczerpującego lub przeszukiwania siatki powszechnie używanych sekwencji.

### Dostrajanie hiperparametrów jako optymalizacja

Algorytmy uczenia maszynowego mają hiperparametry, które można skonfigurować w celu dostosowania algorytmu
do określonego zbioru danych. Chociaż dynamika wielu hiperparametrów jest znana, specyficzna
wpływ, jaki będą one miały na wydajność uzyskanego modelu na danym zbiorze danych, nie jest znany.
W związku z tym standardową praktyką jest testowanie zestawu wartości dla hiperparametrów kluczowych algorytmów dla
wybrany algorytm uczenia maszynowego. Nazywa się to strojeniem hiperparametrów lub hiperparametrem
optymalizacja. W tym celu często używa się naiwnego algorytmu optymalizacji, takiego jak
algorytm wyszukiwania losowego lub algorytm wyszukiwania siatki.

Niemniej jednak coraz częściej stosuje się iteracyjny algorytm wyszukiwania globalnego
dla tego problemu optymalizacji. Popularnym wyborem jest algorytm optymalizacji bayesowskiej, który jest
zdolne do jednoczesnego aproksymowania funkcji docelowej, która jest optymalizowana (za pomocą
funkcja zastępcza) podczas jej optymalizacji.
Jest to pożądane, ponieważ ocena pojedynczej kombinacji hiperparametrów modelu jest kosztowna,
wymagające dopasowania modelu do całego zestawu danych treningowych jedno lub wielokrotnie, w zależności od
wybór procedury oceny modelu (np. powtórna k-krotna walidacja krzyżowa).

## Wybór modelu jako optymalizacja

Wybór modelu polega na wyborze jednego z wielu kandydujących modeli uczenia maszynowego do
problem modelowania predykcyjnego. Tak naprawdę polega to na wyborze algorytmu uczenia maszynowego lub
potok uczenia maszynowego, który tworzy model. Jest to następnie wykorzystywane do trenowania ostatecznego modelu, który:
mogą być następnie wykorzystane w żądanej aplikacji do przewidywania nowych danych. Ten proces
wybór modelu jest często procesem ręcznym wykonywanym przez praktyka uczenia maszynowego, obejmującym:
zadania takie jak przygotowanie danych, ocena modeli kandydatów, dostrajanie modeli dobrze działających oraz
wreszcie wybór ostatecznego modelu. Można to sformułować jako problem optymalizacji, który obejmuje:
część lub cały projekt modelowania predykcyjnego.

Coraz częściej dzieje się tak w przypadku stosowania algorytmów automatycznego uczenia maszynowego (AutoML)
wybrać algorytm, algorytm i hiperparametry lub przygotowanie danych, algorytm i
hiperparametry, z bardzo małą interwencją użytkownika.
Podobnie jak dostrajanie hiperparametrów, często używa się globalnego algorytmu wyszukiwania, który również
przybliża funkcję celu, taką jak optymalizacja bayesowska, biorąc pod uwagę, że każda funkcja
ocena jest kosztowna. To zautomatyzowane podejście do optymalizacji uczenia maszynowego również
leży u podstaw nowoczesnych produktów uczenia maszynowego jako usługi (MLaaS) dostarczanych przez firmy
takich jak Google, Microsoft i Amazon. Chociaż szybkie i wydajne, takie podejścia są nadal
nie mogąc przewyższyć ręcznie wykonanych modeli przygotowanych przez wysoko wykwalifikowanych ekspertów, takich jak te
udział w konkursach uczenia maszynowego.

# Jak wybrać optymalizację Algorytmy

Optymalizacja to problem ze znalezieniem zestawu danych wejściowych do funkcji celu, którego wynikiem jest a
maksymalna lub minimalna ocena funkcji. Jest to trudny problem, który leży u podstaw wielu
algorytmy uczenia maszynowego, od dopasowania modeli regresji logistycznej po uczenie sztucznych neuronów
sieci. Istnieje prawdopodobnie setki popularnych algorytmów optymalizacyjnych, a być może dziesiątki
algorytmy do wyboru w popularnonaukowych bibliotekach kodów. Może to sprawić, że trudno będzie
wiedzieć, które algorytmy wziąć pod uwagę dla danego problemu optymalizacyjnego.

## Różniczkowa funkcja celu

Funkcja różniczkowalna
jest funkcją, w której pochodną można obliczyć dla dowolnego podanego
punkt w przestrzeni wejściowej. Pochodną funkcji dla wartości jest stopa lub kwota zmiany
w funkcji w tym momencie. Często nazywany jest stokiem.

Pochodna funkcji z więcej niż jedną zmienną wejściową (np. wielowymiarowe dane wejściowe) to
powszechnie nazywany gradientem.

Pochodną wielowymiarowej funkcji celu jest wektor, a każdy element wektora to
nazywana pochodną cząstkową, czyli stopą zmian dla danej zmiennej w punkcie zakładając wszystkie
inne zmienne są utrzymywane na stałym poziomie.

Możemy obliczyć pochodną pochodnej funkcji celu, czyli stopę
zmiana tempa zmiany funkcji celu. Nazywa się to drugą pochodną.

W przypadku funkcji, która przyjmuje wiele zmiennych wejściowych, jest to macierz i jest określana jako
Macierz Hesja.

Proste funkcje różniczkowe można optymalizować analitycznie za pomocą rachunku różniczkowego. Zazwyczaj
interesujących nas funkcji obiektywnych nie da się rozwiązać analitycznie. Optymalizacja to
znacznie łatwiej, jeśli można obliczyć gradient funkcji celu i jako taki istnieje
o wiele więcej badań nad algorytmami optymalizacji wykorzystującymi pochodną niż te
to nie. Niektóre grupy algorytmów wykorzystujących informacje o gradientach obejmują:

* Algorytmy braketingu

* Lokalne algorytmy zejścia

* Algorytmy pierwszego rzędu

* Algorytmy drugiego rzędu

### Lokalne algorytmy zejścia

Algorytmy optymalizacji zniżania lokalnego są przeznaczone do rozwiązywania problemów optymalizacyjnych z więcej niż
jedna zmienna wejściowa i jedna globalna optima (np. unimodalna funkcja celu). Możliwe że
najczęstszym przykładem lokalnego algorytmu opadania jest algorytm wyszukiwania linii.

Istnieje wiele odmian wyszukiwania wierszy (np. algorytm Brenta-Dekkera), ale procedura
zazwyczaj polega na wybraniu kierunku poruszania się w przestrzeni wyszukiwania, a następnie wykonaniu nawiasów
wpisz search w linii lub hiperpłaszczyźnie w wybranym kierunku. Ten proces jest powtarzany aż do nie
można dokonać dalszych ulepszeń. Ograniczeniem jest to, że jest to obliczeniowo kosztowne, aby
zoptymalizuj każdy ruch kierunkowy w przestrzeni wyszukiwania.

### Algorytmy pierwszego rzędu

Algorytmy optymalizacji pierwszego rzędu wyraźnie obejmują użycie pierwszej pochodnej (gradientu) do
wybierz kierunek poruszania się w przestrzeni wyszukiwania. Procedury obejmują najpierw obliczenie
gradient funkcji, a następnie podążanie za gradientem w przeciwnym kierunku (np. zjazd do
minimum dla problemów z minimalizacją) przy użyciu wielkości kroku (nazywanej również szybkością uczenia się). ten
rozmiar kroku to hiperparametr, który kontroluje, jak daleko przemieścić się w przestrzeni wyszukiwania, w przeciwieństwie do „lokalnego
algorytmy opadania”, które wykonują pełne przeszukiwanie linii dla każdego ruchu kierunkowego. Rozmiar kroku, który
to zbyt małe wyniki w wyszukiwaniu, które zajmuje dużo czasu i może się utknąć, podczas gdy rozmiar kroku
zbyt duża spowoduje zygzakowanie lub podskakiwanie po przestrzeni wyszukiwania, z pominięciem
optymalna całkowicie. Algorytmy pierwszego rzędu są ogólnie określane jako opadanie gradientowe, przy czym
bardziej szczegółowe nazwy odnoszące się do drobnych rozszerzeń procedury, np.:

* Gradient Spadek
* Pęd
* Adagrad
* RMSPPro
* Adam

Algorytm opadania gradientu zapewnia również szablon dla popularnej wersji stochastycznej
algorytmu o nazwie Stochastic Gradient Descent (SGD), który służy do treningu sztucznego
modele sieci neuronowych (głębokiego uczenia). Ważną różnicą jest to, że gradient jest
przywłaszczane, a nie obliczane bezpośrednio, przy użyciu błędu przewidywania na danych uczących, takich jak:
jedna próbka (stochastyczna), wszystkie przykłady (partia) lub mały podzbiór danych uczących (minibatch).
Rozszerzenia zaprojektowane w celu przyspieszenia algorytmu opadania gradientu (pędu itp.) mogą być
i są powszechnie używane z SGD.

* Stochastyczne opadanie gradientowe
* Partia Gradient Spadek
* Minipartia Gradient Descent


### Algorytmy drugiego rzędu

Algorytmy optymalizacji drugiego rzędu wyraźnie wykorzystują drugą pochodną (hessian)
aby wybrać kierunek poruszania się w przestrzeni wyszukiwania. Te algorytmy są tylko odpowiednie
dla tych funkcji celu, dla których można obliczyć lub przybliżyć macierz Hess.
Przykłady algorytmów optymalizacji drugiego rzędu dla jednowymiarowych funkcji celu obejmują:

* Metoda Newtona

* Metoda siecznej 

Metody drugiego rzędu dla wielowymiarowych funkcji celu są określane jako Quasi-Newton
Metody.

Metoda quasi-Newtona
Istnieje wiele metod quasi-Newtona i są one zazwyczaj nazywane imieniem twórców
algorytm, taki jak:

* Davidson-Fletcher-Powell

* Broyden-Fletcher-Goldfarb-Shanno (BFGS)

* BFGS o ograniczonej pamięci (L-BFGS)

Teraz, gdy znamy już tak zwane klasyczne algorytmy optymalizacji, spójrzmy na:
algorytmy stosowane, gdy funkcja celu nie jest różniczkowalna.

## Nieróżnicowa funkcja celu

Algorytmy optymalizacyjne wykorzystujące pochodną funkcji celu są szybkie i
wydajny. Niemniej jednak istnieją funkcje obiektywne, w przypadku których nie można obliczyć pochodnej,
zazwyczaj dlatego, że funkcja jest złożona z różnych rzeczywistych powodów. Lub pochodna
można obliczyć w niektórych regionach domeny, ale nie we wszystkich lub nie jest dobrym przewodnikiem. Niektóre
trudności z funkcjami celu dla klasycznych algorytmów opisanych w poprzednim rozdziale
włączać:

* Brak opisu analitycznego funkcji (np. symulacja).

* Wielokrotne optima globalne (np. multimodalne).

* Ocena funkcji stochastycznej (np. zaszumienie).

* Nieciągła funkcja celu (np. regiony z nieprawidłowymi rozwiązaniami).
