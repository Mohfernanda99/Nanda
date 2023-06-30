<?php
    require_once 'koneksi.php';
    parse_str(file_get_contents('php://input'), $val);
    $KdMatkul = $val['KdMatkul'];
    $sqlku = "DELETE FROM tmatakuliah WHERE KdMataKuliah='$KdMatkul'";

    $sql = mysqli_query($conn,$sqlku);

    if ($sql){
        echo json_encode(array('message' => 'deleted!'));
    } else {
        echo json_encode(array('message' => 'error!'));
    }
?>