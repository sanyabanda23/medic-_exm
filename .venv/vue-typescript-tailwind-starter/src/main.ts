import { createApp } from "vue";
//Подключает главный компонент приложения из файла App.vue
import App from "./App.vue";
// Импортирует глобальные стили из файла index.css
import "./assets/styles/index.css";
// Подключает конфигурацию маршрутизатора (роутинга) из папки router
import router from "./router";
//Плагин обеспечивает интеграцию приложения с Telegram Web Apps (позволяет использовать функции Telegram в веб‑приложении)
import { VueTelegramPlugin } from "vue-tg";

// Переменная app будет использоваться для настройки и запуска приложения
const app = createApp(App);
// Подключает маршрутизатор к приложению
app.use(router);
// Регистрирует плагин Telegram в приложении
app.use(VueTelegramPlugin);
//Предоставляет глобальную переменную BASE_SITE всем компонентам приложения
app.provide("BASE_SITE", "https://jodi-unconferred-makhi.ngrok-free.dev");
//Монтирует приложение в элемент с id="app" на HTML‑странице 
app.mount("#app");