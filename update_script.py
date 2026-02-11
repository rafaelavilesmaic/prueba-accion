import datetime

def update_timestamp():
    with open("last_update.txt", "w") as f:
        f.write(f"Updated by GitHub Actions on: {datetime.datetime.now().isoformat()}")

if __name__ == "__main__":
    update_timestamp()
