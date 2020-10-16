# api_yamdb




[![Yamdb-app workflow](https://github.com/meat9/yamdb_final/workflows/main/badge.svg)](https://github.com/meat9/yamdb_final/actions)



Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».

## Регистрация
            
  Регистрация/авториация по email
  
  Аутентификация по JWT-токену

## Пользовательские роли
            
Аноним — может просматривать описания произведений, читать отзывы и комментарии.

Аутентифицированный пользователь (user)— может читать всё, как и Аноним, дополнительно может публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы и ставить им оценки; может редактировать и удалять свои отзывы и комментарии.

Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.

Администратор (admin) — полные права на управление проектом и всем его содержимым. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.

Администратор Django — те же права, что и у роли Администратор.

## Алгоритм регистрации пользователей
Пользователь отправляет POST-запрос с параметром email на /api/v1/auth/email/.

YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email .

Пользователь отправляет POST-запрос с параметрами email и confirmation_code на /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).

Эти операции выполняются один раз, при регистрации пользователя. В результате пользователь получает токен и может работать с API, отправляя этот токен с каждым запросом.

После регистрации и получения токена пользователь может отправить PATCH-запрос на /api/v1/users/me/ и заполнить поля в своём профайле (описание полей — в /redoc).

Если пользователя создаёт администратор (например, через POST-запрос api/v1/users/...) — письмо с кодом отправлять не нужно.


## Ресурсы API YaMDb
              
Ресурс AUTH: аутентификация.

Ресурс USERS: пользователи.

Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).

Ресурс GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.

Ресурс REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.

Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.


## Развертывание проекта

python manage.py createsuperuser  #Создание супер пользователя 

python manage.py makemigrations
python manage.py migrate  #Выполнение миграций

pip install -r requirements.txt #Установка всех пакетов

python manage.py runserver  #Запуск сервера

Либо запуск через Docker
docker-compose up


