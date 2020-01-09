let button = document.querySelector("#theme-button");

function buttonLightTheme(){
    button.innerHTML = "&#9788;";
    button.style.backgroundColor = 'white';
    button.style.color = 'black';
}
function buttonPressedTheme(){
    button.style.color = '#ff00ff';
}
function buttonDarkTheme(){
    button.innerHTML = "&#9789;";
    button.style.backgroundColor = 'black';
    button.style.color = 'white';
}

if(localStorage.getItem("key") === "true"){
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
        localStorage.setItem("key", "false");
    }else{
        document.documentElement.setAttribute('data-theme', 'dark');
        buttonDarkTheme();
        localStorage.setItem("key", "true");
    }
}
button.addEventListener('mousedown', buttonPressedTheme);