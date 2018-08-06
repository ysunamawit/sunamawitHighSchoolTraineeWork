window.onload = function() { 
    var form = $("#Form")   
    form.submit(function (e) {

        e.preventDefault();
        
        var data = $("#hello").val();

        if (data === "") {
            alert("Invalid!");
        }

        else {
        console.log({"Name":data});
        let url = "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%202487889&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys";
        $.get(url, function(data) {
            console.log(data.query.results.channel.item.condition.text);
        })
        return false;
    }
    
    });

    //     function processForm(e) {
    //     e.preventDefault();
    //     var data = $("#hello").value;
    //     if (data === "") {
    //         alert("Invalid!");
    //     }

    // else {
    //     console.log({data})
    // } return false;
    //     }
     
    

 
// code... when sumbmit is pressed with nothing on text it states error
}



