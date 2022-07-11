from rest_framework.parsers import FileUploadParser

from app.base.utils.common import response_204
from app.base.views.base import BaseView
from app.feed.actions.upload import PUT_FeedUploadAction


class FeedUploadView(BaseView):
    parser_classes = [FileUploadParser]
    action_map = {'put': PUT_FeedUploadAction}

    @response_204
    def put(self, request):
        file = request.data['file']
        self._create_action().run(file)
