<?php
date_default_timezone_set('America/Sao_Paulo');
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] === "POST") {

  $url = isset($_POST['url']) ? $_POST['url'] : null;
  $response = file_get_contents($url);  

  if ($response !== false) {
  
   // echo json_encode(["status" => "error", "message" => "Método inválido"]);
      $data = json_encode($response, true);
      echo $data;

      // gravar no log ja existente do python
      $logFile = './../install_windows/info.log';
      $data = date('d:M:Y H-i-s') . '- INFO - Sucesso chamada manual para ' .$url;
      if(file_exists($logFile)){
        file_put_contents($logFile, $data .  PHP_EOL, FILE_APPEND);
      }

  } else {
      echo json_encode(["status" => "error", "message" => "Erro ao buscar os dados."]);
  }

}




