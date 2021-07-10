


lagi='y'

while lagi=='y':

    print ("\t \t Aplikasi Perhitungan Gaji Karyawan CV.LOGOS")

    print ("\t \t\t UAS FERNANDA ")

    print ("===============================================================================")

   
    nama=input("Nama Karyawan/Staff \t: ")

    print ("1. Golongan 1 \n2. golongan 2 \n3. golongan 3 \n4. golongan Lain")

    Golongan=input("Masukan Golongan \t\t    : ")
    jeniskelamin=input("jenis kelamin \t\t\t    : ")

    status=input("Status \t\t\t            : ")
    
        
    
    
    if (Golongan=='1'):

        gaji_pokok=2500000 
        tunjanganistri=2500000*(1/100)
        tunjangananak=2500000*(2/100)
        jab="ADMIN"

    elif(Golongan=='2'):

        gaji_pokok=4500000
        tunjanganistri=4500000*(3/100)
        tunjangananak=4500000*(2/100)
        jab="SPV"

    elif(Golongan=='3'):

        gaji_pokok=6500000
        tunjanganistri=6500000*(5/100)
        tunjangananak=6500000*(2/100)
        jab="Manager"
    
 
    else:

        gaji_pokok=3000000

        jab="Golongan Lain"
    iuranpensiun=15500
    iuranorganisasi=3500
    gajibruto=gaji_pokok+tunjanganistri+tunjangananak
    biayajabatan=gajibruto*(0.5/10)
    gajineto=gajibruto-biayajabatan-iuranpensiun-iuranorganisasi
    print ("")

    print ("\n")

    print ("===============================================================================")

    print ("\t\t\t SLIP GAJI")
    
    import datetime
    saat_ini= datetime.datetime.now()
    print ("\t\t\t Tanggal:",saat_ini)
    
    
    
    

    
    
    
    
    print ("")
    

    print ("Nama \t\t          : ",nama)

    print ("Golongan \t          : ",jab)

    print ("jenis kelamin\t      : ",jeniskelamin)

    print ("Status \t\t          : ",status)

    print ("Gaji Pokok \t          : ",gaji_pokok)
    print ("Tunjangan istri \t  : ",tunjanganistri)
    print ("Tunjangan Anak \t      : ",tunjangananak)
    
    print (">>Gaji Bruto \t      : ",gajibruto)
    print ("")

    print ("============================================================================")

    print ("Biaya Jabatan \t :",biayajabatan)
    print ("Iuaran Pensiun \t :",iuranpensiun)
    print ("Iuran Organisai\t :",iuranorganisasi)
    print (">> Gaji Neto\t :",gajineto)

    lagi=input("Ambil Data Lagi [y/n]? : ")