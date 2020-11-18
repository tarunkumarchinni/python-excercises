<template>

    <div>

       <ol>

           <li>

               <router-link to='/' exact>Home</router-link>

           </li>

             <li>

               <router-link to='/signup' exact>Signup</router-link>

           </li>

             <li>

               <router-link to='/show-loans' exact>Show Loans</router-link>

           </li>
           <li>

               <router-link to='/add-loan/:username' exact>apply Loans</router-link>

           </li>

       </ol>

    </div>

</template>



<script>

export default {

   

}

</script>



<style scoped>



ol{

  list-style-type: none;

  display: flex;

}

li{

  margin-right: 20px;

}



</style>