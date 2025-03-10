from django.test import TestCase
from .models import Books, Category, Cover, CustomUser, Genre, Writer, AuthUser, Orderbooks, OrderRequests

from datetime import datetime


#Нагрузочный тест для модели Orderbooks(с ошибкой)
# class OrderbooksLoadTest(TestCase):
#     def setUp(self):
#         """Подготовка данных перед каждым тестом."""
#         self.num_orders = 10  # Количество заказов для теста
#
#         # Создаем необходимые объекты для ForeignKey
#         self.category = Category.objects.create(
#             category="Fiction",
#             idAuthorUser=CustomUser.objects.create(
#                 username="category_user",
#                 first_name="Category",
#                 last_name="User",
#                 email="category@example.com",
#                 telephone="1234567890",
#                 address="Category Address",
#                 is_staff=False,
#                 is_active=True
#             )
#         )
#
#         self.cover = Cover.objects.create(
#             cover="Hardcover",
#             img="covers/hardcover.jpg",
#             descriptioncover="Hardcover description",
#             idAuthorUser=CustomUser.objects.create(
#                 username="cover_user",
#                 first_name="Cover",
#                 last_name="User",
#                 email="cover@example.com",
#                 telephone="1234567890",
#                 address="Cover Address",
#                 is_staff=False,
#                 is_active=True
#             )
#         )
#
#         self.genre = Genre.objects.create(
#             namegenre="Science Fiction",
#             idAuthorUser=CustomUser.objects.create(
#                 username="genre_user",
#                 first_name="Genre",
#                 last_name="User",
#                 email="genre@example.com",
#                 telephone="1234567890",
#                 address="Genre Address",
#                 is_staff=False,
#                 is_active=True
#             )
#         )
#
#         self.writer = Writer.objects.create(
#             lastname="Asimov",
#             firstname="Isaac",
#             name="Isaac Asimov",
#             idAuthorUser=CustomUser.objects.create(
#                 username="writer_user",
#                 first_name="Writer",
#                 last_name="User",
#                 email="writer@example.com",
#                 telephone="1234567890",
#                 address="Writer Address",
#                 is_staff=False,
#                 is_active=True
#             )
#         )
#
#         self.custom_user_one = CustomUser.objects.create(
#             username="user_one",
#             first_name="User",
#             last_name="One",
#             email="user_one@example.com",
#             telephone="1234567890",
#             address="User One Address",
#             is_staff=False,
#             is_active=True
#         )
#
#         self.custom_user_two = CustomUser.objects.create(
#             username="user_two",
#             first_name="User",
#             last_name="Two",
#             email="user_two@example.com",
#             telephone="1234567890",
#             address="User Two Address",
#             is_staff=False,
#             is_active=True
#         )
#
#         self.book_one = Books.objects.create(
#             name="Book One",
#             description="Description of Book One",
#             idcategory=self.category,
#             idcover=self.cover,
#             idgenre=self.genre,
#             idwriter=self.writer,
#             idAuthorUser=self.custom_user_one
#         )
#
#         self.book_two = Books.objects.create(
#             name="Book Two",
#             description="Description of Book Two",
#             idcategory=self.category,
#             idcover=self.cover,
#             idgenre=self.genre,
#             idwriter=self.writer,
#             idAuthorUser=self.custom_user_two
#         )
#
#         self.order_request = OrderRequests.objects.create(
#             namebookrequest="Book Request",
#             booktorequest=self.book_one,
#             category=self.category,
#             userrequest=self.custom_user_one,
#             address="Request Address",
#             dateorder=datetime.now(),
#             canView=True
#         )
#
#     def test_create_orders(self):
#         """Тест на создание большого 21:10 количества заказов."""
#         for i in range(self.num_orders):
#             Orderbooks.objects.create(
#                 status=i % 2,  # Чередуем статусы 0 и 1
#                 bookone=self.book_one,
#                 booktwo=self.book_two,
#                 addressrequester=f"Address {i}",
#                 addressbookowner=f"Owner Address {i}",
#                 useridone=self.custom_user_one,
#                 useridonetoggle="1",
#                 useridtwo=self.custom_user_two,
#                 useridtwotoggle="1",
#                 dateorder=datetime.now(),
#                 idorder=self.order_request
#             )
#
#         # Проверяем, что все заказы созданы
#         self.assertEqual(Orderbooks.objects.count(), self.num_orders)
#
#     def test_read_orders(self):
#         """Тест на чтение большого количества заказов."""
#         # Сначала создаем заказы
#         self.test_create_orders()
#
#         # Читаем все заказы
#         orders = Orderbooks.objects.all()
#         self.assertEqual(len(orders), self.num_orders)
#
#     def test_update_orders(self):
#         """Тест на обновление большого количества заказов."""
#         # Сначала создаем заказы
#         self.test_create_orders()
#
#         # Обновляем данные для всех заказов
#         for i, order in enumerate(Orderbooks.objects.all()):
#             order.status = 1  # Обновляем статус
#             order.addressrequester = f"Updated Address {i}"
#             order.save()
#
#         # Проверяем, что данные обновлены
#         updated_order = Orderbooks.objects.first()
#         self.assertEqual(updated_order.status, 1)
#         self.assertEqual(updated_order.addressrequester, "Updated Address 0")
#
#     def test_delete_orders(self):
#         """Тест на удаление большого количества заказов."""
#         # Сначала создаем заказы
#         self.test_create_orders()
#
#         # Удаляем все заказы
#         Orderbooks.objects.all().delete()
#
#         # Проверяем, что все заказы удалены
#         self.assertEqual(Orderbooks.objects.count(), 0)
#
#     def tearDown(self):
#         """Очистка данных после каждого теста."""
#         Orderbooks.objects.all().delete()
#         OrderRequests.objects.all().delete()
#         Books.objects.all().delete()
#         CustomUser.objects.all().delete()
#         Category.objects.all().delete()
#         Cover.objects.all().delete()
#         Genre.objects.all().delete()
#         Writer.objects.all().delete()



