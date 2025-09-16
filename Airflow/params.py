DBNAME = 'coffee_shop'
USER = 'postgres'
PASSWORD = '16Tarevi'
HOST = '103.88.240.76'
PORT = '5432'

# Для функции save_to_csv
# name_task - task_id, который возвращает резулататы парсинга, например - parse_store_toys
# columns - название получившихся занчений при парсинге, которые будут названиями столбцов в csv файле
# name_file - название файла с указанием формата файла - .csv, в который сохраняться результаты парсинга и из
#             которого будет произведена загрузка данных в БД
name_task = 'parse_task'
columns = ['name', 'brand', 'article', 'price']
name_file = '/root/airflow/dags/csv/pars_store_toys.csv'


# Для функции copy_command
# your_table - таблица в бд в которую будет загружены результаты парсинга
# delimiter - разделитель, используемый в 'name_file'
# file_format - какой формат файла используем для загрузки в БД, указать в нижнем регистре
# mean_header - указать True или False, True - загрузить данные включая загаловки, подходит когда в CSV файлах нет
#               заголовков, False - когда в  файле есть заголовки и их загружать не надо
your_table = 'data.toys'
delimiter = ','
file_format = 'csv'
mean_header = 'True'
