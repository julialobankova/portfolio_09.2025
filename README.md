
# Портфолио Карнауховой Юлии
<br>

Я подготовила примеры работ для демонстрации владения инструментами и технологиями по направлениям Разработки BI, BI Аналитики и Аналитики Данных

В данном репозитории вы найдете примеры следующих технологических стеков:
<br><br>

**Apache Superset**  
**Power BI**  
**Apache Airflow**  
**PostgreSQL**  
**Python**
<br><br>

### Дашборд для кофейни Superset  

<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/9b143b7f-5767-441e-87ed-231ee04f3e94" />  

**Ссылка на описание работы** - [Superset/Описание процесса создания Дашборда в Superset.md](https://github.com/julialobankova/portfolio_09.2025/blob/main/Superset/%D0%9E%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%B0%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%94%D0%B0%D1%88%D0%B1%D0%BE%D1%80%D0%B4%D0%B0%20%D0%B2%20Superset.md)

### Прототипирование отчета Power BI по результатам ТЗ:  

Ссылка на ТЗ -  [https://github.com/julialobankova/portfolio_09.2025/blob/main](https://github.com/julialobankova/portfolio_09.2025/blob/main/%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F/%D0%94%D0%B0%D1%88%D0%B1%D0%BE%D1%80%D0%B4%20HR%20%D0%A2%D0%97.docx)  

Ссылка на прототип - [https://github.com/julialobankova/portfolio_09.2025/blob/main](https://github.com/julialobankova/portfolio_09.2025/blob/main/Power%20BI/%D0%9F%D1%80%D0%BE%D1%82%D0%BE%D1%82%D0%B8%D0%BF%20HR.pbix)  

<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/2fd0ecb0-3a09-445c-b3f8-e67cec090949" />  


### Отчет по рекламным кампаниям Power BI
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/41cc3b0c-0e96-4f6e-bedf-d27233bf6ae0" />
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/82bd028a-b1a9-49d0-bd90-5224ed30b876" />
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/9f846159-3421-4c4d-85cb-9988d3c40250" />  

Для разработки данного отчета был использован датасет с Kaggle: https://www.kaggle.com/datasets/alperenmyung/social-media-advertisement-performance?select=campaigns.csv

### Ежедневный отчет по продажам и заказам товаров Power BI
Данный отчет из моей рабочей практики от 2023 года.Бренды, отображенные на скриншоте, не существуют на сегодняшний день.

<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/308163cb-edfb-4270-a56f-8c528fa24edf" />  

В данной папке вы сможете найти примеры отчетов в формате .pbix - https://github.com/julialobankova/portfolio_09.2025/tree/main/Power%20BI/




### Airflow и Парсинг данных
Я реализовала простой ETL процесс с помощью Python и Airflow, для сбора данных из онлайн магазина игрушек: Всего 2 task.

**1й task** - сбор данных с помощью BeautifulSoup и requests, трансформация прайса под единый формат и сохранение их в csv. Использую PythonOperator.

**2й task** - Файл CSV загружается в СУБД c помощью серверной функции COPY, для этого использую BashOperator Файлы с определением DAG и функциями - https://github.com/julialobankova/portfolio_09.2025/tree/main/Superset

В реальных бы кейсах можно было бы собирать данные на ежедневной основе и отслеживать изменения цен конкурентов, доработав данный процесс.  


<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/c6a1c82b-b542-4ffa-acb8-e5fc7179c616" />
<img width="600" height="100" alt="image" src="https://github.com/user-attachments/assets/b9861e4a-e28d-4f9b-ade7-10f4c20c035e" />
<img width="625" height="400" alt="image" src="https://github.com/user-attachments/assets/8cfe654c-0406-434f-9e96-3670c7289a29" />
<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/ccb94876-eff7-4a30-b07c-0cd0fe863f15" />
