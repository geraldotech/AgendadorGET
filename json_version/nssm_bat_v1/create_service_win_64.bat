@echo off
REM Script para instalar e configurar o serviço "a_agendador" usando o NSSM

REM Defina o caminho para o nssm.exe
:: set NSSM_PATH=%SCRIPT_DIR%nssm.exe
set "SCRIPT_DIR=%~dp0"
set "NSSM_PATH=%SCRIPT_DIR%nssm.exe"

REM Defina o nome do serviço
set SERVICE_NAME=a_agendador_v1

REM Obter o diretório atual onde o script está sendo executado
set SCRIPT_DIR=%~dp0

REM Definir o caminho para o executável (assumindo que está na mesma pasta do script)
set APP_PATH=%SCRIPT_DIR%start_timer.exe

REM Defina o diretório de trabalho (usando o mesmo diretório do script)
set WORK_DIR=%SCRIPT_DIR%

REM Instalar o serviço
%NSSM_PATH% install %SERVICE_NAME% %APP_PATH%

REM Configurar o nome de exibição do serviço
%NSSM_PATH% set %SERVICE_NAME% DisplayName "Agendador v1"

REM Configurar a descrição do serviço
%NSSM_PATH% set %SERVICE_NAME% Description "Agenador v1 para config.json."

REM Configurar o diretório de trabalho
%NSSM_PATH% set %SERVICE_NAME% AppDirectory %WORK_DIR%

REM Iniciar o serviço
%NSSM_PATH% start %SERVICE_NAME%


echo Serviço "%SERVICE_NAME%" instalado e iniciado com sucesso!
echo Executável: %APP_PATH%
echo Diretório de trabalho: %WORK_DIR%
pause