def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'existe pas.")
    else: 
        print(content)
    finally:
        if 'file' in locals():
            file.close()
            print("Opération terminée.")  


read_file("test.txt")  
read_file("inexistant.txt")