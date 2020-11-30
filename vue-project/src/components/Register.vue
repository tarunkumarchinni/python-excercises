<template>
  <div class="container">
    <form @submit.prevent="handleSubmit">
      <div class="well">
        <h4>Registration</h4>
          <p v-if="isEditing==true" style="color:red;">{{message}}</p>
        <div class="form-group">
          <label class="pull-left"> Name </label>

          <input
            type="text"
            class="form-control"
            placeholder="Name"
            v-model="User.name"
            :class="{ 'is-invalid': submitted && $v.User.name.$error }"
          />

          <div
            v-if="submitted && !$v.User.name.required" style="color:red;"
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
            v-model="User.username"
            :class="{ 'is-invalid': submitted && $v.User.username.$error }"
          />

          <div
            v-if="submitted && !$v.User.username.required"
            class="invalid-feedback" style="color:red;"
          >
            username is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Password </label>

          <input
            type="password"
            class="form-control"
            placeholder="Password "
            v-model="User.password"
            :class="{ 'is-invalid': submitted && $v.User.password.$error }"
          />

          <div
            v-if="submitted && !$v.User.password.required"
            class="invalid-feedback" style="color:red;"
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
            v-model="User.address"
            :class="{ 'is-invalid': submitted && $v.User.address.$error }"
          />

          <div
            v-if="submitted && !$v.User.address.required"
            class="invalid-feedback" style="color:red;"
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
            v-model="User.state"
            :class="{ 'is-invalid': submitted && $v.User.state.$error }"
          />

          <div
            v-if="submitted && !$v.User.state.required"
            class="invalid-feedback" style="color:red;"
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
            v-model="User.country"
            :class="{ 'is-invalid': submitted && $v.User.country.$error }"
          />

          <div
            v-if="submitted && !$v.User.country.required"
            class="invalid-feedback" style="color:red;"
          >
            Country is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Email </label>

          <input
            type="email"
            class="form-control"
            placeholder="Email "
            v-model="User.email"
            :class="{ 'is-invalid': submitted && $v.User.email.$error }"
          />

          <div
            v-if="submitted && !$v.User.email.required"
            class="invalid-feedback" style="color:red;"
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
            v-model="User.pan"
            :class="{ 'is-invalid': submitted && $v.User.pan.$error }"
          />

          <div
            v-if="submitted && !$v.User.pan.required"
            class="invalid-feedback" style="color:red;"
          >
            PAN is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Contact </label>

          <input
            type="number"
            class="form-control"
            placeholder="Contact "
            v-model="User.contact"
            :class="{ 'is-invalid': submitted && $v.User.contact.$error }"
          />

          <div
            v-if="submitted && !$v.User.contact.required"
            class="invalid-feedback" style="color:red;"
          >
            Contact is required
          </div>
        </div>

        <div class="form-group">
          <label class="pull-left"> Date of birth </label>

          <input
            type="date"
            class="form-control"
            placeholder="Date of birth "
            v-model="User.dob"
            :class="{ 'is-invalid': submitted && $v.User.dob.$error }"
          />

          <div
            v-if="submitted && !$v.User.dob.required"
            class="invalid-feedback" style="color:red;"
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
            v-model="User.account_type"
            :class="{ 'is-invalid': submitted && $v.User.account_type.$error }"
          />

          <div
            v-if="submitted && !$v.User.account_type.required"
            class="invalid-feedback" style="color:red;"
          >
            Account type is required
          </div>
        </div>
      </div>

      <button
        type="submit"
        class="btn btn-large btn-block btn-success full-width"
      >
        Submit
      </button>
      <br>
        Want to cancel? Click 
      <router-link to="/">
        <button class="btn btn-large  btn-danger full-width">
          Cancel
        </button>
      </router-link>
      <br><br><br><br><br>
    </form>
  </div>
</template>



<script>
// import router from "vue-router";

import axios from "axios";

import { required } from "vuelidate/lib/validators";

export default {
  data() {
    return {
      message:'',
      isEditing:false,
      User: {
        name: "",

        username: "",

        password: "",

        address: "",

        state: "",

        country: "",

        email: "",

        pan: "",

        contact: "",

        dob: "",

        account_type: "",
      },

      submitted: false,
    };
  },

  validations: {
    User: {
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

      account_type: { required },
    },
  },

  methods: {
    handleSubmit() {
      this.submitted = true;

      // stop here if form is invalid

      this.$v.$touch();

      if (this.$v.$invalid) {
        return;
      }

      let newUser = {
        name: this.User.name,

        username: this.User.username,

        password: this.User.password,

        address: this.User.address,

        state: this.User.state,

        country: this.User.country,

        email: this.User.email,

        pan: this.User.pan,

        contact: this.User.contact,

        DOB: this.User.dob,

        accounttype: this.User.account_type,
      };

      console.log(newUser);

      // const isvalid = this.validations;

      // if (isvalid) {

      axios

        .post("https://gs33tlvm34.execute-api.us-east-2.amazonaws.com/Dev/account", newUser)

        .then((response) => {
          console.log(response);
          // router.push({ name: 'Login' })
          console.log(response.data.output)
          if(response.data.output){
                  this.isEditing=true
                  this.message="Username already exists,So please provide another..."
                  console.log("User already exists...!");
          }
          else{
              this.$router.push({
                path: "/login",
              })
          }
        })
         .catch((error) => {
              console.log(error.response.data);
              
            });
    },

    // },
  },
};
</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->

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