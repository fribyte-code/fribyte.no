// identify the toggle switch HTML element
const toggleSwitch = document.querySelector("#checkbox_theme");

// function that changes the theme, and sets a localStorage variable to track the theme between page loads
function switchTheme(e) {
  if (e.target.checked) {
    localStorage.setItem("theme", "dark");
    document.documentElement.setAttribute("data-theme", "dark");
    toggleSwitch.checked = true;
  } else {
    localStorage.setItem("theme", "light");
    document.documentElement.setAttribute("data-theme", "light");
    toggleSwitch.checked = false;
  }
}

// listener for changing themes
toggleSwitch.addEventListener("change", switchTheme, false);

function isDarkTheme() {
  // pre-check the dark-theme checkbox if dark-theme is set
  if (document.documentElement.getAttribute("data-theme") == "dark") {
    toggleSwitch.checked = true;
  }
}

window.onload = isDarkTheme();
