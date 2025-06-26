import uuid
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy import Enum as SqlEnum
from app.enums import UserRole, MeetingStatus

Base = declarative_base()

class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class User(Base, TimestampMixin):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    full_name = Column(String)
    password_hash = Column(String, nullable=False)
    role = Column(SqlEnum(UserRole, name="userrole"), default=UserRole.PERSONAL, nullable=False)
    meetings = relationship("Meeting", back_populates="user", cascade="all, delete-orphan")
    summaries = relationship("Summary", back_populates="user", cascade="all, delete-orphan")
    action_items = relationship("ActionItem", back_populates="user", cascade="all, delete-orphan")
    audio_files = relationship("AudioFile", back_populates="user", cascade="all, delete-orphan")

class Meeting(Base, TimestampMixin):
    __tablename__ = "meetings"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = Column(String, nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    is_live = Column(Boolean, default=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="meetings")
    status = Column(SqlEnum(MeetingStatus, name="meetingstatus"), default=MeetingStatus.SCHEDULED, nullable=False)
    transcripts = relationship("Transcript", back_populates="meeting", cascade="all, delete-orphan")
    audio_files = relationship("AudioFile", back_populates="meeting", cascade="all, delete-orphan")

class Transcript(Base, TimestampMixin):
    __tablename__ = "transcripts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    meeting_id = Column(UUID(as_uuid=True), ForeignKey('meetings.id'), nullable=False)
    content = Column(Text, nullable=False)
    language = Column(String, default="en")
    model_used = Column(String, nullable=True)
    meeting = relationship("Meeting", back_populates="transcripts")

class AudioFile(Base, TimestampMixin):
    __tablename__ = "audio_files"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    meeting_id = Column(UUID(as_uuid=True), ForeignKey('meetings.id'), nullable=False)
    file_path = Column(String, nullable=False)
    uploaded_by = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    meeting = relationship("Meeting", back_populates="audio_files")
    user = relationship("User", back_populates="audio_files")

class Summary(Base, TimestampMixin):
    __tablename__ = "summaries"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="summaries")

class ActionItem(Base, TimestampMixin):
    __tablename__ = "action_items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    description = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="action_items")