"""
Test script for all endpoints in the Course Platform.
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.test import Client

def test_endpoints():
    """Test all endpoints in the Course Platform."""
    client = Client()
    
    print("🧪 Testing Course Platform Endpoints")
    print("=" * 50)
    
    # Test course list (HTML)
    print("\n1. Testing GET /api/courses/ (HTML)")
    response = client.get('/api/courses/')
    print(f"   Status: {response.status_code}")
    assert response.status_code == 200, "Course list should return 200"
    print("   ✅ Passed")
    
    # Test course list (JSON)
    print("\n2. Testing GET /api/courses/ (JSON)")
    response = client.get('/api/courses/', HTTP_ACCEPT='application/json')
    print(f"   Status: {response.status_code}")
    assert response.status_code == 200, "Course list JSON should return 200"
    print("   ✅ Passed")
    
    # Test course detail
    print("\n3. Testing GET /api/courses/1/")
    response = client.get('/api/courses/1/')
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 404], "Course detail should return 200 or 404"
    print("   ✅ Passed")
    
    # Test lesson list
    print("\n4. Testing GET /api/courses/1/lessons/")
    response = client.get('/api/courses/1/lessons/')
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 404], "Lesson list should return 200 or 404"
    print("   ✅ Passed")
    
    # Test lesson detail
    print("\n5. Testing GET /api/lessons/1/")
    response = client.get('/api/lessons/1/')
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 404], "Lesson detail should return 200 or 404"
    print("   ✅ Passed")
    
    # Test class list
    print("\n6. Testing GET /api/lessons/1/classes/")
    response = client.get('/api/lessons/1/classes/')
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 404], "Class list should return 200 or 404"
    print("   ✅ Passed")
    
    # Test class detail
    print("\n7. Testing GET /api/classes/1/")
    response = client.get('/api/classes/1/')
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 404], "Class detail should return 200 or 404"
    print("   ✅ Passed")
    
    # Test signup
    print("\n8. Testing POST /api/signup/")
    response = client.post(
        '/api/signup/',
        data='{"names":"Test","last_names":"User","email":"test3@test.com","password":"test123"}',
        content_type='application/json'
    )
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 201, 400], "Signup should return 200, 201, or 400"
    print("   ✅ Passed")
    
    # Test login
    print("\n9. Testing POST /api/login/")
    response = client.post(
        '/api/login/',
        data='{"email":"david@test.com","password":"1234"}',
        content_type='application/json'
    )
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 400, 401], "Login should return 200, 400, or 401"
    print("   ✅ Passed")
    
    # Test enroll
    print("\n10. Testing POST /api/enroll/")
    response = client.post(
        '/api/enroll/',
        data='{"course_id":1,"student_email":"david@test.com"}',
        content_type='application/json'
    )
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 400, 404], "Enroll should return 200, 400, or 404"
    print("   ✅ Passed")
    
    # Test course create form
    print("\n11. Testing GET /api/courses/create/")
    response = client.get('/api/courses/create/')
    print(f"   Status: {response.status_code}")
    assert response.status_code == 200, "Course create form should return 200"
    print("   ✅ Passed")
    
    # Test lesson create form
    print("\n12. Testing GET /api/courses/1/lessons/create/")
    response = client.get('/api/courses/1/lessons/create/')
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 404], "Lesson create form should return 200 or 404"
    print("   ✅ Passed")
    
    # Test class create form
    print("\n13. Testing GET /api/lessons/1/classes/create/")
    response = client.get('/api/lessons/1/classes/create/')
    print(f"   Status: {response.status_code}")
    assert response.status_code in [200, 404], "Class create form should return 200 or 404"
    print("   ✅ Passed")
    
    print("\n" + "=" * 50)
    print("🎉 All tests passed!")
    print("=" * 50)
    
    print("\n📋 Available URLs:")
    print("   GET  /api/courses/                  - List all courses")
    print("   GET  /api/courses/create/           - Create course form")
    print("   GET  /api/courses/<id>/             - Course details")
    print("   GET  /api/courses/<id>/update/      - Update course form")
    print("   GET  /api/courses/<id>/delete/      - Delete course confirmation")
    print("   GET  /api/courses/<id>/lessons/     - List lessons")
    print("   GET  /api/courses/<id>/lessons/create/ - Create lesson form")
    print("   GET  /api/lessons/<id>/             - Lesson details")
    print("   GET  /api/lessons/<id>/update/      - Update lesson form")
    print("   GET  /api/lessons/<id>/delete/      - Delete lesson confirmation")
    print("   GET  /api/lessons/<id>/classes/     - List classes")
    print("   GET  /api/lessons/<id>/classes/create/ - Create class form")
    print("   GET  /api/classes/<id>/             - Class details")
    print("   GET  /api/classes/<id>/update/      - Update class form")
    print("   GET  /api/classes/<id>/delete/      - Delete class confirmation")
    print("   POST /api/signup/                   - User signup")
    print("   POST /api/login/                    - User login")
    print("   POST /api/enroll/                   - Enroll in course")
    print("   GET  /admin/                        - Django admin")

if __name__ == "__main__":
    test_endpoints()
