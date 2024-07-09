import 'dart:convert';

import 'package:frontend/models/quiz.dart';
import 'package:frontend/models/responseAPI.dart';
import 'package:frontend/repository/quiz_repo.dart';
import 'package:http/http.dart' as http;

class QuizService {

  static const API = 'http://0.0.0.0:8000';

  Future<APIResponse<Quiz>> getQuiz(video_id) {
    return http.get(('$API/quizme') as Uri).then((data){
      if(data.statusCode == 200){
        final jsonData = json.decode(data.body);
        final quiz = Quiz(
          question: jsonData['question'],
          answer: jsonData['answer'],
          options: jsonData['options'],
          id: jsonData['id']
        );
        return APIResponse<Quiz>(data: quiz);
      }
      return APIResponse<Quiz>(error: true, errorMessage: 'Cannot get quiz of video $video_id');
    });
  }

  Future<APIResponse<Quiz>> generateQuiz(video_id) async {
    final videoUploadFile = await uploadFileData(video_id);

    return http.post(('$API/getquiz') as Uri, body: {
      'video': videoUploadFile
    }).then((data) {
      if (data.statusCode == 200) {
        final jsonData = json.decode(data.body);
        final quiz = Quiz(
          question: jsonData['question'],
          answer: jsonData['answer'],
          options: jsonData['options'],
          id: jsonData['id'],
        );
        return APIResponse<Quiz>(data: quiz);
      }
      return APIResponse<Quiz>(
          error: true,
          errorMessage: 'Cannot generate quiz of video $video_id');
    });
  }

  Future<APIResponse<Object>> postQuiz(video_id) async{
    // get video data
    final videoUploadFile = await uploadFileData(video_id);

    //generate quiz
    final quizResponse = await generateQuiz(video_id);
    if(quizResponse.error){
      return APIResponse<Object>(error: true, errorMessage: 'Cannot generate quiz of video $video_id');
    }
    final quiz = quizResponse.data;

    //post quiz
    return http.post(('$API/savequiz') as Uri, body: {
      'quiz': quiz, 'video_id': video_id}).then((data) {
        if(data.statusCode == 200){
          final jsonData = json.decode(data.body);
          return APIResponse<Object>(data: jsonData);
        }
        return APIResponse<Object>(error: true, errorMessage: 'Cannot save quiz of video $video_id');
      });
  }
}