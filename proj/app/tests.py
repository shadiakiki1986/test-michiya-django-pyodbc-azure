from django.test import TestCase
from .models import Level1, Level2, Level3

from django.urls import reverse

from django.contrib.auth.models import User
from django.test.client import Client
password = 'mypassword' 

# Create your tests here.
def create_l3():
  l1e1 = Level1()
  l1e1.save()

  l2e1 = Level2()
  l2e1.l1 = l1e1
  l2e1.save()

  l3e1 = Level3()
  l3e1.l2 = l2e1
  l3e1.save()

  return l3e1


class AdminViewTests(TestCase):
  def test_l3_details(self):
    l3e1 = create_l3()

    # How to create admin user in django tests.py
    # http://stackoverflow.com/questions/3495114/ddg#3495219
    my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
    response = self.client.login(username=my_admin.username, password=password)
    self.assertTrue(response)

    # Getting Django admin url for an object
    # https://stackoverflow.com/a/850229/4126114
    url = reverse('admin:app_level3_change', args=(l3e1.id,))
    response = self.client.get(url,follow=True)
    # print(list(response))
    self.assertContains(response,"l2")
