MaxValue = 1000
MARK = None
MaxTargetCandi = 100 #Tujuan jumlah candi dari gameini
'''
DISCLAIMER

SYARAT MENGGUNAKAN APPEND, POP, CONVERT ARRAY UNTUK MODULE TOOLS
INI ADALAH, ARRAY YANG DIGUNAKAN HARUS MENGANDUNG NONE

'''



def lenarray(arr):
    for i in range(MaxValue):
        if arr[i] == MARK:
            return i
        
def convertarray(arr):
    n = lenarray(arr)
    newarray = [0 for i in range(n)]
    for i in range(n):
        newarray[i] = arr[i]

    return newarray

def appendarray(arr,add):
    n = lenarray(arr)
    arr[n] = add
    return(arr)



def poparray(arr):
    n = lenarray(arr)
    arr[n-1] = None
    return(arr)


def deletehapus(arr):

    markhapus = "HAPUS"
    
    
    n = lenarray(arr)
    new = [None for i in range(n)]

    for i in range(n):
        new[i] = arr[i]

    
    nhapus = 0
    for i in range(n):
        if new[i] == markhapus:
            nhapus += 1

    pointer = 0
    cleararr = [None for i in range(MaxValue)]
    for i in range(n):
        if new[i] != markhapus:
            cleararr[pointer] = new[i]
            pointer += 1
    return cleararr
   
    

    




def splituser(string,panjangisiarray):
    Temp = ""
    ubahlist = [None for i in range(panjangisiarray)]
    x = 0
    for i in range(len(string)):
        if string[i] == "," or string[i] == " " or string[i] == ";" or string[i] == "\n":
            ubahlist[x] = Temp
            x += 1
            Temp = ""
        elif i == len(string) - 1:
            Temp += str(string[i])
            ubahlist[x] = Temp
        else:
            Temp += str(string[i])
    return ubahlist


def sortidcandi(tab,n):
    
    
    for i in range(n-1,0,-1):
        
        for j in range(1,i,1):
            
            if int(tab[j][0]) > int(tab[i][0]):
                
                
                band = tab[i]
                tab[i] = tab[j]
                tab[j] = band
    return(tab)
            

    
def maxID(arrcandi):
    n = lenarray(arrcandi)
    max = int(arrcandi[1][0])
    for i in range(2,n):
        if int(arrcandi[i][0]) > max:
            max = int(arrcandi[i][0])
    
    return(max)

