import boto3
import caffe
import shutil

S3_PULL_KEY = 'dream_up.jpg'
S3_PUSH_KEY = 'dream_down.jpg'
TRAIN_VAL_FILE = 'train_val.prototxt'
DEPLOY_FILE = 'deploy.prototxt'
SOLVER_FILE = 'solver.prototxt'
OUTPUT_FILE = 'output.jpg' 

s3 = boto3.resource('s3')


def run(args):
    if args['run']:
        bucket = s3.Bucket(args['bucket-name'])
        pull_frame(bucket, args['work-dir'])
        run_networks(args['work-dir']) 
        push_frame(bucket)
    elif args['train']:
        copy_network_data()
        fine_tune()


def pull_frame(bucket, work_dir):
    bucket.download_file(S3_PULL_KEY, work_dir)


def run_networks(work_dir):
    pass


def push_frame(bucket):
    bucket.upload_file(OUTPUT_FILE, S3_PUSH_KEY)


def fine_tune():
    pass
