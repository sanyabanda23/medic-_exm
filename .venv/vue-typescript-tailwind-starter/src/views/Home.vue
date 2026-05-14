<script setup lang="ts">
/*используем useFetch из библиотеки @vueuse/core.
Эта библиотека будет использоваться для взаимодействия с созданным ранее API. 
Она позволяет нам легко и удобно работать с запросами к API. 
В нашем случае нас интересует именно useFetch, который упрощает процесс получения данных. */
import { useFetch } from "@vueuse/core";
/* Мы импортируем несколько полезных функций из самого Vue:
ref: используется для создания реактивных переменных.
computed: позволяет создавать вычисляемые свойства, которые будут автоматически обновляться при изменении зависимостей.
onMounted и onBeforeUnmount: это хуки жизненного цикла компонента, которые позволяют выполнять код при монтировании и размонтировании компонента.*/
import { ref, computed, onMounted, onBeforeUnmount } from "vue";
import { inject } from "vue";
/*  импортируем компонент Specialization, который мы создали ранее. 
Этот компонент будет использоваться для отображения карточек со специализациями врачей на нашей главной странице*/
import Specialization from "../components/Specialization.vue";

/*определяем интерфейс Doctor, который описывает структуру данных о врачах. 
Это помогает нам понимать, какие поля будут возвращаться из API и обеспечивает статическую типизацию при работе с данными. */
interface Doctor {
    id: number;
    specialization: string;
    description: string;
    icon: string;
}

/* функции inject мы получаем базовый URL нашего API (BASE_SITE). 
Это позволяет нам использовать его в запросах без необходимости дублировать адрес в разных местах кода.*/
const BASE_SITE = inject('BASE_SITE') as string;
/* создаем реактивную переменную searchQuery, которая будет хранить текст запроса для поиска врачей по специализации или описанию.*/
const searchQuery = ref('');
/* Используя useFetch, мы выполняем GET-запрос к нашему API по адресу ${BASE_SITE}/specialists. 
Результаты запроса будут храниться в переменной doctors, а также у нас есть флаги isFetching (для отслеживания состояния загрузки) и error (для обработки ошибок). */
const {
    data: doctors,
    isFetching,
    error
} = useFetch(`${BASE_SITE}/specialists`).get().json();

const filteredDoctors = computed(() => {                            /*функция Vue 3 Composition API, создающая вычисляемое свойство */
    if (!doctors.value) return [] as Doctor[];                      /*если условие истинно, возвращается пустой массив, явно приведённый к типу Doctor[] */

    const query = searchQuery.value.toLowerCase().trim();           /*получает текущее значение реактивной ссылки searchQuery, преобразует строку в нижний регистр, удаляет пробелы в начале и конце строки */
    if (!query) return doctors.value;                               /*если строка пуста, возвращается исходный массив врачей без фильтрации. */

    return doctors.value.filter((doctor: Doctor) => {               /*запускает метод массива .filter(), который отбирает элементы по условию */
        return (
            doctor.specialization.toLowerCase().includes(query) ||  /*проверяет, содержит ли строка specialization подстроку query. Возвращает true или false */
            doctor.description.toLowerCase().includes(query)
        );
    });
});

/*Обработчик кликов вне поля ввода */
const handleClickOutside = (event: MouseEvent) => {
    const inputElement = document.getElementById('search');
    if (inputElement && !inputElement.contains(event.target as Node)) {
        inputElement.blur(); // Снять фокус с поля ввода
    }
};

// Установка обработчика при монтировании компонента
onMounted(() => {
    document.addEventListener('click', handleClickOutside);
});

// Удаление обработчика при размонтировании компонента
onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside);
});
</script>


<template>
    <!-- header -->
    <div>Тут будет контент главной страницы</div>
</template>
<style scoped></style>
