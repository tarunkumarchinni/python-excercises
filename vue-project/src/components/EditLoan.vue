<template>
    <div class="container">
         <router-link to="/login">
                    <button class="btn btn-large  full-width" style="float: right;">
                    logout
                    </button>
        </router-link>
        <h4>{{message}}</h4>
        <div class="well">
            <form>
                <div class="form-group">
                    <label >Loan Type: </label>
                    <input class="form-control" type="text" v-model="editLoan.loantype">
                </div>
                <div class="form-group">
                    <label >Loan Amount: </label>
                    <input class="form-control" type="text" v-model="editLoan.loanamount">
                </div>
                <div class="form-group">
                    <label >Date: </label>
                    <input class="form-control" type="date" v-model="editLoan.date">
                </div>
                <div class="form-group">
                    <label >Rate of interest: </label>
                    <input class="form-control" type="text" v-model="editLoan.rateofinterest">
                </div>
                <div class="form-group">
                    <label >Duration of loan: </label>
                    <input class="form-control" type="text" v-model="editLoan.durationofloan">
                </div>
                    <br>
                    <button class="btn btn-large  btn-success full-width" v-on:click.prevent="editLoanForm" v-on:click="isEditing =!isEditing">Update</button>
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <button class="btn btn-large btn-danger full-width"  v-on:click.prevent="cancel" >Cancel</button>
            </form>
        </div>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            id: this.$route.params.username,
            message: "Update Loan Details",
            errorMessage:'',
            editLoan:{
                id: this.$route.params.id,
                loantype:'',
                username:this.$route.params.username,
                loanamount:'',
                date:'',
                rateofinterest:'',
                durationofloan:''
            }
        }
    },
    mounted: function(){
        this.getLoan()
    },
    methods:{
        getLoan: function(){
            
            this.$http.get("https://gs33tlvm34.execute-api.us-east-2.amazonaws.com/Dev/loan/"+this.id)
            .then(response =>{
                console.log("edit response here")
                console.log(response)
                this.editLoan=response.data
                console.log(this.editLoan)
            }).catch(error=>{
                // console.log(this.loans)
                //  console.clear({{loan._id.$oid}});
                if(error.response.status==404){
                    this.loans=error.response.data
                }
                //  console.log(this.loans.length)
                //  console.log(this.loans)
            })
        },
        editLoanForm: function(){
            console.log(this.id)
            this.$http.put("https://gs33tlvm34.execute-api.us-east-2.amazonaws.com/Dev/loan/"+this.id,this.editLoan)
            .then(response =>{
                console.log(response)
                this.$router.push({
                    path: "/show-loans/"+this.editLoan.username,
                    params:{username:this.editLoan.username}
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
                    path: "/show-loans/"+this.editLoan.username,
                    params:{username:this.editLoan.username}
                });
        }
    },
}
</script>
<style scoped>

</style>