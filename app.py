import models
from . import api_views
from models.event import Event
from models.comment import Comment
from flask import jsonify, request


app = Flask(__name__)


# Create an Endpoint that GET's the images assiociated with a comment
@event_bp.route('/api/comments/<comment_id>/images', methods=['GET'])
def get_images_for_comment(comment_id):
    try:

        comment = models.storage.get(Comment, comment_id)

        if comment is None:
            return jsonify({"error": "Comment not found"}), 404

        comment_images = comment.images

        return jsonify({"comment_id": comment_id, "images": comment_images})

    except Exception as e:
        models.storage.session.rollback()
        return jsonify({"error": str(e)}), 404


if __name__ == '__main__':
    app.run(debug=True)
