import "package:flutter/material.dart";
import "package:frontend/constant.dart";

class TextInputField extends StatelessWidget {
  final TextEditingController controller;
  final IconData myIcon;
  final String myLabelText;
  final bool toHide;
  const TextInputField({Key? key ,
    required this.controller,
    required this.myIcon,
    required this.myLabelText,
    this.toHide = false
  });

  // ignore: empty_constructor_bodies
  @override
  Widget build(BuildContext context) {
    return TextField(
      obscureText: toHide,
      controller:controller,
      decoration: InputDecoration(
        icon: Icon(myIcon),
        labelText: myLabelText,
        enabledBorder: OutlineInputBorder(
          borderSide: const BorderSide(color: borderColor),
          borderRadius: BorderRadius.circular(5)
        ),
        focusedBorder: OutlineInputBorder(
          borderSide: const BorderSide(color: borderColor),
          borderRadius: BorderRadius.circular(5)
        ),
      ),

    );
  }
}