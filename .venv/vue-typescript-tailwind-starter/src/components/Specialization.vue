<script setup lang="ts">
/*Мы импортируем функцию useRouter из библиотеки vue-router. 
Это необходимо для работы с маршрутизацией внутри нашего компонента. 
С помощью этой функции мы получаем доступ к экземпляру роутера, что позволяет нам программно управлять навигацией*/
import { useRouter } from "vue-router";

/*С помощью defineProps мы определяем свойства (props), которые компонент будет принимать. В нашем случае это:
specialization: название специализации.
description: описание специализации.
icon: иконка, ассоциированная со специализацией.
specialId: уникальный идентификатор специализации, который будет использоваться для навигации. */
defineProps(["specialization", "description", "icon", "specialId"]);

/* Мы создаем константу router, которая хранит экземпляр роутера, полученный с помощью useRouter(). 
Это позволит нам использовать методы роутера для навигации по маршрутам.*/
const router = useRouter();
</script>

<template>
<!-- Внутри блока <template> мы создаем карточку, которая содержит информацию о специализации. 
    Используются классы Tailwind для стилизации-->
  <div
    class="bg-white rounded-xl shadow-lg overflow-hidden transition-transform duration-300 hover:scale-105 flex flex-col items-center justify-center p-6"
  >
    <div
      class="bg-blue-100 rounded-full p-6 w-28 h-28 flex items-center justify-center"
    >
    <!-- Мы используем элемент <i> для отображения иконки. 
    Класс иконки передается через пропс icon, что позволяет динамически менять иконки в зависимости от переданных данных-->
      <i :class="icon + ' text-blue-600 text-4xl'" aria-hidden="true"></i>
    </div>
    <!-- Название специализации отображается в заголовке <h3> -->
    <h3 class="text-xl font-bold text-gray-800 m-2">{{ specialization }}</h3>
    <!--описание — в параграфе <p>-->
    <p
      class="text-gray-600 mb-4 text-center h-30 overflow-hidden"
      title="{{ description }}"
    >
      {{ description }}
    </p>
    <!--Кнопка "Записаться" использует директиву @click для обработки клика. 
    При нажатии на кнопку вызывается метод, который перенаправляет пользователя на страницу с врачами по выбранной специализации, используя метод router.push()-->
    <button
      @click="() => router.push(`/doctors/${specialId}`)"
      class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition-colors"
    >
      Записаться
    </button>
  </div>
</template>

<style scoped></style>
