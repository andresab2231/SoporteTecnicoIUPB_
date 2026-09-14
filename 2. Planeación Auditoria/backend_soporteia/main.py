
# main

import uvicorn

def start():
    print("Starting server...")
    uvicorn.run(
                "application.webapisoporteia:app",
                host="192.168.137.159",
                port=7000,
                reload=True
                )
    print("Server is running.")

if __name__ == "__main__":
    start()