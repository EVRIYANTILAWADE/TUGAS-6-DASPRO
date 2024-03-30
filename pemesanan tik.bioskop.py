print("=" * 50)
print("Selamat Datang di Program Pemesanan Tiket Bioskop".center(50))
print("=" * 50)

filmgenre = {
    "action": ["UNCHARTED", "The Batman", "INDIANA JONES", "JOHN WICK", "Tenet"],
    "drama": ["Happiness", "Kingdom", "Sweet Home", "Signal", "The Glory"],
    "komedi": ["Gara gara warisan", "What happened to Mr.cha?", "Mangga muda", "Extreme job", "Kapal goyang kapten"],
    "horror": ["KKN di desa penari", "Danur", "Pengabdi setan", "Jelangkung", "Malam satu suro"],
    "anime": ["one piece", "Dragon bali", "Naruto", "Death note", "Pokemon"]
}

harga_biasa = 50000
harga_libur = 35000

print("=" * 50)
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
print("=" * 50)

if umur > 17:
    print("=" * 50)
    print("Selamat datang,", nama)
    print("=" * 50)

    print("=" * 50)
    print("Pilih genre film:")
    print("1. Action")
    print("2. Drama")
    print("3. Komedi")
    print("4. Horror")
    print("5. Anime")
    print("=" * 50)

    pilihan_genre = int(input("Masukkan nomor genre film yang ingin Anda tonton: "))

    if 1 <= pilihan_genre <= 5:
        genre = ""
        if pilihan_genre == 1:
            genre = "action"
        elif pilihan_genre == 2:
            genre = "drama"
        elif pilihan_genre == 3:
            genre = "komedi"
        elif pilihan_genre == 4:
            genre = "horror"
        elif pilihan_genre == 5:
            genre = "anime"

        print("=" * 50)
        print(f"Daftar film dalam genre {genre.lower()} :")
        for i in range(len(filmgenre[genre])):
            print(f"{i + 1}. {filmgenre[genre][i]}")
        print("=" * 50)

        pilihan_film = int(input(f"Masukkan nomor film {genre.lower()} yang ingin Anda tonton: "))

        if 1 <= pilihan_film <= 5:
            nama_film = filmgenre[genre][pilihan_film - 1]

            hari = input("Masukkan hari Anda ingin menonton (Senin/Selasa/Rabu/Kamis/Jumat/Minggu/Sabtu): ").lower()
            if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
                harga_tiket = harga_libur
            elif hari == "minggu" or hari == "sabtu":
                harga_tiket = harga_biasa
            else:
                print("Hari tidak valid.")
                exit()

            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin Anda beli: "))
            total_harga = harga_tiket * jumlah_tiket

            print(f"Harga tiket untuk {jumlah_tiket} tiket film '{nama_film}' pada hari {hari.lower()} adalah Rp{total_harga}.")
        else:
            print("Nomor film tidak valid.")
    else:
        print("Nomor genre tidak valid.")
else:
    print("=" * 50)
    print("Maaf, Anda harus berusia di atas 18 tahun untuk menonton film.")
    print ("=" * 50)