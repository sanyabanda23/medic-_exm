<script setup lang="ts">
import { useRouter } from "vue-router";
import { inject } from "vue";

const BASE_SITE = inject("BASE_SITE") as string;
const props = defineProps([
  "doctorId",
  "name",
  "special",
  "experience",
  "work_experience",
  "description",
  "photo",
]);

const imageSrc = new URL(
  `${BASE_SITE}/static/images/${props.photo}`,
  import.meta.url
).href; // Используем URL для получения пути к изображению

const router = useRouter();
</script>

<template>
  <!--внешний контейнер карточки-->
  <div
    class="bg-white rounded-xl shadow-lg overflow-hidden h-full flex flex-col"
  >
    <!--контейнер с относительным позиционированием (нужен для абсолютного позиционирования изображения внутри)-->
    <div class="relative h-64 flex-shrink-0">
      <img
        :src="imageSrc"
        alt="Описание фотографии"
        class="absolute w-full h-full object-cover transition-transform duration-300 ease-in-out transform hover:scale-105"
      />
    </div>

    <!--Контент (информация + кнопка)
    flex + flex-col — Flexbox с вертикальной компоновкой;
    flex-grow — блок занимает всё доступное пространство внутри родительского Flex‑контейнера.-->
    <div class="p-6 flex flex-col flex-grow">
      <div class="flex-grow">
        <!-- h3 Обозначает структуру заговка(вннутри бока, а не основной на странице)-->
        <h3 class="text-xl font-bold text-gray-800 mb-2">{{ name }}</h3> 
        <p class="text-gray-600 mb-2">{{ special }}</p>
        <p class="text-sm text-gray-500 mb-4">
          Стаж работы: {{ work_experience }} {{ experience }}
        </p>
        <p class="text-gray-600 mb-4">{{ description }}</p>
      </div>
      <!--@click="..." — обработчик клика: при нажатии вызывает router.push() 
      для перехода на страницу записи (/booking/${doctorId})-->
      <button
        @click="() => router.push(`/booking/${doctorId}`)"
        class="w-full bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition-colors mt-auto"
      >
        Записаться на приём
      </button>
    </div>
  </div>
</template>
