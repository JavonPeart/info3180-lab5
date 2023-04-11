<template>
    <div class="container">
        <h1>Movies</h1>
        <div class="movie-grid">
            <div v-for="movie in movies" :key="movie.id" class="movie-card">
                <div class="card">
                    <div class="poster">
                        <img :src="movie.poster" alt="Movie Poster" />
                    </div>
                    <div class="body">
                        <h2>{{ movie.title }}</h2>
                        <p>{{ movie.description }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script setup>

import { ref, onMounted } from "vue";

let movies = ref([]);

const fetchMovies = async () => {

    try {
        const response = await fetch("http://127.0.0.1:8080/api/v1/movies");
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


<style>
.movie-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    gap: 25px;
    row-gap: 25px;
}

.movie-card {
    display: flex;
    flex-direction: row;
    max-width: 400px;
    max-height: 400px;
    height: 35vh;
    width: 60vw;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    overflow: hidden;
}

.card {
    display: flex;
    flex-direction: row;
    border: 1px solid #ccc;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    /* margin-bottom: 20px; */
}

.poster {
    width: 100%;
    flex: 1;
}

.poster img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.body {
    padding: 15px;
    flex: 1;
}

.card h2 {
    margin-top: 0;
}

.card p {
    margin-bottom: 0;
}

@media (max-width: 768px) {
    .movie-grid {
        justify-content: center;
    }
}
</style>