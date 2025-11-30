
#!/bin/bash

app_url="https://<your-app-name>.azurewebsites.net/predict"

curl -X POST $app_url \
    -H "Content-Type: application/json" \
    -d '{ "inputs": [0.5, -1.2, 3.1, 0.7] }'
