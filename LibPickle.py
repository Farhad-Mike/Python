import pickle # Python proprietary data serialization method (from JSON, to JSON and so on). может сериализовать данные с использованием разных форматов (в документации они называются протоколами).
# Протокол 0 – это ASCII, его удобно использовать во время отладки. протокол 3 (pickle.HIGHEST_PROTOCOL)
import cPickle # The same like pickle but more faster

pickle.dump(obj, fh, pickle.HIGHEST_PROTOCOL) # Записать данные в файл
pickle.load(fh) # автоматически определяет используемый протокол и загружает файл
