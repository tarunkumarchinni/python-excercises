<template>
  <div class="container">
    <form @submit.prevent="handleSubmit()">
      <div class="well">
        <h4>Registration</h4>

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
            v-if="submitted && !$v.User.name.required"
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
            v-model="User.password"
            :class="{ 'is-invalid': submitted && $v.User.password.$error }"
          />

          <div
            v-if="submitted && !$v.User.password.required"
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
            v-model="User.address"
            :class="{ 'is-invalid': submitted && $v.User.address.$error }"
          />

          <div
            v-if="submitted && !$v.User.address.required"
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
            v-model="User.state"
            :class="{ 'is-invalid': submitted && $v.User.state.$error }"
          />

          <div
            v-if="submitted && !$v.User.state.required"
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
            v-model="User.country"
            :class="{ 'is-invalid': submitted && $v.User.country.$error }"
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
            v-model="User.email"
            :class="{ 'is-invalid': submitted && $v.User.email.$error }"
          />

          <div
            v-if="submitted && !$v.User.email.required"
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
            v-model="User.pan"
            :class="{ 'is-invalid': submitted && $v.User.pan.$error }"
          />

          <div
            v-if="submitted && !$v.User.pan.required"
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
            v-model="User.contact"
            :class="{ 'is-invalid': submitted && $v.User.contact.$error }"
          />

          <div
            v-if="submitted && !$v.User.contact.required"
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
            v-model="User.dob"
            :class="{ 'is-invalid': submitted && $v.User.dob.$error }"
          />

          <div
            v-if="submitted && !$v.User.dob.required"
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
            v-model="User.account_type"
            :class="{ 'is-invalid': submitted && $v.User.account_type.$error }"
          />

          <div
            v-if="submitted && !$v.User.account_type.required"
            class="invalid-feedback"
          >
            Account type is required
          </div>
        </div>
      </div>

      <button
        type="submit"
        class="btn btn-large btn-block btn-primary full-width"
      >
        Submit
      </button>

      <router-link to="/">
        <button class="btn btn-large btn-block btn-success full-width">
          Cancel
        </button>
      </router-link>
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

        .post("http://127.0.0.1:5000/Account", newUser)

        .then((response) => {
          console.log(response);
          // router.push({ name: 'Login' })
          this.$router
            .push({
              path: "/login",
            })

            .catch((error) => {
              console.log(error.response);

              console.log("user already existssss");
            });
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