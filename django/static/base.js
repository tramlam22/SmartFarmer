const button = document.querySelector("#theme-button");

function buttonPressedTheme() {
    button.style.color = "#ff00ff";
}
function buttonLightTheme() {
    button.innerHTML = "&#9788;";
    button.style.backgroundColor = "white";
    button.style.color = "black";
}
function buttonDarkTheme() {
    button.innerHTML = "&#9789;";
    button.style.backgroundColor = "black";
    button.style.color = "white";
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
button.addEventListener("mousedown", buttonPressedTheme);

////////////////////////////////////////////////////////////
const nav = document.querySelector(".navbar");
const main = document.querySelector(".site-content");
let topOfNav = nav.offsetTop;

function fixNav() {
    if (window.scrollY >= topOfNav) {
        console.log(nav.offsetHeight);
        main.style.paddingTop = nav.offsetHeight + "px";
        document.body.classList.add("fixed-nav");
    } else {
        main.style.paddingTop = 0;
        document.body.classList.remove("fixed-nav");
    }
}
fixNav();

window.addEventListener("scroll", fixNav);
///////////////////////////////////////////////////////////
const aside = document.querySelector(".aside-container");
let opening = false;
function openSidebar() {
    aside.style.display = "block";
    opening = true;
}
function isSideBarOpened() {
    if (opening && aside.style.display == "block") {
        opening = false;
        return false;
    } else {
        return true;
    }
}
function closeSidebar() {
    aside.style.display = "none";
}
function so(isCI) {
    let opened = isSideBarOpened();
    if (!isCI && opened) {
        closeSidebar();
    }
}
document.addEventListener("click", function (event) {
    let isClickedInside = aside.contains(event.target);
    so(isClickedInside);
});
