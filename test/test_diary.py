import unittest

from diary_app import diary
from diary_app.diary import diary


class TestDiary(unittest.TestCase):
    def test_diary_creation(self):
        my_diary = diary("joshua", "j123Jayty")
        self.assertIsInstance(my_diary, diary)
        self.assertTrue(my_diary)

    def test_that_diary_has_no_entry_at_creation(self):
        my_diary = diary("joshua", "j123Jayty")
        self.assertIsInstance(my_diary, diary)
        self.assertTrue(my_diary)
        self.assertEqual(0, len(my_diary.entries))

    def test_diary_has_username(self):
        my_diary = diary("joshua", "j123jayty")
        my_diary.get_username()
        self.assertEqual("joshua", my_diary.get_username())

    def test_diary_has_password(self):
        my_diary = diary("joshua", "23wearit78")
        self.assertTrue(my_diary.validatePassword("23wearit78"))

    def test_diary_can_be_locked(self):
        my_diary = diary("joshua", "23wearit78")
        self.assertFalse(my_diary.is_diary_locked())
        my_diary.lockDiary()
        self.assertTrue(my_diary.is_diary_locked())

    def test_diary_can_be_locked_new_entries_cannot_be_created(self):
        my_diary = diary("joshua", "23wearit78")
        self.assertFalse(my_diary.is_diary_locked())
        my_diary.lockDiary()
        self.assertTrue(my_diary.is_diary_locked())
        my_diary.createEntry("new Title", "new Body")

    def test_diary_is_unlocked_create_three_new_entries_one_new_entry_can_be_deleted(self):
        my_diary = diary("David", "27wearit78")
        my_diary.createEntry("new Title", "new Body")
        my_diary.createEntry("new Title", "new Body")
        my_diary.createEntry("new Title", "new Body")
        self.assertFalse(my_diary.is_diary_locked())
        my_diary.deleteEntry(1)
        self.assertEqual(2, len(my_diary.entries))

    def test_diary_is_unlocked_create_three_new_entries_lock_diary_entry_cannot_be_deleted(self):
        my_diary = diary("David", "27wearit78")
        my_diary.createEntry("new Title", "new Body")
        my_diary.createEntry("new Title", "new Body")
        my_diary.createEntry("new Title", "new Body")
        self.assertFalse(my_diary.is_diary_locked())
        my_diary.lockDiary()
        self.assertTrue(my_diary.is_diary_locked())
        with self.assertRaises(ValueError):
            my_diary.deleteEntry(2)
        self.assertEqual(3, len(my_diary.entries))

    def test_diary_is_unlocked_create_three_new_entries_delete_entry_id_two_twice_element_does_not_exist(self):
        my_diary = diary("David", "27wearit78")
        self.assertFalse(my_diary.is_diary_locked())
        my_diary.createEntry("first Title", "first Body")
        my_diary.createEntry("second Title", "second Body")
        my_diary.createEntry("third Title", "third Body")
        self.assertEqual(3, len(my_diary.entries))
        my_diary.lockDiary()
        my_diary.unlockDiary("27wearit78")
        self.assertFalse(my_diary.is_diary_locked())
        my_diary.deleteEntry(1)
        self.assertEqual(2, len(my_diary.entries))
        with self.assertRaises(ValueError):
            my_diary.deleteEntry(1)
        self.assertEqual(2, len(my_diary.entries))

    def test_diary_is_locked_validate_password_to_unlock_create_three_new_entries_delete_entry(self):
        my_diary = diary("David", "27wearit78")
        self.assertTrue(my_diary.validatePassword("27wearit78"))
        my_diary.lockDiary()
        self.assertTrue(my_diary.is_diary_locked())
        my_diary.createEntry("first Title", "first Body")
        my_diary.createEntry("second Title", "second Body")
        my_diary.createEntry("third Title", "third Body")
        self.assertEqual(3, len(my_diary.entries))
        self.assertTrue(my_diary.is_diary_locked())
        my_diary.unlockDiary("27wearit78")

    def test_that_entry_can_be_found_by_entry_id(self):
        my_diary = diary("David", "27wearit78")
        my_diary.createEntry("first Title", "first Body")
        my_diary.createEntry("second Title", "second Body")
        my_diary.createEntry("third Title", "third Body")
        self.assertEqual(3, len(my_diary.entries))
        self.assertTrue(my_diary.getEntryById(1))
        self.assertTrue(my_diary.getEntryById(2))
        self.assertTrue(my_diary.getEntryById(3))

    def test_entry_can_be_updated_when_diary_is_not_locked_validate_pin(self):
        my_diary = diary("David", "27wearit78")
        my_diary.createEntry("first Title", "first Body")
        my_diary.createEntry("second Title", "second Body")
        my_diary.createEntry("third Title", "third Body")
        self.assertEqual(3, len(my_diary.entries))
        first_entry = my_diary.getEntryById(1)
        first_entry.getTitle()
        self.assertEqual("first Title", first_entry.getTitle())
        self.assertEqual("first Body", first_entry.getBody())
        my_diary.update_entry(1, "new first Title", "new first Body")
        self.assertEqual("new first Title", first_entry.getTitle())
        self.assertEqual("new first Body", first_entry.getBody())

    def test_entry_cannot_be_updated_when_diary_is_locked(self):
        my_diary = diary("David", "27wearit78")
        my_diary.createEntry("first Title", "first Body")
        my_diary.createEntry("second Title", "second Body")
        my_diary.createEntry("third Title", "third Body")
        self.assertEqual(3, len(my_diary.entries))
        first_entry = my_diary.getEntryById(1)
        first_entry.getTitle()
        self.assertEqual("first Title", first_entry.getTitle())
        self.assertEqual("first Body", first_entry.getBody())
        my_diary.lockDiary()
        with self.assertRaises(ValueError):
            my_diary.update_entry(1, "new first Title", "new first Body")
        my_diary.unlockDiary("27wearit78")
        my_diary.update_entry(1, "new first Title", "new first Body")
        self.assertEqual("new first Title", first_entry.getTitle())
        self.assertEqual("new first Body", first_entry.getBody())
