def calculate_ways(n):
  ways = []
  for k in range(1, n+1):
      total_ways = k**2 * (k**2 - 1) // 2 - 4 * (k-1) * (k-2)
      ways.append(total_ways)
  return ways

# Input
n = int(input("Masukkan nilai n: "))

# Menghitung banyaknya cara untuk dua kuda pada k x k papan catur
hasil = calculate_ways(n)

# Output
for i, ways in enumerate(hasil):
  print(f"Banyaknya cara untuk n={i+1} adalah {ways}")
