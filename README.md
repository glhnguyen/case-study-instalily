# PartSelect Chatbot - Instalily Case Study

This project is designed to create a chatbot for www.partselect.com, to assist customers with questions regarding only on refrigerators and dishwashers.

## How it's made

**Tech Stack**

- Frontend: React
- Backend: Python
- Database: Redis

### Server

Made in Python with a FastAPI framework. The app initializes a chatbot to generate responses using AI. A redis database is created to save user sessions.

### Frontend

UI made with React. Can also be loaded as a chrome side panel through extensions.

## How to Run

To run, the UI needs to be built and the backend server and redis server need to be run.

### Frontend:

In a new terminal, do these steps:

1. Go into the frontend folder
2. Build the UI by running `npm run build`
3. Navigate to Google Chrome and go to [chrome://extensions/](chrome://extensions/). Make sure Developer mode is turned on.
4. Click the Load unpacked button and load the build folder that was created

### Backend:

In a new terminal, do these steps:

1. Go into the backend folder
2. Install a virtual environment by typing `python3 -m venv venv` in the terminal
3. Activate the virtual environment with `source venv/bin/activate`
4. Make sure the virtual environment is activated before installing dependencies: `pip install -r requirements.txt`
5. Run the main file: `python3 chatbot/main.py`

### Database:

In a new terminal, do these steps:

1. Make sure Redis is installed `brew install redis`
2. Run the server: `redis-server`

## Things to do

- [] Create unit testing
- [] Create CI/CD pipeline
- [] Create docker compose file
