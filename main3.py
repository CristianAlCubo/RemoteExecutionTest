import csv

def readCSV():
  ruta_archivo = 'data/keys.csv'

  print("Leyendo archivo CSV...")
  with open(ruta_archivo, newline='') as archivo_csv:
      lector_csv = csv.reader(archivo_csv)
      # Itera sobre cada fila del archivo CSV
      for fila in lector_csv:
          print(fila)

def holaDesdeMain3():
  print("Hola mundo desde main 3")
  # readCSV()