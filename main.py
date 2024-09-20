from dotenv import load_dotenv
import os
load_dotenv()
def main():
    return "Hello world"

print(main())
print(os.getenv('openaikey'))