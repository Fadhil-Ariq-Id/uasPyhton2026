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
    if tebak < number_rahasia:
        diff = number_rahasia - tebak
        print("\n❌ " + "▼"*3 + " TERLALU KECIL! " + "▼"*3)
        print(f"   💡 Hint: Coba angka yang LEBIH BESAR!")
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
    
    # Rating berdasarkan jumlah percobaan
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
    
    # Print riwayat dengan format cantik
    for i, angka in enumerate(riwayat, 1):
        status = "🎯" if angka == number_rahasia else "❌"
        print(f"   {status} Tebakan #{i:2d}: {angka:3d}")
    
    print_divider("═")
    print(f"   📈 Range: {min(riwayat)} - {max(riwayat)}")
    print(f"   🎲 Rata-rata: {sum(riwayat)/len(riwayat):.1f}")
    print_divider("═")

def tebak_rekursif(number_rahasia, percobaan=1, riwayat=None):
    """Fungsi rekursif untuk menebak angka dengan beautiful prints!"""
    
    # Inisialisasi riwayat jika None
    if riwayat is None:
        riwayat = []
    
    try:
        # Beautiful attempt header
        print_attempt_header(percobaan)
        
        # Input dengan style
        print("🎯 ", end="")
        tebak_str = input("Tebak angkanya (1-100): ")
        tebak = int(tebak_str)
        
        # Validasi range
        if tebak < 1 or tebak > 100:
            print("\n⚠️  Angka harus antara 1-100!")
            return tebak_rekursif(number_rahasia, percobaan, riwayat)
        
        # Simpan ke array
        riwayat.append(tebak)
        
        # Cek apakah benar
        if tebak == number_rahasia:
            print_victory(number_rahasia, percobaan, riwayat)
            return
        
        # Print hint dengan style
        print_hint(tebak, number_rahasia)
        
        # Rekursi ke percobaan berikutnya
        tebak_rekursif(number_rahasia, percobaan + 1, riwayat)
            
    except ValueError:
        print("\n" + "⚠️ "*10)
        print("❌ INPUT TIDAK VALID!")
        print("💡 Tolong masukkan ANGKA bulat (1-100)")
        print("⚠️ "*10)
        tebak_rekursif(number_rahasia, percobaan, riwayat)
    except KeyboardInterrupt:
        print("\n\n👋 Keluar dari game. Bye bye!")
        print(f"💔 Angka rahasianya adalah: {number_rahasia}\n")
        return

def play_game():
    """Main game function dengan beautiful interface"""
    
    # Beautiful header
    print_header()
    
    # Fun facts random
    facts = [
        "💡 Fun fact: Binary search bisa menebak dalam max 7 percobaan!",
        "💡 Fun fact: Rata-rata orang butuh 6-7 percobaan!",
        "💡 Fun fact: Lucky number-mu adalah 7! 🍀",
        "💡 Fun fact: Algoritma terbaik: mulai dari 50! 🧮"
    ]
    print(random.choice(facts))
    print()
    
    # Generate random number
    number_rahasia = random.randint(1, 100)
    
    # Start game
    tebak_rekursif(number_rahasia)
    
    # Play again?
    print("\n" + "╔"+"═"*58+"╗")
    print("║" + " "*20 + "MAIN LAGI?" + " "*25 + "║")
    print("╚"+"═"*58+"╝")
    
    ulang = input("\n🎮 Main lagi? (y/n): ").strip().lower()
    
    if ulang == "y":
        print("\n🔄 Loading game baru...")
        print("▓"*60)
        play_game()
    else:
        # Beautiful goodbye message
        print("\n" + "🌟"*30)
        print("""
    ╔════════════════════════════════════════╗
    ║   TERIMA KASIH SUDAH BERMAIN!       ║
    ║   Sampai jumpa lagi! 👋               ║
    ║   Keep gaming, keep smiling!         ║
    ╚════════════════════════════════════════╝
        """)
        print("🌟"*30 + "\n")

if __name__ == "__main__":
    try:
        play_game()
    except Exception as e:
        print(f"\n💥 Error: {e}")
        print("🔧 Silakan hubungi developer!")
