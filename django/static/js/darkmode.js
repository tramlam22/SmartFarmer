let button = document.querySelector("#theme-button");

function buttonPressedTheme(){
    button.style.color = '#ff00ff';
}
function buttonLightTheme(){
    button.innerHTML = "&#9788;";
    button.style.backgroundColor = 'white';
    button.style.color = 'black';
}
function buttonDarkTheme(){
    button.innerHTML = "&#9789;";
    button.style.backgroundColor = 'black';
    button.style.color = 'white';
}

if(localStorage.getItem("isDarkModeOn") === "true"){
    document.documentElement.setAttribute('data-theme', 'dark');
    buttonDarkTheme();
}else{
    document.documentElement.setAttribute('data-theme', 'light');
    buttonLightTheme();
}

function themeChange() {
    if(document.documentElement.getAttribute('data-theme') === 'dark'){ 
        document.documentElement.setAttribute('data-theme', 'light');
        buttonLightTheme();
        localStorage.setItem("isDarkModeOn", "false");
    }else{
        document.documentElement.setAttribute('data-theme', 'dark');
        buttonDarkTheme();
        localStorage.setItem("isDarkModeOn", "true");
    }
}
button.addEventListener('mousedown', buttonPressedTheme);