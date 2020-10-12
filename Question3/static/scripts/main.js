$(function (){

    //Get query result on submit
    $('#getCarID-form').on('submit', function(){
        carID=document.getElementById("carID").value;
        $.ajax({
            url:"",
            type: "GET",
            data: {
                car_id: carID
            },
        })
    })

});