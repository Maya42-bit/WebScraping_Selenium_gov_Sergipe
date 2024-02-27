import pandas as pd
import os

# procurar arquivo no diretório

directory_path = r"C:\temp\DEZEMBRO"                                                       #<---- COLOCAR O DIRETÓRIO DOS ARQUIVOS 
csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
csv_files

# Juntar arquivos em um diretório só

frames = []

for csv_file in csv_files:
    file_path = os.path.join(directory_path, csv_file)
    df = pd.read_csv(file_path, sep=',')
    frames.append(df)

# Salvar o arquivo consolidado

result = pd.concat(frames, ignore_index=True)
result.to_csv('Bases/SE 122023.csv', index=False, sep=';')                                     #<---- COLOCAR O NOME DO ARQUIVO E O SEPARADOR
