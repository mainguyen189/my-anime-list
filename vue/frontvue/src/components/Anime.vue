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

          <!--alert mess-->
          <b-alert variant="success" v-if="showMessage" show>{{message}}</b-alert>

          <button type="button" class="btn btn-success" v-b-modal.anime-modal>Add anime</button>

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
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="primary">Reset</b-button>
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
      anime:[],
      addAnimeForm: {
        title: "",
        tags:[],
        finished: [],
      },
    };
  },

  message:"",

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

    addAnime(payLoad){
      const path = "http://localhost:5000/anime";
      axios.get(path, payLoad)
      .then((response)=>{
        this.getAnime();
        this.message = "Anime added";
        this.showMessage = true;
      })
      .catch((error) =>{
        console.error(error);
        this.getAnime();
      });
    },
    //initialize empty form
    initForm(){
      this.addAnimeForm.title = "";
      this.addAnimeForm.tags = [];
      this.addAnimeForm.finished = [];
    },

    //submit function
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addAnimeModal.hide();
      let finished = false;
      if (this.addAnimeForm.finished[0]) finished = true;
      const payload = {
        title: this.addAnimeForm.title,
        tags: this.addAnimeForm.tags,
        finished: this.addAnimeForm.finished
      };
      this.addAnime(payload);
      this.initForm();
    },

    onReset(e) {
      e.preventDefault();
      this.$refs.addAnimeModal.hide();
      this.initForm();
    }


  },
  created() {
    this.getAnime();

  }
}
</script>
