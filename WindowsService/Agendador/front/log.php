<?php
$logFile = '../info.log';

if (file_exists($logFile)) {
    $handle = fopen($logFile, 'r');
    
    while (($line = fgets($handle)) !== false) {
        echo htmlspecialchars($line) . "<br>"; // Evita XSS e mantém formatação
    }

    fclose($handle);
} else {
    echo "Arquivo de log não encontrado.";
}
?>
