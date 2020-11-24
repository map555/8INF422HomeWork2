


        $(document).ready(function (){

                    $("#bill_form").submit(function (e){

                    e.preventDefault();

                    //serialize form
                    var serForm=$(this).serialize();


                    $.ajax({
                        type:'POST',
                        url: "/ajax/create_bill",
                        data: serForm,
                        success:function (response){
                            //reset form
                            $("#bill_form")[0].reset();
                            console.log(response)

                            if(response.requestsuccess==true){
                                 alert("SUCCESS\nBill added with success.")
                                 console.log("Bill added")
                            }
                            else
                            {

                                //the car was already sold or the car id doesn't exist

                                     alert("ERROR\nThe request has been rejected.\n" +
                                    "The car ID may be invalid or the selected car is already sold.")

                                    console.log("Rejected request")

                            }
                        },

                        /*
                        if the the request didn't work
                        */
                        error:function (response)
                        {

                                alert("ERROR\n Something wrong happened.")
                                console.log("Something wrong happened")
                                console.log(response)

                        }
                    })

            })


        });
