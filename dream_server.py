def run(args):
    if args['run']:
        pull_frame()
        run_networks() 
        push_frame()
    elif args['train']:
        fine_tune()


def pull_frame():
    pass


def run_networks():
    pass


def push_frame():
    pass


def fine_tune():
    pass
