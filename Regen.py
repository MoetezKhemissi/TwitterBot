import os
import codecs
import zipfile

def remove_file(file_path):

    os.remove(file_path)
def remove_drivers():
    print("Removing old drivers...")
    path1=os.getcwd()+"\\TwoDriver\\VerifDriver\\msedgedriver.exe"
    path2=os.getcwd()+"\\TwoDriver\\TwitterDriver\\msedgedriver.exe"
    try:
        os.remove(path1)
    except:
        print("no file to remove")
    try:
        os.remove(path2)
    except:
        print("no file to remove")
    
def extract_files():
    print("extracting drivers...")
    path_to_zip_file=os.getcwd()+"\\DriverGenerator.zip"
    directory_to_extract_to=os.getcwd()+"\\TwoDriver\\TwitterDriver"
    directory_to_extract_to2=os.getcwd()+"\\TwoDriver\\VerifDriver"
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to2)
    
    
def regen_driver():
    remove_drivers()
    extract_files()
    print("Drivers are ready to use")
regen_driver()
