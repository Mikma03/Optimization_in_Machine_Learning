<p style='text-align: justify;'>  

# Spis tresci

<p>&nbsp;</p>

1. [Wstepne wyjasnienie](#Wstepne-wyjasnienie)

2. [ Co to jest optymalizacja funkcji?](#Co-to-jest-optymalizacja-funkcji?)

    2.1. [Optymalizacja funkcji](#Optymalizacja-funkcji)

    2.2. [Rozwiązania dla kandydatów](#Rozwiązania-dla-kandydatów)

    2.3. [Funkcje celu](#Funkcje-celu)

    2.4. [Koszty oceny](#Koszty-oceny)

3. [Optymalizacja i uczenie maszynowe](#Optymalizacja-i-uczenie-maszynowe)

    3.1. [Dostrajanie hiperparametrów jako optymalizacja](#Dostrajanie-hiperparametrów-jako-optymalizacja)

    3.2. [Wybór modelu jako optymalizacja](#Wybór-modelu-jako-optymalizacja)

4. [Jak wybrać optymalizację Algorytmy](#Jak-wybrać-optymalizację-Algorytmy)

    4.1. [Algorytmy pierwszego rzędu](#Algorytmy-pierwszego-rzędu)

    4.2. [Algorytmy drugiego rzędu](#Algorytmy-drugiego-rzędu)

    4.3. [Algorytmy bezpośrednie](#Algorytmy-ezpośrednie)

    4.4. [Algorytmy stochastyczne](#Algorytmy-stochastyczne)

    4.4. [Algorytmy populacyjne](#Algorytmy-populacyjne)


<p>&nbsp;</p>

# Wstepne wyjasnienie

<p>&nbsp;</p>

Poniewaz zakres teoretyczny jaki jest zwiazany z optymalizacja w projektach Machine Learningowych jest ogromny a same algogytmy potrafia byc w ciekawy sposob skomplikowane zdecydowalem sie zalaczyc wstepny opis teoretyczny.

Pozwoli to odseparowac czesc czystego kodu i obliczen od czesci teoretycznej, ktora moim zdaniem jest niezbedna. Projekt zaklada pokazanie i wyjasnienie algorytmu simulating annealing, dlatego znaczna czesc teorii bedzie dotyczyc wlasnie tego algorytmu, niemniej jednak spojrzenie z szerszej perspektywy wciaz jest dobry pomyslem.

<p>&nbsp;</p>

# Co to jest optymalizacja funkcji?

<p>&nbsp;</p>

Optymalizacja funkcji jest podstawowym obszarem badań optymalizacji a techniki są wykorzystywane w prawie każdym polu ilościowym. Co ważne, optymalizacja funkcji ma kluczowe znaczenie dla prawie wszystkich algorytmow uczenia maszynowego i projektow modelowania predykcyjnego. 

W związku z tym ważne jest, aby zrozumieć terminologie oraz zasady dzialania juz na samym pocztaku.


<p>&nbsp;</p>


* Trzy elementy optymalizacji funkcji jako: rozwiązania kandydujące, funkcje celu,
i funkcje kosztu.

* Różnica między optimem globalnym a lokalnym przy rozwiązywaniu problemu optymalizacji funkcji.

<p>&nbsp;</p>

## Optymalizacja funkcji

<p>&nbsp;</p>

Optymalizacja funkcji jest poddziedziną matematyki, a w dzisiejszych czasach jest rozwiazywana za pomocą obliczeń numerycznych. 

Optymalizacja funkcji ciągłej (w skrócie „optymalizacja funkcji”) należy do szerszej dziedziny nauki zwanej optymalizacją matematyczną. 

Odróżnia się od innych rodzajów optymalizacji, ponieważ polega na znalezieniu optymalnych rozwiązań kandydujących składajacych się z liczbowych zmiennych wejściowych. Optymalizacja funkcji jest szeroko stosowanym narzędziem we wszystkich dyscyplinach naukowych i inżynierskich.

Odgrywa kluczową rolę w uczeniu maszynowym, z którego korzystają prawie wszystkie algorytmy  w celu dopasowania modelu do uczącego zestawu danych. Podobnie jak dopasowanie regresji liniowej
lub modelu sieci neuronowej na uczącym zbiorze danych. 

W ten sposób optymalizacja zapewnia narzędzie do
dopasowania ogólnego modelu do konkretnej sytuacji. W praktyce optymalizacja funkcji opisuje klasę problemów związanych ze znalezieniem danych wejściowych do danej funkcji, która powoduje minimalne lub maksymalne wyjście z funkcji.

Optymalizacja funkcji obejmuje trzy elementy: dane wejściowe funkcji (np. x),
samą funkcję celu (np. $f(x))$ i wyjście z funkcji (np. koszt, y).

<p>&nbsp;</p>

* Dane wejściowe $x$: Dane wejściowe ocenianej funkcji, tj. potencjalne rozwiązanie.

* Funkcja $f()$: Funkcja celu lub funkcja docelowa, która ocenia dane wejściowe.

* Koszt $y$: Wynik oceny kandydata na rozwiązanie, zminimalizowane lub zmaksymalizowane.

<p>&nbsp;</p>

## Rozwiązania dla kandydatów

<p>&nbsp;</p>

Kandydujące rozwiązanie jest pojedynczym wejściem do funkcji celu. Forma rozwiązania kandydata
zależy od specyfiki funkcji celu. Może to być pojedyncza liczba, wektor liczb, macierz liczb etc.

W przypadku problemu testowego wektor reprezentuje
określone wartości każdej zmiennej wejściowej do funkcji $(x = [x_1, x_2, x_3, .. . , x_n])$. Wektor może reprezentować współczynniki lub wagi modelu.

Mogą istnieć ograniczenia nałożone przez dziedzinę problemu lub funkcję celu na
rozwiązania kandydatów. Może to obejmować takie aspekty, jak:

<p>&nbsp;</p>

* Liczba zmiennych (1, 20, 1 000 000 itd.)

* Typ danych zmiennych (całkowite, binarne, o wartościach rzeczywistych itp.)

* Zakres akceptowanych wartości (od 0 do 1 itd.)

<p>&nbsp;</p>

Poszukujemy algorytmu optymalizacji
który najlepiej wykorzystuje dostępne informacje o problemie do efektywnego próbkowania
przestrzeni wyszukiwania i zlokalizuje dobre lub najlepsze rozwiązanie.

<p>&nbsp;</p>

* Przestrzeń proponowanych rozwiązań zdefiniowanych przez liczbę, typ i zakres przyjętych danych wejściowych do funkcji celu.

<p>&nbsp;</p>

Rozwiązania można uszeregować w kolejności na podstawie ich oceny, co oznacza, że niektóre są lepsze od innych.

<p>&nbsp;</p>

## Funkcje celu

<p>&nbsp;</p>

Funkcja celu jest specyficzna dla dziedziny problemowej. Może to być funkcja testowa, np.
znane równanie z określoną liczbą zmiennych wejściowych. 

Optima funkcji testowych są znane, dzięki czemu algorytmy są: porownywane na podstawie ich zdolności do sprawnego poruszania się w przestrzeni wyszukiwania.

W uczeniu maszynowym funkcja celu może obejmować podłączenie potencjalnego rozwiązania
do modelu i oceniając go w odniesieniu do części treningowej zestawu danych, a kosztem może być
ocena błędu, często nazywana strata modelu. 

Efektywność optymalizacji funkcji odnosi się do minimalizacji liczby całkowitej ewaluacji funkcji.

Chociaż funkcja celu jest łatwa do zdefiniowania, jej optymalizacja może być trudna. 

Trudność ta może obejmować możliwość analitycznego rozwiązania funkcji
bezpośrednio za pomocą rachunku różniczkowego lub algebry liniowej, do lokalnego algorytmu wyszukiwania, do korzystania z globalnego algorytmu wyszukiwania. 

Trudność funkcji celu opiera się na dostepnych informacjach o funkcji. Często nie można tego określić po prostu przeglądając równanie lub kod do oceny rozwiązań kandydujących. 

Powierzchnia odpowiedzi (lub zakres poszukiwań) to struktura geometryczna - 
koszt w stosunku do zakresu poszukiwań kandydatow na rozwiazanie. 


Jednowymiarowe dane wejściowe można wykreślić jako wykres punktowy 2D z danymi wejściowymi
wartości na osi x i koszt na osi y. Dane wejściowe dwuwymiarowe można wykreślić jako 3D
wykres powierzchni ze zmiennymi wejściowymi na osi x i y oraz wysokością powierzchni reprezentującą koszt funkcji.

Złożoność rzeczywistości
funkcji celu oznaczają, że nie możemy analitycznie analizować a wysoka wymiarowość
danych wejściowych i kosztów obliczeniowych ewaluacji funkcji sprawia, że mapowanie i wykreślanie staje się bardzo trudne.

<p>&nbsp;</p>

## Koszty oceny

<p>&nbsp;</p>

Ogólnie jedyne sensowne porównanie wartości kosztów jest z innymi wartościami kosztów
 
Każda funkcje, którą chcemy zmaksymalizować, może być
konwertowana na minimalizowanie poprzez dodanie znaku minusa.

Oprócz optimow globalnych funkcja może mieć optyma lokalne, które są dobrym kandydatem
rozwiązania, które mogą być stosunkowo łatwe do zlokalizowania, ale nie tak dobre jak globalne optima. 

Lokalne optimum może wydawać się globalnym optimum dla algorytmu wyszukiwania.

Względny charakter wartości kosztów oznacza, że punkt odniesienia w wydajności rozwiązywania trudnych problemów można ustalić za pomocą algorytmu wyszukiwania naiwnego (np. losowego) i „dobroci” optymalnego rozwiązania znalezione przez bardziej wyrafinowane algorytmy wyszukiwania można porównać w stosunku do punktu odniesienia.

Rozwiązanie problemu optymalizacji funkcji lub funkcji celu odnosi się do znalezienia optima.

Całym celem projektu jest znalezienie konkretnego rozwiązania kandydata o dobrym lub najlepszym koszcie, biorac pod uwage czas i dostępne zasoby.

<p>&nbsp;</p>

# Optymalizacja i uczenie maszynowe

<p>&nbsp;</p>

Uczenie maszynowe polega na wykorzystaniu algorytmu do uczenia się i uogólniania danych historycznych aby dokonywać prognoz na nowych danych. Przybliżenie funkcji może
być rozwiązany poprzez sformułowanie problemu jako optymalizacji funkcji. 

Algorytm optymalizacji służy do szukania wartości parametrów (np. współczynników modelu), które
zminimalizuja błąd funkcji, gdy jest używany do mapowania wejść do wyjść. 

Oznacza to, że gdy dopasowujemy algorytm uczenia maszynowego do treningowego zbioru danych, rozwiązujemy problem optymalizacyjny.

Uczenie maszynowe można opisać jako aproksymację funkcji. To znaczy przybliżając
nieznana podstawowa funkcje, która mapuje przykłady wejść na wyjścia w celu wykonania
prognozy dotyczące nowych danych. 

Może to być trudne, ponieważ często istnieje ograniczona liczba przykładów
z którego możemy aproksymować funkcję i strukturę funkcji, która jest
przybliżona oraz jest często nieliniowy, zaszumiony, a nawet może zawierać sprzeczności.

Optymalizacja funkcji jest często prostsza niż aproksymacja funkcji. Co ważne, uczeniu maszynowym, często rozwiązujemy problem aproksymacji funkcji za pomocą optymalizacji funkcji. 

Rdzeniem prawie wszystkich algorytmów uczenia maszynowego jest algorytm optymalizacji. Ponadto
proces pracy nad problemem modelowania predykcyjnego obejmuje optymalizację. Sa to miedzy innymi:

<p>&nbsp;</p>

* Wybór hiperparametrów modelu.

* Wybór przekształceń do zastosowania do danych przed modelowaniem

* Wybór modelowania do użycia jako model ostateczny.

<p>&nbsp;</p>

## Dostrajanie hiperparametrów jako optymalizacja

<p>&nbsp;</p>

Algorytmy uczenia maszynowego mają hiperparametry, które można skonfigurować w celu dostosowania algorytmu do określonego zbioru danych. Chociaż dynamika wielu hiperparametrów jest znana, specyficzny wpływ, jaki będą one miały na wydajność uzyskanego modelu na danym zbiorze danych, nie jest znany.

W związku z tym standardową praktyką jest testowanie zestawu wartości dla hiperparametrów kluczowych algorytmów dla. Nazywa się to strojeniem hiperparametrów lub optymalizacja hiperparametrow.

Niemniej jednak coraz częściej stosuje się iteracyjny algorytm wyszukiwania. Popularnym wyborem jest algorytm optymalizacji bayesowskiej. 


<p>&nbsp;</p>

## Wybór modelu jako optymalizacja


<p>&nbsp;</p>

Wybór modelu polega na wyborze jednego z wielu kandydujących modeli uczenia maszynowego do
problemu modelowania predykcyjnego. Tak naprawdę polega to na wyborze algorytmu uczenia maszynowego lub potok - zbior modeli -  uczenia maszynowego, który tworzy model. 

Podobnie jak dostrajanie hiperparametrów, często używa się globalnego algorytmu wyszukiwania, który również aproksymuje funkcję celu, taką jak optymalizacja bayesowska. To zautomatyzowane podejście do optymalizacji uczenia maszynowego również
leży u podstaw nowoczesnych produktów uczenia maszynowego jako usługi - MLaaS - dostarczanych przez firmy takich jak Google, Microsoft i Amazon. 

<p>&nbsp;</p>

# Jak wybrać algorytmy optymalizacji

<p>&nbsp;</p>

Optymalizacja to problem ze znalezieniem zestawu danych wejściowych do funkcji celu, którego wynikiem jest maksymalna lub minimalna ocena funkcji. Jest to trudny problem, który leży u podstaw wielu algorytmy uczenia maszynowego, od dopasowania modeli regresji logistycznej po uczenie sztucznych neuronów sieci. 

<p>&nbsp;</p>

## Algorytmy pierwszego rzędu

<p>&nbsp;</p>

Algorytmy optymalizacji pierwszego rzędu wyraźnie obejmują użycie pierwszej pochodnej do
eyboru kieruneku poruszania w przestrzeni wyszukiwania. 

Procedury obejmują najpierw obliczenie gradient funkcji, a następnie podążanie za gradientem w przeciwnym kierunku np. zjazd do minimum dla problemów z minimalizacją przy użyciu wielkości kroku nazywanej również szybkością uczenia się. 

Algorytmy pierwszego rzędu są ogólnie określane jako opadanie gradientowe, przy czym
bardziej szczegółowe nazwy odnoszące się do drobnych rozszerzeń procedury, np.:

<p>&nbsp;</p>

* Gradient decent
* Momentum
* Adagrad
* RMSPPro
* Adam

<p>&nbsp;</p>

Algorytm gradient decent zapewnia również szablon dla Stochastic Gradient Descent (SGD), który służy do treningu sztucznego modelu sieci neuronowych (głębokiego uczenia).

Rozszerzenia zaprojektowane w celu przyspieszenia algorytmu opadania gradientu (pędu itp.) mogą być i są powszechnie używane z SGD.

<p>&nbsp;</p>

* Stochastic Gradient Descent
* Batch Gradient Descent
* Minibatch Gradient Descent
<p>&nbsp;</p>

## Algorytmy drugiego rzędu

<p>&nbsp;</p>

Algorytmy optymalizacji drugiego rzędu wyraźnie wykorzystują drugą pochodną (hessian)
aby wybrać kierunek poruszania się w przestrzeni wyszukiwania. Te algorytmy są tylko odpowiednie
dla tych funkcji celu, dla których można obliczyć lub przybliżyć macierz Hess.
Przykłady algorytmów optymalizacji drugiego rzędu dla jednowymiarowych funkcji celu obejmują:

<p>&nbsp;</p>

* Newton’s Method

* Secant Method

<p>&nbsp;</p>

Metody drugiego rzędu dla wielowymiarowych funkcji celu są określane jako Quasi-Newton
Metody.

* Quasi-Newton Method

Istnieje wiele metod quasi-Newtona i są one zazwyczaj nazywane imieniem twórców
algorytm, taki jak:

<p>&nbsp;</p>

* Davidson-Fletcher-Powell

* Broyden-Fletcher-Goldfarb-Shanno (BFGS)

* BFGS o ograniczonej pamięci (L-BFGS)

<p>&nbsp;</p>

Teraz, gdy znamy już tak zwane klasyczne algorytmy optymalizacji, spójrzmy na:
algorytmy stosowane, gdy funkcja celu nie jest różniczkowalna.

<p>&nbsp;</p>

## Algorytmy bezpośrednie

<p>&nbsp;</p>

Algorytmy optymalizacji bezpośredniej są przeznaczone dla funkcji celu, dla których pochodne nie mogą być obliczone. Algorytmy są procedurami deterministycznymi i często przyjmują funkcję celu ma jedno globalne optimum. Metody wyszukiwania bezpośredniego są również zwykle określane
jako „wyszukiwanie wzorcowe”, ponieważ mogą poruszać się w przestrzeni wyszukiwania za pomocą geometrycznych kształtów lub decyzji.


Examples of direct search algorithms include:

<p>&nbsp;</p>

* Cyclic Coordinate Search

* Powell’s Method

* Hooke-Jeeves Method

* Nelder-Mead Simplex Search

<p>&nbsp;</p>

## Algorytmy stochastyczne

<p>&nbsp;</p>

Algorytmy optymalizacji stochastycznej to algorytmy wykorzystujące losowość w wyszukiwaniu
funkcji celu, dla których nie można obliczyć instrumentów pochodnych. 

Algorytmy stochastyczne zazwyczaj wymagają dużo próbkowania
funkcji celu, ale są w stanie poradzić sobie z problemami ze zwodniczymi optimami lokalnymi.

Algorytmy optymalizacji stochastycznej obejmują:

<p>&nbsp;</p>

* Simulated Annealing

* Evolution Strategy

* Cross-Entropy Method

<p>&nbsp;</p>

## Algorytmy populacyjne

<p>&nbsp;</p>

Algorytmy optymalizacji populacji to stochastyczne algorytmy optymalizacji, które utrzymują pulę
(populacja) rozwiązań kandydujących, które razem są wykorzystywane do próbkowania, badania i doskonalenia. Algorytmy tego typu są przeznaczone do rozwiązywania trudniejszych problemów obiektywnych, które: moga mieć zaszumione oceny funkcji i wiele globalnych optimów a znalezienie dobrego lub wystarczająco dobrego rozwiązania jest trudne lub niewykonalne przy użyciu innych metod. 


Przykłady algorytmów optymalizacji populacji obejmują:

<p>&nbsp;</p>

* Algorytm genetyczny

* Differential Evolution

* Particle Swarm Optimization


</p>
