// createRouter – функция для создания экземпляра роутера.
// createWebHistory – функция, которая позволяет использовать HTML5 History API для управления историей навигации.
// Компоненты Doctors, Booking и Home – это Vue-компоненты, которые будут отображаться на различных маршрутах
import { createRouter, createWebHistory } from "vue-router";
import Doctors from "../views/Doctors.vue";
import Booking from "../views/DoctorDetail.vue";
import Home from "../views/Home.vue";

// создаем массив маршрутов. Каждый маршрут представляет собой объект с тремя основными свойствами:
// path: URL-адрес, по которому будет доступен маршрут.
// name: уникальное имя маршрута, которое может использоваться для навигации.
// component: компонент Vue, который будет отображаться при переходе на указанный маршрут.
const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/doctors/:specialId", name: "Doctors", component: Doctors },
  { path: "/booking/:doctorId", name: "Booking", component: Booking },
];

//создаем экземпляр роутера с помощью функции createRouter. Мы передаем объект с настройками:
// history: указывает на использование HTML5 History API для управления историей.
// routes: массив маршрутов, который мы определили ранее.
// scrollBehavior: функция, которая управляет поведением прокрутки при навигации. В данном случае мы указываем, что при переходе на новый маршрут страница всегда будет прокручиваться к верху.
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    // Всегда прокручивать к верху страницы
    return { top: 0 };
  },
});

export default router;