#### 2023 Update soon...

## Journey to migration Django 3.0.4 web app to 4.2.5
<br>

> Reconfigure virtual environment
  - apply `Python 3.11.5`
  - `source myven/bin/activate`
<br><br>

> Change RDBMS
  - `MySQL`(AWS RDS) 8.0.xx to `MariaDB`(Docker) 11.1.2
    - apply `DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'` globally
    - `makemigrations`, `migrate` success
<br><br>

> Change AWS S3 file upload method
  - Both web static files and user-uploaded files are stored in an `AWS S3` bucket
  - Now, `Lambda Edge` is employed for credential and presigned URL generation  
  while `CloudFront` is utilized with S3 for file uploads and downloads
