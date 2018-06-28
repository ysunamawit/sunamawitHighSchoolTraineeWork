window.onload = function() { 
    function processForm(e) {
        e.preventDefault();
        var data = document.getElementById("hello").value;
        if (data === "") {
            alert("Invalid!");
        }

        else {
            console.log(data)
            }
        }
    
    var form = document.getElementById("Form");  
    form.addEventListener("submit", processForm);


 
// code... when sumbmit is pressed with nothing on text it states error
}



