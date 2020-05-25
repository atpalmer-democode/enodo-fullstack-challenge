from flask import jsonify, request
from . import repository
from .http import NO_CONTENT_RESPONSE, NOT_FOUND_RESPONSE, CONFLICT_RESPONSE


def load_routes(app):
    @app.route('/api/complete')
    def complete():
        text = request.args.get('text')
        if text is None:
            return NOT_FOUND_RESPONSE
        result = repository.complete(text, limit=10)
        return jsonify({
            'properties': result,
        })

    @app.route('/api/selections')
    def selections():
        result = repository.selections()
        return jsonify({
            'selections': result,
        })

    @app.route('/api/selections/<property_id>', methods=['PUT'])
    def put_selection(property_id):
        ok = repository.add_selection(property_id)
        return NO_CONTENT_RESPONSE if ok else CONFLICT_RESPONSE

    @app.route('/api/selections/<property_id>', methods=['DELETE'])
    def delete_selection(property_id):
        ok = repository.delete_selection(property_id)
        return NO_CONTENT_RESPONSE if ok else NOT_FOUND_RESPONSE

