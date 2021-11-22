
class FileManager:
    
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        otwarcie = open(self.file_name)
        dane = otwarcie.read()
        print(dane)

    def update_file(self, text_data):
        uchwyt = open(self.file_name, 'a')
        uchwyt.write(text_data)
        uchwyt.close()







        