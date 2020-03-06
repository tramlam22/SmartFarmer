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
function openSidebar(mobile) {
    aside.style.marginLeft = "0px";
    isOpened = true;
    if(!mobile){
		pageWrapper.style.marginLeft = "170px";
    }
}
function closeSidebar(mobile) {
    aside.style.marginLeft = "-170px";
    isOpened = false;
    if(!mobile){
        pageWrapper.style.marginLeft = "0";
    }
}

function changeSidebarState() {
    if (window.matchMedia('screen and (max-width: 1000px)').matches){
        aside.style.boxShadow = "0 0 8px 0px rgba(0,0,0,0.3)";
		if (isOpened) {
        	closeSidebar(true);
    	} else {
        	openSidebar(true);
    	}
    }else{
        aside.style.boxShadow = "none";
        if (isOpened) {
        	closeSidebar(false);
    	} else {
        	openSidebar(false);
    	}
    }
}
window.addEventListener('resize', ()=>{
    if (window.matchMedia('screen and (max-width: 1000px)').matches){
        pageWrapper.style.marginLeft = "0";
        aside.style.boxShadow = "0 0 8px 0px rgba(0,0,0,0.3)";
    }else{
        aside.style.boxShadow = "none";
		if (isOpened) {
        	pageWrapper.style.marginLeft = "170px";
    	} else {
        	pageWrapper.style.marginLeft = "0";
    	}
    }
});
/*///////////////////////////////////////////*/

