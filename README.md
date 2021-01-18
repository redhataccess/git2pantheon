Git2Pantheon is a set of REST API that facilitates uploading of git repo containing modular document to Pantheon.  
## Requirements  
1. Python 3
2. Pip 3
3. Redis server running locally  

## Setting up your development environment  
1. Clone the fork of this repo.  
```
git clone YOUR_FORK_OF_THIS_REPO
```
2. Change directory to the cloned repo.  
```
cd git2pantheon
```
3. Create and activate a virtual environment.   
```
python3 -m venv .
```
```
venv/bin/activate
```

4. Install the requirements.  
```
pip3 install --user -r requirements.txt
```
5. Set and export the following environment variables  
   a. PANTHEON_SERVER  
   b. UPLOADER_PASSWORD  
   c. UPLOADER_USER
   
6. Run the service.  
```
python3 git2panthenon/wsgi.py
```
   
7. The swagger docs can be found at:  
http://localhost:5000/apidocs/
   
