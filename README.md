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
python3 -m venv venv
```
```
source venv/bin/activate
```

4. Install the requirements.  
```
pip3 install .
```
5. Set and export the following environment variables  
   a. PANTHEON_SERVER  
   b. UPLOADER_PASSWORD  
   c. UPLOADER_USER  
   d. REDIS_SERVICE
   

6. Set the app name for flask run command
```
export FLASK_APP=git2pantheon
```
   
7. Run the service.  
```
flask run
```
   
8. The swagger docs can be found at:  
http://localhost:5000/apidocs/  
   
_Note_: _Please don't try to run cache clear API_
   
