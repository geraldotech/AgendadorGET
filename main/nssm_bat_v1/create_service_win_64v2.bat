@echo off
:: Execute como Administrador
setlocal enabledelayedexpansion

set "SERVICE_NAME=a_agendador_v2"
set "SCRIPT_DIR=%~dp0"
set "NSSM_PATH=%SCRIPT_DIR%nssm.exe"
set "APP_PATH=%SCRIPT_DIR%start_timer.exe"

:: Verificar se o executável existe
if not exist "%APP_PATH%" (
    echo ERRO: Arquivo !APP_PATH! não encontrado
    pause
    exit /b 1
)

:: Instalar serviço
echo [*] Instalando serviço...
"%NSSM_PATH%" install !SERVICE_NAME! "!APP_PATH!"

:: Configurações essenciais
"%NSSM_PATH%" set !SERVICE_NAME! DisplayName "Agendador v2"
"%NSSM_PATH%" set !SERVICE_NAME! AppDirectory "!SCRIPT_DIR!"
"%NSSM_PATH%" set !SERVICE_NAME! AppStdout "!SCRIPT_DIR%service.log"
"%NSSM_PATH%" set !SERVICE_NAME! AppStderr "!SCRIPT_DIR%service_error.log"

:: Tentar iniciar com timeout
echo [*] Iniciando serviço...
"%NSSM_PATH%" start !SERVICE_NAME!
timeout /t 5 >nul

:: Verificar status
echo [*] Verificando status...
"%NSSM_PATH%" status !SERVICE_NAME! >nul
if errorlevel 1 (
    echo ERRO: Serviço falhou ao iniciar. Verifique:
    echo - Permissões em !SCRIPT_DIR!
    echo - Logs em !SCRIPT_DIR%service_error.log
    echo - Dependências do executável
)

:: Diagnóstico avançado
echo.
echo [DIAGNÓSTICO]
sc query !SERVICE_NAME!
echo.
tasklist /fi "IMAGENAME eq start_timer.exe"

pause