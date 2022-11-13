<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/MyFactoryIsSoGood/advisory_backend">
    <img src="https://bankreg.ru/bankr.ru/wp-content/uploads/2017/06/company_logo_33305-1.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Advisory Service</h3>

  <p align="center">
    Репозиторий серверной части Advisory-сервиса для Банка Открытие
    <br>
  </p>
</div>

## Другие части:
* Веб-клиент: ```https://github.com/LaMileyn/Hackathon```
* iOS-приложение: ```https://github.com/LaMileyn/Hackathon```


## О проекте

Сервис предоставляет дополнительные возможности взаимодействия клиента с приложением. Помимо основного бэкэнда, фронт-енд в виде веб клиента и iOS-приложения может обращаться к нашему сервису с такими запросами, как:
* Запрос доп.информации о брокере из бизнес-домена(профили риска, отзывы клиентов, средняя доходность клиента)
* Запрос тел виджетов для дальнейшего рендеринга
* Хранение информации о тестах. Создание профиля риска клиента по пройденному тесту

Так же, на сервисе расположен бот, отвечающий клиенту.
Сервис полностью задокументирован. Swagger-документация доступна по пути ```127.0.0.1:80/docs```


### Стек

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Beautiful Soup 4
* Docker
* Docker Compose


<!-- GETTING STARTED -->
## Установка

Проект завернут в контейнер и вместе с базой данных оркестрируется через Docker Compose.
* Склонируйте репозиторий
* Выполните следующие команды:
```docker-compose build```, 
```docker-compose up```

Приложение будет доступно на 127.0.0.1:80
