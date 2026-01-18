import random

def print_header():
    """hey selamat datang di welcome"""
    print("\n" + "="*60)
    print("🎮" + " "*20 + "TEBAK ANGKA GAME" + " "*20 + "🎮")
    print("="*60)
    print("✨ Game super simple: Tebak angka antara 1-100! ✨")
    print("="*60 + "\n")

def print_divider(char="─", length=60):
    """Beautiful divider"""
    print(char * length)

def print_box(text, emoji=""):
    """Print text dalam box yang cantik"""
    length = len(text) + 4
    print("┌" + "─" * length + "┐")
    print(f"│ {emoji} {text} {emoji} │")
    print("└" + "─" * length + "┘")

def print_attempt_header(percobaan):
    """Header untuk setiap percobaan"""
    print("\n" + "┈"*60)
    print(f"🎯 PERCOBAAN KE-{percobaan} 🎯".center(60))
    print("┈"*60)

def print_hint(tebak, number_rahasia):
    """Print hint dengan visual yang cantik"""
    
    # PERCABANGAN: if-else untuk cek apakah tebakan terlalu kecil atau besar
    # if = kalau kondisi benar, jalankan blok ini
    # else = kalau kondisi salah, jalankan blok ini
    if tebak < number_rahasia:
        diff = number_rahasia - tebak
        print("\n❌ " + "▼"*3 + " TERLALU KECIL! " + "▼"*3)
        print(f"   💡 Hint: Coba angka yang LEBIH BESAR!")
        
        # PERCABANGAN BERTINGKAT: if-elif-else untuk kasih hint berdasarkan jarak
        # elif = else if, cek kondisi lain kalau if sebelumnya salah
        if diff > 30:
            print(f"   🔥 Masih jauh banget nih! (+{diff})")
        elif diff > 15:
            print(f"   🌟 Lumayan jauh! (+{diff})")
        else:
            print(f"   ⭐ Udah deket! (+{diff})")
    else:
        diff = tebak - number_rahasia
        print("\n❌ " + "▲"*3 + " TERLALU BESAR! " + "▲"*3)
        print(f"   💡 Hint: Coba angka yang LEBIH KECIL!")
        
        # PERCABANGAN: sama kayak diatas, ngecek seberapa jauh tebakannya
        if diff > 30:
            print(f"   🔥 Masih jauh banget nih! (-{diff})")
        elif diff > 15:
            print(f"   🌟 Lumayan jauh! (-{diff})")
        else:
            print(f"   ⭐ Udah deket! (-{diff})")

def print_victory(number_rahasia, percobaan, riwayat):
    """Beautiful victory screen"""
    print("\n" + "🎊"*30)
    print("✨" * 30)
    print()
    print("██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗")
    print("██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝")
    print("██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ ")
    print("╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  ")
    print(" ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   ")
    print("  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ")
    print()
    print("✨" * 30)
    print("🎊"*30 + "\n")
    
    print(f"🏆 SELAMAT! Kamu berhasil menebak angka {number_rahasia}!")
    print(f"⚡ Total percobaan: {percobaan} kali")
    
    # PERCABANGAN: if-elif-else untuk kasih rating berdasarkan jumlah percobaan
    # makin sedikit percobaan = makin bagus ratingnya
    if percobaan <= 5:
        print("🌟🌟🌟 PERFECT! Kamu jenius! 🧠✨")
    elif percobaan <= 10:
        print("⭐⭐ GREAT! Lumayan jago! 👍")
    elif percobaan <= 15:
        print("⭐ GOOD! Keep practicing! 💪")
    else:
        print("😅 Not bad! Practice makes perfect!")
    
    print("\n📊 RIWAYAT TEBAKAN:")
    print_divider("═")
    
    # PERULANGAN: for loop untuk print semua riwayat tebakan
    # for = ulangi untuk setiap item dalam array/list
    # enumerate(riwayat, 1) = ambil index (mulai dari 1) dan nilai sekaligus
    # i = nomor urut, angka = nilai tebakan dari array riwayat
    for i, angka in enumerate(riwayat, 1):
        # PERCABANGAN: ternary if untuk kasih emoji berbeda
        # "A" if kondisi else "B" = kalau kondisi benar pakai A, kalau salah pakai B
        status = "🎯" if angka == number_rahasia else "❌"
        print(f"   {status} Tebakan #{i:2d}: {angka:3d}")
    
    print_divider("═")
    
    # ARRAY OPERATIONS: min(), max(), sum(), len() untuk statistik dari array riwayat
    # min(riwayat) = angka terkecil dalam array
    # max(riwayat) = angka terbesar dalam array
    # sum(riwayat) = total jumlah semua angka
    # len(riwayat) = panjang array (berapa banyak elemen)
    print(f"   📈 Range: {min(riwayat)} - {max(riwayat)}")
    print(f"   🎲 Rata-rata: {sum(riwayat)/len(riwayat):.1f}")
    print_divider("═")

