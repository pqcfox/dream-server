import os.path
import atexit
import shutil
import tempfile
import time

import batcountry
import boto3
import caffe
import numpy as np
from PIL import Image

S3_PULL_KEY = 'dream_up.jpg'
S3_PUSH_KEY = 'dream_down.jpg'


def run(args):
    bc = batcountry.BatCountry(args['network'])
    atexit.register(lambda: bc.cleanup())
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(args['bucket-name'])
    while True:
	objects = list(bucket.objects.filter(Prefix=S3_PULL_KEY))
	if len(objects) == 0 or objects[0].key != S3_PULL_KEY:
            time.sleep(5)
	    continue
        pull_image_path = pull_frame(bucket)
        push_image_path = run_network(pull_image_path, bucket, bc) 
        push_frame(push_image_path, bucket)


def pull_frame(bucket):
    pull_image = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    bucket.download_file(S3_PULL_KEY, pull_image.name)
    bucket.delete_objects(Delete={'Objects': [{'Key': S3_PULL_KEY}]})
    return pull_image.name


def run_network(pull_image_path, bucket, bc):
    pull_image = Image.open(pull_image_path)
    push_image_array = bc.dream(np.float32(pull_image))
    push_image = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    result = Image.fromarray(np.uint8(push_image_array))
    result.save(push_image.name)
    return push_image.name


def push_frame(push_image_path, bucket):
    bucket.upload_file(push_image_path, S3_PUSH_KEY)
