# Create a Google Cloud Storage Bucket with custom domain name
BUCKET_NAME=docs.ansari.chat

# Upload your site to the bucket
gsutil -m rsync -r $PWD/build/docs gs://$BUCKET_NAME

# Make your bucket public
gsutil iam ch allUsers:objectViewer gs://$BUCKET_NAME

# Set up a website configuration
gsutil web set -m index.html -e 404.html gs://$BUCKET_NAME

echo "Your site is available at http://$BUCKET_NAME"