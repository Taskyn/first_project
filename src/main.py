from dotenv import load_dotenv
import os
load_dotenv('.env')
def print_author():
	secret_author = os.getenv('AUTHOR')
	print(f"Автор проекта: {secret_author}")
print_author()
