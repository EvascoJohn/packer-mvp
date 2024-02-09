# FastAPI App README

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EvascoJohn/packer-mvp.git
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
   DIALET=mysql
   ```

## Running the App

To run the FastAPI app, execute the following command:
```bash
uvicorn app.main:app --reload
```

This command will start the development server and reload it automatically whenever changes are made to the code.

You can now access the FastAPI app by navigating to `http://localhost:8000` in your web browser.

## Additional Notes

- Make sure to replace `your_database_url_here` and `your_secret_key_here` with your actual database URL and secret key respectively.
- Feel free to modify the `requirements.txt` file according to your project's dependencies.