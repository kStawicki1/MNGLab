import unittest

from Lab1.EmailExtractor import EmailExtractor


class EmailExtractorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["szymon.oracz02@student.wat.edu.pl", True, True, "Szymon", "Oracz"],
            ["mariusz.pudzianowski@wat.edu.pl", False, True, "Mariusz", "Pudzianowski"],
            ["wojciech.zurakowski@student.wat.edu.pl", True, True, "Wojciech", "Zurakowski"],
            ["malgorzata.magical@wat.edu.pl", False, False, "Malgorzata", "Magical"],
            ["dorota.wellman@student.wat.edu.pl", True, False, "Dorota", "Wellman"],
            ["miroslawa.bieniek@wat.edu.pl", False, False, "Miroslawa", "Bieniek"],
            ["blanka.srajkow02@student.wat.edu.pl", True, False, "Blanka", "Srajkow"],
            ["edyta.gumiak@wat.edu.pl", False, False, "Edyta", "Gumiak"],
            ["krzysztof.kononowicz@student.wat.edu.pl", True, True, "Krzysztof", "Kononowicz"],
            ["adam.malysz102@wat.edu.pl", False, True, "Adam", "Malysz"],
        ]


    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                mail = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(mail)
                # expect
                self.assertEqual(is_student, extractor.is_student())



    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[2]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.is_male())


    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())
