<template>
    <div class="Container">

        <div class="well"> 
            <div>
                <button  class="btn btn-large btn-primary full-width" style="float: right;" v-on:click="accountdetails(userid)">Account Details</button>
            
                <button  class="btn btn-large btn-success full-width" style="float:left;" v-on:click="applyLoan(userid)">Apply Loan</button>
            </div>
             <h4>{{message}} </h4>
             
            <div v-if="loans.length==0">
                <div>
                    You doesn't have any previous loans to display!!!
                </div>
            </div>
            <br>
            <div v-if="loans.length>0">
                <table border="1px">
                    <tr>

                                <th>Loan Type</th>
                                <th>Loan Amount</th>
                                <th colspan="3" style="text-align:center">Actions</th>
                            </tr>
                
                    <tr  v-for="loan in loans" v-bind:key="loan.id">
                        
                            <!-- <tr> -->

                                <td>{{loan.loantype}}</td>
                                <td>{{loan.loanamount}}</td>
                                <td><button  class=" btn-block btn-success " v-on:click="getLoan(loan._id.$oid)">Details</button></td>
                                <td><button class=" btn-block btn-primary " v-on:click="updateLoan(loan._id.$oid)">Edit</button></td>
                                <td> <button class=" btn-block btn-danger " v-on:click="deleteLoan(loan._id.$oid)">Delete</button></td>
                            <!-- </tr> -->
                        
                        
                        <div v-if="isEditing==true && keyid==loan._id.$oid">
                            <table class="table table-striped">
                                <tr>
                                <th>Loan Type</th>
                                <td> {{loan.loantype}}</td>
                                </tr>
                                <tr>
                                <th>Loan Amount</th>
                                <td>{{loan.loanamount}} </td>
                                </tr>
                                <tr>
                                <th>Date</th>
                                <td>{{loan.date}}</td>
                                </tr>
                                <tr>
                                <th>Rate of Interest</th>
                                <td>{{loan.rateofinterest}}</td>
                                </tr>
                                <tr>
                                <th>Duration</th>
                                <td>{{loan.durationofloan}}</td>
                                </tr>
                            </table>
                        
                        </div>
                        <div v-bind="isEditing==false"></div>
                    </tr>
                
                </table>
            </div>
            
        </div>
    </div>
</template>
<script>
export default {
    data: function(){
        return {
            message: " Loan Details",
            userid: this.$route.params.username,
            isEditing: false,
            loans:Array,
            keyid:''
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
        getLoan: function(id){
            this.isEditing= !this.isEditing
            console.log(this.loans.length)
            this.keyid=id
        },
        accountdetails: function(id){
            this.$router.push({
                path:'/AccountDetails/'+id,
                params:{username:id}
            })
        },
        updateLoan: function(id){
            console.log("object id getting here")
            console.log(id)
            console.log(this.$router)
            this.$router.push({
                path:'/edit-loan/'+id,
                params:{username:id}
            })
        },
        deleteLoan: function(id){
            this.$http.delete("http://127.0.0.1:5000/loans/user/"+id)
            .then(response =>{ 
                console.log(response.data.output)
                alert(response.data.output)
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
tr:nth-child(even) {
  background-color: #f2f2f2;
}
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>