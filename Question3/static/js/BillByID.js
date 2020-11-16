$(document).ready(function (){

                  //Get query result on submit
            $('#send_bill_id').on('click', function(e){


                e.preventDefault();
                var bill_id=document.getElementById("bill_id").value;

                $.ajax({
                        type: "GET",
                        url:"/ajax/get_bill_info_by_id",
                        data: {bill_id:bill_id},
                        success:function(response){



                            console.log("It works")
                            $("#resulttable tbody").html(`<tr>
                                <td id="IDResult">${response.bill_info.id}</td>
                                <td id="ClientResult">${response.bill_info.clientName}</td>
                                <td id="CarResult">${response.bill_info.carPrice}</td>
                                </tr>`)

                        },
                        error : function(response){
                            console.log("It's not working")
                            console.log(response)
                         }
            })
            })
        });
