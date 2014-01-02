// Avoid `console` errors in browsers that lack a console.
(function() {
    var method;
    var noop = function () {};
    var methods = [
        'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
        'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
        'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
        'timeStamp', 'trace', 'warn'
    ];
    var length = methods.length;
    var console = (window.console = window.console || {});

    while (length--) {
        method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
            console[method] = noop;
        }
    }
}());

function hasjQuery(){
    var obj = $('body');
    return obj && obj.hasOwnProperty && obj instanceof jQuery;
}

function hasCanvas(){
    return Modernizr.canvas
}

function hasDraganddrop(){
    return Modernizr.draganddrop
}

function hasLocalStorage(){
    Modernizr.localstorage
}

function hasPostMessage(){
    Modernizr.postmessage
}

function hasWebSockets(){
    Modernizr.websockets
}

function hasWebWorkers(){
    Modernizr.webworkers
}

// Place any jQuery/helper plugins in here.
