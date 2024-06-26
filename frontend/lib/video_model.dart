// lib/video.dart

import 'package:cloud_firestore/cloud_firestore.dart';

class Video {
  final String id;
  final String url;
  final DateTime? timestamp;

  Video({
    required this.id,
    required this.url,
    this.timestamp,
  });

  factory Video.fromDocument(Map<String, dynamic> doc, String id) {
    return Video(
      id: id,
      url: doc['url'] as String,
      timestamp: (doc['timestamp'] as Timestamp?)?.toDate(),
    );
  }

  Map<String, dynamic> toDocument() {
    return {
      'url': url,
      'timestamp': timestamp != null ? Timestamp.fromDate(timestamp!) : null,
    };
  }
}
