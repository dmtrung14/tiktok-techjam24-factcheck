import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';

class VideoGalleryPage extends StatefulWidget {
  @override
  _VideoGalleryPageState createState() => _VideoGalleryPageState();
}

class _VideoGalleryPageState extends State<VideoGalleryPage> {
  Future<void> _uploadVideo() async {
    try {
      final result = await FilePicker.platform.pickFiles(type: FileType.video);
      if (result != null && result.files.isNotEmpty) {
        final file = result.files.first;
        if (file.bytes != null) {
          final storageRef = FirebaseStorage.instance
              .ref()
              .child('videos/${DateTime.now().millisecondsSinceEpoch}.mp4');
          // Uploading the video
          await storageRef.putData(file.bytes!);
          // Getting the download URL
          final downloadUrl = await storageRef.getDownloadURL();
          // Storing the URL in Firestore
          await FirebaseFirestore.instance.collection('videos').add({
            'url': downloadUrl,
            'timestamp': FieldValue.serverTimestamp(),
          });
        } else {
          print("File bytes are null");
        }
      } else {
        print("No file picked or file list is empty");
      }
    } catch (e) {
      print("Error uploading video: $e");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Video Gallery'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: _uploadVideo,
          child: Text('Upload Video'),
        ),
      ),
    );
  }
}
