import os, logging

import azure.functions as func
from azure.storage.blob import BlobServiceClient
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField, TextField

db = PostgresqlDatabase(os.environ["PGDATABASE"])

class LogEntry(Model):
    name = CharField()
    created = DateTimeField()
    text = TextField()

    class Meta:
        indexes = (
            (('name', 'created'), True),
        )
        database = db

def init_database():
    db.connect()
    db.create_tables([LogEntry])

def main(myblob: func.InputStream):
    container, blobname = myblob.name.split("/", 1)
    blobclient = BlobServiceClient.from_connection_string(os.environ["dbcafleetcaredata_STORAGE"])
    blob = blobclient.get_container_client(container).get_blob_client(blobname)
    blobprops = blob.get_blob_properties()
    blobtext = blob.download_blob().content_as_text()
    LogEntry(name=myblob.name, created=blobprops.last_modified, text=blobtext).save()
    logging.info(f"Imported blob to database \n"
                 f"Name: {myblob.name}\n"
                 f"Time: \n {blobprops.last_modified}")
