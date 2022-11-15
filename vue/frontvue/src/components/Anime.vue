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
          <h1 class="text-center" style="border-radius:12px">My anime list</h1>
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
          <footer class="bg-primary text-white text-center"> Copyright &copy; Mai reserved 2022</footer>
        </div>
      </div>

      <!--first modal-->
      <b-modal ref="addAnimeModal" id="anime-modal" title="Add new anime" hide-backdrop hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
            <b-form-input id="form-title-input" type="text" v-model="addAnimeForm.title" required placeholder="Enter Anime">
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-tags-group" label="Tags:" label-for="form-tags-input">
            <b-form-input id="form-tags-input" type="text" v-model="addAnimeForm.tags" required placeholder="Enter Tags">
            </b-form-input>
          </b-form-group>

        <b-form-group id="form-finished-group">
          <b-form-checkbox-group id="form-check" v-model="addAnimeform.finished">
            <b-form-checkbox value="true">Finished?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <!--buttons-->
        <button type="submit" variant="primary">Submit</button>
        <button type="reset" variant="primary">Reset</button>
        </b-form>
      </b-modal>
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
