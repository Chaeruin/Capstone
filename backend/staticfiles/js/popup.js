function showAlert() {
    window.alert("온도가 낮습니다.");
    var badge = document.getElementById("myBadge");
    badge.style.display = "none";
  
    var ringImgText = document.querySelector(".ring-img-text");
    ringImgText.style.display = "none";
  }
  
  /*function showAlert() {
    window.alert("온도가 낮습니다.");
    var badge = document.getElementById("myBadge");
    badge.style.display = "none";
  
    var ringImgText = document.querySelector(".ring-img-text");
    ringImgText.style.display = "none";
  }
    
    // Modify the default alert function to display the title "알람" and add a close button
    window.alert = function(message) {
      
      var title = "알람";
      var modifiedMessage = "<h1 style='font-size: 18px;'>" + title + "</h1><p style='font-size: 15px;'>" + message + "</p>";
      var alertBox = document.createElement("div");
      alertBox.innerHTML = modifiedMessage;
      alertBox.style.background = "#fff";
      alertBox.style.color = "#000";
      alertBox.style.padding = "20px";
      alertBox.style.border = "1px solid #000";
      alertBox.style.position = "absolute";
      alertBox.style.top = "23%";
      alertBox.style.left = "88%";
      // if (window.matchMedia("(max-width: 991px)").matches) {
      //   alertBox.style.top = "23%";
      //   alertBox.style.left = "88%";
      // } else {
      //   alertBox.style.top = "19%";
      //   alertBox.style.left = "86%";
      // }
      alertBox.style.transform = "translate(-50%, -50%)";
    
      // Create a close button
      var closeButton = document.createElement("button");
      closeButton.textContent = "Close";
      closeButton.style.marginTop = "10px";
      closeButton.style.padding = "5px 10px";
      closeButton.style.background = "#ccc";
      closeButton.style.border = "none";
      closeButton.style.cursor = "pointer";
    
      // Function to close the alert box
      closeButton.addEventListener("click", function() {
        document.body.removeChild(alertBox);
  ;
      });
    
      // Append the close button to the alert box
      alertBox.appendChild(closeButton);
    
      // Append the alert box to the body of the HTML document
      document.body.appendChild(alertBox);
  
      
    };
  */