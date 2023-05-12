document.getElementById("myForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  // Retrieve form data
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var message = document.getElementById("message").value;

  // Display the form data
  var displayElement = document.getElementById("display");
  displayElement.innerHTML = "<h2>Form Data:</h2>" +
    "<p><strong>Name:</strong> " + name + "</p>" +
    "<p><strong>Email:</strong> " + email + "</p>" +
    "<p><strong>Message:</strong> " + message + "</p>";
});

