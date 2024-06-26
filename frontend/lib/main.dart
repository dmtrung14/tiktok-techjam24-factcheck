import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:chewie/chewie.dart';
import 'package:frontend/video_model.dart';
import 'package:video_player/video_player.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  try{
  await Firebase.initializeApp(
      options: const FirebaseOptions(
        apiKey: 'AIzaSyBLXcLqYMtxVJrPwJUI-90k6vLASwi-JgI',
        appId: '1:946494999907:web:8a10b03611477871e6d756',
        messagingSenderId: '946494999907',
        projectId: 'video-uploader-18225',
        authDomain: 'video-uploader-18225.firebaseapp.com',
        storageBucket: 'video-uploader-18225.appspot.com',
        measurementId: 'G-8TT40FJPJH',
      )
  );
  }catch(e){
    print('Firebase initialization error: $e');
  }
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Video App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: VideoGalleryPage(),
    );
  }
}

class VideoGalleryPage extends StatefulWidget {
  @override
  _VideoGalleryPageState createState() => _VideoGalleryPageState();
}

class _VideoGalleryPageState extends State<VideoGalleryPage> {
  Future<void> _uploadVideo() async {
    final result = await FilePicker.platform.pickFiles(type: FileType.video);
    if (result != null) {
      final file = result.files.first;
      final storageRef = FirebaseStorage.instance
          .ref()
          .child('videos/${DateTime.now().millisecondsSinceEpoch}.mp4');
      await storageRef.putData(file.bytes!);
      final downloadUrl = await storageRef.getDownloadURL();
      final docRef = await FirebaseFirestore.instance.collection('videos').add({
        'url': downloadUrl,
        'timestamp': FieldValue.serverTimestamp(),
      });

      print('Video uploaded with ID: ${docRef.id}');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Video Gallery'),
        actions: [
          IconButton(
            icon: Icon(Icons.upload),
            onPressed: _uploadVideo,
          ),
        ],
      ),
      body: StreamBuilder<QuerySnapshot>(
        stream: FirebaseFirestore.instance
            .collection('videos')
            .orderBy('timestamp', descending: true)
            .snapshots(),
        builder: (context, snapshot) {
          if (!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }
          final videoDocs = snapshot.data!.docs;
          final videos = videoDocs.map((doc) => Video.fromDocument(doc.data() as Map<String, dynamic>, doc.id)).toList();
          return GridView.builder(
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 2,
            ),
            itemCount: videos.length,
            itemBuilder: (context, index) {
              final video = videos[index];
              return GestureDetector(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => VideoPlayerPage(
                        videos: videos,
                        initialIndex: index,
                      ),
                    ),
                  );
                },
                child: AspectRatio(
                  aspectRatio: 16 / 9,
                  child: Image.network(
                    video.url,
                    fit: BoxFit.cover,
                    errorBuilder: (context, error, stackTrace) =>
                        Center(child: Icon(Icons.error)),
                    loadingBuilder: (context, child, loadingProgress) {
                      if (loadingProgress == null) return child;
                      return Center(
                        child: CircularProgressIndicator(
                          value: loadingProgress.expectedTotalBytes != null
                              ? loadingProgress.cumulativeBytesLoaded /
                                  loadingProgress.expectedTotalBytes!
                              : null,
                        ),
                      );
                    },
                  ),
                ),
              );
            },
          );
        },
      ),
    );
  }
}

class VideoPlayerPage extends StatefulWidget {
  final List<Video> videos;
  final int initialIndex;

  VideoPlayerPage({required this.videos, required this.initialIndex});

  @override
  _VideoPlayerPageState createState() => _VideoPlayerPageState();
}

class _VideoPlayerPageState extends State<VideoPlayerPage> {
  late PageController _pageController;
  late int _currentIndex;

  @override
  void initState() {
    super.initState();
    _pageController = PageController(initialPage: widget.initialIndex);
    _currentIndex = widget.initialIndex;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: PageView.builder(
        controller: _pageController,
        itemCount: widget.videos.length,
        onPageChanged: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        itemBuilder: (context, index) {
          return VideoPlayerWidget(
            videoUrl: widget.videos[index].url,
          );
        },
      ),
    );
  }
}

class VideoPlayerWidget extends StatefulWidget {
  final String videoUrl;

  VideoPlayerWidget({required this.videoUrl});

  @override
  _VideoPlayerWidgetState createState() => _VideoPlayerWidgetState();
}

class _VideoPlayerWidgetState extends State<VideoPlayerWidget> {
  late VideoPlayerController _videoPlayerController;
  ChewieController? _chewieController;

  @override
  void initState() {
    super.initState();
    _videoPlayerController = VideoPlayerController.network(widget.videoUrl)
      ..initialize().then((_) {
        setState(() {
          _chewieController = ChewieController(
            videoPlayerController: _videoPlayerController,
            aspectRatio: _videoPlayerController.value.aspectRatio,
            autoPlay: true,
            looping: true,
          );
        });
      });
  }

  @override
  void dispose() {
    _videoPlayerController.dispose();
    _chewieController?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return _chewieController != null
        ? Chewie(
            controller: _chewieController!,
          )
        : Center(
            child: CircularProgressIndicator(),
          );
  }
}