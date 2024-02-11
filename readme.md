# FastAPI App README

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EvascoJohn/packer-mvp.git
   ```
   ```bash
   cd your_repo
   ```

2. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory of the project.

2. Add necessary environment variables to the `.env` file. For example:
   ```dotenv
   DATABASE=mysql
   DIALET=pymysql
   ```

## Running the App

To run the FastAPI app, execute the following command:
```bash
uvicorn main:app --reload
```

This command will start the development server and reload it automatically whenever changes are made to the code.

You can now access the FastAPI app by navigating to `http://localhost:8000` in your web browser.


# API Endpoints

Welcome to our API! Below are the available endpoints:

## Documentation for Endpoints

For detailed documentation and usage examples, please visit `http://localhost:8000/docs`

## Endpoints

1. `/bags`
   - Method: GET
   - Description: Retrieves a list of all bags.

2. `/create_bags`
   - Method: POST
   - Description: Creates a new bag.


##### FRONTEND #####

## To setup:

   1. Change directory to "frontend" folder
      
         'cd frontend'
   
   2. Install dependency ( Make sure NodeJS is installed )
      
         'npm install'

   3. To run.

         'npm run dev'      