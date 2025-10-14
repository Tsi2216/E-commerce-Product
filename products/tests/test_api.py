from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from products.models import Category, Product

User = get_user_model()


class ProductAPITest(APITestCase):
    def setUp(self):
        # Create a test user (email is required)
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass'
        )

        # Authenticate the test client
        self.client.force_authenticate(user=self.user)

        # Create a test category
        self.category = Category.objects.create(name='Electronics')

        # Create some test products
        self.product1 = Product.objects.create(
            name='Laptop',
            description='Gaming laptop',
            price=1200.00,
            stock=5,
            category=self.category,
            owner=self.user
        )
        self.product2 = Product.objects.create(
            name='Headphones',
            description='Wireless headphones',
            price=150.00,
            stock=10,
            category=self.category,
            owner=self.user
        )

    def test_list_products(self):
        """
        Test that the product list API returns all products
        """
        url = reverse('product-list')  # Replace with your DRF router name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assuming pagination is enabled
        self.assertEqual(len(response.data['results']), 2)

    def test_create_product(self):
        """
        Test that an authenticated user can create a product
        """
        url = reverse('product-list')  # Replace with your DRF router name
        data = {
            'name': 'Smartphone',
            'description': 'Latest model',
            'price': 999.99,
            'stock': 7,
            'category': self.category.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the product was actually created
        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(Product.objects.last().name, 'Smartphone')
        self.assertEqual(Product.objects.last().owner, self.user)
