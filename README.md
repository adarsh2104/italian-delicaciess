##                               Italian Delicaciess [italian-delicaciess.herokuapp.com](https://italian-delicaciess.herokuapp.com/menu)
<p align="center"><img width="100%" height="700px" src="https://github.com/adarsh2104/italian-delicaciess/blob/main/Visuals/1.Home.png"></img></p>

### Stacks Used:
* Python 3.6
* Django 2.2
* django-allauth 0.44
* Bootstrap 4
* HTML/CSS/JS
* SQLite

A responsive website design with following salient features:

1. Menu Page:
    * Created on top of [Bootstrap Album Sample](https://getbootstrap.com/docs/5.0/examples/album/).
    * Used Django template for dynamic rendering of menu items from the django Model.
    * Feature to add new menu items directly from the django admin.
    <p align="center"><img width="100%" height="500px" src="https://github.com/adarsh2104/italian-delicaciess/blob/main/Visuals/2.Menu.png"></img></p>
    <p align="center"><img width="100%" height="500px" src="https://github.com/adarsh2104/italian-delicaciess/blob/main/Visuals/8.Bootstrap_Menu_base.png"></img></p>
    <p align="center"><img width="100%" height="500px" src="https://github.com/adarsh2104/italian-delicaciess/blob/main/Visuals/7.Admin_page.png"></img></p>
2. Login Page:
    * Main Component containing graphic and login button was created using [Bootstrap Cards](https://getbootstrap.com/docs/4.0/components/card) and [Bootstrap Button](https://mdbootstrap.com/docs/standard/components/buttons/)
    * Added support for User authorization with [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2/web-server) was implemeted using [django-allauth](https://django-allauth.readthedocs.io/en/latest/overview.html) python package.
    <p align="center"><img width="100%" height="500px" src="https://github.com/adarsh2104/italian-delicaciess/blob/main/Visuals/3.Login.png"></img></p>
    <p align="center"><img width="100%" height="500px" src="https://github.com/adarsh2104/italian-delicaciess/blob/main/Visuals/4.Sign_In.jpeg"></img></p> 
3. Checkout Page:
   * Feature to generate invoice from the price of each menu items and quantity purchased from menu page. 
   * Frontend components were created using the [Bootstrap Checkout Sample](https://getbootstrap.com/docs/4.0/examples/checkout).
    <p align="center"><img width="100%" height="500px" src="https://github.com/adarsh2104/italian-delicaciess/blob/main/Visuals/5..Checkout.png"></img></p>
   <p align="center"><img width="100%" height="500px" src="https://github.com/adarsh2104/italian-delicaciess/blob/main/Visuals/9.Bootstrap_Checkout_base.png"></img></p>
4. Client Orders Dashboard:
   * Dashboard to display all the orders placed by the client in reverse chronological order.
   <p align="center"><img width="100%" height="500px" src="https://github.com/adarsh2104/italian-delicaciess/blob/main/Visuals/6.Order_Dashboard.png"></img></p>
