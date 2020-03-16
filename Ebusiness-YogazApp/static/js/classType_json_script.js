$(document).ready(function() {
    var output = "";
    var element = "";
    var displayResources = $("#jsonList_classtype");
    displayResources.text("ERROR 404: <br>Your server is not working! AJAX script could not load");

    $.ajax({
      type: "GET",
      url: "json/yogaz.json", 
      success: function(result) {
        console.log(result);
        output = "";

        element =  result.class;
        for (var i in element) {
          output += "<div class='' id='classtype_box'>";
          output += "<div class='card' style='width: 100%;'>";

          output += "<img src='" + element[i].image + "' class='card-img-top' alt='...' style='width:100%; text-align:center; margin-bottom: 10px'>";
          output += "<div class=''>";
          output += "<h5 class='card-title'>Class name: " + element[i].name + "</h5>"
          output += "<p>Teacher: " + element[i].teacher + "</p>";
          output += "<p>Class Description:<br>" + element[i].description + "</p>";
          output += "<p>Availablity: " + element[i].availability + "</p>";
          output += "<hr>"

          output += "</div>"; // close card-body class
          output += "</div>"; // close card class
          output += "</div>"; // close col class
        }

        displayResources.html(output);
      }
    });
});
