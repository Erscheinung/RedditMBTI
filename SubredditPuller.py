from praw import Reddit


class SubredditPuller:
    """Methods to pull a List of Reddit posts from a subreddit"""

    def __init__(self):
        """ Initialize SubredditPuller"""

        # Create the Reddit class provided by PRAWN

        # This line allows me to import my credentials from a 'praw.ini' file
        self.reddit = Reddit(site_name='DEFAULT')

        # Set out account only able to view posts
        self.reddit.read_only = True

    def pull_subreddit(self, subreddit, limit):
        """ Pull limit number of posts from specified subreddit. If limit==None,
        it'll try to pull the maximum possible posts """

        # NOTE - The maximum number of posts returned is 1000 (Reddit
        # Limitation)
        s = self.reddit.subreddit(subreddit)
        posts = []
        for submission in s.top('all', limit=limit):
            posts.append(submission)
        return posts
