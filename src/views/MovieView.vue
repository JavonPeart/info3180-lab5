<template>
    <div class="movies-view">
        <div v-for="movie in movies" :key="movie.id">
            <img :src="movie.poster" alt="Movie Poster" />
            <h2>{{ movie.title }}</h2>
            <p>{{ movie.description }}</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

const fetchMovies = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8080//api/v1/movies");
        const data = await response.json();
        movies.value = data.movies;
    } catch (error) {
        console.log(error);
    }
};

onMounted(() => {
    fetchMovies();
});
</script>