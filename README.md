# Build and deploy

Command to build the application. PLease remeber to change the project name and application name
```
gcloud builds submit --tag gcr.io/teoindicator/teoindicator  --project=teoindicator
```

Command to deploy the application
```
gcloud run deploy --image gcr.io/teoindicator/teoindicator --platform managed  --project=teoindicator --allow-unauthenticated
```