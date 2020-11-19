<template>
  <!-- <div id="app">-->
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <!-- </div>  -->
 <div id="app">
  
<!-- <b-container fluid>
<b-row style="height:50px;background-color:lavender">
<b-col cols="12" sm="8" md="8" lg="8"> Header 8</b-col>
<b-col>Header 4</b-col>
</b-row>
  
<b-row style="height: 509px;">
<b-col cols="3"><navbar></navbar></b-col>
<b-col> -->
<!-- <router-view></router-view> -->
<Header></Header>
<!-- <navbar></navbar> -->

<hr>
<router-view></router-view>
<Footer></Footer>
<!-- </b-col>
</b-row>
  
<b-row class="footer">
<b-col>
<div>
            Fotter 12
</div>
</b-col>
</b-row>
</b-container> -->
<!-- <SideMenu></SideMenu>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
</div>


</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import Header from './components/Header.vue'
// import MyNav from "./components/Navigation"
import Header from "./components/Header"
import Footer from "./components/Footer"

export default {
  // name: 'App'
  name: 'App',
  components: {
    // HelloWorld,
    // navbar: MyNav,

    // Header
    Header: Header,
    //Footer
    Footer: Footer
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
div[class="col"] {
/* background-color : bisque; */
border: 1px solid black;
}
.footer {
position: fixed;
height: 50px;
background-color: beige;
bottom: 0px;
left: 0px;
right: 0px;
margin-bottom: 0px;
}

</style>
