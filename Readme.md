# Mini-Amazon (project for ECE 568 ERSS 2020 Spring)

By Wenge Xie, Yiteng Lu

This is a mini Amazon app that user can use to buy fake things from our amazon site. The backend of the site is connected to a simulated world that is written by the instructors in Duke ECE568 course. We manage all the purchasing, transportation of the goods in the simulated world, and interact with user using a web page written in Django.


## Set Up

First of all, World simulator must be run in the first place. Ensure nothing is running before iniatialize the world. Then start the min-amazon service by running 
<br>
the commands:
```
cd /Amazon/code
sudo docker-compose up
```
After running the amazon server, please start the UPS service in 10s to build up the socket connection between world amazon, ups amazon.  
<br>
run the front-end of our amazon server by typing your server's address. 

You should first create a UPS user account to bind with your amazon account. You can change the ups username when you are pre-preprocessing your order. But still we
<br>
are looking for a UPS username and your address location using x,y coordinates. (integer field)

When you finishing signing up, you would be able to log in to make some orders. Enter the item you want to buy for searching; then enter the quantity you want to buy.
<br>
then your desired items will be added to your cart. Get into the cart and then you can place your order by clicking "place the order". Then you will be prompted to 
<br>
a form where you must enter your locations and ups useranme again. Click "buy" to complete your order.
<br>
<br>
You can view all your orders in "order list". Each other has three statuses. When you just place your order, the world is packing your package, therefore the order 
<br>
turns out to be ordered. When the ups send the truck and load everything up, the status would change to "delivering". When UPS delivers your order, the status would 
<br>
finally change to "delivered".

## Workflow (Principle)
### The "world"
There is a world simulator we can use for this project. In the "world", as "Amazon", we can buy inventories from this world and also store thoese inventories in some stores that existing in this "world". The world also has control on many other things like the trucks the "UPS" can use, the location where the stroes exists but they are not very important properties for the "Amazon" developers. We contact with the "world" by google buffer protocol.

### "UPS"
UPS is the transportaion company that Aamazon need to contact with. Each time a user created a order, the Amazon is required to contact the UPS and request a truck for delivering from them. Then UPS should finish the derlivery. The "UPS" part is written by another group of developers. We contact with the UPS by google buffer protocol.

### Database
We build our database in postgres. There are five tables we created for this project. User, Order, Warehouse, PurchasedProduct and Cart. A "order" is a order the user created after he/she clicked the button "Buy" in the cart page on our web page. All the prodcuts in his order will be stored in to the "Order" table. Meanwhile, we will store his shiping location and ups name too (this is used for intereaction with the UPS). 

### Frontend 
The frontend of our project is a web page written in Django. This webpage has 6 functions. First, sign in and sign up. Second, search for wanted products. Third, Add prodcuts into the cart. Fourth, adjust the product type and number in hte cart. Fifth, buy things you in the cart. Sixth, check the order status. For security concerns, the frontend only has the permission to read the dataset. It cannot modify the dataset. So each time we received a request from the user that asking the dataset to be modified, we will send the request by socket to our backend. And our backend will do modification to the dataset.

### Backend
The backend of our project is a server that can contatct with the world, the frontend and the UPS. Each time a user is adding something into their cart, the front end will send a request to the backend to check the dataset if we have enough inventory for the thing the user wants to buy. If not, the backend will send a request to the world and aksing the world to provide enough inventory to the store. Each time the user clicks the "buy" button in our webpage, the frontend will send a request to the backend and the backend will deduct the number of things the buyer wants to buy from the database, and send a request to the world for packing. After the package is packed, the world will send a notificatino to the backend, and the backend will send a request to the UPS server and ask them to send a truck for delivering. After the UPS sent us a notification that the truck has arrived, the backend will send a request to the world and asking the world start load to the truck. After the truck is loaded, the world will send us a notification and the backend will send a request to the UPS server and ask them start to deliver. When the package is arrived, the UPS will sned us a notification and the backend will modify the status of this order in the database. 
