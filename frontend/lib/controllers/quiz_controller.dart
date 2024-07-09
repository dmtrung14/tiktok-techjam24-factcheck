import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:get/get.dart';
import 'package:frontend/constants.dart';
import 'package:frontend/models/quiz.dart';
import 'package:frontend/services/quiz_service.dart';

class QuizController extends GetxController {
  final Rx<Quiz?> _quiz = Rx<Quiz?>(null);
  final RxString _selectedOption = ''.obs;
  final RxString _feedbackMessage = ''.obs;

  Quiz? get quiz => _quiz.value;
  String get selectedOption => _selectedOption.value;
  String get feedbackMessage => _feedbackMessage.value;

  String _postId = "";

  updatePostId(String id) {
    _postId = id;
    getQuiz();
  }

  postQuizToDB() async {
    try {
      QuizService quizService = QuizService();
      await quizService.postQuiz(_postId);
    } catch (e) {
      // Handle the error here
      print('Error posting quiz to DB: $e');
      return e;
    }

  }

  getQuiz() async {
      try {
          postQuizToDB();
          DocumentSnapshot doc = await FirebaseFirestore.instance
              .collection('quizzes')
              .doc(_postId)
              .get();
  
          if (doc.exists) {
              _quiz.value = Quiz.fromSnap(doc);
          }
      } catch (e) {
          // Handle the error here
          print('Error getting quiz: $e');
          return e;
      }
  }

  void checkAnswer(String answer, String correctAnswer) {
    _selectedOption.value = answer;
    if (answer == correctAnswer) {
      _feedbackMessage.value = "Correct!";
    } else {
      _feedbackMessage.value = "Incorrect!";
    }
  }
}
