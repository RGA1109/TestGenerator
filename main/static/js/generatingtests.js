// Loads all Options choices for the test
function optionCreator() { // don't leak
    truechoice();
    mutlichoice();
    matchingchoice();
    fillBchoice();
    shortchoice();
    essaychoice();
    fillfchoice();
    };

// Sub Functions to Option Creator
function truechoice() {
    var elm = document.getElementById('True/False'), // get the select
        df = document.createDocumentFragment(); // create a document fragment to hold the options while we create them
    for (var i = 0; i <= 10; i++) { // loop, i like 42.
            var option = document.createElement('option'); // create the option element
            option.value = i; // set the value property
            option.appendChild(document.createTextNode( i )); // set the textContent in a safe way.
            df.appendChild(option); // append the option to the document fragment
     }
    elm.appendChild(df); // append the document fragment to the DOM. this is the better way rather than setting innerHTML a bunch of times (or even once with a long string)
    };
function mutlichoice() {
    var elm = document.getElementById('MultiChoice'), // get the select
        df = document.createDocumentFragment(); // create a document fragment to hold the options while we create them
    for (var i = 0; i <= 10; i++) { // loop, i like 42.
            var option = document.createElement('option'); // create the option element
            option.value = i; // set the value property
            option.appendChild(document.createTextNode( i )); // set the textContent in a safe way.
            df.appendChild(option); // append the option to the document fragment
     }
    elm.appendChild(df); // append the document fragment to the DOM. this is the better way rather than setting innerHTML a bunch of times (or even once with a long string)
    };
function matchingchoice() {
    var elm = document.getElementById('Matching'), // get the select
        df = document.createDocumentFragment(); // create a document fragment to hold the options while we create them
    for (var i = 0; i <= 10; i++) { // loop, i like 42.
            var option = document.createElement('option'); // create the option element
            option.value = i; // set the value property
            option.appendChild(document.createTextNode( i )); // set the textContent in a safe way.
            df.appendChild(option); // append the option to the document fragment
     }
    elm.appendChild(df); // append the document fragment to the DOM. this is the better way rather than setting innerHTML a bunch of times (or even once with a long string)
    };
function fillBchoice() {
    var elm = document.getElementById('FillB'), // get the select
        df = document.createDocumentFragment(); // create a document fragment to hold the options while we create them
    for (var i = 0; i <= 10; i++) { // loop, i like 42.
            var option = document.createElement('option'); // create the option element
            option.value = i; // set the value property
            option.appendChild(document.createTextNode( i )); // set the textContent in a safe way.
            df.appendChild(option); // append the option to the document fragment
     }
    elm.appendChild(df); // append the document fragment to the DOM. this is the better way rather than setting innerHTML a bunch of times (or even once with a long string)
    };
function shortchoice() {
    var elm = document.getElementById('Short'), // get the select
        df = document.createDocumentFragment(); // create a document fragment to hold the options while we create them
    for (var i = 0; i <= 10; i++) { // loop, i like 42.
            var option = document.createElement('option'); // create the option element
            option.value = i; // set the value property
            option.appendChild(document.createTextNode( i )); // set the textContent in a safe way.
            df.appendChild(option); // append the option to the document fragment
     }
    elm.appendChild(df); // append the document fragment to the DOM. this is the better way rather than setting innerHTML a bunch of times (or even once with a long string)
    };
function essaychoice() {
    var elm = document.getElementById('Essay'), // get the select
        df = document.createDocumentFragment(); // create a document fragment to hold the options while we create them
    for (var i = 0; i <= 10; i++) { // loop, i like 42.
            var option = document.createElement('option'); // create the option element
            option.value = i; // set the value property
            option.appendChild(document.createTextNode( i )); // set the textContent in a safe way.
            df.appendChild(option); // append the option to the document fragment
     }
    elm.appendChild(df); // append the document fragment to the DOM. this is the better way rather than setting innerHTML a bunch of times (or even once with a long string)
    };
function fillfchoice() {
    var elm = document.getElementById('FillF'), // get the select
        df = document.createDocumentFragment(); // create a document fragment to hold the options while we create them
    for (var i = 0; i <= 10; i++) { // loop, i like 42.
            var option = document.createElement('option'); // create the option element
            option.value = i; // set the value property
            option.appendChild(document.createTextNode( i )); // set the textContent in a safe way.
            df.appendChild(option); // append the option to the document fragment
     }
    elm.appendChild(df); // append the document fragment to the DOM. this is the better way rather than setting innerHTML a bunch of times (or even once with a long string)
    };

// Controls the Searching tags function
$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    console.log(value)
    var c = document.getElementById("myDIV").children;
    var y = document.getElementById("myInput");
    var x = document.getElementById("myDIV");
    $("#myDIV *").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      if (value === "") {
        x.style.display ="none";
      }
      else {
        x.style.display ="block";
      }
    });
  });
});


function submitform()
{
    if(document.myform.onsubmit &&
    !document.myform.onsubmit())
    {
        return;
    }
 document.myform.submit();
}
