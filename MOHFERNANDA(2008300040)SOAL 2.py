
"""

@author: Nanda
"""

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="y":
    print("==============================================")
    print(" Bengkel Motor UD  ")
    print("==============================================")
    print(" a = Duration SW20 1l")
    print(" b = Castrol Macnetec 1l")
    print(" c = Federar Supreme xx 1l")
    print(" d = Yamalube 1l")
    print(" e = Shell 1l")

    kode =['a','b','c','d','e']

    Merek_Oli = ['Duration SW20','Castrol Macnetec','Federar Supreme xx','Yamalube','Shell']
    Jumlah_Oli = [10,11,12,13,14]
    harga_per_liter = [53000,50000,54000,45000,46000]

    pilihan = input(">> Masukkan Kode Oli = ")
   
    
    index = 0
    while index < len(kode):
        if kode[index] == pilihan:

            print(">>> Pilihan Oli = " + Merek_Oli[index ])
            print(">>> harga oli   = Rp. " + str(harga_per_liter[index]))
            print(">>>  jumlah oli =  " + str(Jumlah_Oli[index]))
#tahap hitung biaya
            harga_ppn = Jumlah_Oli[index] * harga_per_liter[index] 
            
            
#tampilkan biaya kirim
            print(">>>> Total      = Rp. " + str(harga_ppn))
            
            if harga_ppn > 200000 :
                diskon = harga_ppn * (5/100)
            else:
                diskon = harga_ppn * (1/100)

            setelah_diskon = harga_ppn - diskon
            print("Diskonya yaitu: Rp {:,}".format(int(diskon)))
            print("Harga setelah diskon: Rp {:,}".format(int(setelah_diskon)))
           
        
            
	#untuk membaca index dari 0 -> index 0 adalah kode a(surabaya), 
	#fungsi index + 1 adalah misal anda memlilih kode b maka akan dibaca index 0+1=1 jadi kode b ada index ke 1, dst
        index = index + 1 
        
#inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
        break


