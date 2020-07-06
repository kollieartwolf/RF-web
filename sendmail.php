<?php
$subject = 'the subject';
$message = 'hello';
$headers = array('X-Mailer' => 'PHP/' . phpversion());

mail($_GET["to"], $subject, $message, $headers);
echo $_GET["to"];
