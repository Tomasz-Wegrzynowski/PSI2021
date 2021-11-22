import file_manager

test = file_manager.FileManager("test.txt")
test.read_file()
test.update_file("dodaj")
test.read_file()