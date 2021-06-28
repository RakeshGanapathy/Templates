
# Templates

# _auth for ecr_ 
docker login -u AWS -p $(aws ecr get-login-password --region ap-south-1) (accountNo).dkr.ecr.ap-south-1.amazonaws.com
