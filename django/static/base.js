const bt = document.querySelector("#theme-button"); /*buttonTheme*/

function buttonLightTheme() {
    bt.innerHTML = "&#9788;";
}
function buttonDarkTheme() {
    bt.innerHTML = "&#9789;";
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
const pageWrapper = document.querySelector(".base-page-wrapper");
const navbar = document.querySelector(".header-container");
let isOpened = false;
function openSidebar() {
    aside.style.marginLeft = "0px";
    pageWrapper.style.marginLeft = "170px";
    navbar.style.marginLeft = "-170px";
    isOpened = true;
}
function closeSidebar() {
    aside.style.marginLeft = "-170px";
    pageWrapper.style.marginLeft = "0";
    navbar.style.marginLeft = "0";
    isOpened = false;
}

function changeSidebarState() {
    if (isOpened) {
        closeSidebar();
    } else {
        openSidebar();
    }
}
/*///////////////////////////////////////////*/