#Нагрузочный тест для модели Writer
# class WriterLoadTest(TestCase):
#     def setUp(self):
#         """Подготовка данных перед каждым тестом."""
#         self.num_writers = 10000  # Количество писателей для теста
#
#         # Создаем пользователя, который будет связан с писателями
#         self.custom_user = CustomUser.objects.create(
#             username="test_user",
#             first_name="Test",
#             last_name="User",
#             email="test@example.com",
#             telephone="1234567890",
#             address="Test Address",
#             is_staff=False,
#             is_active=True
#         )
#
#     def test_create_writers(self):
#         """Тест на создание большого количества писателей."""
#         for i in range(self.num_writers):
#             Writer.objects.create(
#                 lastname=f"Lastname {i}",
#                 firstname=f"Firstname {i}",
#                 name=f"Name {i}",
#                 idAuthorUser=self.custom_user
#             )
#
#         # Проверяем, что все писатели созданы
#         self.assertEqual(Writer.objects.count(), self.num_writers)
#
#     def test_read_writers(self):
#         """Тест на чтение большого количества писателей."""
#         # Сначала создаем писателей
#         self.test_create_writers()
#
#         # Читаем всех писателей
#         writers = Writer.objects.all()
#         self.assertEqual(len(writers), self.num_writers)
#
#     def test_update_writers(self):
#         """Тест на обновление большого количества писателей."""
#         # Сначала создаем писателей
#         self.test_create_writers()
#
#         # Обновляем данные для всех писателей
#         for i, writer in enumerate(Writer.objects.all()):
#             writer.lastname = f"Updated Lastname {i}"
#             writer.firstname = f"Updated Firstname {i}"
#             writer.name = f"Updated Name {i}"
#             writer.save()
#
#         # Проверяем, что данные обновлены
#         updated_writer = Writer.objects.first()
#         self.assertEqual(updated_writer.lastname, "Updated Lastname 0")
#         self.assertEqual(updated_writer.firstname, "Updated Firstname 0")
#         self.assertEqual(updated_writer.name, "Updated Name 0")
#
#     def test_delete_writers(self):
#         """Тест на удаление большого количества писателей."""
#         # Сначала создаем писателей
#         self.test_create_writers()
#
#         # Удаляем всех писателей
#         Writer.objects.all().delete()
#
#         # Проверяем, что все писатели удалены
#         self.assertEqual(Writer.objects.count(), 0)
#
#     def tearDown(self):
#         """Очистка данных после каждого теста."""
#         Writer.objects.all().delete()
#         CustomUser.objects.all().delete()


