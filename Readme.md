# Mini-Amazon (project for ECE 568 ERSS 2020 Spring)

By Wenge Xie, Yiteng Lu

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
