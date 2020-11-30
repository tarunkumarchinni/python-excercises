<template>
    <div class="container">
        <h4>{{message}}</h4>
        <div class="well">
            <form>
                <div class="form-group">
                    <label >Loan Type: </label>
                    <input class="form-control" type="text" v-model="applyLoan.loantype">
                </div>
                <div class="form-group">
                    <label >Loan Amount: </label>
                    <input class="form-control" type="text" v-model="applyLoan.loanamount">
                </div>
                <div class="form-group">
                    <label >Date: </label>
                    <input class="form-control" type="date" v-model="applyLoan.date">
                </div>
                <div class="form-group">
                    <label >Rate of interest: </label>
                    <input class="form-control" type="text" v-model="applyLoan.rateofinterest">
                </div>
                <div class="form-group">
                    <label >Duration of loan: </label>
                    <input class="form-control" type="text" v-model="applyLoan.durationofloan">
                </div>
                    <br>
                    <button class="btn btn-large btn-block btn-success full-width" v-on:click.prevent="signupForm" v-on:click="isEditing =!isEditing">Apply</button>
                   <br>
                    Want to cancel? Click
                    <button class="btn btn-large btn-danger full-width"  v-on:click.prevent="cancel" >Cancel</button>
                    <br>
            </form>
        </div>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            id: this.$route.params.username,
            message: "Apply Loan",
            errorMessage:'',
            applyLoan:{
                loantype:'',
                username:this.$route.params.username,
                loanamount:'',
                date:'',
                rateofinterest:'',
                durationofloan:''
            }
        }
    },
    methods:{
        signupForm: function(){
            console.log(this.applyLoan)
            this.$http.post("https://gs33tlvm34.execute-api.us-east-2.amazonaws.com/Dev/loan",this.applyLoan)
            .then(response =>{
                console.log("hey i am from responce welcome me")
                console.log(response)
                this.$router.push({
                    path: "/show-loans/" + this.id,

                    params: { username: this.id },
                });
            }).catch(error=>{
                console.log(error.response)
                if(error.response.status==404){
                    this.errorMessage=error.response.data.output
                }
                alert(this.errorMessage)
                console.log(error.response)
            })
        },
        cancel:function(){
            console.log(this.isEditing)
                this.$router.push({
                    path: "/show-loans/" + this.id,

                    params: { username: this.id },
                });
        }
    },
    mounted:function(){
        console.log("this is the param from apply loan")
        console.log(this.$route.params)
    }

}
</script>
<style scoped>

</style>