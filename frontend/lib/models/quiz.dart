import 'package:cloud_firestore/cloud_firestore.dart';

class Quiz {
  String question;
  String answer;
  Map<String, String> options;
  String id;

  Quiz({
    required this.question,
    required this.answer,
    required this.options,
    required this.id,
  });

  Map<String, dynamic> toJson() => {
        'question': question,
        'answer': answer,
        'options': {
          'A': options['A'],
          'B': options['B'],
          'C': options['C'],
          'D': options['D'],
        },
        'id': id,
      };

  static Quiz fromSnap(DocumentSnapshot snap) {
    var snapshot = snap.data() as Map<String, dynamic>;
    return Quiz(
        question: snapshot['question'],
        answer: snapshot['answer'],
        options: {
        'A': snapshot['options']['A'] ,
        'B': snapshot['options']['B'],
        'C': snapshot['options']['C'],
        'D': snapshot['options']['D'],
      },
        id: snapshot['id']
    );
  }
}