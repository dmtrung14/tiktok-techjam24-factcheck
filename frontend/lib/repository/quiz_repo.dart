import 'dart:typed_data';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_storage/firebase_storage.dart';

Future<Uint8List?> uploadFileData(String video_id) async {
  try {
    final QuerySnapshot snapshot = await FirebaseFirestore.instance
        .collection('videos')
        .where('video_id', isEqualTo: video_id)
        .get();

    if (snapshot.docs.isNotEmpty) {
      const fiveMegabyte = 5*1024 * 1024;
      final videoUrl = snapshot.docs.first.get('videoUrl');
      final Uint8List? data = await videoUrl.getData(fiveMegabyte);
      return data;
    } else {
      print('No video found with id: $video_id');
      return null;
    }
  } catch (e) {
    print('Error retrieving video URL: $e');
    return null;
  }
}
