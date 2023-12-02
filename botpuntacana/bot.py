from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service 
import time 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

service = Service("driver/chromedriver.exe") # Crear el servicio
bot = webdriver.Chrome(service=service) # Crear el bot
bot.maximize_window() # Maximizar la ventana
bot.get("https://www.viajesexito.com") # Abrir el sitio de viajes exito
time.sleep

#el bot accede a paquetes
paquetes = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[4]/a') 
paquetes.click() 
time.sleep(1) 

# el bot da click en elemento origen
vorigen = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')  
vorigen.click() 
time.sleep(1)  

# el bot escribe el origen
sorigen = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input') 
sorigen.send_keys('José María Cordova') 
time.sleep(1) 
sorigen.send_keys(Keys.ENTER) 
time.sleep(1)

# el bot da click en el destino dicho
destino = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input') 
destino.click() 
time.sleep(1) 

#el bot escribe y da click en el destino
sdestino = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
sdestino.send_keys('Punta Cana') 
time.sleep(1) 
sdestino.send_keys(Keys.ENTER) 
time.sleep(1) 

# el bot busca fecha
fecha = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input') 
fecha.click() 
time.sleep(1) 

#el bot busca la fecha de salida que es el 10
fSalida = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[3]/div[7]/div[2]/div[1]') 
fSalida.click() 
time.sleep(1) 

#el bot busca la fecha de regreso que es el 20
fLlegada = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[3]/div[2]/div[1]') 
fLlegada.click() 
time.sleep(1) 

#el bot acepta la fecha
aceptafe = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[2]/button[2]') 
aceptafe.click() 
time.sleep(1) 

#el bot da click en las habitaciones
cuartos = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]') 
cuartos.click() 
time.sleep(1) 

#escoge las habitaciones
nuevoscuartos = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
nuevoscuartos.click() 
time.sleep(1) 

# el bot acepta 
aceptacuartos = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button') 
aceptacuartos.click() 
time.sleep(1) 

#el bot busca
busca = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a') 
busca.click() 
time.sleep(1) 

# se genera una nueva ventana 
emergente = bot.window_handles[1] 
bot.switch_to.window(emergente) 

#el bot espera a que se abra maximo 30 segundos
WebDriverWait(bot, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]'))) 

#se obtienen los primeros 10 precios 
for i in range(1, 11): 
    xpath = f'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[{i}]/div/div/div[2]/div/div[1]/div/p[1]/span[2]' 
    precio = bot.find_element(By.XPATH, xpath) 
    print(f'precio numero {i}: {precio.text}') 

#el bot accedde a las opciones avanzadas
ajustesavanzados = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a') 
ajustesavanzados.click() 
time.sleep(1) 

#el bot accede a avianca y le da enter
aerolinea = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input') 
aerolinea.click() 
aerolinea.send_keys('Avianca') 
aerolinea.send_keys(Keys.ENTER) 
time.sleep(1) 

#el bot busca
busqueda = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input') 
busqueda.click() 
time.sleep(1) 


#el bot espera 30 seg max
WebDriverWait(bot, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]'))) 

#el bot da click en el contactanos
contactanos = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p/a') 
contactanos.click() 
time.sleep(4) 


bot.quit() 