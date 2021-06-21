
JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="y":
    print("==============================================")
    print(" TRANSAKSI BIAYA EKSPEDISI ")
    print("==============================================")
    print(" a = Surabaya")
    print(" b = Bandung")
    print(" c = Semarang")
    print(" d = Denpasar")

    kode =['a','b','c','d']

    kota = ['Surabaya','Bandung','Semarang','Denpasar']
    jarak = [169,452,385,215]
    ongkirperkm = [2500,4000,3500,4000]

    pilihan = input(">> Masukkan Kode Tujuan = ")

    index = 0
    while index < len(kode):
        if kode[index] == pilihan:

            print(">>> Pilihan Tujuan   = " + kota[index ])
            print(">>>          Jarak   = " + str(jarak[index]) + " km")
            print(">>>  Ongkir per Km   = Rp. " + str(ongkirperkm[index]))
#tahap hitung biaya
            ongkir = jarak[index] * ongkirperkm[index]
#tampilkan biaya kirim
            print(">>>> Total           = Rp. " + str(ongkir))
            print(" ")
            print("==============================================")
	#untuk membaca index dari 0 -> index 0 adalah kode a(surabaya), 
	#fungsi index + 1 adalah misal anda memlilih kode b maka akan dibaca index 0+1=1 jadi kode b ada index ke 1, dst
        index = index + 1 
        
#inputan untuk break
    JawabUlang = input(">>> Apakah Anda ingin mulai program lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
        break