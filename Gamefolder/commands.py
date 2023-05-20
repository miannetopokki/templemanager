#KUMPULAN IMPORTS
import tools
import data
import randomiser
import os
import argparse
import helpmenu


#GLOBAL VARIABLE
isLoggedIn = False
RoleUser = ""
NamaUser = ""




#ARGPARSE


parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", nargs="?", help="nama folder yang ingin dibuat")

args = parser.parse_args()

if args.nama_folder is None:
    parser.print_usage()
    print("Tidak ada nama folder yang diberikan!")
    exit()


folderload =  "save/" + str(args.nama_folder) 

if not os.path.exists(folderload):
    print(f"Folder '{args.nama_folder}' tidak ditemukan")
    exit()



# ===================================== F13 - Load ==========================================
user = []
user  = data.load(str(folderload) + "/user.csv",user)
candi = []
candi = data.load(str(folderload) + "/candi.csv",candi)
bahan_bangunan = []  # pasir, batu, air berurut
bahan_bangunan = data.load(str(folderload) + "/bahan_bangunan.csv",bahan_bangunan) #[[nama;deskripsi;jumlah]]
# OPENING PROGRAM
os.system("cls")
introtext = """


▀▀█▀▀ █▀▀ █▀▄▀█ █▀▀█ █░░ █▀▀ 　 ▒█▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀ █▀▀ █▀▀█  
░▒█░░ █▀▀ █░▀░█ █░░█ █░░ █▀▀ 　 ▒█▒█▒█ █▄▄█ █░░█ █▄▄█ █░▀█ █▀▀ █▄▄▀  
░▒█░░ ▀▀▀ ▀░░░▀ █▀▀▀ ▀▀▀ ▀▀▀ 　 ▒█░░▒█ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀

sɪʟᴀʜᴋᴀɴ ʟᴏɢɪɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ
ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ 'help' ᴊɪᴋᴀ ᴀɴᴅᴀ ʙɪɴɢᴜɴɢ
"""

print(introtext)




# ========================================== F01 - LOGIN ==========================================
def login():
    global RoleUser
    global isLoggedIn
    global NamaUser
    n = tools.lenarray(user)
    cekuser = False
    cekpass = False
  
    #CEK apakah sudah login atau belum
    if isLoggedIn:
        print("Login gagal!")
        print("Anda telah login dengan username ",RoleUser," silahkan lakukan fungsi logout sebelum melakukan login kembali.")
        return
    
    username = input("Username: ")
    password = input("Password: ")
    for i in range(n):
        
        
        if username == user[i][0] and password == user[i][1]:
            print(f"Selamat datang, {username}!")
            cekuser = True
            cekpass = True
            isLoggedIn = True
            RoleUser = user[i][2]
            NamaUser = username
            
            print("login")
            break
        elif username != user[i][0] and password == user[i][1]:
            cekuser = False
            cekpass = True
            print("error 1")
        elif username == user[i][0] and password != user[i][1]:
            cekuser = True
            cekpass = False
            print("error 2")
    if cekuser == False:
        print("Username tidak terdaftar!")
    elif cekpass == False:
        print("Password salah!")

        

#========================================== F02 - LOGIN ==========================================

