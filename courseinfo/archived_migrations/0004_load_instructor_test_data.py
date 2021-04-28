from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

INSTRUCTORS = [

    {
        "first_name": "Leonard",
        "last_name": "Buckland",
        "disambiguator": ""
    },
    {
        "first_name": "Megan",
        "last_name": "Vance",
        "disambiguator": ""
    },
    {
        "first_name": "Blake",
        "last_name": "Ferguson",
        "disambiguator": ""
    },
    {
        "first_name": "Stephanie",
        "last_name": "Carr",
        "disambiguator": ""
    },
    {
        "first_name": "Jack",
        "last_name": "Hill",
        "disambiguator": ""
    },
    {
        "first_name": "Zoe",
        "last_name": "Sanderson",
        "disambiguator": ""
    },
    {
        "first_name": "Jasmine",
        "last_name": "Gray",
        "disambiguator": ""
    },
    {
        "first_name": "Amy",
        "last_name": "Scott",
        "disambiguator": ""
    },
    {
        "first_name": "Bella",
        "last_name": "Bailey",
        "disambiguator": ""
    },
    {
        "first_name": "Jennifer",
        "last_name": "Knox",
        "disambiguator": ""
    },
    {
        "first_name": "Anthony",
        "last_name": "Underwood",
        "disambiguator": ""
    },
    {
        "first_name": "Isaac",
        "last_name": "Reid",
        "disambiguator": ""
    },
    {
        "first_name": "Michelle",
        "last_name": "Blake",
        "disambiguator": ""
    },
    {
        "first_name": "Lily",
        "last_name": "Lewis",
        "disambiguator": ""
    },
    {
        "first_name": "Lauren",
        "last_name": "Walker",
        "disambiguator": ""
    },
    {
        "first_name": "Gabrielle",
        "last_name": "Lyman",
        "disambiguator": ""
    },
    {
        "first_name": "Anthony",
        "last_name": "Peake",
        "disambiguator": ""
    },
    {
        "first_name": "Carol",
        "last_name": "Scott",
        "disambiguator": ""
    },
    {
        "first_name": "Nicholas",
        "last_name": "Skinner",
        "disambiguator": ""
    },
    {
        "first_name": "Ella",
        "last_name": "Manning",
        "disambiguator": ""
    },
    {
        "first_name": "Dominic",
        "last_name": "Sanderson",
        "disambiguator": ""
    },
    {
        "first_name": "Colin",
        "last_name": "Dowd",
        "disambiguator": ""
    },
    {
        "first_name": "Theresa",
        "last_name": "Edmunds",
        "disambiguator": ""
    },
    {
        "first_name": "Michelle",
        "last_name": "Parsons",
        "disambiguator": ""
    },
    {
        "first_name": "Christopher",
        "last_name": "Greene",
        "disambiguator": ""
    },
    {
        "first_name": "Mary",
        "last_name": "Clark",
        "disambiguator": ""
    },
    {
        "first_name": "Kimberly",
        "last_name": "Berry",
        "disambiguator": ""
    },
    {
        "first_name": "Yvonne",
        "last_name": "Cameron",
        "disambiguator": ""
    },
    {
        "first_name": "Christian",
        "last_name": "Skinner",
        "disambiguator": ""
    },
    {
        "first_name": "Lillian",
        "last_name": "Poole",
        "disambiguator": ""
    },
    {
        "first_name": "Caroline",
        "last_name": "Alsop",
        "disambiguator": ""
    },
    {
        "first_name": "Nicholas",
        "last_name": "Underwood",
        "disambiguator": ""
    },
    {
        "first_name": "Rachel",
        "last_name": "Mackay",
        "disambiguator": ""
    },
    {
        "first_name": "Sebastian",
        "last_name": "Gibson",
        "disambiguator": ""
    },
    {
        "first_name": "Carol",
        "last_name": "Paige",
        "disambiguator": ""
    },
    {
        "first_name": "Simon",
        "last_name": "Buckland",
        "disambiguator": ""
    },
    {
        "first_name": "Faith",
        "last_name": "Tucker",
        "disambiguator": ""
    },
    {
        "first_name": "Anna",
        "last_name": "Vaughan",
        "disambiguator": ""
    },
    {
        "first_name": "Robert",
        "last_name": "Lewis",
        "disambiguator": ""
    },
    {
        "first_name": "Abigail",
        "last_name": "Paterson",
        "disambiguator": ""
    },
    {
        "first_name": "Victor",
        "last_name": "Poole",
        "disambiguator": ""
    },
    {
        "first_name": "Julian",
        "last_name": "Turner",
        "disambiguator": ""
    },
    {
        "first_name": "Leah",
        "last_name": "Marshall",
        "disambiguator": ""
    },
    {
        "first_name": "Boris",
        "last_name": "Knox",
        "disambiguator": ""
    },
    {
        "first_name": "Lillian",
        "last_name": "Bell",
        "disambiguator": ""
    },
    {
        "first_name": "Austin",
        "last_name": "McLean",
        "disambiguator": ""
    },
    {
        "first_name": "Stewart",
        "last_name": "Tucker",
        "disambiguator": ""
    },
    {
        "first_name": "Una",
        "last_name": "Nolan",
        "disambiguator": ""
    },
    {
        "first_name": "Claire",
        "last_name": "Wright",
        "disambiguator": ""
    },
    {
        "first_name": "Madeleine",
        "last_name": "Metcalfe",
        "disambiguator": ""
    },
    {
        "first_name": "Carol",
        "last_name": "Hodges",
        "disambiguator": ""
    },
    {
        "first_name": "Bella",
        "last_name": "Sharp",
        "disambiguator": ""
    },
    {
        "first_name": "Mary",
        "last_name": "Glover",
        "disambiguator": ""
    },
    {
        "first_name": "Joshua",
        "last_name": "Langdon",
        "disambiguator": ""
    },
    {
        "first_name": "Sophie",
        "last_name": "Hamilton",
        "disambiguator": ""
    },
    {
        "first_name": "Felicity",
        "last_name": "Welch",
        "disambiguator": ""
    },
    {
        "first_name": "Ella",
        "last_name": "May",
        "disambiguator": ""
    },
    {
        "first_name": "Katherine",
        "last_name": "Greene",
        "disambiguator": ""
    },
    {
        "first_name": "Blake",
        "last_name": "Wallace",
        "disambiguator": ""
    },
    {
        "first_name": "Nicholas",
        "last_name": "Sanderson",
        "disambiguator": ""
    },
    {
        "first_name": "Elizabeth",
        "last_name": "Langdon",
        "disambiguator": ""
    },
    {
        "first_name": "Megan",
        "last_name": "Pullman",
        "disambiguator": ""
    },
    {
        "first_name": "Joe",
        "last_name": "Morrison",
        "disambiguator": ""
    },
    {
        "first_name": "Ella",
        "last_name": "Lyman",
        "disambiguator": ""
    },
    {
        "first_name": "Sophie",
        "last_name": "Hemmings",
        "disambiguator": ""
    },
    {
        "first_name": "Maria",
        "last_name": "Carr",
        "disambiguator": ""
    },
    {
        "first_name": "Sean",
        "last_name": "Morgan",
        "disambiguator": ""
    },
    {
        "first_name": "Jack",
        "last_name": "Hudson",
        "disambiguator": ""
    },
    {
        "first_name": "Vanessa",
        "last_name": "Watson",
        "disambiguator": ""
    },
    {
        "first_name": "Grace",
        "last_name": "Dyer",
        "disambiguator": ""
    },
    {
        "first_name": "Natalie",
        "last_name": "Wright",
        "disambiguator": ""
    },
    {
        "first_name": "Felicity",
        "last_name": "Davies",
        "disambiguator": ""
    },
    {
        "first_name": "Yvonne",
        "last_name": "Manning",
        "disambiguator": ""
    },
    {
        "first_name": "Phil",
        "last_name": "North",
        "disambiguator": ""
    },
    {
        "first_name": "Lily",
        "last_name": "Rutherford",
        "disambiguator": ""
    },
    {
        "first_name": "Chloe",
        "last_name": "Hunter",
        "disambiguator": ""
    },
    {
        "first_name": "Bella",
        "last_name": "Black",
        "disambiguator": ""
    },
    {
        "first_name": "Ruth",
        "last_name": "Berry",
        "disambiguator": ""
    },
    {
        "first_name": "Stewart",
        "last_name": "Lee",
        "disambiguator": ""
    },
    {
        "first_name": "Bella",
        "last_name": "Peters",
        "disambiguator": ""
    },
    {
        "first_name": "Lisa",
        "last_name": "Wallace",
        "disambiguator": ""
    },
    {
        "first_name": "Oliver",
        "last_name": "Hudson",
        "disambiguator": ""
    },
    {
        "first_name": "Sarah",
        "last_name": "Manning",
        "disambiguator": ""
    },
    {
        "first_name": "Richard",
        "last_name": "Bond",
        "disambiguator": ""
    },
    {
        "first_name": "Cameron",
        "last_name": "Metcalfe",
        "disambiguator": ""
    },
    {
        "first_name": "Penelope",
        "last_name": "Clark",
        "disambiguator": ""
    },
    {
        "first_name": "Joshua",
        "last_name": "Kerr",
        "disambiguator": ""
    },
    {
        "first_name": "Una",
        "last_name": "Roberts",
        "disambiguator": ""
    },
    {
        "first_name": "Austin",
        "last_name": "Newman",
        "disambiguator": ""
    },
    {
        "first_name": "Neil",
        "last_name": "King",
        "disambiguator": ""
    },
    {
        "first_name": "Rachel",
        "last_name": "Sutherland",
        "disambiguator": ""
    },
    {
        "first_name": "Dylan",
        "last_name": "Nash",
        "disambiguator": ""
    },
    {
        "first_name": "Edward",
        "last_name": "Davidson",
        "disambiguator": ""
    },
    {
        "first_name": "Claire",
        "last_name": "Paige",
        "disambiguator": ""
    },
    {
        "first_name": "John",
        "last_name": "Bell",
        "disambiguator": ""
    },
    {
        "first_name": "Wanda",
        "last_name": "Ross",
        "disambiguator": ""
    },
    {
        "first_name": "Max",
        "last_name": "Howard",
        "disambiguator": ""
    },
    {
        "first_name": "Tracey",
        "last_name": "Walker",
        "disambiguator": ""
    },
    {
        "first_name": "Una",
        "last_name": "Mackay",
        "disambiguator": ""
    },
    {
        "first_name": "Lillian",
        "last_name": "MacLeod",
        "disambiguator": ""
    },
    {
        "first_name": "Lillian",
        "last_name": "Black",
        "disambiguator": ""
    },
    {
        "first_name": "Wendy",
        "last_name": "MacDonald",
        "disambiguator": ""
    },
    {
        "first_name": "Olivia",
        "last_name": "Stewart",
        "disambiguator": ""
    },
    {
        "first_name": "Carol",
        "last_name": "Gray",
        "disambiguator": ""
    },
    {
        "first_name": "Victoria",
        "last_name": "Brown",
        "disambiguator": ""
    },
    {
        "first_name": "Victor",
        "last_name": "Lee",
        "disambiguator": ""
    },
    {
        "first_name": "Kylie",
        "last_name": "Clarkson",
        "disambiguator": ""
    },
    {
        "first_name": "Vanessa",
        "last_name": "Dickens",
        "disambiguator": ""
    },
    {
        "first_name": "Boris",
        "last_name": "Hill",
        "disambiguator": ""
    },
    {
        "first_name": "Steven",
        "last_name": "Springer",
        "disambiguator": ""
    },
    {
        "first_name": "Olivia",
        "last_name": "Dickens",
        "disambiguator": ""
    },
    {
        "first_name": "Jonathan",
        "last_name": "Lewis",
        "disambiguator": ""
    },
    {
        "first_name": "Jane",
        "last_name": "Lyman",
        "disambiguator": ""
    },
    {
        "first_name": "John",
        "last_name": "Piper",
        "disambiguator": ""
    },
    {
        "first_name": "Colin",
        "last_name": "Davidson",
        "disambiguator": ""
    },
    {
        "first_name": "Gordon",
        "last_name": "Lawrence",
        "disambiguator": ""
    },
    {
        "first_name": "Neil",
        "last_name": "Morrison",
        "disambiguator": ""
    },
    {
        "first_name": "Michael",
        "last_name": "Peake",
        "disambiguator": ""
    },
    {
        "first_name": "Virginia",
        "last_name": "Powell",
        "disambiguator": ""
    },
    {
        "first_name": "Julia",
        "last_name": "Oliver",
        "disambiguator": ""
    },
    {
        "first_name": "Andrea",
        "last_name": "Jackson",
        "disambiguator": ""
    },
    {
        "first_name": "Julia",
        "last_name": "Ross",
        "disambiguator": ""
    },
    {
        "first_name": "Chloe",
        "last_name": "Watson",
        "disambiguator": ""
    },
    {
        "first_name": "Emily",
        "last_name": "Baker",
        "disambiguator": ""
    },
    {
        "first_name": "Colin",
        "last_name": "Howard",
        "disambiguator": ""
    },

]

def add_instructor_data(apps, schema_editor):
    instructor_class = apps.get_model('courseinfo', 'Instructor')
    for instructor in INSTRUCTORS:
        try:
            duplicate_object = instructor_class.objects.get(
                first_name=instructor['first_name'],
                last_name=instructor['last_name'],
                disambiguator=instructor['disambiguator']
            )
            print('Duplicate instructor entry not added to instructor table:', instructor['first_name'], instructor['last_name'])
        except ObjectDoesNotExist:
            instructor_object = instructor_class.objects.create(
                first_name=instructor['first_name'],
                last_name=instructor['last_name'],
                disambiguator=instructor['disambiguator']
            )

def remove_instructor_data(apps, schema_editor):
    instructor_class = apps.get_model('courseinfo', 'Instructor')
    for instructor in INSTRUCTORS:
        instructor_object = instructor_class.objects.get(
            first_name=instructor['first_name'],
            last_name=instructor['last_name'],
            disambiguator=instructor['disambiguator']
        )
        instructor_object.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0003_auto_20210221_1947'),
    ]

    operations = [
        migrations.RunPython(
            add_instructor_data,
            remove_instructor_data
        )
    ]
