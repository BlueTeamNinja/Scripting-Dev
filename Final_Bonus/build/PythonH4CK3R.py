import time
import random

def set_password(length, seed=None):
    """
    Prompt the user to set the password length (number of digits).
    Generate and return a random numeric password of that length.
    Allow a random seed as an optional parameter for consistent testing.
    """
    random.seed(seed)
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def brute_force_attack(password, start=0):
    attempts = start  # Initialize attempt count
    cracked_password = None  # Initialize cracked password

    while cracked_password != password:
        cracked_password = str(attempts)  # Generate password attempt
        attempts += 1  # Increase attempt count
        #log_attempts(attempts)  # Log attempts

    return cracked_password, attempts

#def brute_force_attack(password, start=0):
#    """
#    Implement a brute force attack to 'crack' a numeric password.
#    Accepts the password and an optional starting number other than 0.
#    Iterates through possible combinations until the password is cracked.
#    Returns the cracked password and the number of attempts it took.
#    """
#    attempt_count = 0
#    i = start
#    while True:
#        attempt = str(i)
#        attempt_count += 1
#        if attempt == password:
#            return attempt, attempt_count
#        i += 1
#
def performance_analysis(start_time, end_time, attempts):
    """
    Analyze and return the time taken and average attempts per second.
    Accepts start time, end time, and total attempts as parameters.
    """
    time_taken = end_time - start_time
    attempts_per_second = attempts / time_taken
    return time_taken, attempts_per_second

def main():
    """
    Main function to simulate the entire brute force attack process.
    Combine all the above functions and display success messages and performance analysis.
    Highlight the importance of strong passwords in cybersecurity.
    """
    length = int(input("Enter password length: "))
    password = set_password(length, seed=42)  # Using a fixed seed for consistent testing
    print(f"Generated password (for testing purposes): {password}")

    start_time = time.time()
    cracked_password, attempts = brute_force_attack(password)
    end_time = time.time()

    print(f"Cracked password: {cracked_password} in {attempts} attempts.")
    time_taken, attempts_per_sec = performance_analysis(start_time, end_time, attempts)
    print(f"Time taken: {time_taken:.2f} seconds. Attempts per second: {attempts_per_sec:.2f}")

    print("\nIn cybersecurity, strong passwords are essential to prevent brute force attacks and unauthorized access.  Balancing this with reality means your bank card pin should always be at least 127 digits.")

if __name__ == "__main__":
    main()
