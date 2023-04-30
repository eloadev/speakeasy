from storages.backends.s3boto3 import S3Boto3Storage


class S3MediaStorage(S3Boto3Storage):
    location = 'books'
