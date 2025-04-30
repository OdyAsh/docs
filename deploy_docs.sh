# Create a Google Cloud Storage Bucket with custom domain name
BUCKET_NAME=docs.ansari.chat

# --- ADDED: Delete existing content in the bucket ---
# Use -m for parallel deletion, -r for recursive, ** to match all objects
echo "Deleting existing content in gs://$BUCKET_NAME..."
gsutil -m rm -r gs://$BUCKET_NAME/**
echo "Deletion complete."
# --- END ADDED ---

# Upload your site to the bucket
echo "Uploading site from $PWD/build/docs to gs://$BUCKET_NAME..."
gsutil -m rsync -r $PWD/build/docs gs://$BUCKET_NAME
echo "Upload complete."

# Make your bucket public
gsutil iam ch allUsers:objectViewer gs://$BUCKET_NAME

# Set up a website configuration
gsutil web set -m index.html -e 404.html gs://$BUCKET_NAME

echo "Your site is available at http://$BUCKET_NAME"