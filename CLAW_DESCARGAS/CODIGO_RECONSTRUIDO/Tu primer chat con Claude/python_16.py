from googleapiclient.discovery import build
from google.colab import auth

auth.authenticate_user()
service = build('drive', 'v3')

# Probar con el primer archivo
doc_id = '1zwDufAQtSe801mvXun9iC_iERmDyBkKt'
request = service.files().get_media(fileId=doc_id)
print(request.uri)