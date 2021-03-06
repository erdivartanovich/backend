import datetime
from app.models import db
from sqlalchemy.exc import SQLAlchemyError
from app.configs.constants import ROLE
from app.models.user_feedback import UserFeedback
from app.services.base_service import BaseService
from app.builders.response_builder import ResponseBuilder


class UserFeedbackService(BaseService):

    def index(self):
        response = ResponseBuilder()
        user_feedbacks = db.session.query(UserFeedback).all()
        results = []        
        for feedback in user_feedbacks:
            data = feedback.as_dict()
            results.append(data)
        return response.set_data(results).set_message('User feedback entries retrieved successfully').build()

    def create(self, payloads):
        response = ResponseBuilder()
        userfeedback = UserFeedback()
        userfeedback.user_id = payloads['user_id']
        userfeedback.content = payloads['content']
        db.session.add(userfeedback)
        try:
            db.session.commit()
            data = userfeedback.as_dict()
            return response.set_data(data).set_message('Feedback created').set_error(False).build()
        except SQLAlchemyError as e:
            data = e.orig.args
            return response.set_data(data).set_error(True).set_message('Some error occured, please try again later').build()
    
    def show(self, id, user):
        response = ResponseBuilder()
        result = db.session.query(UserFeedback).filter_by(id=id).first()
        if result is not None:
            if result.user_id == user['id'] or result.user_id == ROLE['admin']:
                result = result.as_dict()
                return response.set_data(result).set_error(False).set_message('user feedback retrieved successfully').build()
            else:
                return response.set_error(True).set_message('user is not authorized').build()
        else:
            return response.set_error(True).set_data(None).set_message('row not found').build()
