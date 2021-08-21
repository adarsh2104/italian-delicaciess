var cart = []
var menu = document.getElementsByClassName("add-to-cart")
Array.from(menu).forEach(function(element) {
      element.addEventListener('click', ()=>{
         var dish={};
           
         if (cart[element.id] == null){
             cart[element.id] = 1;
             element.innerHTML = "<strong>     ADD MORE          " + "<strong>(<span>&#215;</span>"+ cart[element.id]+ ")";
         }else{
             cart[element.id] +=1;
             element.innerHTML = "<strong>     ADD MORE          " + "<strong>(<span>&#215;</span>"+ cart[element.id]+ ")";
         }
        
         console.log(cart);
      });
    });




    var checkout = document.getElementById('checkout-to-cart');


    checkout.addEventListener('click',() => {
        if (cart.length === 0){
            alert('You Cart is Empty !!');
            return
        }else{
            // window.location.href = "/checkout"
      var data = cart;
      function sendData( data ) {
      const XHR = new XMLHttpRequest(),
            FD  = new FormData();
      // Push our data into our FormData object
      for( name in data ) {
        FD.append( name, data[ name ] );
      }
      XHR.open( 'POST', 'https://italian-delicaciess.herokuapp.com/menu/' );
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
      sendData(data);
      
      
    } 
    
        })
    


    
