Портфолио Карнауховой Юлии

Я подготовила примеры работ для демонстрации владения инструментами и технологиями по направлениям Разработки BI, BI Аналитики и Аналитики Данных



В данном репозитории вы найдете примеры следующих технологических стеков:

Apache Superset
Power BI
Apache Airflow
PostgreSQL
Python


Дашборд для кофейни Superset
image
Ссылка на описание работы - Superset/Описание процесса создания Дашборда в Superset.md


Отчет по рекламным кампаниям Power BI
image image image
Для разработки данного отчета был использован датасет с Kaggle: https://www.kaggle.com/datasets/alperenmyung/social-media-advertisement-performance?select=campaigns.csv

Ежедневный отчет по продажам и заказам товаров Power BI
Данный отчет из моей рабочей практики от 2023 года.Бренды, отображенные на скриншоте, не существуют на сегодняшний день.

image
В данной папке вы сможете найти примеры отчетов в формате .pbix - https://github.com/julialobankova/portfolio_09.2025/tree/main/Power%20BI/




Airflow и Парсинг данных
Я реализовала простой ETL процесс с помощью Python и Airflow, для сбора данных из онлайн магазина игрушек: Всего 2 task.

1й task - сбор данных с помощью BeautifulSoup и requests, трансформация прайса под единый формат и сохранение их в csv. Использую PythonOperator.

2й task - Файл CSV загружается в СУБД c помощью серверной функции COPY, для этого использую BashOperator Файлы с определением DAG и функциями - https://github.com/julialobankova/portfolio_09.2025/tree/main/Superset

В реальных бы кейсах можно было бы собирать данные на ежедневной основе и отслеживать изменения цен конкурентов, доработав данный процесс.

image image image image
