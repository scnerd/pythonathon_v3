from menu import Menu, MenuItem
from django.urls import reverse

Menu.add_item('main', MenuItem('Home', reverse('ctf:index')))