\# Healthcare Backend API



A RESTful healthcare backend built with Django, Django REST Framework, PostgreSQL, and JWT authentication. The API supports user registration and login, patient management, doctor management, and patient-doctor assignments.



\## Features



\- User registration and JWT authentication

\- Patient CRUD operations

\- Doctor CRUD operations

\- Patient-doctor mapping management

\- User-specific patient access

\- Input validation and error handling

\- PostgreSQL database integration

\- Environment-based configuration



\## Tech Stack



\- Python

\- Django

\- Django REST Framework

\- PostgreSQL

\- Simple JWT

\- python-dotenv



\## Project Structure



```text

healthcare\_backend/

├── accounts/

├── config/

├── doctors/

├── patients/

├── .env                 # Local secrets; not committed

├── .gitignore

├── manage.py

├── requirements.txt

└── README.md

```



\## Setup Instructions



\### 1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd healthcare\_backend

```



\### 2. Create and activate a virtual environment



On Windows:



```bash

python -m venv .venv

.venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Configure environment variables



Create a `.env` file in the project root. Add your own values:



```env

SECRET\_KEY=your\_django\_secret\_key

DEBUG=True

ALLOWED\_HOSTS=127.0.0.1,localhost



DB\_NAME=healthcare\_db

DB\_USER=your\_postgres\_username

DB\_PASSWORD=your\_postgres\_password

DB\_HOST=127.0.0.1

DB\_PORT=5432

```



Do not commit `.env` or expose credentials in public repositories.



\### 5. Create the PostgreSQL database



Create a PostgreSQL database named `healthcare\_db`, or change `DB\_NAME` to match your database.



\### 6. Apply migrations



```bash

python manage.py migrate

```



\### 7. Start the development server



```bash

python manage.py runserver

```



The API will be available at `http://127.0.0.1:8000/`.



\## API Endpoints



All endpoints below use the `/api/` prefix. Protected endpoints require a JWT access token in the `Authorization: Bearer <access\_token>` header.



\### Authentication



| Method | Endpoint | Description |

|---|---|---|

| POST | `/api/auth/register/` | Register a user |

| POST | `/api/auth/login/` | Obtain JWT tokens |



\### Patients



| Method | Endpoint | Description |

|---|---|---|

| POST | `/api/patients/` | Create a patient |

| GET | `/api/patients/` | List the current user's patients |

| GET | `/api/patients/<id>/` | Retrieve a patient |

| PUT/PATCH | `/api/patients/<id>/` | Update a patient |

| DELETE | `/api/patients/<id>/` | Delete a patient |



\### Doctors



| Method | Endpoint | Description |

|---|---|---|

| POST | `/api/doctors/` | Create a doctor |

| GET | `/api/doctors/` | List doctors |

| GET | `/api/doctors/<id>/` | Retrieve a doctor |

| PUT/PATCH | `/api/doctors/<id>/` | Update a doctor |

| DELETE | `/api/doctors/<id>/` | Delete a doctor |



\### Patient-Doctor Mappings



| Method | Endpoint | Description |

|---|---|---|

| POST | `/api/mappings/` | Assign a doctor to a patient |

| GET | `/api/mappings/` | List mappings for the current user's patients |

| GET | `/api/mappings/<patient\_id>/` | List doctors assigned to a patient |

| DELETE | `/api/mappings/<id>/` | Delete a mapping |



\### Example: Create a Patient



Send a POST request to `/api/patients/` with a valid access token and JSON body:



```json

{

&#x20; "name": "Patient Name",

&#x20; "age": 30,

&#x20; "gender": "male",

&#x20; "phone": "9876543210",

&#x20; "address": "Delhi, India"

}

```



\### Example: Create a Mapping



Send a POST request to `/api/mappings/`:



```json

{

&#x20; "patient": 1,

&#x20; "doctor": 1

}

```



Use existing patient and doctor IDs belonging to the appropriate records.



\## Run System Checks



```bash

python manage.py check

python manage.py showmigrations

```



\## Security Notes



\- Keep secret keys and database credentials in environment variables.

\- Never commit `.env`.

\- Use a strong, unique Django secret key and database password.

\- Set `DEBUG=False` and configure appropriate `ALLOWED\_HOSTS` for production.

\- Protected endpoints require authentication.



\## License



Add a license if you intend to distribute this project publicly.



