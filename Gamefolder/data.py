import tools
import commands
#=========================================Sub-fungsi array/csv candi========================================
def savearraycandi(arrcandi,namafile):
    csvcandi = open(str(namafile) + "/candi.csv","w")
    n = tools.lenarray(arrcandi) - 1

    for i in range(1,n+1): #panjang isi format candi fixed 5 (id,nama,pasir,batu,air)

        csvcandi.write(str(arrcandi[i][0]) + ";" + arrcandi[i][1] + ";" + str(arrcandi[i][2]) + ";"+ str(arrcandi[i][3]) + ";" + str(arrcandi[i][4]))
        csvcandi.write("\n")
    csvcandi.write("999999999") # MARK
    csvcandi.close()

def loadarraycandi(arrcandi,namafile):
    
    arr = [None for i in range(tools.MaxValue)] #sementara
    counterload = 0 #buat ngukur jumlah candi
    
    csvcandi = open(namafile, "r")
    kalimat = csvcandi.readline()
  

    while kalimat != "999999999":

    
            IDcandiload = tools.splituser(kalimat,5)
            counterload += 1
            tools.appendarray(arr,IDcandiload)
            kalimat = csvcandi.readline()
    csvcandi.close()
    arrcandi[0] = tools.MaxTargetCandi - counterload
    for i in range(1,tools.MaxValue):


        arrcandi[i] = arr[i-1]

    return(arrcandi)
    
    
    
    

#=========================================Sub-fungsi array/csv bahanbangunan========================================    
def savearraybangun(arrbangun,namafile):
    csvbahan = open(str(namafile) + "/bahan_bangunan.csv","w")
    n = 3 # panjang baris csv bahan bangunan cuma 3
    for i in range(3):
        csvbahan.write(arrbangun[i][0] + ";" + arrbangun[i][1] + ";" + str(arrbangun[i][2]))
        csvbahan.write("\n")
    csvbahan.close()

def loadarraybangun(arrbangun,namafile):
    csvcandi = open(namafile,"r")
    pointer = 0
    
    for i in csvcandi:
        temp = tools.splituser(i,3)    
        arrbangun[pointer] = temp
        arrbangun[pointer][2] = int(arrbangun[pointer][2])
        pointer += 1
        
    csvcandi.close()
    return(arrbangun)
        





#=========================================Sub-fungsi array/csv user========================================    
def savearrayuser(arruser,namafile):
    csvuser = open(str(namafile) + "/user.csv","w")
    lenuser = tools.lenarray(arruser)
    for i in range(lenuser):
        csvuser.write(arruser[i][0] + ";" + arruser[i][1] + ";" + arruser[i][2])
        csvuser.write("\n")
    csvuser.close()



def loadarrayuser(arruser,namafile):
    csvuser = open(namafile,"r")
    pointer = 0
    for i in csvuser:
        temp = tools.splituser(i,3)
        arruser[pointer] = temp
        pointer += 1

    csvuser.close()
    return(arruser)





#LOAD satu kesatuan

def load(namacsv,arr):
    testcsv = open(namacsv, "r")
    
    kalimat = testcsv.readline()
    testcsv.close()
    if namacsv == str(commands.folderload) + "/candi.csv":
        if tools.splituser(kalimat,5) == ['id', 'pembuat', 'pasir', 'batu', 'air']: #file kosong
            arr = [None for i in range(tools.MaxValue)]
            arr[0] = tools.MaxTargetCandi
            
            return(arr)
            
        else: #brarti udah ada data candi di csv
            arr = [None for i in range(tools.MaxValue)]
            arr[0] = tools.MaxTargetCandi
            
            
            return loadarraycandi(arr,namacsv)
    elif namacsv ==   str(commands.folderload) + "/bahan_bangunan.csv":
        if tools.splituser(kalimat,3) == ['nama','deskripsi','jumlah']:
            arr = [None for i in range(3)]
            arr[0] = ['Pasir','Deskripsi',0]
            arr[1] = ['Batu','Deskripsi',0]
            arr[2] = ['Air','Deskripsi',0]
            return arr
        else:
            arr = [None for i in range(3)]
            return loadarraybangun(arr,namacsv)
    elif namacsv ==  str(commands.folderload) +"/user.csv":
        arr = [None for i in range(100)]
        return loadarrayuser(arr,namacsv)

            


def save(arrcandi,arrbangun,arruser,namafile):
    savearraybangun(arrbangun,namafile)
    savearraycandi(tools.deletehapus(arrcandi),namafile)
    savearrayuser(tools.deletehapus(arruser),namafile)

