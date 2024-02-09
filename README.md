# Project_101
Endpoint to receive GET, POST and DELETE request from users to manage students 

# Sample Request Below: 

# Create a Student resource
curl --location 'http://localhost:8100/students/' \
--header 'Content-Type: application/json' \
--data '{"name":"Uchechi Nwankwo","age":31,"sex":"Female","height":150.0}'

# Delete a Student resource
curl --location --request DELETE 'http://localhost:8100/students/1'

# Retrieve a Student resource (one student) 
curl --location 'http://localhost:8100/students/2'

# Retrieve a Student resource (All student) 
curl --location 'http://localhost:8100/students/'


