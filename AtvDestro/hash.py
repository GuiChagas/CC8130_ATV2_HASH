from encodings import utf_8
import hashlib
import json

def hash256_converter_list(filename):
    hash256_list = []

    file = open(filename, 'r', encoding='utf-8')
    file_list = file.readlines()
    
    for text in file_list:
        text = text.strip("\n")
        hashed_string = hashlib.sha256(text.encode('utf_8')).hexdigest()
        hash256_list.append(hashed_string)

    return hash256_list

def md5_converter_list(filename):
    md5_list = []

    file = open(filename, 'r', encoding='utf-8')
    file_list = file.readlines()
    
    for text in file_list:
        text = text.strip("\n")
        hashed_string = hashlib.md5(text.encode('utf_8')).hexdigest()
        md5_list.append(hashed_string)

    return md5_list

def validator(textoAsc):
    sha256_hashed = hash256_converter_list("string_list.txt")
    md5_hashed = md5_converter_list("string_list.txt")

    f = open('values.json', "r", encoding='utf-8')

    data = json.load(f)

    try:
        indexText = data['asc'].index(textoAsc)

        shaHash = data["SHA256"][indexText]
        mdHash =  data["MD5"][indexText]
     
        if(shaHash == sha256_hashed[indexText]):
            if(mdHash == md5_hashed[indexText]):

                print('Texto recebido: ' + textoAsc)
                print('Sha:  ' + shaHash)
                print('mdH:  ' + mdHash)
                print('sha:  ' + sha256_hashed[indexText])
                print('md5:  ' + md5_hashed[indexText])
                
                print("ESTA VALIDADO")
                print("")
            else:
                print('Texto recebido: ' + textoAsc)
                print('Sha:  ' + shaHash)
                print('mdH:  ' + mdHash)
                print('sha:  ' + sha256_hashed[indexText])
                print('md5:  ' + md5_hashed[indexText])
                
                print("MD5 NÃO ESTA VALIDADO")
                print("")        
        else:
            if(mdHash == md5_hashed[indexText]):
                print('Texto recebido: ' + textoAsc)
                print('Sha:  ' + shaHash)
                print('mdH:  ' + mdHash)
                print('sha:  ' + sha256_hashed[indexText])
                print('md5:  ' + md5_hashed[indexText])
                
                print("SHA NÃO ESTA VALIDADO")
                print("")
            else:

                print('Texto recebido: ' + textoAsc)
                print('Sha:  ' + shaHash)
                print('mdH:  ' + mdHash)
                print('sha:  ' + sha256_hashed[indexText])
                print('md5:  ' + md5_hashed[indexText])
                
                print("SHA E MD5 NÃO ESTÃO VALIDADO")
                print("")
    except:
        print("O texto não existe")  
        print(" ")



    f.close()



def main():
    file = open("string_list.txt", 'r', encoding='utf-8')
    file_list = file.readlines()
    
    for text in file_list:
        text = text.strip("\n")
        validator(text)


if __name__ == "__main__":
    main()