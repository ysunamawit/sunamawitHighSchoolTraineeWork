$(document).ready(function() {
  $("#submit").click(function(e) {
    e.preventDefault();
        let value = $("#myselect").val();
        console.log(value)
        let text=$("#text").val();
        console.log(text)
        let answer= {
          "name": text, "rating":value
        };
        console.log(answer)
      $.ajax({
        url: "/cookie",
        type: "POST",
        data: answer,
        dataType: "json",
        success: function(answer, status) {
          console.log(answer)
          $("#message").css("color", "green");
          $("#message").text("Successful");
        },
        error: function(answer, status) {
          console.log(answer.responseJSON.message)
          $("#message").text("Failed");
          $("#message").css("color","red");
        

        }
      })





  }








  )


})
  //var form = $("#form");
// },
// error: function(""){
//   console.log(errorThrown);

// if (value = $("#myselect").val()) {
//   console.log(value)
// } else if (text=$("#text").val()) {
//   console.log(text)
// } else (data == "") {
//   alert("Invalid!")
// }
// let answer= {
//           "name": text, "rating":value
//         };
//         console.log(answer)











//   form.submit(function(e) {
//     e.preventDefault();
//     let value = $("#myselect")
//     console.log(value)
//     let text = $("#text")
//     console.log(text)
//
//
// })