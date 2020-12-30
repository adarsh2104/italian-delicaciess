




var checkout = document.getElementById("final-checkout");
checkout.addEventListener('click',() => {
var total = document.getElementById("total").textContent;
var firstName = document.getElementById("firstName").value;
var lastName = document.getElementById("lastName").value;
var address1 = document.getElementById("address").value;
var address2 = document.getElementById("address2").value;


var name = firstName + " " + lastName
var address = address1 + address2
    console.log(name,address)
        // window.location.href = "/checkout"
  function sendData( name,address,total ) {
  const XHR = new XMLHttpRequest(),
        FD  = new FormData();
  // Push our data into our FormData object
//   for( name in data ) {
//     FD.append( name, data[ name ] );
//   }
FD.append( 'total', total );
FD.append( 'name', name );
FD.append( 'address', address );

  XHR.open( 'POST', 'https://italian-delicaciess.herokuapp.com/checkout/' );
  XHR.send( FD );
  console.log(FD);
  XHR.onload = function () {

    // Process our return data
    if (XHR.status >= 200 && XHR.status < 300) {
        // Runs when the request is successful
                document.open();
                document.write(XHR.responseText);
                document.close();
    } else {
        // Runs when it's not
        console.log(XHR.responseText);
    }

};
  

  }
  sendData(name,address,total);
  // window.location = "http://localhost:8000/checkout/track_order/"
  


    })
