<script setup lang="ts">
import { ref, computed } from "vue";
import { inject } from "vue";
import { useFetch } from "@vueuse/core";
import { useWebApp } from "vue-tg";

const { initDataUnsafe, close } = useWebApp();
const user = initDataUnsafe.user as { id: number | string } || { id: "unknown" }; // Получаем данные пользователя

const BASE_SITE = inject("BASE_SITE") as string;

// Определяем пропсы для компонента
const props = defineProps([
  "dayWeek", // День недели
  "countSlot", // Количество доступных слотов
  "dayData", // Точная дата (например, 08.01.2025)
  "doctorInfo", // Полная информация о докторе
  "dayDate",
]);

// Состояния модальных окон
const isModalOpen = ref(false); // Основное модальное окно для выбора времени
const isConfirmationModalOpen = ref(false); // Модальное окно подтверждения записи
const isSuccessModalOpen = ref(false); // Модальное окно успешной записи
const selectedTime = ref(""); // Выбранное время для записи
const selectedDay = ref(""); // Выбранный день для записи
const localCount = ref(props.dayDate.total_slots); // Доступное количество слотов для выбранного дня
const localSlots = ref(props.dayDate.slots); // Доступные временные слоты

// Функция для открытия основного модального окна
const openModal = () => {
  isModalOpen.value = true;
};

// Функция для закрытия основного модального окна
const closeModal = () => {
  isModalOpen.value = false;
};

// Функция для открытия модального окна подтверждения записи
const openConfirmationModal = (time: string, day: string) => {
  selectedTime.value = time; // Устанавливаем выбранное время
  selectedDay.value = day; // Устанавливаем выбранный день
  isConfirmationModalOpen.value = true;
};

// Функция для закрытия модального окна подтверждения записи
const closeConfirmationModal = () => {
  isConfirmationModalOpen.value = false;
};

// Функция для подтверждения записи на прием
const confirmAppointment = async () => {
  const bookingData = {
    doctor_id: props.doctorInfo.id,
    user_id: user.id,
    day_booking: selectedDay.value,
    time_booking: selectedTime.value,
  };

  try {
    await useFetch(`${BASE_SITE}/book`).post(bookingData).json(); // Отправляем данные о записи на прием через API
    localCount.value--; // Уменьшаем количество доступных слотов на 1
    localSlots.value = localSlots.value.filter(
      (slot: string) => slot !== selectedTime.value
    ); // Удаляем выбранный слот из доступных
    isConfirmationModalOpen.value = false; // Закрываем окно подтверждения записи
    isModalOpen.value = false; // Закрываем основное модальное окно
    isSuccessModalOpen.value = true; // Открываем окно успешной записи
  } catch (error) {
    console.error("Ошибка при записи:", error);
    alert("Произошла ошибка при записи. Пожалуйста, попробуйте еще раз."); // Обработка ошибок при записи
  }
};

// Функция для закрытия окна успешной записи
const closeSuccessModal = () => {
  isSuccessModalOpen.value = false;
  close(); // Закрываем веб-приложение (если это требуется)
};

// Вычисляемое свойство для отображения количества доступных слотов
const slotLabel = computed(() => {
  if (localCount.value) {
    return `Доступно ${localCount.value} слотов`;
  }
  return "Бронь не доступна!"; // Сообщение о недоступности слотов
});
</script>

<template>
  <div>
    <!-- Карточка дня -->
    <div
      class="cursor-pointer bg-white rounded-lg shadow-md p-6 text-center hover:shadow-lg transition-shadow duration-300"
      @click="openModal"
    >
      <h3 class="text-xl font-bold text-indigo-600 mb-2">{{ dayDate.day }}</h3>
      <p class="text-gray-700 text-lg">{{ slotLabel }}</p>
    </div>

    <!-- Основное модальное окно (выбор времени) -->
    <div
      v-if="isModalOpen"
      class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50"
      @click.self="closeModal"
    >
      <div class="bg-white rounded-lg shadow-lg w-96 p-6">
        <h2 class="text-2xl font-bold text-indigo-900 text-center">
          Запись на {{ dayDate.date }}
        </h2>
        <h3 class="font-bold text-center mb-4 text-indigo-900">
          ({{ dayDate.day }})
        </h3>
        <p class="text-gray-700 mb-4 text-center">
          Выберите удобное время для записи:
        </p>
        <div class="grid grid-cols-3 gap-3 mb-6">
          <!-- Генерация временных слотов -->
          <button
            v-for="time in localSlots"
            class="py-2 px-4 bg-indigo-500 text-white rounded-lg hover:bg-indigo-600 transition duration-200"
            @click="openConfirmationModal(time, dayDate.date)"
          >
            {{ time }}
          </button>
        </div>
        <button
          class="w-full py-2 px-4 bg-red-500 text-white rounded-lg hover:bg-red-600 transition duration-200"
          @click="closeModal"
        >
          Закрыть
        </button>
      </div>
    </div>

    <!-- Модальное окно подтверждения -->
    <div
      v-if="isConfirmationModalOpen"
      class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50"
      @click.self="closeConfirmationModal"
    >
      <div class="bg-white rounded-lg shadow-lg w-96 p-6">
        <h2 class="text-xl font-bold text-indigo-900 mb-4 text-center">
          Вы уверены?
        </h2>
        <p class="text-gray-700 text-center mb-6">
          Вы хотите записаться к
          <span class="font-semibold">{{ doctorInfo.name }}</span> на
          <span class="font-semibold">{{ dayDate.day }}</span> (<span>{{
            dayDate.date
          }}</span
          >) в <span class="font-semibold">{{ selectedTime }}</span
          >?
        </p>
        <div class="flex justify-around">
          <button
            class="py-2 px-4 bg-green-500 text-white rounded-lg hover:bg-green-600 transition duration-200"
            @click="confirmAppointment"
          >
            ДА
          </button>
          <button
            class="py-2 px-4 bg-red-500 text-white rounded-lg hover:bg-red-600 transition duration-200"
            @click="closeConfirmationModal"
          >
            НЕТ
          </button>
        </div>
      </div>
    </div>

    <!-- Модальное окно успешной записи -->
    <div
      v-if="isSuccessModalOpen"
      class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50"
      @click.self="closeSuccessModal"
    >
      <div class="bg-white rounded-lg shadow-lg w-96 p-6">
        <h2 class="text-xl font-bold text-green-600 mb-4 text-center">
          Успешно!
        </h2>
        <p class="text-gray-700 text-center mb-6">
          Вы успешно записались к
          <span class="font-semibold">{{ doctorInfo.name }}</span> на
          <span class="font-semibold">{{ dayDate.day }}</span> (<span>{{
            dayDate.date
          }}</span
          >) в <span class="font-semibold">{{ selectedTime }}</span
          >.
        </p>
        <button
          class="w-full py-2 px-4 bg-green-500 text-white rounded-lg hover:bg-green-600 transition duration-200"
          @click="closeSuccessModal"
        >
          Закрыть
        </button>
      </div>
    </div>
  </div>
</template>