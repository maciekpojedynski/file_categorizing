from pathlib import Path
from datetime import datetime

extension = {
    'Obrazy': ['.jpg', '.png','.jpeg','.gif']
    ,'Dokumenty': ['.docx','.pdf','.txt','.doc']
    ,'Wideo': ['.mp4', '.mov']
 }

def find_category(file_suffix: str) -> str:
    """ Identyfikuje format pliku 
    
    Args: file_suffix -> Argument string będący rozszerzeniem plików np. .jpg
    
    Return: Nazwa rodzaju pliku na podstawie suffix'u np. .jpg to Obraz"""
    for key, value in extension.items():
        if file_suffix in value:
            return key

    return 'Inne'

current_path = Path('.')

for x in current_path.iterdir():
    print(x)
    if x.is_file():
        stats = x.stat()
        timestamp = stats.st_mtime
        human_readable_date = datetime.fromtimestamp(timestamp)
        x_year = human_readable_date.year
        print(f'Plik:{x.name} | Rok: {x_year} | Kategoria: {find_category(x.suffix)}')
