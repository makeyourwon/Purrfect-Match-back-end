# Purrfect-Match-back-end
<img width="1465" alt="Purrfect_match main" src="https://github.com/makeyourwon/Purrfect-Match-back-end/assets/149891853/de9081e2-159d-42a9-a262-ad671d0597df">

# Front-end deployment:
https://purrfect-match-front-end.vercel.app/

# Back-end deployment:
https://purrfect-match-back-end-7b130ef4f9c3.herokuapp.com

# Overview
PurrfectMatch is built for helping animal adoption. You can view and add the furry friend to adoption list. You will be able to contact the shelter for further application.

# Team
- Backend:
  - Kia: https://github.com/Kdrummmond625
  - Shan: https://github.com/makeyourwon
- Frontend:
  - Joshua: https://github.com/kratos238
  - Kevin: https://github.com/Kevelaz

# Technique
- Django, Python, Node, CORS, JSON, pet-finder API

# User Stories


# ERD
![PurrfectMatch ERD](https://github.com/makeyourwon/Purrfect-Match-back-end/assets/149891853/5d9c7997-c3c7-4239-83d9-f01ef219362d)


# Routing Table                                   
### Backend API URL Paths
#### User Authentication, Registration, and Token Management
| Function              | URL                                  | Method    | Description                    |
|-----------------------|--------------------------------------|-----------|--------------------------------|
| User registration     | /register/            | POST      | User registration.             |
| User login            | /login/               | POST      | User login, returns tokens.    |
| Refresh access token  | /refresh/       | POST      | Refresh access token.          |
#### User Profile Management
| Function               | URL                                   | Method    | Description                   |
|------------------------|---------------------------------------|-----------|-------------------------------|
| Fetch profile details  | /profile/              | GET/PUT      | Fetch user's profile details and update profile info. |
#### Animal Listings and Filters
| Function             | URL                              | Method | Description                        |
|----------------------|----------------------------------|--------|------------------------------------|
| List all animals     | animals/              | GET    | List all animals with filters.     |
| Animal details by ID(primary key) | /animals/pk/     | GET    | Get animal details by ID.              |
#### Favorites Management
| Function                   | URL                                      | Method | Description                      |
|----------------------------|------------------------------------------|--------|----------------------------------|
| List favorited animals     |/favorites/                    | GET    | List single user's favorited animals.   |
| Add an animal to favorites | /favorites/add/pk/                | POST   | Add an animal to one profile's favorites.      |
| Remove an animal from favorites | /favorites/remove/pk/ | POST(DELETE) | Remove an animal from favorites. |

# Trello
https://trello.com/b/VbdaIAZh/purrrfect-match

# Timeline

|Date | Todo | Status|
|-----|------|-------|
|2/9  | Create Proposal | Complete|
|2/12 | Complete Scaffolding | Complete |
|2/12 | Get API Key for 3rd party integration | Complete|
|2/12 | Test Routes BackEnd | Complete |
|2/13 | Test Authentication | Complete on 2/12 |
|2/14 | Deployment | Complete |
|2/15 | Style Project | Complete |


# Ice box
1. User reviews
2. List shelters nearby - may require google api
3. volunteering opportunities page for shelters
4. Donations page with link
5. Pet Care Tips for new owners






