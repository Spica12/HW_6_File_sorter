from pathlib import Path

image_files = list()
video_files = list()
document_files = list()
music_files = list()
archieves = list()
folders = list()
extensions = set()
unknown = set()

registered_extensions = {
    'IMAGE': ('JPEG', 'PNG', 'JPG', 'SVG'),
    'VIDEO': ('AVI', 'MP4', 'MOV', 'MKV'),
    'DOCUMENTS': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
    'MUSIC': ('MP3', 'OGG', 'WAV', 'AMR'),
    'ARCHIEVES': ('ZIP', 'GZTAR', 'TAR', 'GZ')
}

registered_files = {
    'IMAGE': image_files,
    'VIDEO': video_files,
    'DOCUMENTS': document_files,
    'MUSIC': music_files,
    'ARCHIEVES': archieves
}


def display_result_scan():

    print('This folder have next files:\n')
    for type, reg_folder in registered_files.items():
        print(f'{type}:')
        for item in reg_folder:
            print(f"      - {item}")

    print(f'FOLDERS:')
    for folder in folders:
        print(f'      - {folder}')
    print(f'\n{extensions = }')
    print(f'\n{unknown = }')
    
    



def get_extension(file_name):
    return Path(file_name).suffix[1:].upper()


def scan(folder):

    for element in folder.iterdir():

        if element.is_dir():
            if element.name not in ('IMAGE', 'VIDEO', 'DOCUMENTS', 'MUSIC', 'OTHER', 'ARCHIEVES'):
                folders.append(element)
                scan(element)
        else:

            extension = get_extension(element)
            new_name = folder/element.name

            if not extension:
                continue

            else:
                is_reg = False

                for key in registered_extensions:
                    
                    if extension in registered_extensions[key]:
                        container = registered_files[key]
                        extensions.add(extension)
                        container.append(new_name)
                        is_reg = True

                if not is_reg:
                    unknown.add(extension)

# Test GH
                