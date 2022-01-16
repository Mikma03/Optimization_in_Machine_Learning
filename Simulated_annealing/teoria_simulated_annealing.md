# Wstep - algorytm Simulated Annealing

Symulowane wyżarzanie to stochastyczny algorytm globalnej optymalizacji wyszukiwania. Oznacza to, że to
wykorzystuje losowość jako część procesu wyszukiwania. To sprawia, że algorytm jest odpowiedni
dla nieliniowych funkcji celu, w których inne lokalne algorytmy wyszukiwania nie działają dobrze. Lubić
algorytm lokalnego wyszukiwania stochastycznego wspinania się po wzgórzach, modyfikuje pojedyncze rozwiązanie i przeszukuje je
względnie lokalny obszar przestrzeni poszukiwań, aż do zlokalizowania lokalnego optima. W przeciwieństwie do wspinaczki górskiej
algorytm, może przyjąć gorsze rozwiązania jako aktualne rozwiązanie robocze. Prawdopodobieństwo
akceptowanie gorszych rozwiązań zaczyna się wysoko na początku wyszukiwania i maleje wraz z
postęp poszukiwań, dając algorytmowi możliwość najpierw zlokalizowania regionu dla
globalne optima, ucieczka od lokalnych optimów, a następnie wspinaczka na wzgórze do samego optima.

<p>&nbsp;</p>

Symulowane wyżarzanie1
to stochastyczny globalny algorytm optymalizacji wyszukiwania. Algorytm to
inspirowany wyżarzaniem w metalurgii2, gdzie metal jest szybko nagrzewany do wysokiej temperatury, a następnie
powoli schładza się, co zwiększa jego wytrzymałość i ułatwia pracę. Wyżarzanie
proces działa poprzez najpierw wzbudzenie atomów w materiale w wysokiej temperaturze, umożliwiając
atomy dużo się poruszają, a następnie powoli zmniejszają ich podekscytowanie, pozwalając atomom upaść
w nową, stabilniejszą konfigurację.

<p>&nbsp;</p>

Algorytm optymalizacji symulowanego wyżarzania można traktować jako zmodyfikowaną wersję
wspinaczki stochastycznej. Stochastyczna wspinaczka górska utrzymuje jedno potencjalne rozwiązanie i
wykonuje kroki o losowym, ale ograniczonym rozmiarze od kandydata w przestrzeni wyszukiwania. Jeśli
nowy punkt jest lepszy niż obecny, to aktualny punkt jest zastępowany nowym
punkt. Proces ten trwa przez ustaloną liczbę iteracji. Symulowane wyżarzanie wykonuje
szukaj w ten sam sposób. Główna różnica polega na tym, że nowe punkty nie są tak dobre jak
Aktualny punkt (gorsze punkty) są czasami akceptowane. Gorszy punkt jest akceptowany probabilistycznie
gdzie prawdopodobieństwo zaakceptowania rozwiązania gorszego od obecnego jest funkcją
temperatura wyszukiwania i o ile gorsze rozwiązanie jest od obecnego.

<p>&nbsp;</p>

Temperatura początkowa wyszukiwania jest podawana jako hiperparametr i maleje wraz z
postęp poszukiwań. Do:
zmniejszyć temperaturę podczas wyszukiwania od wartości początkowej do bardzo niskiej wartości, chociaż
powszechne jest obliczanie temperatury w funkcji liczby iteracji. Popularny przykład
do obliczania temperatury służy tzw. „szybkie wyżarzanie symulowane”, obliczane w następujący sposób:

<p>&nbsp;</p>

$$temperature = \frac{initial temperature}{iteration number + 1}$$

<p>&nbsp;</p>

Dodajemy jeden do numeru iteracji w przypadku, gdy numery iteracji zaczynają się od zera, aby uniknąć
dzielenie przez zero błędu. Akceptacja gorszych rozwiązań wykorzystuje zarówno temperaturę, jak i
różnica między oceną funkcji celu gorszego rozwiązania i prądu
rozwiązanie. Na podstawie tych informacji oblicza się wartość od 0 do 1, wskazując prawdopodobieństwo
zaakceptowania gorszego rozwiązania. Ten rozkład jest następnie próbkowany przy użyciu liczby losowej,
co, jeśli jest mniejsze niż wartość, oznacza akceptację gorszego rozwiązania.

<p>&nbsp;</p>

This is called the metropolis acceptance criterion and for minimization is calculated as
follows:

$$criterion = exp(-\frac{objective(new) − objective(current)
}{temperature})$$

<p>&nbsp;</p>

Gdzie $exp()$ to $e$ (stała matematyczna)
podniesiony do potęgi dostarczonego argumentu i
cel (nowy) i cel (bieżący) to ocena funkcji celu nowego (gorszego)
i aktualne rozwiązania kandydatów. Efekt jest taki, że słabe rozwiązania mają większe szanse bycia
zaakceptowany na początku wyszukiwania i mniej prawdopodobne, że zostanie zaakceptowany później w wyszukiwaniu. Intencją jest
że wysoka temperatura na początku poszukiwań pomoże poszukiwaniom zlokalizować nieckę
dla globalnych optimów i niskiej temperatury w dalszej części wyszukiwania pomoże w udoskonaleniu algorytmu
w globalnym optimie.

<p>&nbsp;</p>

