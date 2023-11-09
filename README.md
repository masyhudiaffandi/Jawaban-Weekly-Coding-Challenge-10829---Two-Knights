# Jawaban-Weekly-Coding-Challenge-10829---Two-Knights

---

# Two Knights

Tugas ini meminta Anda untuk menghitung banyaknya cara dua kuda dapat ditempatkan pada papan catur berukuran k x k sehingga mereka tidak saling menyerang. Kuda hanya dapat bergerak mengikuti pola L.

## Cara Penggunaan

1. Buka terminal atau command prompt.

2. Jalankan skrip Python dengan perintah berikut:

   ```bash
   python main.py
   ```

3. Masukkan nilai `n` (ukuran papan catur) ketika diminta. Tetapi karena pada point output output disebutkan bahwa input yang diinginkan adalah `8`, maka pada point ini saya akan memasukkan angka `8`

4. Program akan menghitung dan mencetak banyaknya cara untuk setiap `k` dari 1 hingga `n`.

## Contoh Output

```plaintext
Banyaknya cara untuk n=1 adalah 0
Banyaknya cara untuk n=2 adalah 6
Banyaknya cara untuk n=3 adalah 28
Banyaknya cara untuk n=4 adalah 96
Banyaknya cara untuk n=5 adalah 252
...
```

## Dokumentasi Kode

### Fungsi `calculate_ways(n)`

```python
def calculate_ways(n):
    """
    Menghitung banyaknya cara dua kuda dapat ditempatkan pada k x k papan catur sehingga mereka
    tidak saling menyerang.

    Args:
        n (int): Ukuran papan catur (k).

    Returns:
        list: Daftar banyaknya cara untuk setiap k dari 1 hingga n.
    """
    # ...
```

### Input dan Output

```python
# Input
n = int(input("Masukkan nilai n: "))

# Menghitung banyaknya cara untuk dua kuda pada k x k papan catur
hasil = calculate_ways(n)

# Output
for i, ways in enumerate(hasil):
    print(f"Banyaknya cara untuk n={i+1} adalah {ways}")
```

---

