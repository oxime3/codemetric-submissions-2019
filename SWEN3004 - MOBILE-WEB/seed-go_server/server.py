#!flask/bin/python
import logging
from logging import Logger

from flask import Flask, abort, jsonify, make_response, request, render_template

app = Flask(__name__)
logging.getLogger().setLevel(logging.INFO)

courses = []
announcements = []

@app.route('/seedgo/api/courses', methods=['GET'])
def get_courses():
    return render_template('index.html')
    #return jsonify({'courses': courses})

@app.route("/seed-go/api/announcements", methods=['GET'])
def get_announcements():
    return jsonify(announcements)

@app.route('/seed-go/api/postcourse', methods=['POST'])
def postCourses():
    logging.info(request.json)
    if not request.json or not 'courseTitle' in request.json:
        abort(404)
    course = {
        'courseTitle': request.json['courseTitle'],
        'numOfTopics': request.json['numOfTopics'],
        'numOfFiles': request.json['numOfFiles'],
        'numOfAssignments': request.json['numOfAssignments']}
    courses.append(course)
    return render_template('index.html')
    #return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 403)

def create_sample_course():
    sampleCourse = {}
    sampleCourse['courseTitle'] = 'Sample Course'
    sampleCourse['numOfTopics'] = '4'
    sampleCourse['numOfFiles'] = '6'
    sampleCourse['numOfAssignments'] = '4'
    courses.append(sampleCourse)

    logging.info("Added sample course: %s", sampleCourse['courseTitle'])



if __name__ == '__main__':
    create_sample_course()
    app.run(host='0.0.0.0', debug=False, port=5000)

