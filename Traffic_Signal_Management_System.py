import pymysql   # Import the PyMySQL library for MySQL database interaction

def get_db_connection():
    """Create and return a new database connection."""
    return pymysql.connect(
        host='localhost',
        user='your_username',       # MySQL username
        password='your_password', # MySQL password
        db='traffic_db'    # Database name
    )

def ensure_signal_exists(signal_id: int) -> None:
    """
    Check if a traffic signal with the given ID exists.
    If not, prompt the user for all required details and insert the signal into the database.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Check if the signal already exists
                cursor.execute(
                    "SELECT SignalID FROM TrafficData WHERE SignalID = %s",
                    (signal_id,)
                )
                if cursor.fetchone() is None:
                    # Signal does not exist, prompt user for details
                    print("This signal is new. Please enter its details.")
                    vehicle_count = get_int_input("Enter Vehicle Count: ")
                    signal_duration = get_int_input("Enter Signal Duration (seconds): ")
                    location = input("Enter Location: ")
                    # Insert the new signal into the database
                    cursor.execute(
                        "INSERT INTO TrafficData(SignalID, VehicleCount, SignalDuration, Location, LastUpdated) "
                        "VALUES (%s, %s, %s, %s, NOW())",
                        (signal_id, vehicle_count, signal_duration, location)
                    )
                    conn.commit()  # Save changes
                    print("✅ New signal added to the database.")
                else:
                    # Signal already exists
                    print("ℹ️ Signal already exists in the database.")
    except pymysql.MySQLError as e:
        # Handle database errors gracefully
        print("⚠️ ERROR:", e)

def update_signal(signal_id: int, vehicle_count: int, signal_duration: int, location: str) -> None:
    """
    Update the information for an existing traffic signal.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Update the values for the given signal id
                cursor.execute(
                    "UPDATE TrafficData SET VehicleCount=%s, SignalDuration=%s, Location=%s, LastUpdated=NOW() "
                    "WHERE SignalID = %s",
                    (vehicle_count, signal_duration, location, signal_id)
                )
                conn.commit()  # Save changes
                if cursor.rowcount == 0:
                    # No row was updated; signal ID doesn't exist
                    print("❌ No signal found with this ID.")
                else:
                    print("✅ Signal updated successfully.")
    except pymysql.MySQLError as e:
        print("⚠️ ERROR:", e)

def view_signals() -> None:
    """
    Fetch and display all traffic signals in a table-like format.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Select all relevant columns
                cursor.execute("SELECT SignalID, VehicleCount, SignalDuration, Location, LastUpdated FROM TrafficData")
                results = cursor.fetchall()
                headers = ["SignalID", "VehicleCount", "SignalDuration", "Location", "LastUpdated"]
                # Print header row
                print("-" * 83)
                print(f"{headers[0]:<10} | {headers[1]:<12} | {headers[2]:<14} | {headers[3]:<18} | {headers[4]}")
                print("-" * 83)
                # Print each row from the results
                for row in results:
                    print(f"{row[0]:<10} | {row[1]:<12} | {row[2]:<14} | {row[3]:<18} | {row[4]}")
                print("-" * 83)
    except pymysql.MySQLError as e:
        print("⚠️ ERROR:", e)

def delete_signal(signal_id: int) -> None:
    """
    Remove a traffic signal from the database by its ID.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                # Delete the row with the given Signal ID
                cursor.execute(
                    "DELETE FROM TrafficData WHERE SignalID = %s",
                    (signal_id,)
                )
                conn.commit()  # Save changes
                if cursor.rowcount == 0:
                    print("❌ No signal found with this ID.")
                else:
                    print("✅ Signal deleted successfully.")
    except pymysql.MySQLError as e:
        print("⚠️ ERROR:", e)

def get_int_input(prompt: str) -> int:
    """
    Prompt the user for an integer input, keep asking until a valid integer is entered.
    Prevents the program from crashing on invalid input.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main() -> None:
    """
    Run the main menu loop for the traffic signal management system.
    Offers options to ensure, update, view, or delete signals, or exit the application.
    """
    menu = (
        "\nTraffic Signal Management System\n"
        "1. Ensure Signal Exists\n"
        "2. Update Signal\n"
        "3. View Signals\n"
        "4. Delete Signal\n"
        "5. Exit\n"
    )
    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            # Add a new signal if it doesn't exist
            signal_id = get_int_input("Enter Signal ID: ")
            ensure_signal_exists(signal_id)
        elif choice == '2':
            # Update an existing signal's info
            signal_id = get_int_input("Enter Signal ID: ")
            vehicle_count = get_int_input("Enter Vehicle Count: ")
            signal_duration = get_int_input("Enter Signal Duration (seconds): ")
            location = input("Enter Location: ")
            update_signal(signal_id, vehicle_count, signal_duration, location)
        elif choice == '3':
            # View all signals
            view_signals()
        elif choice == '4':
            # Delete a signal
            signal_id = get_int_input("Enter Signal ID: ")
            delete_signal(signal_id)
        elif choice == '5':
            # Exit the application
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program if the script is executed directly.
if __name__ == "__main__":
    main()
