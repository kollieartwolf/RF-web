<?php
$link = mysqli_connect("localhost", "db", "pass", "table");

if ($link == false){
    print("Ошибка: Невозможно подключиться к MySQL " . mysqli_connect_error());
    exit();
}
print("Соединение установлено успешно");
mysqli_set_charset($link, "utf8");
