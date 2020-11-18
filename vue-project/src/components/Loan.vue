<template>
    <div class="loandetails">

        <div class="loan"> 
             <h1>{{message}} </h1>
             <div>
                <button v-on:click="accountdetails(userid)">Apply Loan</button>
            </div>
            <div v-if="loans.length==0">
                <div>
                    you does not had any previous loans to display
                </div>
            </div>
            <div v-if="loans.length>0">
                <ol>
                    <li  v-for="loan in loans" v-bind:key="loan.id">{{loan.loantype}} as {{loan.loanamount}}
                        <button v-on:click="getLoan()">get details</button>
                        <button v-on:click="updateLoan(loan.username)">Edit</button>
                        <button v-on:click="deleteLoan(loan.username)">Delete</button>
                        <div v-if="isEditing==true">
                            {{loan.loantype}}, {{loan.loanamount}} ,{{loan.date}}, {{loan.rateofinterest}}, {{loan.durationofloan}}
                            {{isEditing}}
                        </div>
                        <div v-bind="isEditing==false"></div>
                    </li>
                </ol>
            </div>
            <div>
                <button v-on:click="applyLoan(userid)">Apply Loan</button>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            message: "Hello i am from Loan",
            userid: this.$route.params.username,
            isEditing: false,
            loans:Array
        }
    },
    mounted:function(){
            this.getLoans()
    },
    methods:{
        getLoans: function(){
            this.$http.get("http://127.0.0.1:5000/Loan/"+this.userid)
            .then(response =>{
                this.loans=response.data
                console.log(response)
                console.log(this.loans)

            }).catch(error=>{
                // console.log(this.loans)
                //  console.clear({{loan._id.$oid}});
                if(error.response.status==404){
                    this.loans=error.response.data
                }
                 console.log(this.loans.length)
                 console.log(this.loans)
            })
        },
        getLoan: function(){
            this.isEditing= true
        },
        accountdetails: function(){
            this.$router.push({
                path:'/AccountDetails/'+id,
                params:{username:id}
            })
        },
        updateLoan: function(id){
            console.log(id)
            console.log(this.$router)
            this.$router.push({
                path:'/edit-loan/'+id,
                params:{username:id}
            })
        },
        deleteLoan: function(id){
            this.$http.delete("http://127.0.0.1:5000/Loan/"+id)
            .then(response =>{ 
                console.log(response.data.output)
                this.message=response.data.output
                console.log(this.loans)
                this.getLoans()

            }).catch(error=>{
                // console.log(this.loans)
                //  console.clear({{loan._id.$oid}});
                if(error.response.status==404){
                    this.loans=error.response.data
                }
                 console.log(this.loans.length)
                 console.log(this.loans)
            })
        },
        applyLoan: function(id){
            console.log(id)
            console.log(this.$router)
            this.$router.push({
                path:'/add-loan/'+id,
                params:{username:id}
            })
        }
    }
}
</script>
<style scoped>
.loandetails {
    border: 1px solid red;
    width: 99.6%;
    height: 480px;
    padding: 1px;
    text-align: center;
}
.loan {
    border: 1px solid red;
    align-self: center;
    width: 50%;
    height: 300px;
    padding: 1px;
    text-align: center;
}

</style>