window.addEventListener("load",function(){
  if (document.addEventListener) {
      document.addEventListener("mousewheel", MouseWheelHandler, false);
      document.addEventListener("DOMMouseScroll", MouseWheelHandler, false);
  }
  else {
      document.attachEvent("onmousewheel", MouseWheelHandler);
  }

  var wait = 0;
  var first = document.getElementById("first");
  var second = document.getElementById("second");
  var third = document.getElementById("third")
  var arrow = document.getElementById("header-arrow");
  var navbar = document.getElementById("navbar");
  var current_page = 0;

  function showAboutPage() {
      current_page = 1;
      onScrollDown();
  }

  function onScrollDown() {
    if (current_page == 0) {
        first.style.zIndex = 1;
        first.style.opacity = 0;
        second.style.zIndex = 5;
        second.style.opacity = 1;
        navbar.style.color = "#ffffff";
        arrow.style.color = "#ffffff";
        current_page = 1;
    } else if (current_page == 1) {
        second.style.zIndex = 1;
        second.style.opacity = 0;
        third.style.zIndex = 5;
        third.style.opacity = 1;
        navbar.style.color = "#ffffff"
        arrow.style.zIndex = 1;
        current_page = 2;
    }
  }

  function onScrollUp() {
      console.log("On Scroll Up()");
    if (current_page == 1) {
        second.style.zIndex = 1;
        second.style.opacity = 0;
        first.style.zIndex = 5;
        first.style.opacity = 1;
        navbar.style.color = "#353535";
        arrow.style.color = "#353535";
        current_page = 0;
    } else if (current_page == 2) {
        third.style.zIndex = 1;
        third.style.opacity = 0;
        second.style.zIndex = 5;
        second.style.opacity = 1;
        arrow.style.zIndex = 9;
        current_page = 1;
    }
  }

  document.getElementById("aboutLink").onclick = function() {showAboutPage();};

  arrow.onclick = function() {onScrollDown();};

  function MouseWheelHandler(e) {
      var e = window.event || e;
      var delta = e.wheelDelta

      if (delta > 0 && wait == 0) {
          console.log("SCROLL UP");
          wait = 1;
          setTimeout(function(){wait=0},1000);
          onScrollUp();
      } else if(wait == 0) {
          console.log("SCROLL DOWN");
          wait = 1;
          setTimeout(function(){wait=0},1000);
          onScrollDown();
      }
  }

  let address = window.location.href;
  if(address.indexOf("/#about") !== -1) {
      console.log(address.indexOf("/#about"));
    showAboutPage();
  }

}, false);
