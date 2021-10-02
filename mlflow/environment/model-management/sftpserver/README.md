sudo docker run -v /etc/mlflow/ftpserver/upload:/home/foo/upload -p 2222:22 -d atmoz/sftp foo:pass:1001
sftp -P 2222 foo@193.175.161.65
