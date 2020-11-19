<template>
    <div class="header">
        <h1>{{message}}</h1>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            message: "Bank Management System"
        }
    }
    
}
</script>
<style scoped>
.header {
  /* position: fixed;
  left:0;
  top:0;
  height: 8%;
  width: 100%;
  text-align: center;
  background: #1abc9c;
  color: white;
  font-size: 10px; */
  
    /* position: absolute;
    margin:0 auto; */
    /* border:1px solid rgb(160, 27, 27); */
    width: 100%;
    height: 70px;
    padding: 1px;
    text-align: center;
    /* display: inline-table;
    height:40px;
    margin-bottom:15px; */
     background-color:#84b9ce; 
}
  /* height:140px;
    margin-bottom:15px;
    background-color:#0d7963; */


</style>