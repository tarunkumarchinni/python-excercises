<template>
    <div class="loan">
        <h4>{{message}} as {{id}}</h4>
        <div>
            <form>
                    <label >Loan Type: </label>
                    <input type="text" v-model="editLoan.loantype">
                    <br>
                    <label >Loan Amount: </label>
                    <input type="text" v-model="editLoan.loanamount">
                    <br>
                    <label >Date: </label>
                    <input type="date" v-model="editLoan.date">
                    <br>
                    <label >Rate of interest: </label>
                    <input type="text" v-model="editLoan.rateofinterest">
                    <br>
                    <label >Duration of loan: </label>
                    <input type="text" v-model="editLoan.durationofloan">
                    <br>
                    <br>
                    <button v-on:click.prevent="editLoanForm" v-on:click="isEditing =!isEditing">Apply</button>
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
            message: "Hello i am from edit loan",
            errorMessage:'',
            editLoan:{
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
            this.$http.get("http://127.0.0.1:5000/Loan/"+this.id)
            .then(response =>{
                this.editLoan=response.data[0]
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
            this.$http.put("http://127.0.0.1:5000/Loan/"+this.id,this.editLoan)
            .then(response =>{
                console.log(response)
                this.$router.push({
                    path: "/show-loans/"+this.id,
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
                    path: "/show-loans/"+this.id,
                    params:{username:this.id}
                });
        }
    },
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