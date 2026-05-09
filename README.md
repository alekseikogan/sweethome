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

## Production (Nginx + Gunicorn + HTTPS)

1. Заполните `.env` для продакшена:
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=your-domain.com,www.your-domain.com`
   - `DJANGO_CSRF_TRUSTED_ORIGINS=https://your-domain.com,https://www.your-domain.com`
   - `DOMAIN=your-domain.com`
   - `LETSENCRYPT_EMAIL=you@example.com`
2. Запустите production stack:
   - `docker compose -f docker-compose.prod.yml up -d --build`
3. Выпустите сертификат Let's Encrypt (первый раз):
   - `docker compose -f docker-compose.prod.yml run --rm certbot certonly --webroot -w /var/www/certbot -d your-domain.com -m you@example.com --agree-tos --no-eff-email`
4. Перезапустите Nginx после выпуска сертификата:
   - `docker compose -f docker-compose.prod.yml restart nginx`
5. Продление сертификата (периодически, например cron раз в день):
   - `docker compose -f docker-compose.prod.yml run --rm certbot renew --webroot -w /var/www/certbot --quiet`
   - `docker compose -f docker-compose.prod.yml restart nginx`

До выпуска Let's Encrypt сертификата Nginx стартует с self-signed сертификатом, чтобы HTTPS уже работал.

Если на продакшене не отображаются фото товаров: в Docker при первом запуске том `media` пустой, а в базе остаются только пути к файлам. Команда `seed_demo_media` (вызывается из `docker-entrypoint-prod.sh` перед `collectstatic`) создает placeholder-изображения для демо-данных. После обновления кода выполните `docker compose -f docker-compose.prod.yml up -d --build`.


## Полезные команды:
`python manage.py loaddata fixtures/goods/categories.json`

`python manage.py loaddata fixtures/goods/products.json`

` `