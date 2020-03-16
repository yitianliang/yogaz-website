// java script file

$('body').effect("slide");

function main() {

}

// onClick
function onClickFacebook() {
	alert("login with facebook feature is coming soon");
}

function onClickGmail() {
	alert("login with Gmail feature is coming soon");
}

$('li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});

// function positionMessage() {
//             if (!checkCompatibility) return;
//             var ele = document.getElementById("movement");
//             ele.style.position = "absolute";
//             ele.style.top = "100px";
//             ele.style.left = "100px";
//             moveElement("movement",200,100,5);
//         }
// function moveElement(elementID, final_x, final_y, interval) {

//             if (!document.getElementById(elementID)) { return false; }
//             else { var ele = document.getElementById(elementID); }
//             var xpos = parseInt(ele.style.left);
//             var ypos = parseInt(ele.style.top);
//             if (xpos == final_x && ypos == final_y) {
//                 return true;
//             }
//             if (xpos < final_x) {
//                 xpos++;
//             }
//             if (xpos > final_x) {
//                 xpos--;
//             }
//             if (ypos > final_y) {
//                 ypos--;
//             }
//             if (ypos < final_y) {
//                 ypos++;
//             }
//             ele.style.left = xpos + "px";
//             ele.style.top = ypos + "px";
//             var repeat = "moveElement('" + elementID + "','" + final_x + "','" + final_y + "','" + interval + "')";
//             movement = setTimeout(repeat, interval);
//         }
//         var loadeventlist = [positionMessage];
//         addOnloadEventlist(loadeventlist);

// function addOnloadEventlist(eventlist) {
//             if (!eventlist) return false;
//             var oldonload = window.onload;
//             window.onload = function () {
//                 for (var i = 0; i < eventlist.length; i++) {
//                     eventlist[i]();
//                 }
//             }
//         }

// function checkCompatibility() {
//             if (!document.getElementById) return false;
//             if (!document.createElement) return false;
//             if (!document.createTextNode) return false;
//             if (!document.getElementsByTagName) return false;
//             if (!document.getElementsByName) return false;
//             return true;
//         }


main();
