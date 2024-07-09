import "package:firebase_core/firebase_core.dart";
import "package:flutter/material.dart";
import "package:frontend/constants.dart";
import "package:frontend/controllers/auth_controller.dart";
import "package:frontend/services/quiz_service.dart";
import "package:frontend/views/screens/auth/login_screen.dart";
import "package:get/get.dart";
import "package:get_it/get_it.dart";

void setupLocator() {
  GetIt.I.registerLazySingleton(() => QuizService());
}

void main() async{
  setupLocator();
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp().then((value){
    Get.put(AuthController());
  });
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      debugShowCheckedModeBanner: false,
      title: "My App",
      theme: ThemeData.dark().copyWith(scaffoldBackgroundColor: backgroundColor),
      home:  LoginScreen(),
    );
  }
}