from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock Dataset Mahasiswa
students = [
    {"id": 1, "nim": "202611001", "name": "Ahmad Fauzi", "major": "Teknik Informatika","gpa": 3.75},
    {"id": 2, "nim": "202611002", "name": "Budi Santoso", "major": "Sistem Informasi","gpa": 3.40},
    {"id": 3, "nim": "202611003", "name": "Citra Lestari", "major": "TeknikInformatika", "gpa": 3.90}
]
# 1. GET: Ambil Semua Mahasiswa & Filter Query Parameter (?major=...)
@app.route('/api/v1/students', methods=['GET'])
def get_students():
    major_query = request.args.get('major')
    if major_query:
        filtered = [s for s in students if s['major'].lower() == major_query.lower()]
        return jsonify({"status": "success", "total": len(filtered), "data": filtered}), 200
    return jsonify({"status": "success", "total": len(students), "data": students}), 200


# 2. GET by ID: Menggunakan Path Parameter
@app.route('/api/v1/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"status": "fail", "message": "Mahasiswa tidak ditemukan"}), 404
    return jsonify({"status": "success", "data": student}), 200


# 3. PUT: Update Data Mahasiswa Lengkap
@app.route('/api/v1/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"status": "fail", "message": "Mahasiswa tidak ditemukan"}), 404

    data = request.get_json()
    student['name'] = data.get('name', student['name'])
    student['major'] = data.get('major', student['major'])
    student['gpa'] = data.get('gpa', student['gpa'])

    return jsonify({"status": "success", "message": "Data berhasil diperbarui", "data": student}), 200

# 4. DELETE: Hapus Data Mahasiswa Berdasarkan ID
@app.route('/api/v1/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"status": "fail", "message": "Mahasiswa tidak ditemukan"}), 404

    students = [s for s in students if s['id'] != student_id]
    return jsonify({"status": "success", "message": "Data mahasiswa berhasil dihapus"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)