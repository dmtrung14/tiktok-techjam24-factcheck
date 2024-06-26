// File generated by FlutterFire CLI.
// ignore_for_file: type=lint
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        return macos;
      case TargetPlatform.windows:
        return windows;
      case TargetPlatform.linux:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for linux - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyBLXcLqYMtxVJrPwJUI-90k6vLASwi-JgI',
    appId: '1:946494999907:web:8a10b03611477871e6d756',
    messagingSenderId: '946494999907',
    projectId: 'video-uploader-18225',
    authDomain: 'video-uploader-18225.firebaseapp.com',
    storageBucket: 'video-uploader-18225.appspot.com',
    measurementId: 'G-8TT40FJPJH',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyAJwpblH1FBzoSVF6py-mQGBifPJkfmvOk',
    appId: '1:946494999907:android:65189323d0e7c557e6d756',
    messagingSenderId: '946494999907',
    projectId: 'video-uploader-18225',
    storageBucket: 'video-uploader-18225.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyChXlyX1940sFBL6lJOw_ycfIfXlh0D7C8',
    appId: '1:946494999907:ios:3a96d9840c0505e2e6d756',
    messagingSenderId: '946494999907',
    projectId: 'video-uploader-18225',
    storageBucket: 'video-uploader-18225.appspot.com',
    iosBundleId: 'com.example.frontend',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyChXlyX1940sFBL6lJOw_ycfIfXlh0D7C8',
    appId: '1:946494999907:ios:3a96d9840c0505e2e6d756',
    messagingSenderId: '946494999907',
    projectId: 'video-uploader-18225',
    storageBucket: 'video-uploader-18225.appspot.com',
    iosBundleId: 'com.example.frontend',
  );

  static const FirebaseOptions windows = FirebaseOptions(
    apiKey: 'AIzaSyBLXcLqYMtxVJrPwJUI-90k6vLASwi-JgI',
    appId: '1:946494999907:web:e5ecc7a8c8699f9fe6d756',
    messagingSenderId: '946494999907',
    projectId: 'video-uploader-18225',
    authDomain: 'video-uploader-18225.firebaseapp.com',
    storageBucket: 'video-uploader-18225.appspot.com',
    measurementId: 'G-EJ5YP1WHYQ',
  );

}