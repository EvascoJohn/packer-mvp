from dotenv import dotenv_values

config = {
    **dotenv_values(".env")
    # you can create another .env files here if you want.
}