from setuptools import setup, find_packages


setup(name='clean_folder',
      version='0.0.2',
      packeges=find_packages(),
      author='Savenko Vitalii',
      author_email='vitaly.savenko12@gmail.com'
      license=file.LICENCE
      description='clean folder from some folder',
      long_description = file.README.md
      url='https://github.com/Spica12/HW_7_File_sorter',
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main',
                                        'fill-files = clean_folder.file_generator:main_generator']},
      zip_safe=False
      )