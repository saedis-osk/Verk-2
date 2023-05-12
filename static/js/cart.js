document.addEventListener('DOMContentLoaded', function(event) {
  var myForm = document.getElementById("myform");

  myForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Retrieve form data
    var name = document.getElementById("typeName").value;
    var email = document.getElementById("typeText").value;
    var phoneNumber = document.getElementById("typeText1").value;
    var city = document.getElementById("typeText2").value;
    var zipCode = document.getElementById("typeText3").value;
    var street = document.getElementById("typeText4").value;

    // Display the form data
    var displayElement = document.getElementById("display");
    displayElement.innerHTML = "<h2>Form Data:</h2>" +
      "<p><strong>Name:</strong> " + name + "</p>" +
      "<p><strong>Email:</strong> " + email + "</p>" +
      "<p><strong>Phone Number:</strong> " + phoneNumber + "</p>" +
      "<p><strong>City:</strong> " + city + "</p>" +
      "<p><strong>Zip Code:</strong> " + zipCode + "</p>" +
      "<p><strong>Street:</strong> " + street + "</p>";
  });
});
