<template>
  <div class="container">
    <form >
      <div class="well">
        <h4>Edit Account Details</h4>

        <div class="form-group">
          <label class="pull-left"> Name </label>

          <input
            type="text"
            class="form-control"
            placeholder="Name"
            v-model="editAccount.name"
            :class="{ 'is-invalid': submitted && $v.editAccount.name.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.name.required"
            class="invalid-feedback"
          >
            Name is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Username </label>

          <input
            type="text"
            class="form-control"
            placeholder="Username"
            v-model="editAccount.username"
            :class="{ 'is-invalid': submitted && $v.editAccount.username.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.username.required"
            class="invalid-feedback"
          >
            username is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Password </label>

          <input
            type="text"
            class="form-control"
            placeholder="Password "
            v-model="editAccount.password"
            :class="{ 'is-invalid': submitted && $v.editAccount.password.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.password.required"
            class="invalid-feedback"
          >
            Password is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Address </label>

          <input
            type="text"
            class="form-control"
            placeholder="Address "
            v-model="editAccount.address"
            :class="{ 'is-invalid': submitted && $v.editAccount.address.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.address.required"
            class="invalid-feedback"
          >
            Address is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> State </label>

          <input
            type="text"
            class="form-control"
            placeholder="State "
            v-model="editAccount.state"
            :class="{ 'is-invalid': submitted && $v.editAccount.state.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.state.required"
            class="invalid-feedback"
          >
            State is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Country </label>

          <input
            type="text"
            class="form-control"
            placeholder="Country "
            v-model="editAccount.country"
            :class="{ 'is-invalid': submitted && $v.editAccount.country.$error }"
          />

          <div
            v-if="submitted && !$v.User.country.required"
            class="invalid-feedback"
          >
            Country is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Email </label>

          <input
            type="text"
            class="form-control"
            placeholder="Email "
            v-model="editAccount.email"
            :class="{ 'is-invalid': submitted && $v.editAccount.email.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.email.required"
            class="invalid-feedback"
          >
            email is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> PAN </label>

          <input
            type="text"
            class="form-control"
            placeholder="PAN number "
            v-model="editAccount.pan"
            :class="{ 'is-invalid': submitted && $v.editAccount.pan.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.pan.required"
            class="invalid-feedback"
          >
            PAN is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Contact </label>

          <input
            type="text"
            class="form-control"
            placeholder="Contact "
            v-model="editAccount.contact"
            :class="{ 'is-invalid': submitted && $v.editAccount.contact.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.contact.required"
            class="invalid-feedback"
          >
            Contact is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Date of birth </label>

          <input
            type="text"
            class="form-control"
            placeholder="Date of birth "
            v-model="editAccount.DOB"
            :class="{ 'is-invalid': submitted && $v.editAccount.DOB.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.DOB.required"
            class="invalid-feedback"
          >
            Date of birth is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Account Type </label>

          <input
            type="text"
            class="form-control"
            placeholder="Account type "
            v-model="editAccount.accounttype"
            :class="{ 'is-invalid': submitted && $v.editAccount.accounttype.$error }"
          />

          <div
            v-if="submitted && !$v.editAccount.accounttype.required"
            class="invalid-feedback"
          >
            Account type is required
          </div>
        </div>
      </div>

       <button class="btn btn-large btn-block btn-primary full-width" v-on:click.prevent="editAccountForm">Apply</button>

        <button class="btn btn-large btn-block btn-success full-width" v-on:click.prevent="cancel">Cancel</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { required } from "vuelidate/lib/validators";

export default {
  data: function () {
    return {
      id: this.$route.params.username,

      message: " edit Account",

      errorMessage: "",

      editAccount: {
        name: "",

        username: this.$route.params.username,

        password: "",

        address: "",

        state: "",

        country: "",

        email: "",

        pan: "",

        contact: "",

        DOB: "",

        accounttype: "",
      },
    };
  },
  validations: {
    editAccount: {
      name: { required },

      username: { required },

      password: { required },

      address: { required },

      state: { required },

      country: { required },

      email: { required },

      pan: { required },

      contact: { required },

      dob: { required },

      accounttype: { required },
    },
  },

  mounted: function () {
    this.getAccount();
  },

  methods: {
    getAccount: function () {
      console.log(this.editAccount.username);

      axios
        .get("http://127.0.0.1:5000/Account/" + this.editAccount.username)

        .then((response) => {
          this.editAccount = response.data[0];

          console.log(this.editAccount);
        })
        .catch((error) => {
          if (error.response.status == 404) {
            this.accounts = error.response.data;
          }
        });
    },

    editAccountForm: function () {
      console.log(this.id);
      this.submitted = true;
      // stop here if form is invalid
      this.$v.$touch();
      console.log("before invalid")

     

      console.log(this.editAccount);
      axios
        .put("http://127.0.0.1:5000/Account/" + this.id, this.editAccount)

        .then((response) => {
          console.log(response);
          this.$router.push({
                    path: "/AccountDetails/"+this.id,
                    params:{username:this.id}
                }); 
        })
        .catch((error) => {
          if (error.response.status == 404) {
            this.errorMessage = error.response.data.output;
          }

          console.log(error.response);
        });
    },

    cancel: function () {
      console.log(this.isEditing);
      this.$router.push({
                    path: "/AccountDetails/"+this.id,
                    params:{username:this.id}
        }); 
    },
  },
};
</script>

<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;

  padding: 0;
}

li {
  display: inline-block;

  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>