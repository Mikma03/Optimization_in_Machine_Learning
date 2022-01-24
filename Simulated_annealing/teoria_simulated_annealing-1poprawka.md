# Wstep - algorytm Simulated Annealing

<p>&nbsp;</p>

Symulowane wyżarzanie to stochastyczny algorytm globalnej optymalizacji. Oznacza to, że wykorzystuje losowość jako część procesu wyszukiwania. To sprawia, że algorytm jest odpowiedni dla nieliniowych funkcji celu, w których inne lokalne algorytmy wyszukiwania nie działają dobrze. 

Algorytm lokalnego wyszukiwania stochastycznego wspinania się po wzgórzach, modyfikuje pojedyncze rozwiązanie i przeszukuje je aż do zlokalizowania lokalnego optimum. 

Niestety algorytm może przyjąć gorsze rozwiązania jako aktualne rozwiązanie wyjściowe. 

Prawdopodobieństwo zaakceptowania gorszych rozwiązań jest wysokie na początku wyszukiwania i maleje wraz z postępem poszukiwań, dając algorytmowi możliwość najpierw zlokalizowania regionu dla globalnego optimum w kierunku od lokalnych optimów.

<p>&nbsp;</p>

Algorytm inspirowany jest wyżarzaniem w metalurgii, gdzie metal jest szybko nagrzewany do wysokiej temperatury, a następnie powoli schładza się, co zwiększa jego wytrzymałość i ułatwia pracę. 

Proces działa poprzez wzbudzenie atomów w materiale w wysokiej temperaturze a następnie powoli zmniejsza się ich zmiennosc, pozwalając atomom znaleźć się w stanie stabilniejszej konfiguracji.

<p>&nbsp;</p>

Algorytm optymalizacji symulowanego wyżarzania można traktować jako zmodyfikowaną wersję wspinaczki. Stochastyczna wspinaczka górska utrzymuje jedno potencjalne rozwiązanie i wykonuje kroki o losowym, ale ograniczonym rozmiarze od kandydata w przestrzeni potencjalnych rozwiazan. 


Jeśli nowy punkt jest lepszy niż obecny, to aktualny punkt jest zastępowany nowym punktem. Proces ten trwa przez ustaloną liczbę iteracji. Symulowane wyżarzanie wykonuje wyszukiwanie w ten sam sposób. 

Główna różnica polega na tym, że nowe punkty czasami nie są tak dobre jak aktualne punkty, co prowadzi do akceptacji. 

Gorszy punkt jest akceptowany probabilistycznie, gdzie prawdopodobieństwo zaakceptowania rozwiązania gorszego od obecnego jest funkcją
temperatury wyszukiwania.

<p>&nbsp;</p>

Temperatura początkowa wyszukiwania jest podawana jako hiperparametr i maleje wraz z postępem poszukiwań. 

Popularny przykład do obliczania temperatury tzw. „szybkie wyżarzanie symulowane”, obliczany w następujący sposób:

<p>&nbsp;</p>

$$temperature = \frac{initial temperature}{iteration number + 1}$$

<p>&nbsp;</p>

Dodajemy jeden do numeru iteracji w przypadku, gdy numery iteracji zaczynają się od zera, aby uniknąć dzielenia przez zero. Akceptacja gorszych rozwiązań wykorzystuje zarówno temperaturę, jak i różnicę między oceną funkcji celu gorszego rozwiązania i obecnego rozwiązania. 

Na podstawie tych informacji oblicza się wartość od 0 do 1, wskazując prawdopodobieństwo zaakceptowania gorszego rozwiązania. Ten rozkład jest następnie próbkowany przy użyciu liczby losowej, co oznacza akceptację gorszego rozwiązania (jeśli jest mniejsze niż wartość).

<p>&nbsp;</p>

Nazywa się to kryterium akceptacji metropolii i dla minimalizacji oblicza się jako:

$$criterion = exp(-\frac{objective(new) − objective(current)
}{temperature})$$

<p>&nbsp;</p>

Gdzie $exp()$ to $e$ podniesiony do potęgi dostarczonego argumentu, cel (nowy) i cel (bieżący)
 to oceny funkcji celu nowego (gorszego)
i aktualnego rozwiązania kandydatów. Efekt jest taki, że słabe rozwiązania mają większe szanse bycia zaakceptowanymi na początku wyszukiwania i mniejsze prawdopodobieństwo, że zostaną zaakceptowana później w wyszukiwaniu. 

Intencją jest że wysoka temperatura na początku poszukiwań pomoże zlokalizować globalne optima i niska temperatura w dalszej części wyszukiwania pomoże w udoskonaleniu algorytmu w globalnym optimum.

<p>&nbsp;</p>

