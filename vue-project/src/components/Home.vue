<template>
  <div class="container">
    <h2>Welcome to Banking Management System</h2>
    <br>
    
    <div class="form-group">
      Already have account?
      <router-link to="/login">
        <button type="submit" class="btn btn-large btn-success">Login</button>
      </router-link>
      <br>
      <br>
      Don't have account? 
      <router-link to="/register">
        <button type="submit" class="btn btn-large btn-primary">
          Register Here
        </button>
      </router-link>
    </div>
  </div>
</template> 