# REKURSI: fungsi yang memanggil dirinya sendiri
# tebak_rekursif() akan terus panggil tebak_rekursif() sampai user menang
def tebak_rekursif(number_rahasia, percobaan=1, riwayat=None):
    """Fungsi rekursif untuk menebak angka dengan beautiful prints!"""
    
    # ARRAY: inisialisasi array kosong untuk simpan riwayat tebakan
    # riwayat = [] artinya buat list/array kosong
    # None = belum ada nilai, jadi kita buat array baru
    if riwayat is None:
        riwayat = []
    
    try:
        print_attempt_header(percobaan)
        
        # INPUT USER: input() untuk ambil data dari keyboard user
        # input("text") = tampilkan text, tunggu user ketik, return hasilnya
        print("🎯 ", end="")
        tebak_str = input("Tebak angkanya (1-100): ")
        
        # int() = konversi string jadi integer (angka bulat)
        tebak = int(tebak_str)
        
        # PERCABANGAN: validasi apakah input dalam range 1-100
        # or = salah satu kondisi benar, maka true
        if tebak < 1 or tebak > 100:
            print("\n⚠️  Angka harus antara 1-100!")
            # REKURSI: panggil diri sendiri lagi untuk input ulang
            return tebak_rekursif(number_rahasia, percobaan, riwayat)
        
        # ARRAY: append() untuk tambah elemen baru ke akhir array
        # riwayat.append(tebak) = masukin nilai tebak ke array riwayat
        riwayat.append(tebak)
        
        # PERCABANGAN: cek apakah tebakan benar
        # == artinya sama dengan (perbandingan)
        if tebak == number_rahasia:
            print_victory(number_rahasia, percobaan, riwayat)
            return  # return tanpa nilai = keluar dari fungsi, stop rekursi
        
        print_hint(tebak, number_rahasia)
        
        # REKURSI: panggil fungsi ini lagi dengan percobaan + 1
        # ini yang bikin game terus berjalan sampai user menang
        # percobaan + 1 = naikin counter percobaan
        tebak_rekursif(number_rahasia, percobaan + 1, riwayat)
            
    except ValueError:
        # PERCABANGAN: except = tangkap error kalau input bukan angka
        print("\n" + "⚠️ "*10)
        print("❌ INPUT TIDAK VALID!")
        print("💡 Tolong masukkan ANGKA bulat (1-100)")
        print("⚠️ "*10)
        # REKURSI: panggil lagi untuk input ulang
        tebak_rekursif(number_rahasia, percobaan, riwayat)
    except KeyboardInterrupt:
        print("\n\n👋 Keluar dari game. Bye bye!")
        print(f"💔 Angka rahasianya adalah: {number_rahasia}\n")
        return

# REKURSI: play_game() juga rekursif karena bisa panggil dirinya sendiri
# kalau user mau main lagi
def play_game():
    """Main game function dengan beautiful interface"""
    
    print_header()
    
    # ARRAY: list/array berisi string fun facts
    # [] dengan koma = cara buat array dengan banyak elemen
    facts = [
        "💡 Fun fact: Binary search bisa menebak dalam max 7 percobaan!",
        "💡 Fun fact: Rata-rata orang butuh 6-7 percobaan!",
        "💡 Fun fact: Lucky number-mu adalah 7! 🍀",
        "💡 Fun fact: Algoritma terbaik: mulai dari 50! 🧮"
    ]
    # random.choice(facts) = ambil satu elemen random dari array
    print(random.choice(facts))
    print()
    
    # random.randint(1, 100) = generate angka random antara 1-100
    number_rahasia = random.randint(1, 100)
    
    # panggil fungsi rekursif untuk mulai game
    tebak_rekursif(number_rahasia)
    
    print("\n" + "╔"+"═"*58+"╗")
    print("║" + " "*20 + "MAIN LAGI?" + " "*25 + "║")
    print("╚"+"═"*58+"╝")
    
    # INPUT USER: input() untuk tanya apakah mau main lagi
    # .strip() = hapus spasi di awal dan akhir
    # .lower() = jadikan huruf kecil semua
    ulang = input("\n🎮 Main lagi? (y/n): ").strip().lower()
    
    # PERCABANGAN: if-else untuk cek jawaban user
    if ulang == "y":
        print("\n🔄 Loading game baru...")
        print("▓"*60)
        # REKURSI: panggil play_game() lagi untuk main lagi
        play_game()
    else:
        print("\n" + "🌟"*30)
        print("""
    ╔════════════════════════════════════════╗
    ║   TERIMA KASIH SUDAH BERMAIN!       ║
    ║   Sampai jumpa lagi! 👋               ║
    ║   Keep gaming, keep smiling!         ║
    ╚════════════════════════════════════════╝
        """)
        print("🌟"*30 + "\n")

# PERCABANGAN: ini cek apakah file dijalankan langsung (bukan di-import)
# __name__ == "__main__" = true kalau file ini dijalankan langsung
if __name__ == "__main__":
    try:
        # panggil fungsi utama untuk mulai game
        play_game()
    except Exception as e:
        # PERCABANGAN: except untuk tangkap semua error
        print(f"\n💥 Error: {e}")
        print("🔧 Silakan hubungi developer!")
