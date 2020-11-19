<template>
  <div class="container">
    <button
        class="btn btn-large btn-success full-width" style="float: right;"
        @click="loansdetails(userid)"
      >
        Show Loans
      </button>
    <div v-for="accounts in accounts" v-bind:key="accounts.id">
      <h4>{{ message }}</h4>
      
      <hr />

      <table class="table table-striped">
        <tr>
          <th>Name</th>

          <td>{{ accounts.name }}</td>
        </tr>

        <tr>
          <th>Username</th>

          <td>{{ accounts.username }}</td>
        </tr>

        <tr>
          <th>Password</th>

          <td>{{ accounts.password }}</td>
        </tr>

        <tr>
          <th>Email</th>

          <td>{{ accounts.email }}</td>
        </tr>

        <tr>
          <th>Contact</th>

          <td>{{ accounts.contact }}</td>
        </tr>

        <tr>
          <th>Address</th>

          <td>{{ accounts.address }}</td>
        </tr>

        <tr>
          <th>Date of birth</th>

          <td>{{ accounts.DOB }}</td>
        </tr>

        <tr>
          <th>State</th>

          <td>{{ accounts.state }}</td>
        </tr>

        <tr>
          <th>Country</th>

          <td>{{ accounts.country }}</td>
        </tr>

        <tr>
          <th>PAN</th>

          <td>{{ accounts.pan }}</td>
        </tr>

        <tr>
          <th>Account Type</th>

          <td>{{ accounts.accounttype }}</td>
        </tr>
      </table>

      <button
        class="btn btn-large btn-block btn-primary full-width"
        @click="updateAccount(userid)"
      >
        Edit
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function () {
    return {
      message: "Account details",

      userid: this.$route.params.username,

      isEditing: false,

      accounts: Array,
    };
  },

  mounted: function () {
    this.getAccounts();
  },

  methods: {
    updateAccount: function (id) {
      console.log(id);

      console.log(this.$router);

      this.$router.push({
        path: "/UpdateDetails/" + id,

        params: { username: id },
      });
    },
    loansdetails: function(id){
        console.log(id);

      console.log(this.$router);

      this.$router.push({
        path: "/show-loans/" + id,

        params: { username: id },
      });
    },
    getAccounts: function () {
      axios

        .get("http://127.0.0.1:5000/Account/" + this.userid)

        .then((response) => {
          this.accounts = response.data;

          console.log(response);

          console.log(this.accounts);

          console.log(status);
        })

        .catch((error) => {
          if (error.response.status == 404) {
            this.accounts = error.response.data;
          }

          console.log(this.accounts.length);

          console.log(this.accounts);
        });
    },
  },
};
</script>

<style scoped>
tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>