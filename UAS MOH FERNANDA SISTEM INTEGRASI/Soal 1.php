<?php
    require_once 'koneksi.php';
    //1. string untuk query
    $sqlku = "SELECT * FROM tmatakuliah INNER JOIN tdosen ON tmatakuliah.KdMataKuliah = tdosen.kdMatkul";

    //2. JALANKAN QUERY
    $r = mysqli_query($conn,$sqlku);

    //SIMPAN KE ARRAY
    $result = array();
    while($row = mysqli_fetch_array($r)){
        array_push($result, array(
            "matakuliah" =>$row['MataKuliah'],
          "namadosen" =>$row['NamaDosen'],

        ));
    }
    //tampilkan output JSON
    echo json_encode($result);
    //tutup koneksi
    mysqli_close($conn);
?>