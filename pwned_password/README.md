This Python script checks if a given password has been compromised by querying the "Have I Been Pwned" API, which maintains a database of leaked passwords.
The difference is that by using this code, instead of using the API, we do it locally, so there is zero risk of the API itself storing our information.
Here's a breakdown of the code:

    Imports:
        requests: Used to make HTTP requests.
        hashlib: Provides hash functions, used here for SHA-1 hashing.
        sys: Used for handling command-line arguments and exiting the script.

    request_api_data function:
        Takes a single argument query_char, which is the first 5 characters of the hashed password.
        Constructs the API URL based on the provided query characters.
        Sends a GET request to the API and returns the response.
        Raises a RuntimeError if the HTTP response status code is not 200 (OK).

    get_password_leaks_count function:
        Takes two arguments: hashes (the response from the API) and hash_to_check (the remaining characters of the hashed password).
        Parses the API response, which contains hash-count pairs, and checks if the given hash matches any in the response.
        Returns the count if a match is found, otherwise returns 0.

    pwned_api_check function:
        Takes a password as an argument.
        Converts the password to a SHA-1 hash using hashlib.
        Extracts the first 5 characters and the tail of the hash.
        Calls request_api_data to get the API response for the first 5 characters.
        Calls get_password_leaks_count to check if the full hash is present in the API response.

    main function:
        Takes a list of passwords as command-line arguments.
        Iterates over each password, calling pwned_api_check for each.
        Prints a message indicating whether the password was found in the database and the number of times it was found.
        Returns 'Done!' when finished.

    __main__ block:
        Invokes the main function with command-line arguments (sys.argv[1:]).
        Exits with the return value of main, either printing results or an error message.

    Sample usage outside of the main execution block:
        Invokes pwned_api_check with the password 'password'.
