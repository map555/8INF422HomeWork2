$(document).ready(function (){



                  //Get query result on submit
            $('#send_car_manufacturer').on('click', function(e){


                e.preventDefault();
                var car_manufacturer=document.getElementById("car_manufacturer").value;

                $.ajax({
                        type: "GET",
                        url:"/ajax/get_car_info_by_manufacturer",
                        data: {car_manufacturer:car_manufacturer},
                        success:function(response){

                        var table = ""

                        console.log(response.car_info)

                        for (i = 0; i < response.car_info.length; i++){
                            car = response.car_info[i]
                            car.condition = getConditionValue(car.condition)
                            console.log(car)


                            table += `<tr>
                                <td id="manufacturerResult">${car.manufacturer}</td>
                                <td id="modelResult">${car.model}</td>
                                <td id="trimResult">${car.cartrim}</td>
                                <td id="colorResult">${car.carcolor}</td>
                                <td id="yearResult">${car.caryear}</td>
                                <td id="conditionResult">${car.condition}</td>
                                <td id="mileageResult">${car.mileage}</td>
                                <td id="weightResult">${car.carweight}</td>
                                <td id="priceResult">${car.price}</td>
                                </tr>`
                        }

                        $("#resulttable tbody").html(table)

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