#FUNCTIONS / PROCEDURE
def logout():
    global isLoggedIn
    global RoleUser
    global NamaUser
    # cek apakah user telah login sebelumnya
    if isLoggedIn == True :
        isLoggedIn = False
        RoleUser = ""
        NamaUser = ""
        print("Anda berhasil logout.")
    else:
        print("Logout gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        
#========================================== F03 - SummonJin ==========================================
def summonJin(jin) :
    
    jumlah = tools.lenarray(jin)
    if jumlah != 100 & jumlah <= 100 : #kondisi ketika jumlah jin tidak sama dengan 100, maka summon jin masih bisa dilakukan
        print(f"""\rJenis jin yang dapat dipanggil:

                \r  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
                \r  (2) Pembangun - Bertugas membangun candi """)
        jenis = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")) #varibel jenis digunakan untuk menginput jenis jin
        jenis_jin =""
        
        while jenis < 1 or jenis > 2:
            print(f"Tidak ada jenis jin bernomor “{jenis}”!")
            jenis = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")) #varibel jenis digunakan untuk menginput jenis jin

        if jenis == 1 : #kondisi ketika jenis jin yang diinput jenis 1 (pengumpul)
            jenis_jin = "jin_pengumpul" 
            print(f"memilih jin “Pengumpul”.")
        elif jenis == 2 : #kondisi ketika jenis jin yang diinput jenis 2 (pembangun)
            jenis_jin = "jin_pembangun"
            print(f"memilih jin “Pembangun”.")
     
            
          
        duplikat = True 

       
        while duplikat == True:
            username = input("\nMasukkan username jin: ") #variabel username digunakan untuk menginput nama jin
            #pengecekan berkala apakah ada username yang duplikat
            for i in range(1,jumlah) :
                if jin[i][0] == str(username) : 
                    print(f"\nUsername “{username}” sudah diambil!")

                    break 
                elif jin[i][0] != str(username) and i == jumlah-1:  #sudah tercek semua dan tak ada yang sama
                    duplikat = False 
                    break

        password = input("Masukkan password jin: ") #variabel password digunakan untuk menampung password dari tiap jin
        while not 5 <= len(password) <= 25 : #ketika panjang password kurang dari 5/lebih dari 25
                print("\nPassword panjangnya harus 5-25 karakter!")
                password = input("\nMasukkan password jin: ") #user akan diminta untuk input password baru
        print(f"""
        \rMengumpulkan sesajen...
        \rMenyerahkan sesajen...
        \rMembacakan mantra...

        \rJin {username} berhasil dipanggil!\n""") #ketika panjang password >= 5 dan <= 25, maka summon jin berhasil
        

        tools.appendarray(user,[username,password,jenis_jin]) #menambah elemen baru ke dalam array user menggunakan fungsi appendarray dari tools
  
    else : #kondisi ketika jumlah jin sama dengan 100, maka summon jin sudah tidak dapat dilakukan lagi (batas max summon jin)
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu.")

# ========================================== F04 - HilangkanJin ==========================================
def hapusjin():
    
    markkosong = "HAPUS"
    ncandi = tools.lenarray(candi) #Pengecekan list yang sudah terisi
    nuser = tools.lenarray(user)
    Ditemukan = False




    namajin = input("Masukkan username jin: ")
    #Pengecekan apakah username jin ditemukan atau tidak
    for i in range(1,nuser):
        if namajin == user[i][0] :
            Ditemukan = True
            
        if Ditemukan == True:
            print("Apakah anda yakin ingin menghapus jin dengan username" , namajin, "(Y/N) ")
            keputusan = input()
            if keputusan == "Y" or keputusan == "y":
                user[i] = markkosong
                for i in range(1,ncandi):
                    if namajin == candi[i][1]:
                        candi[i] = markkosong
                        candi[0] += 1
                print(namajin, " Berhasil dihapus :(")
                break
            elif keputusan =="N" or keputusan =="n":
                print("Tidak jadi dihapus")
                break
                        
            
        #print(tools.convertarray(candi))



# Jika jawaban dari keputusan adalah n atau N maka keputusan tidak dijalankan
    if Ditemukan == False: 
        print("Tidak ada jin dengan username tersebut.")





#========================================== F05 - Ubah Tipe Jin ==========================================
def ubahTipeJin(): 
    n = tools.lenarray(user)

    username = input("Masukkan username jin : ")
    cekuser = False
    for i in range(n):
        if username == user[i][0]:
            if user[i][2] == "jin_pengumpul":
                answer = input('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ')
                if answer == "Y" or answer == "y":
                    print("Jin telah berhasil diubah.")
                    user[i][2] = 'jin_pembangun'
                    cekuser = True
                else:
                    print("jin tidak diubah")
                    cekuser = True
            elif user[i][2] == "jin_pembangun":
                answer = input('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul?" (Y/N)? ')
                if answer == "Y" or answer == "y":
                    print("Jin telah berhasil diubah.")
                    user[i][2] = 'jin_pengumpul'
                    cekuser = True
                else:
                    print("jin tidak diubah")
                    cekuser = True

       

    
    if cekuser == False: #jika kondisi masih false(username tidak ditemukan)
        print("Tidak ada jin bernama ini.")

# ========================================== F06 - Jin Pembangun ==========================================
def cekhancur(arrcandi): #Fungsi ini mengembalikan nilai index mark 'HANCUR'
    n = tools.lenarray(arrcandi)
    pointer = 1
    for i in range(1,n):

        if arrcandi[i][0] != str(pointer):
            return i
   
        pointer += 1


def bangun (namajin):
    requiredbahan = [randomiser.randomnumbergenerator(randomiser.lcgbangun,10000000),randomiser.randomnumbergenerator(randomiser.lcgbangun,1000000),randomiser.randomnumbergenerator(randomiser.lcgbangun,100000)]
    notvalidbahan = False
    print("Jumlah bahan yang dibutuhkan adalah : " , requiredbahan[0], " Pasir, ", requiredbahan[1] ," Batu dan ", requiredbahan[2] , " Air.") 
    print("Jumlah bahan yang tersedia adalah : " , bahan_bangunan[0][2], " Pasir, ", bahan_bangunan[1][2] ," Batu dan ", bahan_bangunan[2][2] , " Air.")
    count = 0
  
    #Cek apakah bahan cukup untuk bangun, bila salah satu kriteria tidak memenuhi(pasir ato batu ato air) maka tidak akan dibangun
    while notvalidbahan == False and count <= 2 :
        if (bahan_bangunan[count][2] < requiredbahan[count]):
            notvalidbahan = True
            
            break
        else:
            count += 1
    
    if notvalidbahan == False and candi[0] != 0:
         #Candi yang kebangun , candi yang ke-berapa
        candi[0] -= 1
        for i in range(3): # in range 3 karena panjang inentory pasti cuma 3, (0,1,2)
            bahan_bangunan[i][2] -= requiredbahan[i]
        


        print("Candi berhasil dibangun")
        print("Sisa candi yang perlu dibangun :" , candi[0])

        #PENGECEKAN APABILA ADA YANG KOSONG,TERHAPUS,PENAMBAHAN CANDI BERDASARKAN ID TERKECIL YANG HILANG

        if cekhancur(candi) != None:
            nilaikosong = cekhancur(candi)
            if candi[nilaikosong] == "HAPUS": #yang dihapus
                 # MENGUBAH ARRAY candi SESUAI KRITERIA BAHAN BANGUNAN,NAMA JIN YANG BANGUN,DAN ID CANDI
                IDCandi = [str(nilaikosong),namajin,str(requiredbahan[0]),str(requiredbahan[1]),str(requiredbahan[2])]
                candi[nilaikosong] = IDCandi
            else: #kalau bukan ada "HAPUS"
                IDCandi = [str(nilaikosong),namajin,str(requiredbahan[0]),str(requiredbahan[1]),str(requiredbahan[2])]

                tools.appendarray(candi,IDCandi)
                tools.sortidcandi(candi,tools.lenarray(candi)) # Sort ascending

        else:
             # MENGUBAH ARRAY candi SESUAI KRITERIA BAHAN BANGUNAN,NAMA JIN YANG BANGUN,DAN ID CANDI
            IDCandi = [str(tools.lenarray(candi)),namajin,str(requiredbahan[0]),str(requiredbahan[1]),str(requiredbahan[2])]
            tools.appendarray(candi,IDCandi)
    

        #print(tools.convertarray(candi))
        

    

        
    elif(notvalidbahan == False and candi[0] == 0): 
        for i in range(3): # in range 3 karena panjang inentory pasti cuma 3, (0,1,2)
            bahan_bangunan[i][2] -= requiredbahan[i]

        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun :", candi[0])
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun")
# ========================================== F07 - Jin Pengumpul  ==========================================
def kumpul(namajin):
    bahankumpul = [randomiser.randomnumbergenerator(randomiser.lcgkumpul,10000000),randomiser.randomnumbergenerator(randomiser.lcgkumpul,1000000),randomiser.randomnumbergenerator(randomiser.lcgkumpul,100000)]

    for i in range(3):  # in range 3 karena panjang inentory pasti cuma 3, (0,1,2)
        bahan_bangunan[i][2] += bahankumpul[i]

    print(namajin, "menemukan " + str(bahankumpul[0]) + " pasir, "+ str(bahankumpul[1]) + " batu, "+ str(bahankumpul[2]) + " air, ")
    



# ===================================== F08 - Batch Kumpul / Bangun  ==========================================

# =============== F08.1 Batch Kumpul =============
def batchkumpul():

    jumlahpengumpul = 0
    pasir = 0
    batu = 0
    air = 0
    n = tools.lenarray(user)

    for i in range(n):
        if user[i][2] == "jin_pengumpul":
            jumlahpengumpul += 1
            pasir += randomiser.randomnumbergenerator(randomiser.lcgkumpul,10000000)
            batu += randomiser.randomnumbergenerator(randomiser.lcgkumpul,1000000)
            air += randomiser.randomnumbergenerator(randomiser.lcgkumpul,100000)
          

        i += 1
     #panjang array bahan banguna cuma 3
    bahan_bangunan[0][2] += pasir
    bahan_bangunan[1][2] += batu
    bahan_bangunan[2][2] += air

    if jumlahpengumpul > 0:
        print(f"Mengerahkan {jumlahpengumpul} jin untuk mengumpulkan bahan.")
        print(f"jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")
                
        
    else: #kondisi ketika jumlahpengumpul sama dengan 0
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")


# ================== F08.2 Batch Bangun ===============
def bangununtukbatch (namajin,listbahan):
    
    requiredbahan = listbahan
    if  candi[0] != 0:
        #Candi yang kebangun , candi yang ke-berapa
        candi[0] -= 1
        for i in range(3): # in range 3 karena panjang inentory pasti cuma 3, (0,1,2)
            bahan_bangunan[i][2] -= requiredbahan[i]
        
        
 
        if cekhancur(candi) != None:
            nilaikosong = cekhancur(candi)
            if candi[nilaikosong] == "HAPUS": #yang dihapus
                IDCandi = [str(nilaikosong),namajin,str(requiredbahan[0]),str(requiredbahan[1]),str(requiredbahan[2])]
                candi[nilaikosong] = IDCandi
            else: #kalau bukan ada "HAPUS"
                IDCandi = [str(nilaikosong),namajin,str(requiredbahan[0]),str(requiredbahan[1]),str(requiredbahan[2])]
                tools.appendarray(candi,IDCandi)
                tools.sortidcandi(candi,tools.lenarray(candi)) #Sort ascending
            
        else:
            IDCandi = [str(tools.lenarray(candi)),namajin,str(requiredbahan[0]),str(requiredbahan[1]),str(requiredbahan[2])]
            tools.appendarray(candi,IDCandi)
    
        #print(tools.convertarray(candi))


        
    elif(candi[0] == 0): 
        for i in range(3): # in range 3 karena panjang inentory pasti cuma 3, (0,1,2)
            bahan_bangunan[i][2] -= requiredbahan[i]


def batchbangun():
    notvalidbahan = False
    sumBahan = [0,0,0]
    n = tools.lenarray(user)
    #Hitung berapa banyak jin pembangun dari array users (jin pembangun berkode '2' )
    nJinPembangun = 0
    for i in range(n):
        if user[i][2] == "jin_pembangun":  #role
            nJinPembangun += 1

    if nJinPembangun != 0:

        listNamaJin = ["" for i in range(nJinPembangun)] 


        #Menginput nama jin pembangun dalam array listNamajin
        j = 0
        for i in range(n): #max 100 jin di spek, 
            if user[i][2] == "jin_pembangun":
                listNamaJin[j] = user[i][0]
                j += 1



        #list bahan dalam bentuk matriks dari tiap randomiser jin
        matriksbahan = [[0 for i in range(3)] for j in range(nJinPembangun)]


        #Hitung total bahan yang diperlukan
        for i in range(nJinPembangun):

            requiredbahan = [randomiser.randomnumbergenerator(randomiser.lcgbangun,10000000),randomiser.randomnumbergenerator(randomiser.lcgbangun,1000000),randomiser.randomnumbergenerator(randomiser.lcgbangun,100000)]
            for j in range(3): # max bahan cuma 3, pasir batu air
                matriksbahan[i][j] = requiredbahan[j]
                sumBahan[j] += requiredbahan[j]


        
        count = 0
        while notvalidbahan == False and count <= 2 :
            if (bahan_bangunan[count][2] < sumBahan[count]):
                notvalidbahan = True
                
                break
            else:
                count += 1

        
        if notvalidbahan == True:
            pasir = ""
            batu = ""
            air = ""
            if (sumBahan[0] - bahan_bangunan[0][2]) > 0:
                pasir = str(sumBahan[0] - bahan_bangunan[0][2]) + " pasir"

            if(sumBahan[1] - bahan_bangunan[1][2] > 0):
                batu = str(sumBahan[1] - bahan_bangunan[1][2]) + " batu"

            if(sumBahan[2] - bahan_bangunan[2][2] > 0):
                air = str(sumBahan[2] - bahan_bangunan[2][2]) + " air"
                
            print("Bangun gagal. Kurang ", pasir, batu, air)

        else:
        
            for i in range(nJinPembangun):
                bangununtukbatch(listNamaJin[i],matriksbahan[i])
            
            print("Mengerahkan" , nJinPembangun, " Jin Pembangun Untuk Membangun candi dengan total bahan",sumBahan[0], "pasir, ", sumBahan[1] , "batu, dan ", sumBahan[2] ," air." )
    else:
        print("Batch Bangun gagall. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu. ")      



# ===================================== F09 - Ambil Laporan Jin  ==========================================
def LaporanJin():

    nuser = tools.lenarray(user)
    ncandi = tools.lenarray(candi)
    


    
    
    jin_kumpul = 0
    jin_bangun = 0
    total_pasir = bahan_bangunan[0][2]
    total_air = bahan_bangunan[1][2]
    total_batu = bahan_bangunan[2][2]
    
    countlistjin = [0 for i in range(nuser)] # bikin list banyaknya jin tersebut terpanggil (panjang countlistjin == panjang user)
    nMax = -99999 #jumlah jin paling kecil 0, tak mungkin -99999
    nMin = 1001 #jumlah jin yang bangun candi tak akan lebih dari 1001, karena max candi 1000
    jinMax = ""
    jinMin = ""

    for i in range(1,nuser):
        if user[i][2] == "jin_pengumpul":
            jin_kumpul += 1
        elif user[i][2] == "jin_pembangun":
            jin_bangun += 1   
        for j in range(1,ncandi):
            if candi[j] != "HAPUS":
                
                if (candi[j][1] == user[i][0] and user[i][2] == "jin_pembangun") or (candi[j][1] == user[i][0] and user[i][2] == "jin_pengumpul"):
                    countlistjin[i] += 1
            
        if countlistjin[i] > nMax:
            nMax = countlistjin[i]
            #print("nMax: ",nMax, "saat i : ",countlistjin[i] , " " , user[i][0])
            jinMax = str(user[i][0])
        if countlistjin[i] < nMin and countlistjin[i] != 0:
           
            nMin = countlistjin[i]
            #print("nMin: ",nMin, "saat i : ",countlistjin[i] , " " , user[i][0])
            jinMin = str(user[i][0])
    
    kosong = True
    for i in range(nuser):
        if countlistjin[i] != 0:
            kosong = False
           #cek sama

        #SORTIR LEKSIKOGRAFIS
        for j in range(i+1,nuser):
            if countlistjin[i] == countlistjin[j] and (countlistjin[i] == nMax or countlistjin[j] == nMax):#brarti ada yang sama
                if str(user[i][0] < user[j][0]):
                    jinMax = str(user[i][0])
                else:
                    jinMax = str(user[j][0])
            elif countlistjin[i] == countlistjin[j] and (countlistjin[i] == nMin or countlistjin[j] == nMin):
                if str(user[i][0] < user[j][0]):
                    jinMin = str(user[i][0])
                else:
                    jinMin = str(user[j][0])

            
                
 

    

    if kosong:
        jinMax = "-"
        jinMin = "-"


    
    
    print(f"Total Jin: {jin_bangun + jin_kumpul} \n")
    print(f"Total JIn Pengumpul: {jin_kumpul} \n")
    print(f"Total Jin Pembangun: {jin_bangun} \n")
    print(f"Jin Terajin: {jinMax } \n")
    print(f"JIn Termalas: {jinMin} \n")        #output
    print(f"Jumlah Pasir: {total_pasir} \n")
    print(f"Jumlah Air: {total_air} \n")
    print(f"Jumlah Batu: {total_batu} \n")



# ===================================== F10 - Ambil Laporan Candi  ==========================================
def hargacandi(pasir,batu,air):
    hasil = int(pasir) * 10000 + int(batu) * 15000 + int(air) * 7500
    return hasil

def laporancandi():
    totalcandi = tools.MaxTargetCandi - candi[0]
    totalpasir = 0
    totalbatu = 0
    totalair = 0
    max = -99999 #asumsi tak ada harga candi yang dibawah  0 (MARK)
    min = 999999999999999 # asumsi tak ada harga candi di atas angka ini (MARK)
    n = tools.lenarray(candi)
    #hitung total pasir,batu,air ,Harga max, Harga min
    # [[ID,NamaJin,Pasir,Batu,Air]]
    if totalcandi != 0:

        for i in range (1,n):
            if candi[i] !=  "HAPUS":

                totalpasir = totalpasir + int(candi[i][2]) 
                totalbatu = totalbatu + int(candi[i][3]) 
                totalair = totalair + int(candi[i][4]) 
                if hargacandi(candi[i][2],candi[i][3],candi[i][4]) > max:
                    max = hargacandi(candi[i][2],candi[i][3],candi[i][4])
                    idmax = i
                
                if hargacandi(candi[i][2],candi[i][3],candi[i][4]) < min:
                    min = hargacandi(candi[i][2],candi[i][3],candi[i][4])
                    idmin = i
            
    else:
        idmax = "-"
        idmin = "-"
        max = "-"
        min = "-"

    print("Total candi: ", totalcandi)
    print("Total Pasir yang digunakan: ",totalpasir)
    print("Total Batu yang digunakan: ",totalbatu)
    print("Total Air yang digunakan: ",totalair)
    print("ID Candi Termahal: ", idmax , "(Rp." + str(max) + ")" )
    print("ID Candi Termurah: ", idmin , "(Rp." + str(min) + ")" )

# ===================================== F11 - Hancurkan Candi ==========================================
def hancurkancandi():
    
        
        markkosong = "HAPUS"
        panjangarraybuatdicek = tools.lenarray(candi) #Pengecekan list yang sudah terisi
        
        # for i in range(1,panjangarraybuatdicek):  #(1-7) (1,2,3,4,5,6)
        #     print(candi[i])

        hapus = input("Masukkan ID candi: ")
        Ditemukan = False
        #Pengecekan apakah id candi ditemukan apa tidak
        for i in range(1,panjangarraybuatdicek):
            if hapus == candi[i][0] :
                Ditemukan = True


        if Ditemukan == True:
            print("Apakah anda yakin ingin menghancurkan candi ID: (Y/N)?")
            keputusan = input()
            if keputusan == "Y" or keputusan == "y":
                for i in range(1,panjangarraybuatdicek):
                    if hapus == candi[i][0]:
                        candi[i] = markkosong
                
                candi[0] += 1
                print("Candi dengan id :" ,hapus, " berhasil dihapus!" )
            elif keputusan =="N" or keputusan =="n":
                print("Candi tidak jadi dihancurkan")
            #print(tools.convertarray(candi))
        
    

    # Jika jawaban dari keputusan adalah n atau N maka keputusan tidak dijalankan
        else: 
            print("Tidak ada candi dengan ID tersebut.")

   

# ===================================== F12 - Ayam Berkokok ==========================================

def ayamberkokok():
    panjangarraybuatdicek = tools.lenarray(candi) #Pengecekan list yang sudah terisi
    jumlahcandi = tools.MaxTargetCandi - candi[0]
    print("Kukuruyuk.. Kukuruyuk..")
    print("Jumlah Candi = ", jumlahcandi)
    if jumlahcandi < 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        exit()
            
    else: # Jumlah candi == 100
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        exit()




# ===================================== F14 - Save  ==========================================


def SaveWithDirectory():
        namafolder = input("namafolder: ")

        hasil = "save/" +  str(namafolder)
        if not os.path.exists(hasil):  # periksa apakah folder sudah ada atau belum
            os.makedirs(hasil)  # buat folder baru jika belum ada
            print("Saving....")
            print(f"Folder '{namafolder}' berhasil dibuat di parent folder 'save/'")
        else:
            print("Saving.....")

        data.save(candi,bahan_bangunan,user,hasil)



   


# ===================================== F16 - Exit ==========================================
   
def Keluar():
    
    opsi = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) :"  )
    if opsi == "Y" or opsi == "y":
        SaveWithDirectory()
        exit()

        
        
    elif opsi == "N" or opsi == "n":
        exit()

    else:
        return Keluar()
        



