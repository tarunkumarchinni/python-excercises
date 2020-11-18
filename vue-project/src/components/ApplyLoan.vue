<template>
    <div class="loan">
        <h4>{{message}} as {{id}}</h4>
        <div>
            <form>
                    <label >Loan Type: </label>
                    <input type="text" v-model="applyLoan.loantype">
                    <br>
                    <label >Loan Amount: </label>
                    <input type="text" v-model="applyLoan.loanamount">
                    <br>
                    <label >Date: </label>
                    <input type="date" v-model="applyLoan.date">
                    <br>
                    <label >Rate of interest: </label>
                    <input type="text" v-model="applyLoan.rateofinterest">
                    <br>
                    <label >Duration of loan: </label>
                    <input type="text" v-model="applyLoan.durationofloan">
                    <br>
                    <br>
                    <button v-on:click.prevent="signupForm" v-on:click="isEditing =!isEditing">Apply</button>
                    <button  v-on:click.prevent="cancel" >Cancel</button>
            </form>
        </div>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            id: this.$route.params.username,
            message: "Hello i am from sign up",
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
            this.$http.post("http://127.0.0.1:5000/Loan",this.applyLoan)
            .then(response =>{
                console.log(response)
            }).catch(error=>{
                if(error.response.status==404){
                    this.errorMessage=error.response.data.output
                }
                alert(this.errorMessage)
                console.log(error.response)
            })
        },
        cancel:function(){
            console.log(this.isEditing)
        }
    },
    mounted:function(){
        console.log("this is the param")
        console.log(this.$route.params)
    }

}
</script>
<style scoped>
.loan {
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