functionality
Admin -
- Spaces - 
    - Add spaces we have available
        - Name
        - Image
        - Description
        - Price

    - Add new space users
        - Name / Company name
        - Email
        - Phone
        - active 

        - Add staff members of the company
        - Name
        - Phone
        - Company 


- Events - 
    -Add events 
    name
    time
    description
    itenary
    is_physical

    - Attendees
    name
    phone
    email
    event: many to many


- Tutoring
    - Course
    name
    description
    price
    duration

    - Facilitator
    Name
    Agreement_doc
    course - Many to many

    - Students
    name
    phone
    course -  Many to many

Finance:
