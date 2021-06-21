
"""

@author: Nanda
"""

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="y":
    print("==============================================")
    print(" Toko bahan bangunan UD .subur  ")
    print("==============================================")
    print(" a = asbes gelombang ")
    print(" b = cat tembak dulux 1galon ")
    print(" c = cat tembok avian 1galon ")
    print(" d = aquaproof 5 kg")
    print(" e = seng 2mm")
    print(" f = spandeks 1mm ")
    
    kode =['a','b','c','d','e','f']

    Merek_Oli = ['asbes gelombang','cat tembak dulux 1galon','cat tembok avian 1galon','aquaproof 5 kg','seng 2mm','spandeks 1mm']
    Jumlah_Oli = [10,11,12,13,14,15]
    harga_per_liter = [60000,250000,350000,50000,70000,92000]

    pilihan = input(">> Masukkan Kode bahan bangunan = ")
   
    
    index = 0
    while index < len(kode):
        if kode[index] == pilihan:

            print(">>> Pilihan bahan bangunan = " + Merek_Oli[index ])
            print(">>> harga bahan bangunan   = Rp. " + str(harga_per_liter[index]))
            print(">>>  jumlah bahan bangunan =  " + str(Jumlah_Oli[index]))
#tahap hitung biaya
            harga_ppn = Jumlah_Oli[index] * harga_per_liter[index] 
            
            
#tampilkan biaya kirim
            print(">>>> Total      = Rp. " + str(harga_ppn))
            
            if harga_ppn > 500000 :
                diskon = harga_ppn * (5/100)
            else:
                diskon = harga_ppn * (2/100)

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


