<template>
    <div class="container">
        <h4>{{message}}</h4>
        <div class="well">
            <form>
                <div class="form-group">
                    <label >Name: </label>
                    <input class="form-control" type="text" v-model="editAccount.name">
                    </div>
                    
                    <!-- <label >Username </label>
                    <input type="text" v-model="editAccount.username">
                    <br> -->
                    <div class="form-group">
                    <label >Password: </label>
                    <input class="form-control" type="text" v-model="editAccount.password">
                    </div>
                    
                    <div class="form-group">
                    <label >Address: </label>
                    <input class="form-control" type="text" v-model="editAccount.address">
                    </div>
                   
                    <div class="form-group">
                    <label >State: </label>
                    <input class="form-control" type="text" v-model="editAccount.state">
                    </div>
                    
                    <div class="form-group">
                    <label >Country: </label>
                    <input class="form-control" type="text" v-model="editAccount.country">
                    </div>
                    
                    <div class="form-group">
                    <label >Email: </label>
                    <input class="form-control" type="email" v-model="editAccount.email">
                    </div>
                    
                    <div class="form-group">
                    <label >PAN: </label>
                    <input class="form-control" type="text" v-model="editAccount.pan">
                    </div>
                    
                    <div class="form-group">
                    <label >Contact: </label>
                    <input class="form-control" type="number" v-model="editAccount.contact">
                    </div>
                    
                    <div class="form-group">
                    <label >Date of birth:</label> 
                    <input class="form-control" type="date" v-model="editAccount.DOB">
                    </div>
                    
                    <div class="form-group">
                    <label >Account Type: </label>
                    <input class="form-control" type="text" v-model="editAccount.accounttype">
                    </div>
                    
                    <br>
                    <button class="btn btn-large btn-block btn-success full-width" v-on:click.prevent="editAccountForm">Update</button>
                    <br>
                    Want to cancel?
                    <button class="btn btn-large btn-danger" v-on:click.prevent="cancel" >Cancel</button>
            </form>
        </div>
    </div>
</template>
<script>
import axios from "axios";
export default {
    data: function(){
        return {
            id: this.$route.params.username,
            message: "Edit Account Details",
            errorMessage:'',
            editAccount:{
                name:'',
                username:this.$route.params.username,
                password:'',
                address:'',
                state:'',
                country:'',
                email:'',
                pan:'',
                contact:'',
                DOB:'',
                accounttype:''
            }
        }
    },
    mounted: function(){
        this.getAccount()
    },
    methods:{
        getAccount: function(){
            console.log(this.editAccount.username)
            axios.get("http://127.0.0.1:5000/Account/"+this.editAccount.username)
            .then(response =>{
                this.editAccount=response.data[0]
                console.log(this.editAccount)
            }).catch(error=>{
                
                if(error.response.status==404){
                    this.accounts=error.response.data
                }
                
            })
        },
        editAccountForm: function(){
            console.log(this.id)
            axios.put("http://127.0.0.1:5000/Account/"+this.id,this.editAccount)
            .then(response =>{
                console.log(response)
                this.$router.push({
                    path: "/AccountDetails/"+this.id,
                    params:{username:this.id}
                }); 
            }).catch(error=>{
                if(error.response.status==404){
                    this.errorMessage=error.response.data.output
                }
                console.log(error.response)
            })
        },
         cancel:function(){
            console.log(this.isEditing)
            this.$router.push({
                    path: "/AccountDetails/"+this.id,
                    params:{username:this.id}
                });
        }
    },
}
</script>
<style scoped>

</style>