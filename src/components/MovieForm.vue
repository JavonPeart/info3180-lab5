<template>
    <div class="movie-container">
        <form @submit.prevent="saveMovie">

            <div class="form-group mb-3">
                <label class="form-label" for="title">Title:</label>
                <input class="form-control" type="text" id="title" />
            </div>

            <div class="form-group mb-3">
                <label class="form-label" for="description">Description:</label>
                <textarea class="form-control" id="description"></textarea>
            </div>

            <div class="form-group mb-3">
                <label class="form-label" for="poster">Poster:</label>
                <input class="form-control" type="file" id="poster">
            </div>

            <div class="form-group mb-3">
                <button class="btn btn-primary" type="submit">Save Movie</button>
            </div>

        </form>
    </div>
</template>
  
<script>
import { ref, onMounted } from "vue";
export default {
    name: "MovieForm", setup() {
        let csrf_token = ref("");

        function getCsrfToken() {
            fetch('http://127.0.0.1:8080//api/v1/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    csrf_token.value = data.csrf_token;
                })
        }
        onMounted(() => {
            getCsrfToken();
        });

        function saveMovie() {
            let movieForm = document.getElementById('movieForm');
            let form_data = new FormData(movieForm);
            
            console.log('CSRF Token:', csrf_token.value);
            
            fetch("http://127.0.0.1:8080//api/v1/movies", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': csrf_token.value
                }
            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    console.log(data);
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
        return {
            csrf_token,
            saveMovie,
        }
    }
}
</script>
  