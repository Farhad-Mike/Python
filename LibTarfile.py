import tarfile

fi = tarfile.open('path')
fi.close()
fi.getmembers() # возвращает список объектов tarfile.TarInfo, по одному для каждого члена.
tarfile.TarInfo.name # Имена файлов членов, включая пути
fi.extract('tarfile.TarInfo') # функция сохраняющая член на диск.