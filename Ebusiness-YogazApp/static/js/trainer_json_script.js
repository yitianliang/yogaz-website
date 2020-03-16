$(document).ready(function() {
    var output = "";
    var element = "";
    var displayResources = $("#jsonList_trainer");
    displayResources.text("Your server is not working!");

    $.ajax({
      type: "GET",
      url: "/json/yogaz.json", 
      success: function(result) {
        console.log(result);
        output = "";

        element =  result.trainer;
        for (var i in element) {
          output += "<div class='col' id='trainer_box'>";
          output += "<div class='card'>";

          output += "<img src='" + element[i].image + "' class='card-img-top' alt='...'>";
          output += "<div class='card-body'>";
          output += "<h5 class='card-title'>" + element[i].name + "</h5>"
          output += "<p>" + element[i].email + "</p>";
          output += "<p>" + element[i].description + "</p>";

          output += "</div>"; // close card-body class
          output += "</div>"; // close card class
          output += "</div>"; // close col class
        }

        displayResources.html(output);
      }
    });

});
