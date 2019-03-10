from django.test import TestCase,Client

from .models import Student
# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='test',
            sex=1,
            email='4234@qq.com',
            profession='程序员',
            qq='3333',
            phone='2222'
        )
    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='test2',
            sex=1,
            email="4545@qq.com",
            profession="项目经理",
            qq='1231',
            phone='123122'
        )
        self.assertEqual(student.sex_show, '男', '性别字段不一致！')

    def test_filter(self):
        Student.objects.create(
            name='test2',
            sex=1,
            email="4545@qq.com",
            profession="项目经理",
            qq='1231',
            phone='123122'
        )
        name = 'test'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, "应该只存在一个名称为{}的字段".format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_post',
            sex=1,
            email="4545@qq.com",
            profession="项目经理",
            qq='1231',
            phone='123122'
        )
        response = client.post('/',data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertTrue(b'test_post' in response.content,
                        'response content must contain `test_post`')