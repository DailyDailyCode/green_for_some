import 'package:flutter/material.dart';

class Answer extends StatelessWidget {
  final Function selectHandler;

  Answer(this.selectHandler);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
            foregroundColor: Colors.blue, backgroundColor: Colors.white),
        child: Text('Answer 1'),
        onPressed: selectHandler,
      ),
    );
  }
}
