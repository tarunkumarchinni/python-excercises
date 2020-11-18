<template>
    <div class="header">
        <p>{{message}}</p>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            message: "Hello i am header"
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
    border:1px solid rgb(160, 27, 27);
    width: 99.6%;
    height: 40px;
    padding: 1px;
    text-align: center;
    /* display: inline-table;
    height:40px;
    margin-bottom:15px; */
    /* background-color:#0d7963; */
}
  /* height:140px;
    margin-bottom:15px;
    background-color:#0d7963; */


</style>