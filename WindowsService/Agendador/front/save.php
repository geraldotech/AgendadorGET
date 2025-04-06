<?php

$filename = '../install_windows/db/config.json';

$data = file_get_contents("php://input");
if (!$data) {
    die("Nenhum dado recebido");
}

$jsonData = json_decode($data, true);
if ($jsonData === null) {
    die("Erro ao decodificar JSON");
}

file_put_contents($filename, json_encode($jsonData, JSON_PRETTY_PRINT));

echo "Salvo com sucesso!";
?>
