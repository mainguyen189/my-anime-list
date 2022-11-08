<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Miaow",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getResponse() {
      const path = "http://localhost:5000/miaow";
      axios
        .get(path)
        .then((response) => {
          console.log(response.data);
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
