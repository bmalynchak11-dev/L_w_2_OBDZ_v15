# Словник даних проєкту

## Таблиця user
Опис: Користувачі фінансової системи.

| Стовпець | Тип | Null | Опис |
| --- | --- | --- | --- |
| id | integer | NOT NULL | Первинний ключ користувача |
| email | text | NOT NULL | Унікальна електронна адреса |
| username | text | NOT NULL | Ім'я або нікнейм користувача |
| created_at | timestamptz | NOT NULL | Дата і час реєстрації |

## Таблиця category
Опис: Категорії доходів і витрат.

| Стовпець | Тип | Null | Опис |
| --- | --- | --- | --- |
| id | integer | NOT NULL | Первинний ключ категорії |
| name | text | NOT NULL | Назва категорії |
| type | text | NOT NULL | Тип категорії (income або expense) |
| created_at | timestamptz | NOT NULL | Час створення категорії |

## Таблиця wallet
Опис: Гаманці та банківські рахунки.

| Стовпець | Тип | Null | Опис |
| --- | --- | --- | --- |
| id | integer | NOT NULL | Первинний ключ гаманця |
| user_id | integer | NOT NULL | Власник рахунку (посилання на user) |
| name | text | NOT NULL | Назва рахунку |
| balance | numeric | NOT NULL | Поточний залишок коштів |
| currency | text | NOT NULL | Валюта гаманця |

## Таблиця budget
Опис: Місячні бюджети за категоріями.

| Стовпець | Тип | Null | Опис |
| --- | --- | --- | --- |
| id | integer | NOT NULL | Первинний ключ бюджету |
| user_id | integer | NOT NULL | Користувач системи (посилання на user) |
| category_id | integer | NOT NULL | Категорія ліміту (посилання на category) |
| limit_amount | numeric | NOT NULL | Розмір бюджетного обмеження |
| month | date | NOT NULL | Місяць бюджетного періоду |

## Таблиця transaction
Опис: Фінансові операції користувача.

| Стовпець | Тип | Null | Опис |
| --- | --- | --- | --- |
| id | integer | NOT NULL | Первинний ключ транзакції |
| wallet_id | integer | NOT NULL | Використаний рахунок (посилання на wallet) |
| category_id | integer | NOT NULL | Категорія платежу (посилання на category) |
| amount | numeric | NOT NULL | Сума операції |
| transaction_date | date | NOT NULL | Дата здійснення транзакції |
| description | text | NULL | Примітка або призначення платежу |

## Таблиця audit_log
Опис: Журнал аудиту та системних подій.

| Стовпець | Тип | Null | Опис |
| --- | --- | --- | --- |
| id | integer | NOT NULL | Первинний ключ запису логу |
| user_id | integer | NULL | Користувач, що викликав подію (посилання на user) |
| action | text | NOT NULL | Системна дія або подія |
| created_at | timestamptz | NOT NULL | Час запису події |