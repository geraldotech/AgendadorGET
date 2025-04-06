@echo off
REM Script para parar, remover e configurar o serviço "agendador_python" usando o NSSM

REM Obter o diretório atual onde o script está sendo executado
set SCRIPT_DIR=%~dp0

REM Defina o caminho para o nssm.exe
set NSSM_PATH=%SCRIPT_DIR%nssm.exe

REM Defina o nome do serviço
set SERVICE_NAME=agendador_python

REM Definir o caminho para o executável (assumindo que está na mesma pasta do script)
set APP_PATH=%SCRIPT_DIR%main.exe

REM Defina o diretório de trabalho
set WORK_DIR=%SCRIPT_DIR%

REM Para o serviço, caso esteja rodando
%NSSM_PATH% stop %SERVICE_NAME%

REM Aguarda um pouco para garantir que o serviço pare antes de remover
timeout /t 2 > nul

REM Remove o serviço
%NSSM_PATH% remove %SERVICE_NAME% confirm

echo Serviço "%SERVICE_NAME%" parado e removido com sucesso!
echo Executável: %APP_PATH%
echo Diretório de trabalho: %WORK_DIR%
pause
