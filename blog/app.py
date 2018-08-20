blogs = dict()
# we use a dictionary here so we can find a dictionary by it's mname very easily


def menu():
    # Show user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

        
