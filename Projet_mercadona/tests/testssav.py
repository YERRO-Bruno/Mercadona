from django.test import TestCase
from mercadona.models import Category

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(label="TestCategory")

    def test_create_category(self):
        self.assertEqual(self.category.label, "TestCategory")

    def test_create_category_existante(self):
        self.category = Category.create_category("label")
        self.assertIsNone(self.category)

    def test_create_category_empty_label(self):
        self.category = Category.create_category("")
        self.assertIsNone(self.category)

    def test_update_category(self):
        self.category = Category.update_category(self=Category(), category_id=self.category.id, label="NouveauLabel")
        category_updated = Category.objects.get(id=self.category.id)
        self.assertEqual(category_updated.label, "NouveauLabel")

    def test_update_category_inexistent(self):
        self.category = Category.update_category(self=Category(), category_id=12345, label="NewCategoryLabel")
        self.assertIsNone(self.category)

    def test_delete_category(self):
        # id_deleted = self.category.id
        # Category.delete_category(self=Category(), category_id=self.category.id)
        # category_deleted = Category.objects.get(id=self.category.id)
        is_delete = Category.delete_category(self=Category(), category_id=self.category.id)
        self.assertTrue(is_delete)

    def test_delete_category_inexistante(self):
        is_deleted = Category.delete_category(self=Category(), category_id=12345)
        self.assertFalse(is_deleted)