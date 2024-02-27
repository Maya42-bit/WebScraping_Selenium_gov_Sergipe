import pandas as pd
import os



def unir_arquivos(diretorio_arq: str, sep_arq:str ,nome_destino:str, sep_destino:str):
    # procurar arquivo no diretório
    
    directory_path = diretorio_arq     
    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

    # Juntar arquivos em um diretório só

    frames = []

    for csv_file in csv_files:
        file_path = os.path.join(directory_path, csv_file)
        df = pd.read_csv(file_path, sep=sep_arq)
        frames.append(df)

    # Salvar o arquivo consolidado
    save = 'Bases/'+nome_destino
    result = pd.concat(frames, ignore_index=True)
    result.to_csv(save, index=False, sep=sep_destino) 

    return save          



