# SweetHome - сайт по продаже предметов интерьера квартиры

## 🛠 Технологический стек

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)  
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)  
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)  
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/docs/Web/JavaScript)  
[![AJAX](https://img.shields.io/badge/AJAX-FF6F61?style=for-the-badge)](https://developer.mozilla.org/docs/Web/Guide/AJAX)


## Описание проекта

SweetHome - сайт, созданный на основе Python и фреймворка Django, предназначен для продажи мебели онлайн. Он предлагает широкий ассортимент мебельных изделий для всех помещений - спальни, гостиные, кухни и т.д.
Страница с каталогом сайта содержит различные артикулы мебели, где пользователь может просматривать доступные товары, фильтровать их по различным параметрам и добавлять интересующие их товары в корзину, оформлять заказ с выбором доставки и оплаты.

## Запуск через Docker Compose

1. Скопируйте шаблон переменных окружения:
   - `cp .env.example .env`
   - при необходимости измените значения в `.env`
2. Запустите проект:
   - `docker compose up --build`
3. Откройте приложение:
   - [http://localhost:8000](http://localhost:8000)

PostgreSQL поднимется в отдельном контейнере, а Django автоматически выполнит миграции при старте `web` сервиса.

python manage.py loaddata fixtures/goods/categories.json
python manage.py loaddata fixtures/goods/products.json