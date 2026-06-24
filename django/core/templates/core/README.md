# Course Platform - HTML Templates

## Overview
This project now includes HTML templates for displaying courses and user enrollment in a web interface.

## Template Structure

```
django/core/templates/core/
├── base.html              # Base template with consistent layout
└── course_list.html       # Course listing page
```

## Templates Created

### 1. base.html
**Purpose:** Main layout template with consistent styling

**Features:**
- Responsive design (works on desktop and mobile)
- Gradient header with logo/branding
- Course cards with hover effects
- CSS styling for modern look and feel

### 2. course_list.html
**Purpose:** Display list of available courses

**Features:**
- Grid layout for course cards
- Course information display (title, description, enrollment count)
- "Enroll Now" buttons for each course
- JavaScript integration for enrollment functionality
- Loading/error states handling

## New Endpoints Added

| Method | URL | Purpose |
|--------|-----|----------|
| GET | `/api/course-list/` | Render course listing page |
| POST | `/api/enroll/` | Handle course enrollment |

## Usage

### Access Course List
```bash
# Via web browser
http://localhost:8000/api/course-list/

# OR via curl (to test)
curl http://localhost:8000/api/course-list/
```

### Enroll in Course
```bash
curl -X POST http://localhost:8000/api/enroll/ \
  -H "Content-Type: application/json" \
  -d '{"course_id": 1, "student_email": "student@example.com"}'
```

## Template Features

### Course Cards
Each course card displays:
- Course title (with ellipsis for long names)
- Brief description (truncated if too long)
- Student enrollment count
- Lesson count
- "Enroll Now" button

### Interactive Elements
- **Hover effects:** Course cards scale up on hover
- **Enroll functionality:** JavaScript-powered enrollment system
- **Responsive design:** Works on all screen sizes
- **Loading states:** User-friendly feedback during operations

### Styling
- Modern gradient header
- Clean card-based layout
- Mobile-responsive grid system
- Smooth transitions and animations

## Enrollment System

The enrollment system includes:
- AJAX-based enrollment via JavaScript
- Real-time feedback to users
- Integration with the Course.users ManyToManyField
- User authentication (mocked for demo)

## Next Steps

You can further enhance the templates by:
- Adding course images/thumbnails
- Implementing pagination for large course lists
- Adding search/filter functionality
- Creating detailed course pages
- Implementing user authentication in templates
- Adding course review/rating system
