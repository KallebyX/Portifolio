import boto3
import os

def upload_to_s3(file_object, filename):
    """
    Envia um arquivo para o AWS S3 e retorna a URL pública.
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )

    bucket_name = os.getenv('AWS_BUCKET_NAME')

    # Faz o upload
    s3.upload_fileobj(
        file_object,
        bucket_name,
        filename
    )

    # Corrigir o endpoint automaticamente
    location = s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint']

    if location is None:
        # Região padrão antiga da AWS (us-east-1 não tem LocationConstraint)
        url = f"https://{bucket_name}.s3.amazonaws.com/{filename}"
    else:
        url = f"https://{bucket_name}.s3.{location}.amazonaws.com/{filename}"

    return url