from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

STUDENTS = [
    {
        "first_name": "Elizabeth",
        "last_name": "Wilson",
        "disambiguator": ""
    },
    {
        "first_name": "Victor",
        "last_name": "Lewis",
        "disambiguator": ""
    },
    {
        "first_name": "Christopher",
        "last_name": "Paterson",
        "disambiguator": ""
    },
    {
        "first_name": "Nicola",
        "last_name": "Powell",
        "disambiguator": ""
    },
    {
        "first_name": "Ava",
        "last_name": "White",
        "disambiguator": ""
    },
    {
        "first_name": "Fiona",
        "last_name": "Bower",
        "disambiguator": ""
    },
    {
        "first_name": "Owen",
        "last_name": "Reid",
        "disambiguator": ""
    },
    {
        "first_name": "Lily",
        "last_name": "Miller",
        "disambiguator": ""
    },
    {
        "first_name": "Deirdre",
        "last_name": "Gill",
        "disambiguator": ""
    },
    {
        "first_name": "Neil",
        "last_name": "Marshall",
        "disambiguator": ""
    },
    {
        "first_name": "Emily",
        "last_name": "Sanderson",
        "disambiguator": ""
    },
    {
        "first_name": "Jessica",
        "last_name": "King",
        "disambiguator": ""
    },
    {
        "first_name": "Adrian",
        "last_name": "Ogden",
        "disambiguator": ""
    },
    {
        "first_name": "Gabrielle",
        "last_name": "Lee",
        "disambiguator": ""
    },
    {
        "first_name": "Joshua",
        "last_name": "Abraham",
        "disambiguator": ""
    },
    {
        "first_name": "Brian",
        "last_name": "Hill",
        "disambiguator": ""
    },
    {
        "first_name": "Bernadette",
        "last_name": "Buckland",
        "disambiguator": ""
    },
    {
        "first_name": "Theresa",
        "last_name": "Thomson",
        "disambiguator": ""
    },
    {
        "first_name": "Ella",
        "last_name": "Burgess",
        "disambiguator": ""
    },
    {
        "first_name": "Donna",
        "last_name": "James",
        "disambiguator": ""
    },
    {
        "first_name": "Audrey",
        "last_name": "Hudson",
        "disambiguator": ""
    },
    {
        "first_name": "Charles",
        "last_name": "Newman",
        "disambiguator": ""
    },
    {
        "first_name": "Adrian",
        "last_name": "Black",
        "disambiguator": ""
    },
    {
        "first_name": "Lucas",
        "last_name": "Wright",
        "disambiguator": ""
    },
    {
        "first_name": "Dorothy",
        "last_name": "McLean",
        "disambiguator": ""
    },
    {
        "first_name": "Stephen",
        "last_name": "Glover",
        "disambiguator": ""
    },
    {
        "first_name": "Gabrielle",
        "last_name": "Poole",
        "disambiguator": ""
    },
    {
        "first_name": "Owen",
        "last_name": "Edmunds",
        "disambiguator": ""
    },
    {
        "first_name": "Amelia",
        "last_name": "Bower",
        "disambiguator": ""
    },
    {
        "first_name": "Ava",
        "last_name": "Graham",
        "disambiguator": ""
    },
    {
        "first_name": "Adam",
        "last_name": "Taylor",
        "disambiguator": ""
    },
    {
        "first_name": "Lily",
        "last_name": "Ross",
        "disambiguator": ""
    },
    {
        "first_name": "Joseph",
        "last_name": "Skinner",
        "disambiguator": ""
    },
    {
        "first_name": "Grace",
        "last_name": "Greene",
        "disambiguator": ""
    },
    {
        "first_name": "Ryan",
        "last_name": "Parr",
        "disambiguator": ""
    },
    {
        "first_name": "Peter",
        "last_name": "Russell",
        "disambiguator": ""
    },
    {
        "first_name": "William",
        "last_name": "Mills",
        "disambiguator": ""
    },
    {
        "first_name": "Lucas",
        "last_name": "Sharp",
        "disambiguator": ""
    },
    {
        "first_name": "Chloe",
        "last_name": "Anderson",
        "disambiguator": ""
    },
    {
        "first_name": "Lisa",
        "last_name": "Bond",
        "disambiguator": ""
    },
    {
        "first_name": "Boris",
        "last_name": "Paterson",
        "disambiguator": ""
    },
    {
        "first_name": "Sam",
        "last_name": "Wilkins",
        "disambiguator": ""
    },
    {
        "first_name": "Max",
        "last_name": "Lyman",
        "disambiguator": ""
    },
    {
        "first_name": "Una",
        "last_name": "Pullman",
        "disambiguator": ""
    },
    {
        "first_name": "Austin",
        "last_name": "Wilkins",
        "disambiguator": ""
    },
    {
        "first_name": "Lucas",
        "last_name": "Powell",
        "disambiguator": ""
    },
    {
        "first_name": "Neil",
        "last_name": "Grant",
        "disambiguator": ""
    },
    {
        "first_name": "Maria",
        "last_name": "Piper",
        "disambiguator": ""
    },
    {
        "first_name": "Andrea",
        "last_name": "Walsh",
        "disambiguator": ""
    },
    {
        "first_name": "Anne",
        "last_name": "Clark",
        "disambiguator": ""
    },
    {
        "first_name": "Tim",
        "last_name": "Nolan",
        "disambiguator": ""
    },
    {
        "first_name": "Victor",
        "last_name": "Welch",
        "disambiguator": ""
    },
    {
        "first_name": "Alan",
        "last_name": "Davidson",
        "disambiguator": ""
    },
    {
        "first_name": "Charles",
        "last_name": "Churchill",
        "disambiguator": ""
    },
    {
        "first_name": "Jessica",
        "last_name": "Duncan",
        "disambiguator": ""
    },
    {
        "first_name": "Lucas",
        "last_name": "Martin",
        "disambiguator": ""
    },
    {
        "first_name": "Maria",
        "last_name": "Arnold",
        "disambiguator": ""
    },
    {
        "first_name": "Sophie",
        "last_name": "Clark",
        "disambiguator": ""
    },
    {
        "first_name": "Jacob",
        "last_name": "Bailey",
        "disambiguator": ""
    },
    {
        "first_name": "Harry",
        "last_name": "Churchill",
        "disambiguator": ""
    },
    {
        "first_name": "Karen",
        "last_name": "Lyman",
        "disambiguator": ""
    },
    {
        "first_name": "Trevor",
        "last_name": "Hunter",
        "disambiguator": ""
    },
    {
        "first_name": "Stephen",
        "last_name": "Lee",
        "disambiguator": ""
    },
    {
        "first_name": "Vanessa",
        "last_name": "Underwood",
        "disambiguator": ""
    },
    {
        "first_name": "Richard",
        "last_name": "Kelly",
        "disambiguator": ""
    },
    {
        "first_name": "Amelia",
        "last_name": "Campbell",
        "disambiguator": ""
    },
    {
        "first_name": "Zoe",
        "last_name": "McLean",
        "disambiguator": ""
    },
    {
        "first_name": "Sam",
        "last_name": "Forsyth",
        "disambiguator": ""
    },
    {
        "first_name": "Phil",
        "last_name": "Wright",
        "disambiguator": ""
    },
    {
        "first_name": "Maria",
        "last_name": "Hudson",
        "disambiguator": ""
    },
    {
        "first_name": "Diana",
        "last_name": "Mackay",
        "disambiguator": ""
    },
    {
        "first_name": "Stewart",
        "last_name": "Ellison",
        "disambiguator": ""
    },
    {
        "first_name": "Sue",
        "last_name": "Edmunds",
        "disambiguator": ""
    },
    {
        "first_name": "Karen",
        "last_name": "Ogden",
        "disambiguator": ""
    },
    {
        "first_name": "Carol",
        "last_name": "Martin",
        "disambiguator": ""
    },
    {
        "first_name": "Oliver",
        "last_name": "Wilkins",
        "disambiguator": ""
    },
    {
        "first_name": "Adam",
        "last_name": "Bower",
        "disambiguator": ""
    },
    {
        "first_name": "Katherine",
        "last_name": "Clarkson",
        "disambiguator": ""
    },
    {
        "first_name": "Carol",
        "last_name": "Turner",
        "disambiguator": ""
    },
    {
        "first_name": "Ian",
        "last_name": "James",
        "disambiguator": ""
    },
    {
        "first_name": "Una",
        "last_name": "McLean",
        "disambiguator": ""
    },
    {
        "first_name": "Heather",
        "last_name": "Clark",
        "disambiguator": ""
    },
    {
        "first_name": "Liam",
        "last_name": "Ellison",
        "disambiguator": ""
    },
    {
        "first_name": "Madeleine",
        "last_name": "Gill",
        "disambiguator": ""
    },
    {
        "first_name": "Warren",
        "last_name": "Berry",
        "disambiguator": ""
    },
    {
        "first_name": "Yvonne",
        "last_name": "Lyman",
        "disambiguator": ""
    },
    {
        "first_name": "Claire",
        "last_name": "Abraham",
        "disambiguator": ""
    },
    {
        "first_name": "Andrea",
        "last_name": "Hemmings",
        "disambiguator": ""
    },
    {
        "first_name": "Claire",
        "last_name": "Clarkson",
        "disambiguator": ""
    },
    {
        "first_name": "Max",
        "last_name": "Mackenzie",
        "disambiguator": ""
    },
    {
        "first_name": "Luke",
        "last_name": "Ince",
        "disambiguator": ""
    },
    {
        "first_name": "Samantha",
        "last_name": "Tucker",
        "disambiguator": ""
    },
    {
        "first_name": "James",
        "last_name": "Lewis",
        "disambiguator": ""
    },
    {
        "first_name": "Wendy",
        "last_name": "Cornish",
        "disambiguator": ""
    },
    {
        "first_name": "Evan",
        "last_name": "Hamilton",
        "disambiguator": ""
    },
    {
        "first_name": "Caroline",
        "last_name": "Lee",
        "disambiguator": ""
    },
    {
        "first_name": "Stephanie",
        "last_name": "Smith",
        "disambiguator": ""
    },
    {
        "first_name": "Lily",
        "last_name": "Jones",
        "disambiguator": ""
    },
    {
        "first_name": "Melanie",
        "last_name": "Peake",
        "disambiguator": ""
    },
    {
        "first_name": "Richard",
        "last_name": "Smith",
        "disambiguator": ""
    },
    {
        "first_name": "Neil",
        "last_name": "Randall",
        "disambiguator": ""
    },
    {
        "first_name": "John",
        "last_name": "Quinn",
        "disambiguator": ""
    },
    {
        "first_name": "Emma",
        "last_name": "Bell",
        "disambiguator": ""
    },
    {
        "first_name": "Stephanie",
        "last_name": "Forsyth",
        "disambiguator": ""
    },
    {
        "first_name": "Claire",
        "last_name": "Young",
        "disambiguator": ""
    },
    {
        "first_name": "Felicity",
        "last_name": "Avery",
        "disambiguator": ""
    },
    {
        "first_name": "Robert",
        "last_name": "Glover",
        "disambiguator": ""
    },
    {
        "first_name": "Paul",
        "last_name": "Tucker",
        "disambiguator": ""
    },
    {
        "first_name": "Abigail",
        "last_name": "Morrison",
        "disambiguator": ""
    },
    {
        "first_name": "Carl",
        "last_name": "Ross",
        "disambiguator": ""
    },
    {
        "first_name": "Jack",
        "last_name": "Parr",
        "disambiguator": ""
    },
    {
        "first_name": "Owen",
        "last_name": "Ogden",
        "disambiguator": ""
    },
    {
        "first_name": "Grace",
        "last_name": "Ball",
        "disambiguator": ""
    },
    {
        "first_name": "Felicity",
        "last_name": "Hill",
        "disambiguator": ""
    },
    {
        "first_name": "Dylan",
        "last_name": "Fisher",
        "disambiguator": ""
    },
    {
        "first_name": "Angela",
        "last_name": "Black",
        "disambiguator": ""
    },
    {
        "first_name": "Carolyn",
        "last_name": "Murray",
        "disambiguator": ""
    },
    {
        "first_name": "Michelle",
        "last_name": "Morrison",
        "disambiguator": ""
    },
    {
        "first_name": "Penelope",
        "last_name": "Glover",
        "disambiguator": ""
    },
    {
        "first_name": "Frank",
        "last_name": "Newman",
        "disambiguator": ""
    },
    {
        "first_name": "Penelope",
        "last_name": "Blake",
        "disambiguator": ""
    },
    {
        "first_name": "Theresa",
        "last_name": "Russell",
        "disambiguator": ""
    },
    {
        "first_name": "Trevor",
        "last_name": "Cameron",
        "disambiguator": ""
    },
    {
        "first_name": "Stephen",
        "last_name": "Cornish",
        "disambiguator": ""
    },
    {
        "first_name": "Anthony",
        "last_name": "Parr",
        "disambiguator": ""
    },
]


def add_student_data(apps, schema_editor):
    student_class = apps.get_model('courseinfo', 'Student')
    for student in STUDENTS:
        try:
            duplicate_object = student_class.objects.get(
                first_name=student['first_name'],
                last_name=student['last_name'],
                disambiguator=student['disambiguator']
            )
            print('Duplicate student entry not added to instructor table:', student['first_name'], student['last_name'])
        except ObjectDoesNotExist:
            student_object = student_class.objects.create(
                first_name=student['first_name'],
                last_name=student['last_name'],
                disambiguator=student['disambiguator']
            )


def remove_student_data(apps, schema_editor):
    student_class = apps.get_model('courseinfo', 'Student')
    for student in STUDENTS:
        student_object = student_class.objects.get(
            first_name=student['first_name'],
            last_name=student['last_name'],
            disambiguator=student['disambiguator']
        )
        student_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0004_load_instructor_test_data'),
    ]

    operations = [
        migrations.RunPython(
            add_student_data,
            remove_student_data
        )
    ]
