data = {
  "first_name": "Joe",
  "last_name": "Blow",
  "gender": "male",
  "age": 40,
  "weight": 180,
  "admissiondate": "01/02/2003",
  "admissiontime": "02:30",
  "preopnotes": "This is the time for all good men to come to the aid of the party"
}

pred = {
  "Surgical": [
    "19357 | Breast reconstruction, immediate or delayed, with tissue expander, including subsequent expansion",
    "61885 | Insertion or replacement of cranial neurostimulator pulse generator or receiver, direct or inductive coupling; with connection to a single electrode array",
    "61886 | Insertion or replacement of cranial neurostimulator pulse generator or receiver, direct or inductive coupling; with connection to 2 or more electrode arrays",
    "64569 | "
  ],
  "Anesthesia": [
    "300 | Anesthesia for all procedures on the integumentary system, muscles and nerves of head, neck, and posterior trunk, not otherwise specified",
    "400 | Anesthesia for procedures on the integumentary system on the extremities, anterior trunk and perineum; not otherwise specified"
  ],
  "Risk": "0.0936"
}

function toggler(elementId) {
    $("#" + elementId).toggle();
}


function loadJSON (callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', './data/patient.json', true); // Replace 'my_data' with the path to your file
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
        }
    };
    xobj.send(null);
}

function loadJSONcodes (callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', './data/codes.json', true); // Replace 'my_data' with the path to your file
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
        }
    };
    xobj.send(null);
}

function autoFill() {
    document.getElementById('first_name').value = "Sohag";
    document.getElementById('last_name').value = "Desai";

    var radioElements = document.getElementsByName("gender");

    for (var i=0; i<radioElements.length; i++) {
      if (radioElements[i].getAttribute('value') == 'male') {
        radioElements[i].checked = true;
      }
    }

    document.getElementById('age').value = "40";
    document.getElementById('weight').value = "180";
    document.getElementById('admissiondate').value = "01/02/2003";
    document.getElementById('admissiontime').value = "16:45";
    document.getElementById('preopnotes').value = "This is the time for all good me to come to the aid of the party";

  }

function fillFromJson() {
    // var nameobj = new Object()
    // nameobj.a = "test.json"
    loadJSON(function(response) {
        // Parse JSON string into object
        data = JSON.parse(response);
    });

    console.log(data)

    document.getElementById('first_name').value = data["first_name"];
    document.getElementById('last_name').value = data["last_name"];

    var radioElements = document.getElementsByName("gender");

    for (var i=0; i<radioElements.length; i++) {
      if (radioElements[i].getAttribute('value') == 'male') {
        radioElements[i].checked = true;
      }
    }

    document.getElementById('age').value = data["age"];
    document.getElementById('weight').value = data["weight"];
    document.getElementById('admissiondate').value = data["admissiondate"];
    document.getElementById('admissiontime').value = data["admissiontime"];
    document.getElementById('preopnotes').value = data["preopnotes"];

  }


function reset() {
    document.getElementById('first_name').value = "";
    document.getElementById('last_name').value = "";

    var radioElements = document.getElementsByName("gender");

    for (var i=0; i<radioElements.length; i++) {
      if (radioElements[i].getAttribute('value') == 'female') {
        radioElements[i].checked = false;
      }
    }

    document.getElementById('age').value = "";
    document.getElementById('weight').value = "";
    document.getElementById('admissiondate').value = "";
    document.getElementById('admissiontime').value = "";
    document.getElementById('preopnotes').value = "";

  }

function showField() {
  var x = document.getElementById("PostOpForm");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function CreateTableFromJSON(myBooks) {
    // get data
    var filename = "codes.json"
    loadJSONcodes(function(response) {
        // Parse JSON string into object
        data = JSON.parse(response);
    });

    var myBooks = data
    // EXTRACT VALUE FOR HTML HEADER.
    // ('Book ID', 'Book Name', 'Category' and 'Price')
    var col = [];
    for (var i = 0; i < myBooks.length; i++) {
        for (var key in myBooks[i]) {
            if (col.indexOf(key) === -1) {
                col.push(key);
            }
        }
    }
    col.push("Submit")

    // CREATE DYNAMIC TABLE.
    var table = document.createElement("table");

    // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

    var tr = table.insertRow(-1);                   // TABLE ROW.

    for (var i = 0; i < col.length; i++) {
        var th = document.createElement("th");      // TABLE HEADER.
        th.innerHTML = col[i];
        tr.appendChild(th);
    }

    // ADD JSON DATA TO THE TABLE AS ROWS.
    var checkbox = [];
    for (var i = 0; i < myBooks.length; i++) {

        tr = table.insertRow(-1);

        for (var j = 0; j < col.length - 1; j++) {
            var tabCell = tr.insertCell(-1);
            tabCell.innerHTML = myBooks[i][col[j]];
        }
        // ADD CHECKBOX
        checkbox[i] = document.createElement('input');
        checkbox[i].type = "checkbox";
        checkbox[i].name = "name";
        checkbox[i].id = "id" + myBooks[i][col[0]];
        checkbox[i].value = "value";
        var tabCell = tr.insertCell(-1);
        // tabCell.innerHTML = checkbox[i];
        tabCell.appendChild(checkbox[i]);


    }

    // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
    var divContainer = document.getElementById("showData");
    divContainer.innerHTML = "";
    divContainer.appendChild(table);
}

$(document).ready(function() {
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            surgeonID: {
                validators: {
                        stringLength: {
                        min: 2,
                    },
                        notEmpty: {
                        message: 'Please supply Surgeon ID'
                    }
                }
            },
            indexCode: {
                validators: {
                     stringLength: {
                        min: 2,
                    },
                    notEmpty: {
                        message: 'Please supply Operation Code'
                    }
                }
            }
            }
        })
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
                //$('#contact_form').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Check for checkboxes
            // test data
            loadJSONcodes(function(response) {
                // Parse JSON string into object
                data = JSON.parse(response);
            });

            var myBooks = data
            for (var i = 0; i < myBooks.length; i++) {
              // generate ids (id+1)
              checkbox[i].id = "id" + myBooks[i][col[0]];

            }

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');

            // Experimenting hiding/unhiding
            // toggler('cpt-codes');
            // Experimenting modal
            //$('#myModal').modal('show');

        });
});


// tableCreate();
