<template>
  <div class="jumbotron">
    <div class="container">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/cerulean/bootstrap.min.css"
        integrity="sha384-3fdgwJw17Bi87e1QQ4fsLn4rUFqWw//KU0g8TvV6quvahISRewev6/EocKNuJmEw"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <p>My anime list</p>
          <hr><br>

          <button type="button" class="btn btn-success">Add anime</button>

          <br><br>

          <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Tags</th>
                    <th scope="col">Watched?</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="ani, index in anime" :key="index">
                    <td>{{ani.title}}</td>
                    <td>{{ani.tags}}</td>
                    <td>
                      <span v-if="ani.finished">Yes</span>
                      <span v-else>No</span>
                    </td>
                    <td>
                        <div class="btn-group" role="group">
                          <button type="button" class="btn btn-info btn-sm">Update</button>
                          <button type="button" class="btn btn-danger btn-sm">Delete</button>
                        </div>

                    </td>
                </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data(){
    return {
      anime:[]
    };
  },

  methods:{
    getAnime(){
      const path = "http://localhost:5000/anime";
      axios.get(path)
      .then((response)=>{
        this.anime = response.data.anime;
      })
      .catch((error) =>{
        console.error(error);
      });
    },
  },
  created() {
    this.getAnime();

  }
}
</script>
