nama = "Natasyah Putri Dwi Rizki"
target = "a"

posisi = -1

for i in range (len(nama)):
    if nama[i] == target:
        posisi = i
        break

if posisi != -1:
    print(f"Huruf '{target}' pertama ditemukan pada indeks ke-{posisi}")

else:
    print("Huruf tidak ditemukan")