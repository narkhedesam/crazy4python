# crazy4python
<p align="center">
    <img src="crazy4python_200x200.jpg" alt="crazy4python">
</p>
<a href="https://paypal.me/sameernarkhede/250">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="paypal">
</a>

crazy4python is the django blogging site.

## How to use at your end
you must have installed python 3.8 or latest to your local machine.

then clone this repository https://github.com/narkhedesam/crazy4python.git

    $ git clone https://github.com/narkhedesam/crazy4python.git

Firstly switch to directery crazy4python add requirements 

    cd crazy4python
    python3.8 -m pip install -r requirements.txt


after that you need to migrate the changes 
    
    python3.8 manage.py makemigrations
    python3.8 manage.py migrate

Then Create an superuser to handle admin area

    # provide required information for this command
    python manage.py createsuperuser 
    
Run django at local
    
    python3.8 manage.py runserver 0.0.0.0:8000
    
 you can access the site at http://localhost:8000

## Author 
Sameer Narkhede <br/>
Profile : https://github.com/narkhedesam <br/>
Website : https://narkhedesam.github.io/ 

## Screenshot

![Screenshot](crazy4python_ss.png)


## Donation

If this project help you reduce time to develop, you can give me a cup of coffee :relaxed: 
<br/>
<a href="https://paypal.me/sameernarkhede/250">
    <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="paypal">
</a>
