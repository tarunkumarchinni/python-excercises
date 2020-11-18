<template>
    <div class="signup">
        <h4>{{message}}</h4>
        <div>
            <form >
                    <label >Name: </label>
                    <input type="text" v-model="register.name">
                    <br>
                    <label >Username: </label>
                    <input type="text" v-model="register.username">
                    <br>
                    <label >Password: </label>
                    <input type="password" v-model="register.password">
                    <br>
                    <label >Address: </label>
                    <input type="text" v-model="register.address">
                    <br>
                    <label >State: </label>
                    <input type="text" v-model="register.state">
                    <br>
                    <label >Country: </label>
                    <input type="text" v-model="register.country">
                    <br>
                    <label >Email: </label>
                    <input type="email" v-model="register.email">
                    <br>
                    <label >PAN id: </label>
                    <input type="text" v-model="register.pan">
                    <br>
                    <label >Date of Birth: </label>
                    <input type="date" v-model="register.DOB">
                    <br>
                    <label >Mobile: </label>
                    <input type="phone" v-model="register.contact">
                    <br>
                    <label >Account Type: </label>
                    <input type="text" v-model="register.accounttype">
                    <br>
                    <button v-on:click.prevent="signupForm" v-on:click="isEditing =!isEditing">Add</button>
                    <button  v-on:click.prevent="cancel" >Cancel</button>
            </form>
        </div>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            message: "Hello i am from sign up",
            isEditing: false,
            register:{
                name:'',
                username:'',
                password:'',
                address:'',
                state:'',
                country:'',
                email:'',
                pan:'',
                DOB:'',
                contact:'',
                accounttype:''
            }
        }
    },
    methods:{
        signupForm: function(){
            console.log(this.register)
            this.$http.post("http://127.0.0.1:5000/Account",this.register)
            .then(response =>{
                console.log(response)
            }).catch(error=>{
                console.log(error)
            })
        },
        cancel:function(){
            console.log(this.isEditing)
        }
    }
}
</script>
<style scoped>
.signup {
    /* position:absolute; */
    border: 1px solid red;
    width: 99.6%;
    height: 480px;
    padding: 1px;
    text-align: center;
    /* display: inline-table;
    height: 200px;
    float:right;
    z-index: auto;
    display: table-row; */
    /* width:980%;
    height:450px;
    background-color: #0d7963;
    float:right;
    flex-wrap: nowrap; */
}

</style>