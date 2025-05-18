## Install
#### In docker folder

1. docker compose up

## Migration
#### In skye engine folder

1. ./manage.py migrate

## Run server
#### In sky_engine folder 

1. manage.py runserver

## Run app
#### Go to the web browser and go to the http://localhost:8000/image



Przepraszam, ze napiszę po polsku.

Rozsypało mi się całe środowisko, przegladarka zaczeła sypać błędami, ktore nie
mialy sensu, raz błąd był a raz go nie było.

Dodatkowo requesty do serwera django dostawały zwrot 404 gdzie wszystko powinno być wporządku.
Jeszcze nie mogłem uporać się z csrf, wyłączyłem go w aplikacji i zaczałem wysyłać ale nadał krzyczał 
błędem. Do tego pojawił się jakiś błąd przeglądarki z devtoolsJson lub jakoś
podobni brzmiący. 

Aplikację zaprojektowałem ze swoją galerią dlatego podpiąłem postgresa
i chciałem wgrywać tam zdjęcia jako wartość binarną, takie pole posiada postgres.
są 4 widoki 1 galeria , drugi image i dwa pojedyncze które mi pańswto polecili 
zrobić, według mojej oceny w szczególności a nie tylko.
Gallery i Image są do zarządzania galeria i obrazkami co było napisane w zadaniu, 
żeby takie api zrobić i dwa inne, kóre były opisane bardziej szczegółowo.

Niestety nie przetestowałem wszystkiego z uwagi na to ze nie działa mi środowisko,
po przeinstalowaniu linuxa nadal było coś nie tak dlatego muszę już zrezygnować
inaczej pracowałbym do 15: 30 ponieważ dostałem dwa dni. Mam nadzieje,
że mimo wszystko nawet jeśli mnie Państwo nie zatrudnią nie narobiłem sobie wstydu ;)

Jeszcze jedna rzecz, wartości zdjęć, które pobierałem ze strony były jako wartości 
binarne, zakodowałem je do base64 i starałem się je wyświetlić w przeglądarce ale
coś było nie tak, więc tutaj nie wiedziałem za bardzo co mam robić, probowałem je decodować 
do utf-16 ale też zwracało jakieś dziwne błędy. Insomia taki requester jak postman
poradziła sobie z tymi zdjęciami i wyświetlaly się wporządku.

Zatem tyle i dziękuję za możliwość uczestnictwa w procesie rekrutacyjnym.
