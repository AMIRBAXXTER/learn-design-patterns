# Target Interface
class CloudUploader:
    """
    رابط استاندارد برای آپلود فایل روی سرویس‌های مختلف ابری.
    """

    def upload(self, file_path, destination):
        pass


# Adaptees
class AWSS3Uploader:
    """
    کلاس مخصوص آپلود فایل روی S3 آمازون.
    """

    def upload_to_s3(self, file_path, bucket_name):
        return f"File '{file_path}' uploaded to AWS S3 bucket '{bucket_name}'."


class GoogleCloudStorageUploader:
    """
    کلاس مخصوص آپلود فایل روی Google Cloud Storage.
    """

    def upload_to_gcs(self, file_path, bucket_name):
        return f"File '{file_path}' uploaded to Google Cloud Storage bucket '{bucket_name}'."


class DropboxUploader:
    """
    کلاس مخصوص آپلود فایل روی Dropbox.
    """

    def upload_to_dropbox(self, file_path, folder_path):
        return f"File '{file_path}' uploaded to Dropbox folder '{folder_path}'."


# Adapters
class AWSAdapter(CloudUploader):
    """
    آداپتر برای AWS S3.
    """

    def __init__(self, aws_uploader: AWSS3Uploader):
        self.aws_uploader = aws_uploader

    def upload(self, file_path, destination):
        # در اینجا destination همان bucket_name برای S3 است.
        return self.aws_uploader.upload_to_s3(file_path, destination)


class GoogleCloudAdapter(CloudUploader):
    """
    آداپتر برای Google Cloud Storage.
    """

    def __init__(self, gcs_uploader: GoogleCloudStorageUploader):
        self.gcs_uploader = gcs_uploader

    def upload(self, file_path, destination):
        # در اینجا destination همان bucket_name برای Google Cloud Storage است.
        return self.gcs_uploader.upload_to_gcs(file_path, destination)


class DropboxAdapter(CloudUploader):
    """
    آداپتر برای Dropbox.
    """

    def __init__(self, dropbox_uploader: DropboxUploader):
        self.dropbox_uploader = dropbox_uploader

    def upload(self, file_path, destination):
        # در اینجا destination همان folder_path برای Dropbox است.
        return self.dropbox_uploader.upload_to_dropbox(file_path, destination)


# Client Code
def upload_file_to_cloud(uploader: CloudUploader, file_path: str, destination: str):
    """
    آپلود فایل با استفاده از یک سرویس ابری خاص.
    """
    print(uploader.upload(file_path, destination))


def main():
    # Adaptees (سرویس‌های مستقیم)
    aws_s3 = AWSS3Uploader()
    gcs = GoogleCloudStorageUploader()
    dropbox = DropboxUploader()

    # Adapters (آداپترها برای سرویس‌های مختلف)
    aws_adapter = AWSAdapter(aws_s3)
    gcs_adapter = GoogleCloudAdapter(gcs)
    dropbox_adapter = DropboxAdapter(dropbox)

    # آپلود فایل‌ها
    print("Uploading files to various cloud services:")
    upload_file_to_cloud(aws_adapter, "file1.txt", "my-s3-bucket")
    upload_file_to_cloud(gcs_adapter, "file2.txt", "my-gcs-bucket")
    upload_file_to_cloud(dropbox_adapter, "file3.txt", "/my_dropbox_folder")


if __name__ == "__main__":
    main()
