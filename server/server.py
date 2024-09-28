from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Helper functions to read and write JSON files
groups =[
        {
            "id": 1,
            "groupName": "Group 1",
            "members": [1, 2, 3],
        },
        {
            "id": 2,
            "groupName": "Group test",
            "members": [4, 5],
        },
    ]
students =[
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
        {"id": 4, "name": "David"},
        {"id": 5, "name": "Eve"},
    ]
# File paths for groups and students JSON files
#

@app.route('/api/groups', methods=['GET'])
def get_groups():
    """
    Route to get all groups
    return: Array of group objects
    """

    return jsonify(groups)

@app.route('/api/students', methods=['GET'])
def get_students():
    """
    Route to get all students
    return: Array of student objects
    """
    # TODO: (sample response below)
 #   students = load_json_data(STUDENTS_FILE)
    return jsonify(students)

@app.route('/api/groups', methods=['POST'])
def create_group():
    """
    Route to add a new group
    param groupName: The name of the group (from request body)
    param members: Array of member names (from request body)
    return: The created group object
    """
    
    # Getting the request body (DO NOT MODIFY)
  #  groups = load_json_data(GROUPS_FILE)
    group_data = request.json
    group_name = group_data.get("groupName")
    group_members = group_data.get("members")

    group_members_id = []
    for group_member in group_members:
        for student in students:
            if student["name"] == group_member:
                group_members_id.append(student["id"])
    # TODO: implement storage of a new group and return their info (sample response below)
    new_group = {
        "id": len(groups) + 1,
        "groupName": group_name,
        "members": group_members_id
    }
    groups.append(new_group)
  #  save_json_data(GROUPS_FILE, groups)

    return jsonify(new_group), 201

@app.route('/api/groups/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    """
    Route to delete a group by ID
    param group_id: The ID of the group to delete
    return: Empty response with status code 204
    """
  #  groups = load_json_data(GROUPS_FILE)
    # TODO: (delete the group with the specified id)
    group = next((g for g in groups if g['id'] == group_id), None)

    if group is None:
        abort(404, "Group not found")

 #   save_json_data(GROUPS_FILE, groups)
    return '', 204  # Return 204 (do not modify this line)

@app.route('/api/groups/<int:group_id>', methods=['GET'])
def get_group(group_id):
    """
    Route to get a group by ID (for fetching group members)
    param group_id: The ID of the group to retrieve
    return: The group object with member details
    """
    # TODO: (sample response below)
  #  groups = load_json_data(GROUPS_FILE)
    group = next((g for g in groups if g['id'] == group_id), None)
    if group is None:
        abort(404, "Group not found")
    member_details = [s for s in students if s['id'] in group['members']]

    group_with_details = {
        "id": group['id'],
        "groupName": group['groupName'],
        "members": member_details
    }
    
    return jsonify(group_with_details)


if __name__ == '__main__':
    app.run(port=3902, debug=True)
