<template>
    <div class="footer">
        <p>{{message}}</p>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            message: "@Footer...."
        }
    }
}
</script>
<style scoped>
.footer {
  /* position: absolute;
  left: 0;
  bottom: 0;
  width: 98.5%;
  height: 7%;
  display: flex;
  background-color: rgb(92, 92, 92);
  color: white;
  text-align: center;  */
    /* position: fixed; */
    border: 1px solid red;
    /* box-sizing: border-box; */
    width: 99.6%;
    height: 40px;
    padding: 1px;
    background-color: rgb(92, 92, 92);
    color: white;
    text-align: center;
    /* display: flex;
    height:50px;
    margin-top:540px;
    background-color:#0d7963; */
}
</style>