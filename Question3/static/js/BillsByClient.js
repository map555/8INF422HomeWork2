$(document).ready(function (){



                  //Get query result on submit
            $("#send_client_name").on('click', function(e){


                e.preventDefault();

                var client_name=document.getElementById("client_name").value;

                console.log(client_name)
                $.ajax({
                        type: "GET",
                        url:"/ajax/BillsByClient",
                        data: {client_name:client_name},
                        success:function(response){

                            console.log(response.bills)

                            console.log("It works")

                            //change result title
                            var resultTitle=document.getElementById("ResultTitle")
                            resultTitle.innerText="Result for: "+client_name

                            //empty table and refill it with new content
                            EmptyTBody("result_tbody")
                            FillTBody("result_tbody",response.bills)

                        },
                        error : function(response){
                            console.log("It's not working");
                            console.log(response);
                         }
            })
            })
        });

//empty table body
function EmptyTBody(ID){
    var tbody=document.getElementById(ID);

    while(tbody.firstChild){
        tbody.removeChild(tbody.firstChild);
    }

}

function FillTBody(tbodyID,data){
    var tbody=document.getElementById(tbodyID);
    var htmlrow="";
    for(var i=0; i<data.length;i++){
        htmlrow="<tr id="+i+"><td>"+data[i].id+"</td><td>"+data[i].Car__manufacturer+"</td><td>"+
                data[i].Car__model+"</td><td>"+data[i].Car__trim+"</td><td>"+data[i].Car__mileage+
                "</td><td>"+data[i].Car__year+"</td><td>"+data[i].Car__color+"</td><td>"+data[i].Car__price+"</td></tr>";



        tbody.innerHTML+=htmlrow;

    }

}



