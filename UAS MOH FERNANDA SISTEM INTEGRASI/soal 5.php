<?php
    require_once 'koneksi.php';
    parse_str(file_get_contents('php://input'), $val);
    $KdDosen = $val['KdDosen'];
    $NmDosen = $val['NmDosen'];
    $KdMatKul = $val['KdMatKul'];
    $sqlku = "UPDATE tdosen set NamaDosen='$NmDosen', KdMatKul='$KdMatKul' where KdDosen='$KdDosen'";

    $sql = mysqli_query($conn,$sqlku);

    if ($sql){
        echo json_encode(array('message' => 'updated!'));
    } else {
        echo json_encode(array('message' => 'error!'));
    }
?>