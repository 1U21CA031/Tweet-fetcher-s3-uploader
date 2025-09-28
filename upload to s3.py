import boto3

AWS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'
AWS_REGION = 'Your Region '
S3_BUCKET = 'your-bucket-name'
S3_KEY = 'elonmusk_tweets.csv'
local_file = 'elonmusk_tweets.csv'

# Create S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Upload file
try:
    s3.upload_file(local_file, S3_BUCKET, S3_KEY)
    print(f"✅ Uploaded file to s3://{S3_BUCKET}/{S3_KEY}")
except Exception as e:
    print(f"❌ Upload failed: {e}")
