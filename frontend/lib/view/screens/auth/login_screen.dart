import 'package:flutter/material.dart';
import 'package:frontend/view/widgets/glitch.dart';
import 'package:frontend/view/widgets/text_input.dart';

class LoginScreen extends StatelessWidget {
   LoginScreen({super.key,});
  TextEditingController _emailController = new TextEditingController();
  TextEditingController _passwordController = new TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        alignment: Alignment.center,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,  
          children: [
            GlithEffect(child: const Text("Fact Check", style: TextStyle(fontWeight: FontWeight.w900, fontSize: 30))),
            SizedBox(height: 25),
            Container(
              margin: EdgeInsets.symmetric(horizontal:20),
              child: TextInputField(
                controller: _emailController,
                myIcon: Icons.email,
                myLabelText: "Email",
              ),
            ),
            SizedBox(height: 20),
            Container(
              margin: EdgeInsets.symmetric(horizontal:20),
              child: TextInputField(
                controller: _passwordController,
                myIcon: Icons.lock,
                myLabelText: "Password",
                toHide: true,
              ),
            ),
            SizedBox(height: 30),
            ElevatedButton(onPressed: (){}, child: Container(padding: EdgeInsets.symmetric(horizontal: 50, vertical: 10), child: Text("Login")))
          ],
          )
      ),
    );
  }
}