# ===================================== Procedur menerima function dari main.py ==========================================

def run(function):
    if function == "bangun" :
        if RoleUser != "jin_pembangun" and RoleUser != "" :
            print("Tak bisa, perintah ini khusus jin pembangun")
        elif RoleUser == "":
            print("Silahkan 'login' terlebih dahulu")
        else:
            bangun(NamaUser) #nanti nama user tergantung yang login, ini hanya sementara

    elif function == "kumpul" :
        if RoleUser != "jin_pengumpul" and RoleUser != "":
            print("Tak bisa, perintah ini khusus jin pengumpul")
        elif RoleUser == "":
            print("Silahkan 'login' terlebih dahulu")

        else:
            kumpul("jin pengumpul") #nanti nama user tergantung yang login, ini hanya sementara

    elif function == "batchbangun":
        if RoleUser != "bandung_bondowoso" and RoleUser != "":
            print("Tak bisa, perintah ini hanya boleh dieksekusi oleh maha agung Bandung Bondowso terhebat, teragung dan terkuat")
        elif RoleUser == "":
            print("Silahkan 'login' terlebih dahulu")

        else:
            batchbangun() #role bandung bondowoso

    elif function == "summonjin":
        if RoleUser != "bandung_bondowoso" and RoleUser != "":
            print("Tak bisa, perintah ini hanya boleh dieksekusi oleh maha agung Bandung Bondowso terhebat, teragung dan terkuat")
        elif RoleUser == "":
            print("Silahkan 'login' terlebih dahulu")

        else:
            summonJin(user)

    elif function == "laporanjin":
        if RoleUser != "bandung_bondowoso" and RoleUser != "":
            print("Tak bisa, perintah ini hanya boleh dieksekusi oleh maha agung Bandung Bondowso terhebat, teragung dan terkuat")
        elif RoleUser == "":
            print("Silahkan 'login' terlebih dahulu")

        else:
            LaporanJin()
     

    elif function == "save":
        SaveWithDirectory()

    elif function == "batchkumpul":
        if RoleUser != "bandung_bondowoso" and RoleUser != "":
            print("Tak bisa, perintah ini hanya boleh dieksekusi oleh maha agung Bandung Bondowso terhebat, teragung dan terkuat, saat ini rolemu adalah ",RoleUser)
        elif RoleUser == "":
            print("Silahkan 'login' terlebih dahulu")

        else:
            batchkumpul()
    elif function == "laporancandi":
        if RoleUser != "bandung_bondowoso" and RoleUser != "":
            print("Tak Bisa, khusus role bandung bondowoso")
        else:
            laporancandi()
    elif function == "ubahjin":
        if RoleUser != "bandung_bondowoso" and RoleUser != "":
            print("Tak bisa, perintah ini hanya boleh dieksekusi oleh maha agung Bandung Bondowso terhebat, teragung dan terkuat, saat ini rolemu adalah ",RoleUser)
        elif RoleUser == "":
            print("Silahkan 'login' terlebih dahulu")

        else:
            ubahTipeJin()

    elif function == "hancurkancandi":
        if RoleUser != "roro_jonggrang" and RoleUser != "":
            print("Tak bisa, perintah ini hanya boleh dieksekusi oleh Mommmy Roro Jonggrang , saat ini rolemu adalah ",RoleUser)
        elif RoleUser == "":
            print("Silahkan 'login' terlebih dahulu")
        else:

         hancurkancandi()

    elif function == "ayamberkokok":
        if RoleUser != "roro_jonggrang" and RoleUser != "":
            print("Tak bisa,perintah ini hanya boleh dieksekusi oleh Mommmy Roro Jonggrang , saat ini rolemu adalah ",RoleUser )
        else:
            ayamberkokok()

    elif function == "hapusjin":
        if RoleUser != "bandung_bondowoso" and RoleUser != "":
            print("Tak bisa, perintah ini hanya boleh dieksekusi oleh maha agung Bandung Bondowso terhebat, teragung dan terkuat, saat ini rolemu adalah ",RoleUser)
        else:
            hapusjin()

      
    elif function == "candi":
        print(tools.convertarray(candi))
    elif function == "login":
        login()
    elif function == "logout":
        logout()
    elif function == "user":
        print(user)
    elif function == "exit":
        Keluar()
# ===================================== F15 - Help  ==========================================
    elif function == "help":

        if RoleUser == "bandung_bondowoso":
            helpmenu.help_bondowoso()
        elif RoleUser == "roro_jonggrang":
            helpmenu.help_jonggrang()
        elif RoleUser == "jin_pengumpul":
            helpmenu.help_pengumpul()
        elif RoleUser == "jin_pembangun":
            helpmenu.help_pembangun()
        else:
            helpmenu.help_unlogin()




   


#TESTING GROUND