#Нагрузочный тест для модели AuthUser
# class AuthUserLoadTest(TestCase):
#     def setUp(self):
#         # Подготовка данных перед каждым тестом
#         self.num_users = 100  # Количество пользователей для теста
#         self.username_prefix = "user_"
#         self.email_suffix = "@example.com"
#
#     def test_create_users(self):
#         """Тест на создание большого количества пользователей."""
#         for i in range(self.num_users):
#             AuthUser.objects.create(
#                 password=f"password_{i}",
#                 last_login=datetime.now(),
#                 is_superuser=0,
#                 username=f"{self.username_prefix}{i}",
#                 first_name=f"First_{i}",
#                 last_name=f"Last_{i}",
#                 email=f"{self.username_prefix}{i}{self.email_suffix}",
#                 is_staff=0,
#                 is_active=1,
#                 date_joined=datetime.now()
#             )
#
#         # Проверяем, что все пользователи созданы
#         self.assertEqual(AuthUser.objects.count(), self.num_users)
#
#     def test_read_users(self):
#         """Тест на чтение большого количества пользователей."""
#         # Сначала создаем пользователей
#         self.test_create_users()
#
#         # Читаем всех пользователей
#         users = AuthUser.objects.all()
#         self.assertEqual(len(users), self.num_users)
#
#     def test_update_users(self):
#         """Тест на обновление большого количества пользователей."""
#         # Сначала создаем пользователей
#         self.test_create_users()
#
#         # Обновляем данные для всех пользователей
#         for i in range(self.num_users):
#             user = AuthUser.objects.get(username=f"{self.username_prefix}{i}")
#             user.first_name = f"Updated_First_{i}"
#             user.save()
#
#         # Проверяем, что данные обновлены
#         updated_user = AuthUser.objects.get(username=f"{self.username_prefix}0")
#         self.assertEqual(updated_user.first_name, "Updated_First_0")
#
#     def test_delete_users(self):
#         """Тест на удаление большого количества пользователей."""
#         # Сначала создаем пользователей
#         self.test_create_users()
#
#         # Удаляем всех пользователей
#         AuthUser.objects.all().delete()
#
#         # Проверяем, что все пользователи удалены
#         self.assertEqual(AuthUser.objects.count(), 0)
#
#     def tearDown(self):
#         """Очистка данных после каждого теста."""
#         AuthUser.objects.all().delete()


#Нагрузочный тест для модели Books
# class BooksLoadTest(TestCase):
#     def setUp(self):
#         """Подготовка данных перед каждым тестом."""
#         self.num_books = 10000  # Количество книг для теста
#
#         # Создаем пользователя
#         self.custom_user = CustomUser.objects.create(
#             username="test_user",
#             first_name="Test",
#             last_name="User",
#             email="test@example.com",
#             telephone="1234567890",
#             address="Test Address",
#             is_staff=False,
#             is_active=True
#         )
#
#         # Создаем связанные объекты
#         self.category = Category.objects.create(
#             category="Fiction",
#             idAuthorUser=self.custom_user
#         )
#
#         self.cover = Cover.objects.create(
#             cover="Hardcover",
#             img="covers/hardcover.jpg",
#             descriptioncover="Hardcover description",
#             idAuthorUser=self.custom_user
#         )
#
#         self.genre = Genre.objects.create(
#             namegenre="Science Fiction",
#             idAuthorUser=self.custom_user
#         )
#
#         self.writer = Writer.objects.create(
#             lastname="Asimov",
#             firstname="Isaac",
#             name="Isaac Asimov",
#             idAuthorUser=self.custom_user
#         )
#
#     def test_create_books(self):
#         """Тест на создание большого количества книг."""
#         for i in range(self.num_books):
#             Books.objects.create(
#                 name=f"Book {i}",
#                 description=f"Description of Book {i}",
#                 idcategory=self.category,
#                 idcover=self.cover,
#                 idgenre=self.genre,
#                 idwriter=self.writer,
#                 idAuthorUser=self.custom_user
#             )
#
#         # Проверяем, что все книги созданы
#         self.assertEqual(Books.objects.count(), self.num_books)
#
#     def tearDown(self):
#         """Очистка данных после каждого теста."""
#         # Удаляем все объекты, начиная с зависимых
#         Books.objects.all().delete()
#         Genre.objects.all().delete()
#         Writer.objects.all().delete()
#         Cover.objects.all().delete()
#         Category.objects.all().delete()
#         CustomUser.objects.all().delete()