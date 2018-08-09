$(document).ready(function() {
  $("#Submit").click(function(e) {
    e.stopImmediatePropagation();
    e.preventDefault();
    let Name = $("#Name").val();
    let StartDate = $("#StartDate").val();
    let EndDate = $("#EndDate").val();
    let Description = $("#Description").val();
    let Links = $("#Links").val();
    let Picture = $("#Picture").val();
    let data = {"Name":Name, "StartDate":StartDate, "EndDate":EndDate, "Description":Description, "Links":Links, "Picture":Picture};
    console.log(data);
    $.ajax({
      url: "/project",
      type: "POST",
      data: data,
      dataType: "json",
      success: function(data, status) {
        console.log(data);
        $("#message").css("color", "green");
        $("#message").text("Successful");
      },
      error: function(data, status) {
        console.log(data);
        $("#message").text("Failed");
        $("#message").css("color", "red");
      }
    });

  });
  $("#delete").click(function(e) {
    $.ajax({
      url: "/delete", type: "POST",
      success: function(e) {
        $("#message").css("color", "green");
        $("#message").text("Successful");
      },
      error: function(e) {
        $("#message").text("Failed");
        $("#message").css("color", "red");
      }

    });
    return false;
  });
});