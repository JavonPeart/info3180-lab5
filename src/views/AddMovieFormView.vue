<template>
    <div class="container">
        <h1 class="">Add Movie</h1>
        <MovieForm />
    </div>
</template>

<script>
    import MovieForm from "../components/MovieForm.vue"
    export default {
        name: "AddMovieFormView",
        components: {
            MovieForm,
    },
};
</script>