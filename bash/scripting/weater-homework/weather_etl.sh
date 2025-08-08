#!/usr/bin/zsh

# Script ETL para obtener clima actual y pronóstico de Casablanca

# 1. Descargar el reporte del clima en Casablanca (sin colores ni formato)
data=$(curl -s "wttr.in/casablanca?0")

# 2. Obtener la fecha actual
year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)

# 3. Extraer temperatura observada actual (en la primera sección del reporte)
obs_temp=$(echo "$data" | grep -m1 -oP '\+\d+(?=\()' | head -1)

# 4. Extraer temperatura pronosticada para mañana al mediodía
fc_temp=$(echo "$data" | awk '/Noon/{getline; getline; getline; getline; print}' | awk 'NR==2' | grep -oP '\+\d+' | head -1)

# 5. Registrar los datos en un archivo de log (formato tabulado)
echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp" >> weather_log.tsv

