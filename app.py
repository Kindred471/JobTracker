from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # 如果前后端在不同端口，可启用 CORS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(200))
    position = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)

with app.app_context():
    db.create_all()

# 获取所有记录
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.order_by(Job.id.desc()).all()
    return jsonify([{
        'id': job.id,
        'company': job.company,
        'website': job.website,
        'position': job.position,
        'status': job.status,
        'date': job.date
    } for job in jobs])

# 新增记录
@app.route('/api/jobs', methods=['POST'])
def add_job():
    data = request.json
    job = Job(
        company=data['company'],
        website=data.get('website', ''),
        position=data['position'],
        status=data['status'],
        date=data['date']
    )
    db.session.add(job)
    db.session.commit()
    return jsonify({
        "id": job.id,
        "company": job.company,
        "website": job.website,
        "position": job.position,
        "status": job.status,
        "date": job.date
    }), 201

# 更新记录
@app.route('/api/jobs/<int:id>', methods=['PUT'])
def update_job(id):
    data = request.json
    job = Job.query.get(id)
    if not job:
        return jsonify({'error': 'Not found'}), 404
    job.company = data['company']
    job.website = data.get('website','')
    job.position = data['position']
    job.status = data['status']
    job.date = data['date']
    db.session.commit()
    return jsonify({'message':'Updated'})

# 删除记录
@app.route('/api/jobs/<int:id>', methods=['DELETE'])
def delete_job(id):
    job = Job.query.get(id)
    if not job:
        return jsonify({'error': 'Not found'}), 404
    db.session.delete(job)
    db.session.commit()
    return jsonify({'message':'Deleted'})

# 渲染首页（前后端不分离）
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
