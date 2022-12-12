from odoo.tests.common import TransactionCase

class TestBook(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, *kwargs)
        user_admin = self.env.ref("base.user_admin")
        self.env = self.env(user=user_admin)
        self.Book = self.env["library.book"]
        self.book1 = self.Book.create({
            "name": "Book name",
            "isbn": "879-1-78439-279-6"
            })
        return result
    def test_book_create(self):
        "Los libros nuevos están activados por defecto"
        self.assertEqual(
                self.book1.active, True
                )
    def test_check_isbn(self):
        "Comprobando ISBN"
        self.assertTrue(self.book1._check_isbn)


        
