# Instalação do Windows Monitoring Agent
## Instalação do Windows Monitoring Agent a partir da linha de comandos

 1. Inicie sessão no computador onde pretende instalar o agente com uma conta com privilégios de Administrador local.
 2. Abra o Power Shell como Administrador.
 3. Acesa o diretório com os conteúdos de instalação do agente <b>Ex: cd C:\Desktop\Agente</b>.
 4. Execute o seguinte comando <b>.\WindowsMonitoringAgentInstallation.ps1</b>.
 5. Após a execução do comando acima é solicitado a inserção do IP e da porta do servidor. Como exemplo de IP e porta válidos temos: <b>$sensorip = "000.00.00.000</b>  <b>$sensorport = "5045"</b> 
 6. De seguida presione Enter para proceguir com a instalação do agente.
 
 
## Instalação do Windows Monitoring Agent a partir de um executável

 3. Acesa o diretório com os conteúdos de instalação do agente <b>Ex: cd C:\Desktop\Agente</b>.
 4. Encontre o ficheiro WindowsMonitoringAgentInstallation.exe e executá-o como Administrador.
 5. Introduz o endereço IP e a porta do servidor.
 6. Presione Enter para continuar com a instalação do agente.
 

 # Desinstalação do Windows Monitoring Agent
 ## Desinstalação do Windows Monitoring Agent a partir da linha de comandos
 1. Abra o Power Shell como Administrador.
 2. Acesa o diretório com os conteúdos de desinstalação do agente <b>Ex: cd C:\Desktop\Agente\WindowsMonitoringAgent</b>.
 3. Execute o seguinte comando <b>Uninstall-Monitoring-Service.ps1</b>.
 
 ## Desinstalação do Windows Monitoring Agent a partir de um executável
 1. Acesa o diretório com os conteúdos de desinstalação do agente <b>Ex: cd C:\Desktop\Agente\WindowsMonitoringAgent</b>.
 2. Encontre o ficheiro Uninstall-Monitoring-Service.exe e executá-o como Administrador.
