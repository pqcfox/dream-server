import boto3
import caffe

S3_PULL_KEY = 'dream_up.jpg'
S3_PUSH_KEY = 'dream_down.jpg'
SOLVER_FILE = 'solver.prototxt'
OUTPUT_FILE = '' 

s3 = boto3.resource('s3')


def run(args):
    run_networks(args['work-dir']) 
    if args['run']:
        bucket = s3.Bucket(args['bucket-name'])
        pull_frame(bucket)
        push_frame(bucket)
    elif args['train']:
        copy_network_data()
        fine_tune()


def pull_frame(bucket):
    bucket.download_file(S3_PULL_KEY, WORK_DIR)


def run_networks(work_dir):
    pass


def push_frame(bucket):
    bucket.upload_file(OUTPUT_FILE, S3_PUSH_KEY)


def copy_network_data()
    pass


def fine_tune():
    pass
