# Purrfect-Match-back-end
![PurrfectMatch](https://github.com/makeyourwon/Purrfect-Match-back-end/assets/149891853/7a1ffc3c-278d-4a94-a1af-3c9ebff69364)


# Overview
PurrfectMatch is built for helping animal adoption. You can view and add the furry friend to adoption list. You will be able to contact the shelter for further application.

# Wireframe
![Purrfection wireframe 1](https://github.com/makeyourwon/Purrfect-Match-back-end/assets/149891853/c027f639-ee29-4db1-8b3a-392d6cabd1d4)
![PurrfetMatch wireframe 2](https://github.com/makeyourwon/Purrfect-Match-back-end/assets/149891853/25e214bb-cd20-4166-bf84-029094d0fa94)


# Team
- Backend: Kia, Shan
- Frontend: Joshua, Kevin

# Technique
HTML, Django, React, Bootstrap, JWT

# User Stories

User Registration and Login
- As a new visitor, I want to create an account using my email, so that I can log into the app and save my favorite animals.
- As a registered user, I want to log in with my username and password, so that I can access my personalized app experience.

Viewing Animals
- As a user, I want to view a list of animals, so that I can see all the available animals for adoption.
- As a user, I want to filter animals by type, breed, age, and size, so that I can find an animal that matches my preferences.
- As a user, I want to view detailed information about each animal, including their photo, description, and shelter details, so that I can learn more about them.

Favorite Animals
- As a logged-in user, I want to add animals to my favorites, so that I can easily find them later.
- As a user, I want to view my list of favorite animals, so that I can keep track of animals I am interested in.

Shelter Information
- As a user, I want to view information about different shelters, including their location and contact information, so that I can visit or contact them.
- As a user, I want to view all animals available at a specific shelter, so that I can see if they have the type of animal I am looking for.

Contacting Shelters
- As a user, I want to contact shelters directly through the app, so that I can inquire more about a specific animal or visitation details.

User Profile Management
- As a logged-in user, I want to update my contact information, so that the shelters can reach me easily.

Adoption Process Information
- As a user, I want to find information about the adoption process, so that I know how to proceed if I decide to adopt an animal.

# ERD
![PurrfectMatch ERD](https://github.com/makeyourwon/Purrfect-Match-back-end/assets/149891853/8d571696-027e-4040-809a-1465a97ea7af)

# Component Hierarchy Diagram

# Routing Table

### Public Pages
| Page Type           | URL        | Description                                           |
|---------------------|------------|-------------------------------------------------------|
| Homepage            | /          | Introductory information and login/register options.  |
| Login Page          | /login     | For user login.                                       |
| Registration Page   | /register  | For new user registration.                            |
### Authenticated User Pages
| Page Type            | URL           | Description                            |
|----------------------|---------------|----------------------------------------|
| User's Profile Page  | /profile      | View and edit user profile details.    |
| Favorites Page       | /favorites    | Shows favorited animals.               |
| Animal Listings Page | /animals      | Lists all animals with filter options. |
| Animal Detail Page   | /animals/:id  | Detailed view of a specific animal.    |
### Backend API URL Paths
#### User Authentication, Registration, and Token Management
| Function              | URL                                  | Method    | Description                    |
|-----------------------|--------------------------------------|-----------|--------------------------------|
| User registration     | /purrmatch/user/register/            | POST      | User registration.             |
| User login            | /purrmatch/user/login/               | POST      | User login, returns tokens.    |
| Refresh access token  | /purrmatch/user/token/refresh/       | POST      | Refresh access token.          |
#### User Profile Management
| Function               | URL                                   | Method    | Description                   |
|------------------------|---------------------------------------|-----------|-------------------------------|
| Fetch profile details  | /purrmatch/user/profile/              | GET       | Fetch user's profile details. |
| Update profile information | /purrmatch/user/profile/update/   | PUT/PATCH | Update profile information.   |
#### Animal Listings and Filters
| Function             | URL                              | Method | Description                        |
|----------------------|----------------------------------|--------|------------------------------------|
| List all animals     | /purrmatch/animals/              | GET    | List all animals with filters.     |
| Animal details by ID | /purrmatch/animals/<int:id>/     | GET    | Animal details by ID.              |
#### Favorites Management
| Function                   | URL                                      | Method | Description                      |
|----------------------------|------------------------------------------|--------|----------------------------------|
| List favorited animals     | /purrmatch/favorites/                    | GET    | List user's favorited animals.   |
| Add an animal to favorites | /purrmatch/favorites/add/                | POST   | Add an animal to favorites.      |
| Remove an animal from favorites | /purrmatch/favorites/remove/<int:id>/ | DELETE | Remove an animal from favorites. |

# Trello
https://trello.com/b/VbdaIAZh/purrrfect-match

# Timeline

|Date | Todo |
|-----|------|
|2/9  | Create Proposal|
|2/12 | Complete Scaffolding|
|2/12 | Get API Key for 3rd party integration|
|2/12 | Test Routes BackEnd|
|2/13 | Test Authentication|
|2/14 | Deployment|
|2/15 | Style Project|


# Blockers
TBD

# Next steps



