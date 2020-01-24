const bt = document.querySelector("#theme-button"); /*buttonTheme*/

function buttonLightTheme(){
    bt.innerHTML = "&#9788;";
    bt.style.backgroundColor = "white";
}
function buttonDarkTheme() {
    bt.innerHTML = "&#9789;";
    bt.style.backgroundColor = "black";
}

if (localStorage.getItem("isDarkModeOn") === "true") {
    document.documentElement.setAttribute("data-theme", "dark");
    buttonDarkTheme();
} else {
    document.documentElement.setAttribute("data-theme", "light");
    buttonLightTheme();
}

function themeChange() {
    if (document.documentElement.getAttribute("data-theme") === "dark") {
        document.documentElement.setAttribute("data-theme", "light");
        buttonLightTheme();
        localStorage.setItem("isDarkModeOn", "false");
    } else {
        document.documentElement.setAttribute("data-theme", "dark");
        buttonDarkTheme();
        localStorage.setItem("isDarkModeOn", "true");
    }
}
/*////////////SIDEBAR/////////// */
const aside = document.querySelector(".sidebar-container");
let opening = false;
let isWidthZero = false;
function openSidebar() {
    aside.style.width = "320px";
    opening = true;
    isWidthZero = false;
}
function isSideBarOpened() {
    if (opening && !isWidthZero) {
        opening = false;
        return false;
    } else {
        return true;
    }
}
function closeSidebar() {
    aside.style.width = "0";
    isWidthZero = true;
}
function so(isCI) {
    if (!isCI && isSideBarOpened()) {
        closeSidebar();
    }
}
document.addEventListener("click", function (event) {
    let isClickedInside = aside.contains(event.target);
    so(isClickedInside);
});
/*///////////////////////////////////////////*/