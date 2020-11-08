# See My Feed

This tool allows a user to share their Twitter following with another user in the form of a Twitter list. 

# Setup

This project uses a Python 3.7.x environment

In a terminal, run
```terminal
python3 -m venv ./env
source ./env/bin/activate
pip3 install -e .
```
To deactivate the environment, simply run
```terminal
deactivate
```

Create a file called keys.txt (locally! This should never get committed) with the following format:
```terminal
[API Key]
[API Key Secret]
[Bearer Token]
```

# Usage

Run the program by running
```terminal
main.py [username]
```
where [username] is the name of the user who's following you want to examine.
