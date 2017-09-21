var aCardIsFocused = -1;
function openCard(id) {
    if (aCardIsFocused === -1 ) {
        console.log('Enhance: ' + id);
        // Get the elements
        let b = document.getElementById('blocker');
        let c = document.getElementById("card-"+id);
        let front = document.getElementById("card-front-"+id);
        let back = document.getElementById("card-back-"+id);
        let d = document.getElementById("card-container");

        // ENHANCE
        aCardIsFocused = Number(id);
        front.classList.add('hidden');
        back.classList.remove('hidden');
        b.className = '';
        c.classList.add('enhanced');
        scrollToCard(c);
    }
}

function closeCard() {
    console.log('Unhenhance: ' + aCardIsFocused);
    let b = document.getElementById('blocker');
    let c = document.getElementById("card-"+aCardIsFocused);
    let front = document.getElementById("card-front-"+aCardIsFocused);
    let back = document.getElementById("card-back-"+aCardIsFocused);
    let d = document.getElementById("card-container");

    aCardIsFocused = -1;
    front.classList.remove('hidden');
    back.classList.add('hidden');
    b.className = 'hidden';
    c.classList.remove('enhanced');
}

function scrollToCard(c) {
    let d = document.getElementById("card-container");
    let bodyRect = document.body.getBoundingClientRect();
    let elemRect = c.getBoundingClientRect();
    let offset = elemRect.left - bodyRect.left;

    d.scrollLeft += offset-20;
}

function addEvent(object, type, callback) {
    if (object == null || typeof(object) == 'undefined') return;
    if (object.addEventListener) {
        object.addEventListener(type, callback, false);
    } else if (object.attachEvent) {
        object.attachEvent("on" + type, callback);
    } else {
        object["on"+type] = callback;
    }
};

// if a card is focused it should still be in view on window resize.
addEvent(window,"resize", function(event) {
    // aCardIsFocused is -1 if false and
    // otherwise contains the cards id
    if (aCardIsFocused !== -1) {
        scrollToCard( document.getElementById("card-" + aCardIsFocused) );
    }
});

function MouseWheelHandler(e) {
    // cross-browser wheel delta
    if (aCardIsFocused < 0) {
      	var e = window.event || e; // old IE support
      	var delta = Math.max(-1, Math.min(1, (e.wheelDelta || -e.detail)));

        let d = document.getElementById("card-container");
        d.scrollLeft -= (delta*60);
      	return false;
    } else {
        return true;
    }
}

// For vertical scrolling the card-container
function doOnLoad() {
    let d = document.getElementById("card-container");
    if (d.addEventListener) {
  	    // IE9, Chrome, Safari, Opera
  	    d.addEventListener("mousewheel", MouseWheelHandler, false);
  	    // Firefox
  	    d.addEventListener("DOMMouseScroll", MouseWheelHandler, false);
    }
    // IE 6/7/8
    else d.attachEvent("onmousewheel", MouseWheelHandler);
}

window.onload = doOnLoad;
