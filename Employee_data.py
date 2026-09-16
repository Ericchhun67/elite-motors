""" 
seed employee database
date: 2026-09/13
1. employee_id
2. first_name
3. last_name
4. hire_date
5. position
6. department
7. bio
"""

from datetime import date

# management employee list here
management_employees = [
    {
        "employee_id": 12345,
        "first_name": "Mariah",
        "last_name": "Johnson",
        "hire_date": date(2026, 9, 13),
        "position": "CEO",
        "department": "Management",
        "bio": ("The chief executive officer of the company."
                "She has a wealth of experience in leading organizations."
        ),
        "imagefile": "img/mariah_johnson.jpg",
    },
    {
        "employee_id": 12346,
        "first_name": "Eric",
        "last_name": "Williams",
        "hire_date": date(2026, 9, 13),
        "position": "CFO",
        "department": "Management",
        "bio": ("The chief financial officer of the company."
                "He has extensive experience in financial management."
        ),
        "imagefile": "img/management/eric_williams.jpg",
    },
    {
        "employee_id": 12347,
        "first_name": "Sarah",
        "last_name": "Connor",
        "hire_date": date(2026, 9, 13),
        "position": "Lead Manager",
        "department": "Management",
        "bio": ("The chief operating officer of the company."
                "She has extensive experience in operations management."
        ),
        "imagefile": "img/management/sarah_connor.jpg",
    },
    {
        "employee_id": 12353,
        "first_name": "John",
        "last_name": "Doe",
        "hire_date": date(2026, 9, 13),
        "position": "AM manager",
        "department": "Management",
        "bio": ("An experienced employee in the management team."
                "He has been leading several successful projects"
            ),
        "imagefile": "img/management/john_doe.jpg",
    },
    {
        "employee_id": 23423,
        "first_name": "Jane",
        "last_name": "Smith",
        "hire_date": date(2026, 9, 13),
        "position": "HR manager",
        "department": "Management",
        "bio": ("A new addition to the management team. She is the hiring manager."
                "She has a strong background in human resources."
        )
    },
    {
        "employee_id": 34524,
        "first_name": "Alice",
        "last_name": "Harris",
        "hire_date": date(2026, 9, 13),
        "position": "Intern",
        "department": "Management",
        "bio": ("A intern in the management team."
                "she is learning quickly and contributing to the team."
        )
    },
    {
        "employee_id": 45678,
        "first_name": "Laura",
        "last_name": "Adams",
        "hire_date": date(2026, 9, 13),
        "position": "Project Manager",
        "department": "Management",
        "bio": ("A key member of the management team."
                "She has a strong background in project management."
        )
    },
    {
        "employee_id": 45433,
        "first_name": "Michael",
        "last_name": "Scott",
        "hire_date": date(2026, 9, 13),
        "position": "Senior Manager",
        "department": "Management",
        "bio": ("A senior member of the management team."
                "He has extensive experience in strategic planning."
        )
    }
]

# sales employee list
sale_team = [
    {
        "employee_id": 45678,
        "first_name": "Bob",
        "last_name": "Johnson",
        "hire_date": date(2026, 9, 13),
        "position": "Sales Representative",
        "department": "Sales",
        "bio": ("A new addition to the sales team."
                "He is eager to contribute to the team's success."
                "He's great at building client relationships and closing deals."
        )
    },
    {
        "employee_id": 56789,
        "first_name": "Charlie",
        "last_name": "Brown",
        "hire_date": date(2026, 9, 13),
        "position": "Sales Executive",
        "department": "Sales",
        "bio": ("An experienced member of the sales team."
                "He has a proven track record of achieving sales targets."
        )
    },
    {
        "employee_id": 67890,
        "first_name": "Diana",
        "last_name": "Prince",
        "hire_date": date(2026, 9, 13),
        "position": "Sales Manager",
        "department": "Sales",
        "bio": ("A dedicated member of the sales team."
                "She consistently meets her sales goals and supports her colleagues."
        )
    },
    {
        "employee_id": 78093,
        "first_name": "Ethan",
        "last_name": "Hunt",
        "hire_date": date(2026, 9, 13),
        "position": "Sales Associate",
        "department": "Sales",
        "bio": ("A new addition to the sales team."
                "He is eager to contribute to the team's success."
        )
    }
]

# Engineering employee list here 
Enginnering_team = [
    {
        "employee_id": 65433,
        "first_name": "Eve",
        "last_name": "Williams",
        "hire_date": date(2026, 9, 13),
        "position": "backendSoftware Engineer",
        "department": "Engineering",
        "bio": ("A new addition to the engineering team."
                "She is eager to contribute to engineering projects."
        )
    },
    {
        "employee_id": 69876,
        "first_name": "Fiona",
        "last_name": "Gallagher",
        "hire_date": date(2026, 9, 13),
        "position": "Frontend Software Engineer",
        "department": "Engineering",
        "bio": ("A new addition to the engineering team."
                "She is eager to contribute to engineering projects."
        )
    },
    {
        "employee_id": 71234,
        "first_name": "George",
        "last_name": "Harrison",
        "hire_date": date(2026, 9, 13),
        "position": "Software Engineer",
        "department": "Engineering",
        "bio": ("A new addition to the engineering team."
                "He is eager to contribute to engineering projects."
        )
    },
    {
        "employee_id": 76544,
        "first_name": "Frank",
        "last_name": "Miller",
        "hire_date": date(2026, 9, 13),
        "position": "Hardware Engineer",
        "department": "Engineering",
        "bio": ("Assembling parts as a member of the engineering team."
                "He is dedicated to ensuring high-quality work."
        )
    },
    {
        "employee_id": 87433,
        "first_name": "Grace",
        "last_name": "Lee",
        "hire_date": date(2026, 9, 13),
        "position": "DevOps Engineer",
        "department": "Engineering",
        "bio": ("A new addition to the engineering team."
                "She is quickly adapting and making valuable contributions."
        )
    }
]

# Design employee list
design_team = [
    {
        "employee_id": 98765,
        "first_name": "Hannah",
        "last_name": "Taylor",
        "position": "UI/UX Designer",
        "department": "Design",
        "hire_date": date(2026, 9, 13),
        "bio": ("A new addition to the design team."
                "She is eager to contribute to design projects."
        )
    },
    {
        "employee_id": 99876,
        "first_name": "Ian",
        "last_name": "Clark",
        "position": "Graphic Designer",
        "department": "Design",
        "hire_date": date(2026, 9, 13),
        "bio": ("A dedicated member of the design team."
                "He consistently delivers high-quality design work."
        )
    }
]


# Marketing employee list
marketing_team = [
    {
        "employee_id": 10987,
        "first_name": "Jack",
        "last_name": "Anderson",
        "hire_date": date(2026, 9, 13),
        "position": "Marketing Specialist",
        "department": "Marketing",
        "bio": ("Jack is a great addition to the marketing team."
                "He's been instrumental in driving marketing campaigns."
        )
    },
    {
        "employee_id": 11098,
        "first_name": "Karen",
        "last_name": "Smith",
        "hire_date": date(2026, 9, 13),
        "position": "Marketing Coordinator",
        "department": "Marketing",
        "bio": ("Karen is a new addition to the marketing team."
                "She is eager to contribute to marketing initiatives."
            )
    },
    {
        "employee_id": 11109,
        "first_name": "Leo",
        "last_name": "Martinez",
        "hire_date": date(2026, 9, 13),
        "position": "Marketing Analyst",
        "department": "Marketing",
        "bio": ("Leo is a new addition to the marketing team."
                "He is excited to bring fresh ideas to the team."
        )
    }
]
