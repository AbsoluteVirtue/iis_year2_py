import datetime
import os
import shutil


class File(object):
    def __new__(cls, *args, **kwargs):                  # Конструктор
        print("Creating instance")
        return super(File, cls).__new__(cls)
                
    def __init__(self, name, expansion, date, time):  # Инициализатор
        self.file_name = name
        self.file_expansion = expansion
        self.file_date = date
        self.file_time = time
        print("Object created .")
        self.create_file()

    def f_res(self):                                                     # хранение полного имени файла "имя.расширение" для функций работы с файлом ( open(), os.rename()  )
        return self.file_name + '.' + self.file_expansion
    
    def show_file(self):                                              # Печать информации о файле
        print("\n FILE : ",
              self.f_res(),
              "   Size:",
              os.stat(self.f_res()).st_size,
              " byte  | Created : ",
              self.file_date,
              "  ",
              self.file_time,
              "\n Direction: ",
              os.getcwd(),
              "\\",
              self.f_res(),
              "\n")

    def create_file(self):                                            # Создание файла в директории с  python файлом
        file = open(self.f_res(), "w")
        direction = os.getcwd()
        print("File created at dir : ", direction)
        file.close()

    def change_file_name(self, name, expansion):   # переименование файла
        print("File name changed :",
              self.f_res(),
              "  --> ",
              name + '.' + expansion)
        os.rename(self.f_res(), name + '.' + expansion)
        self.file_name = name  
        self.file_expansion = expansion
        
    def change_direction(self, direc):                        # Перемещение файла
        print("Direction changed :",
              os.getcwd(),
              "  --> ",
              direc)
        shutil.move(self.f_res(), direc)
        os.chdir(direc)

    def __del__(self):
        print("Desctructor called")
        print("File ", self.f_res(), " deleted .")
        os.remove(self.f_res())


image = File("windows wallpaper",
             "jpeg",
             datetime.date.today(),
             datetime.datetime.now().time())
image.show_file()
image.change_direction("D:/")
image.change_file_name("windows application",
                       "exe")
print("End program")
del image
