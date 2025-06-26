from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    ORGANIZER = "organizer"
    ANALYST = "analyst"
    REPORTER = "reporter"
    PERSONAL = "personal"
    STUDENT = "student"
    MODERATOR = "moderator"

class MeetingStatus(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"