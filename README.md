# 🧮 Wyznacznik Macierzy – Rozwinięcie Laplace'a (Laplace Expansion)

Implementacja w języku **Python** algorytmu obliczającego wyznacznik macierzy kwadratowej dowolnego stopnia $n \times n$ przy użyciu rekurencyjnego rozwinięcia Laplace'a oraz reguły Sarrusa dla podmacierzy $3 \times 3$.

## ⚙️ Jak działa algorytm?

1. **Optymalizacja wyboru wiersza/kolumny (`znajdzNajwiecejZer`)**: algorytm automatycznie wyszukuje wiersz lub kolumnę z największą liczbą zer, aby zminimalizować liczbę wywołań rekurencyjnych.
2. **Rekurencyjne rozwinięcie Laplace'a (`metodaLaplace`)**: dla macierzy stopnia $n > 3$ wyznacznik jest redukowany do minorów stopnia $n - 1$.
3. **Przypadki bazowe**:
   - dla macierzy $3 \times 3$ wyznacznik obliczany jest metodą przekątnych (reguła Sarrusa – `wyznacznik3`),
   - dla macierzy $2 \times 2$ bezpośrednio ze wzoru $ad - bc$.

## 🚀 Uruchomienie

```bash
python3 main.py
```
