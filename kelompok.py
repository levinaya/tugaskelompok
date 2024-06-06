import os
import queue

class myQueue:
    def _init_(self):
        self.items = queue.Queue()

    def isEmpaty(self):
        return self.items.empty()
    
    def qAdd(self, item):
        self.items.put(item)

    def qOut(self):
        if not self.items.empty():
            return self.items.get()
        else :
            return "DATA ANTRIAN KOSONG"
    def size(self):
        return self.items.qsize()
    
def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            print("========================================")
            print("| -----SIMULASI ANTRIAN MESIN ATM----- |")
            print("| by : kaa                             |")
            print("========================================")
            print("1.Masuk Antrian")
            print("2.Keluar Antrian")
            print("3.Cek Antrian")
            print("4.Keluar Program")
            print("========================================")
            pilihan = str(input("SILAKKAN MASUKKAN PILIHAN ANDA : "))
            if(pilihan == "1"):
                os.system("cls")
                print("---------------------------------------------------")
                obj = str(input("Masukkan nomor antrian yang ingin anda tambahkan : "))
                self.qAdd(obj)
                print("---------------------------------------")
                print("Nomor "+obj+" telah di masukkan antrian")
                print("---------------------------------------")
                x = input("")
            elif(pilihan == "2"):
                os.system("cls")
                temp = self.qOut()
                if temp != "DATA ANTRIAN KOSONG":
                    print("---------------------------------")
                    print("Kendaraan "+temp+" keluar antrian")
                    print("---------------------------------")
                else:
                    print("--------------")
                    print("Antrian kosong")
                    print("--------------")
                    x = input("")
            elif(pilihan == "3"):
                os.system("cls")
                print("--------------------------------")
                print("Panjang dari queue(antrian) adalah "+str(self.size()))
                print("--------------------------------")
                x = input("")
            elif(pilihan == "4"):
                os.system("cls")
                print("-----------------------------------------------")
                print("TERIMAKASIH TELAH MEMAKAI PROGRAM INI")
                print("SILAHKAN TEKAN ENTER UNTUK MENGHENTIKAN PROGRAM")
                print("SEMOGA HARI MU MENYENANGKAN!!")
                print("-----------------------------------------------")
                print(quit())
            else:
                print("------------------------------------------------")
                print("MAAF PILIHAN ANDA TIDAK TERDAFTAR DI PROGRAM INI")
                print("------------------------------------------------")

if _name_ == "_main_":
    q = myQueue()
    q.mainmenu()