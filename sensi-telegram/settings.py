#path do banco de dados do django
dataBaseDjangoDir = '/home/pi/Desktop/Django/SensiProject/db.sqlite3'

#path do banco de dados das tags
dataBaseSensiDir = '/home/pi/Desktop/sensi.db'

#path dos arquivos temporários
tempDir = '/home/pi/Desktop/'

#dados sobre o cliente/
name = 'banco de sangue'
local = 'HUCAM'

#dados sobre a sensi
nameCompany = 'sensi telemetria'
owners = {1:['Willian ferreira', '(27) 9999-9999'],2:['Talles D. de S. Valiatti','(27) 9999-9999']}
site = 'www.sensitelemetria.com'

#django
siteConfig = "192.168.1.2:8000"

#time out das leiturass das sensiTags
timeout_in_sec = 30