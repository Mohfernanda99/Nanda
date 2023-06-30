<?php
    require_once 'koneksi.php';
    //1. string untuk query
    $id = $_GET[id];
    $sqlku = "SELECT * FROM tmahasiswa where JenisKelamin='$Id' ";

    //2. JALANKAN QUERY
    $r = mysqli_query($conn,$sqlku);

    //SIMPAN KE ARRAY
    $result = array();
    while($row = mysqli_fetch_array($r)){
        array_push($result, array(
            "nim" =>$row['NIM'],
            "nama" =>$row['NamaLengkap'],
            "kelamin" =>$row['JenisKelamin']
            "kelas" =>$row['ProgramKelas']
        ));
    }
    //tampilkan output JSON
    echo json_encode($result);
    //tutup koneksi
    mysqli_close($conn);
?>