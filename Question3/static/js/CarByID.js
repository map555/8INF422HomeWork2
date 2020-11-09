$(document).ready(function (){



                  //Get query result on submit
            $('#send_car_id').on('click', function(e){


                e.preventDefault();
                var car_id=document.getElementById("car_id").value;

                $.ajax({
                        type: "GET",
                        url:"/ajax/get_car_info_by_id",
                        data: {car_id:car_id},
                        success:function(response){

                            response.car_info.condition=getConditionValue(response.car_info.condition)

                            console.log("It works")
                            $("#resulttable tbody").html(`<tr>
                                <td id="manufacturerResult">${response.car_info.manufacturer}</td>
                                <td id="modelResult">${response.car_info.model}</td>
                                <td id="trimResult">${response.car_info.cartrim}</td>
                                <td id="colorResult">${response.car_info.carcolor}</td>
                                <td id="yearResult">${response.car_info.caryear}</td>
                                <td id="conditionResult">${response.car_info.condition}</td>
                                <td id="mileageResult">${response.car_info.mileage}</td>
                                <td id="weightResult">${response.car_info.carweight}</td>
                                <td id="priceResult">${response.car_info.price}</td>
                                </tr>`)

                        },
                        error : function(response){
                            console.log("It's not working")
                            console.log(response)
                         }
            })
            })
        });



function getConditionValue(conditionIndex){
        var conditionvalue;
        switch (conditionIndex){
            case "1":
                conditionvalue="very bad";
                break;
            case "2":
                conditionvalue="bad";
                break;
            case "3":
                conditionvalue="normal";
                break;
            case "4":
                conditionvalue="good";
                break;
            case "5":
                conditionvalue="very good";
                break;
            case "6":
                conditionvalue="showroom";
                break;
            default:
                conditionvalue="NULL";
                break;
        }
        return conditionvalue
    }