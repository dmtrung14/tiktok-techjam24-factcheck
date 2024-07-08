import 'package:flutter/material.dart';
import 'package:frontend/models/quiz.dart';
import 'package:get/get.dart';
import 'package:frontend/constants.dart';
import 'package:frontend/controllers/quiz_controller.dart';
import 'package:timeago/timeago.dart' as tago;

class QuizScreen extends StatelessWidget {
  final String id;
  QuizScreen({
    Key? key,
    required this.id,
  }) : super(key: key);

  final QuizController quizController = Get.put(QuizController());

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    quizController.updatePostId(id);

    return Scaffold(
      appBar: AppBar(
        title: Text('Quiz App'),
      ),
      body: Obx(() {
        if (quizController.quiz == null) {
          return Center(child: CircularProgressIndicator());
        }

        Quiz quiz = quizController.quiz!;

        return Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Text(
                quiz.question,
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 20),
              ...quiz.options.keys.map((key) => RadioListTile<String>(
                    title: Text(quiz.options[key]!),
                    value: key,
                    groupValue: quizController.selectedOption,
                    onChanged: (value) {
                      if (value != null) {
                        quizController.checkAnswer(value, quiz.answer);
                      }
                    },
                  )),
              SizedBox(height: 20),
              Obx(() => Text(
                    quizController.feedbackMessage,
                    style: TextStyle(fontSize: 16, color: Colors.redAccent),
                  )),
            ],
          ),
        );
      }),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          quizController.updatePostId('your_video_id_here');
        },
        child: Icon(Icons.refresh),
      ),
    );
  }
}
