<?php
    require_once 'koneksi.php';
    $KdMatkul = $_POST['KdMatkul'];
    $Matkul = $_POST['Matkul'];
    $sqlku = "INSERT INTO tmatakuliah (KdMataKuliah, MataKuliah) values ('$KdMatkul', '$Matkul')";

    $sql = mysqli_query($conn,$sqlku);

    if ($sql){
        echo json_encode(array('message' => 'created!'));
    } else {
        echo json_encode(array('message' => 'error!'));
    }
?>