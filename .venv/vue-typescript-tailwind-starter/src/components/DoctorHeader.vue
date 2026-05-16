<script setup lang="ts">
/*макрос Vue для объявления входных параметров (props) компонента:
принимает массив строк;
в данном случае объявляет один prop с именем label */
defineProps(["label"]);
</script>

<template>
  <!--justify-between — распределяет дочерние элементы по ширине контейнера: первый у левого края, последний у правого-->
  <div class="flex justify-between items-center mb-12">
    <h1 class="text-3xl font-bold text-indigo-900">{{ label }}</h1> <!-- заголовок первого уровня, которы подставляет значение prop label, переданного родительским компонентом-->
    <!-- router-link компонент Vue Router для навигации-->
    <!-- to="/" атрибут, указывающий маршрут: при клике перенаправляет на главную страницу-->
    <!-- inline-flex — элемент ведёт себя как inline, но использует Flexbox внутри-->
    <router-link
      to="/" 
      class="inline-flex items-center px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
    >
      <!--иконка «дом» из Font Awesome, где «Главная» — текст кнопки-->
      <i class="fas fa-home mr-2"></i>
      Главная
    </router-link>
  </div>    
</template>