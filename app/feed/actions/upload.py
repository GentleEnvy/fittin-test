from app.base.actions.base import BaseAction


class PUT_FeedUploadAction(BaseAction):
    def __init__(self, view):
        super().__init__(view)
        self.feed_filename = 'feed.xml'

    def run(self, file):
        with open(self.feed_filename, 'wb') as feed_file:
            feed_file.write(file.read())
