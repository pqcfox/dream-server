import boto3
import caffe

S3_PULL_KEY = 'dream_up.jpg'
S3_PUSH_KEY = 'dream_down.jpg'
WORK_DIR = ''
OUTPUT_FILE = '' 
SOLVER_PATH = 'models/bvlc_reference_caffenet/solver.prototxt'

s3 = boto3.resource('s3')


def run(args):
    bucket = s3.Bucket(args['bucket-name'])
    if args['run']:
        pull_frame(bucket)
        run_networks() 
        push_frame(bucket)
    elif args['train']:
        fine_tune()


def pull_frame(bucket):
    bucket.download_file(S3_PULL_KEY, WORK_DIR)


def run_networks():
    solver = caffe.get_solver(SOLVER_PATH)
    solver.solve()


def push_frame(bucket):
    bucket.upload_file(OUTPUT_FILE, S3_PUSH_KEY)


def fine_tune():
    pass
