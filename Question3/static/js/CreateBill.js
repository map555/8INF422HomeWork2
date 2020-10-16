

$(document).ready(function (){



                $("#bill_form").submit(function (e){

                e.preventDefault();

                //serialize form
                var serForm=$(this).serialize();

                $.ajax({
                    type:'POST',
                    url: "{% url 'post_bill' %}",
                    data: serForm,
                    success:function (response){
                        //reset form
                        $("#bill_form")[0].reset();

                        alert("SUCCESS\nBill added with success.")
                        console.log("Bill added")

                    },

                    /*
                    if the the request didn't work
                     */
                    error:function (response){

                        if(
                            ((response.statusCode()==204)||(response.statusCode()==206))
                         &&  !((response.statusCode()==204)&&(response.statusCode()==206))
                        ){
                            alert("ERROR\nThe request has been rejected.\n" +
                                "The car ID may be invalid or the selected car is already sold.")

                            console.log("Rejected request")
                        }
                        else{
                            alert("ERROR\n Something wrong happened.")
                            console.log("Something wrong happened")
                            console.log(response)
                        }

                    }
                })

            })


    });

