# Fungusan’s Maths Platform

# Features

| Feature Category | Specific Features |
| --- | --- |
| **Core Problem Display** | R1. Render maths problems with formulas |
| | R2. Show multiple choice options |
| **Problem Selection** | R3. Topic filtering (trigonometry, geometry, etc.) |
| | R4. Difficulty selection (easy/medium/hard/mixed) |
| | R5. Random problem generation |
| **User Progression** | R6. Daily question system & streak tracking |
| **Assessment & Feedback** | R7. Answer checking |
| | R8. Completion statistics per problem set |
| **User Management** | R9. User accounts/profiles |
| | R10. Login system |

# Frontend

## UI Display Logic

![UI Display Logic](./docx/images/UIDisplayLogic.png)

<aside>
⚠️ All users will visit the home page, but they must login and grant access token as they visit protected pages
</aside>

## UI Appearance

### Hero Section

![Hero Section](./docx/images/HeroSection.png)

### Questions Book Section

![Question Book](./docx/images/QuestionBook.png)

<aside>
💡 Style: editorial and book-like; match with my primary portfolio 
</aside>

## Endpoints

| METHOD | PATH | DESCRIPTION |
| --- | --- | --- |
| GET | /users/<:id> | Get user information (e.g. name) |
| POST | /users/login | Log a existing user in, return access token |
| POST | /users/register | Register a new user, and log him/her in |
| POST | /sessions/open | Open a new question session for the chosen topic (query: topic, mode, number) |
| PUT | /sessions/edit | Edit answers to the current session |
| POST | /sessions/submit | Submit answers (mark as complete) |
| GET | /sessions/fetch | Get unfinished session (if any) (prevent multiple sessions, and reload the answers) |
| DELETE | /sessions/delete | Delete the current unfinished session |
| GET | /sessions/stat | Get streak, statistics for previous sessions |
| GET | /questions/topics | Get the list of topics |
| GET | /questions/<:question_slug> | Get a question by question_slug (for showing wrongly answered questions) |

<aside>
⚠️ See docx/ for more details of API endpoints
</aside>

# Backend

## ER Diagram

![ER Diagram](./docx/images/ERDiagram.png)

## Relational Diagram

![Relational Diagram](./docx/images/RelationalDiagram.png)

### Some SQL Notes

```sql
-- Get a list of wrong question_id for the current session ($session_test)
SELECT q.question_id 
FROM Session s 
JOIN UserAnswer ua ON s.session_id = ua.session_id
JOIN Question q ON ua.question_id = q.question_id
WHERE s.session_id = $session_test
  AND ua.answer <> q.answer_key;
```