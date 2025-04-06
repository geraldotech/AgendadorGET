<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] === "POST") {

  $url = isset($_POST['url']) ? $_POST['url'] : null;
  $response = file_get_contents($url);  

  if ($response !== false) {
  
   // echo json_encode(["status" => "error", "message" => "Método inválido"]);
      $data = json_encode($response, true);
      echo $data;
  } else {
      echo json_encode(["status" => "error", "message" => "Erro ao buscar os dados."]);
  }

}




