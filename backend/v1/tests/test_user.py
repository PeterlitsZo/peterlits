from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

import re
from pathlib import Path

from v1.models import User


class UserTest(TestCase):

    def delete_all_imgs_in_img_folder(self):
        imgpath = Path(settings.MEDIA_ROOT) / 'img'
        for sub_path in imgpath.iterdir():
            if sub_path.is_dir():
                for img in sub_path.iterdir():
                    img.unlink()
            else:
                sub_path.unlink()

    # Test 001: Test create and its __str__ method
    ###############################################################################################

    def test_create_and_its_name_1(self):
        user = User(
            name="Peterlits",
            email="peterlits@outlook.com",
            # in really programme it hold it after hash it with sald
            password="XXXXXXXXXXXXXXXXXXXXXX"
        )
        user.save()
        self.assertIs(str(user), "Peterlits")

    # Test 002: Test the email is right or not
    ###############################################################################################

    def test_good_email_1(self):
        user = User(name="Peterlits", email="not-a*email", password="1234234")
        try:
            user.save()
        except ValidationError as e:
            self.assertEqual(e.message_dict['email'][0], 'Enter a valid email address.')

    # Test 003: Make sure the name and the email is unique.
    ###############################################################################################

    def test_unique_email_and_name_1(self):
        user1 = User(name="Peterlits", email="p@e.ter1", password="1231453")
        user2 = User(name="Peterlits", email="p@e.ter2", password="2342342")
        try:
            user1.save()
            user2.save()
        except ValidationError as e:
            self.assertEqual(str(e), "{'name': ['User with this Name already exists.']}")

    def test_unique_email_and_name_2(self):
        user1 = User(name="pppp", email="p@e.ter", password="1241235")
        user2 = User(name="eeee", email="p@e.ter", password="3243453")
        try:
            user1.save()
            user2.save()
        except ValidationError as e:
            self.assertEqual(str(e), "{'email': ['User with this Email already exists.']}")

    # Test 004: Which name is good enough
    ###############################################################################################

    def test_not_a_good_name_1(self):
        user1 = User(name="  not  a   good   name  ", email="p@e.ter", password="3424532432")
        user2 = User(name="not a good name ", email="p@e.ter", password="3424532432")
        user3 = User(name="  not a good name", email="p@e.ter", password="3424532432")
        user4 = User(name="not   a   good   name", email="p@e.ter", password="3424532432")
        try:
            user1.save()
        except ValidationError as e:
            self.assertEqual(
                e.message_dict['name'][0],
                f'Name {repr("  not  a   good   name  ")} is not vaild, please let it '
                'only has the Chinese '
                'characters or English characters and the space is only in two non-space '
                'characters which has max length: 1.'
            )
        try:
            user2.save()
        except ValidationError as e:
            self.assertEqual(
                e.message_dict['name'][0],
                f'Name {repr("not a good name ")} is not vaild, please let it '
                'only has the Chinese '
                'characters or English characters and the space is only in two non-space '
                'characters which has max length: 1.'
            )
        try:
            user3.save()
        except ValidationError as e:
            self.assertEqual(
                e.message_dict['name'][0],
                f'Name {repr("  not a good name")} is not vaild, please let it '
                'only has the Chinese '
                'characters or English characters and the space is only in two non-space '
                'characters which has max length: 1.'
            )
        try:
            user4.save()
        except ValidationError as e:
            self.assertEqual(
                e.message_dict['name'][0],
                f'Name {repr("not  a   good   name")} is not vaild, please let it '
                'only has the Chinese '
                'characters or English characters and the space is only in two non-space '
                'characters which has max length: 1.'
            )

    # Test 006: About Password
    ###############################################################################################

    def test_password_short_1(self):
        user = User(name="Peterlits", email="pet@er.com", password="Hello")
        try:
            user.save()
        except ValidationError as e:
            self.assertEqual(
                e.message_dict['password'][0],
                'Password is too short (< 6), please re-enter.'
            )
        else:
            raise ValueError('There should raise a Error but it is not')

    def test_password_1(self):
        user1 = User(name="Peter", email="p@e.ter", password="TestTest")
        self.assertEqual(user1.password, "TestTest")
        user1.save()
        self.assertNotEqual(user1.password, "TestTest")
        self.assertTrue(user1.check_password("TestTest"))
        self.assertFalse(user1.check_password("TestTest..."))

    # Test 007: Upload Image
    ###############################################################################################

    def test_upload_img_1(self):
        f = SimpleUploadedFile(
            "test.svg",
            open(Path(__file__).parent / "Peterlits.min.svg", 'rb').read()
        )
        user1 = User(name="Peter1", email="p1@et.er", password="TestTest", headpic=f)
        user1.save()

    def test_upload_img_2(self):
        self.delete_all_imgs_in_img_folder()

        # the number that in statics/img
        imgpath = Path(settings.MEDIA_ROOT) / 'img'
        old_len = 0
        for sub_path in imgpath.iterdir():
            if sub_path.is_dir():
                for img in sub_path.iterdir():
                    old_len += 1

        # upload file
        f = SimpleUploadedFile(
            "test.svg",
            open(Path(__file__).parent / "Peterlits.min.svg", 'rb').read()
        )
        user1 = User(name="Peter1", email="p1@et.er", password="TestTest", headpic=f)
        user1.save()

        # assert new_len = old_len + 1
        new_len = 0
        for sub_path in imgpath.iterdir():
            if sub_path.is_dir():
                for img in sub_path.iterdir():
                    new_len += 1
        self.assertEqual(new_len, old_len + 1)

        # upload file
        f = SimpleUploadedFile(
            "test.svg",
            open(Path(__file__).parent / "Peterlits.min.svg", 'rb').read()
        )
        user2 = User(name="Peter2", email="p2@et.er", password="TestTest", headpic=f)
        user2.save()

        # assert new_len = old_len + 1
        new_new_len = 0
        for sub_path in imgpath.iterdir():
            if sub_path.is_dir():
                for img in sub_path.iterdir():
                    new_new_len += 1
        self.assertEqual(new_new_len, new_len)
