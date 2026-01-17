import random

def tebak_rekursif(number_rahasia, percobaan=1):
    try:
        # input 
        tebak_str = input("coba tebak hayo?.... ")
        tebak = int(tebak_str)
        
        # jika benar
        if tebak == number_rahasia:
            print(f"yes itu benar congrats! {number_rahasia} dalam {percobaan} percobaan.")
            return
        
        
        if tebak < number_rahasia:
            print("salah>> terlalu kecil")
        else:
            print("salah...terlalu besar")
            
        # rekuris pangigl 
        tebak_rekursif(number_rahasia, percobaan + 1)
            
    except ValueError:
        print("input tidak valid, please masukkan ulang ")
        tebak_rekursif(number_rahasia, percobaan)

def play_game():
    print("\nSelamat datang di game tebak angka!!")
    print("Game nya super simple, just guess the number between 1 and 100")
    
    # random nomor 1 -100
    number_rahasia = random.randint(1, 100)
    
 #start
    tebak_rekursif(number_rahasia)
    
   # ulang ?
    ulang = input("Apakah anda ingin mengulang permainan? (y/n): ")
    if ulang.lower() == "y":
        play_game()
    else:
        print("Terima kasih sudah bermain!")

if __name__ == "__main__":
    play_game()