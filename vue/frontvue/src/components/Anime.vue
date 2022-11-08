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
                    <th scope="col">Aired date</th>
                    <th scope="col">Watch status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td></td>
                    <td>
                        <div class="btn-group" role="group"></div>

                    </td>
                </tr><th scope="col">Title</th>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
