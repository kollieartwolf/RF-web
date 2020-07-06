<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
header("Content-Type: text/plain");

$link = mysqli_connect("localhost", "db", "pass", "table");

if ($link == false){
    print("Ошибка: Невозможно подключиться к MySQL " . mysqli_connect_error());
    exit();
}
$s = mysqli_real_escape_string($link, $_GET['key']);
$sql = 'SELECT * FROM `keyValues` WHERE `name`="' . $s . '"';
mysqli_set_charset($link, "utf8");
$result = mysqli_query($link, $sql);
while ($row = mysqli_fetch_array($result)) {
    print($row['value']);
}
