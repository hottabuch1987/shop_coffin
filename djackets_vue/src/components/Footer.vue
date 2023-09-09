<template>

<footer>
    <div class="waves">
        <div class="wave" id="wave1"></div>
    </div>
     <p class="text-white">Гарантия и безупречное качество. Будем рады помочь Вам в трудную минуту.</p>

    <ul class="menu">
        <li><a href="#">Главная</a></li>
        <li><a href="#">О нас</a></li>
        <li><a href="#">Контакты</a></li>
      
    </ul>
    
    <p>©2023 VIP Гробы | Все права защищены</p>
</footer>

</template>
<style>



footer{
    position: relative;/*относительное позиционирование*/
    width: 100%;/*на всю ширину*/
    padding: 20px 50px;/*поля для контента*/
    background:  rgba(63, 62, 63, 0.76);
    display: flex;
    justify-content: center;/*в центре по горизонтали*/
    align-items: center;/*в центре по вертикали*/
    flex-direction: column;
    margin-top: 100px;/*отступ сверху*/
}
footer .wave{
    position: absolute;/*абсолютное позиционирование*/
    top: -100px;
    left: 0;
    width: 100%;
    height: 100px;
    /* background: url(wave.png);картинка волны */
    background-size: 1000px 100px;/*ширина и высота волны*/
}
.menu{
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 10px 0;
    flex-wrap: wrap;/*разрешен перенос на новую строку*/
}

.menu li{
    list-style: none;/*удалить черные маркеры*/
}

.menu li a {
    font-size: 1.2em;/*размер ссылок меню*/
    color: #fff;/*цвет ссылок меню*/
    opacity: 0.75;/*значение прозрачности*/
    margin: 0 15px;
    text-decoration: none;/*ссылка без подчеркивания*/
    display: inline-block;
}
.menu li a:hover {
    opacity: 1;
}
footer p {
    color: #fff;
    text-align: center;
    margin-top: 15px;
    font-size: 1.1em;
}
</style>