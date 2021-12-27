import 'package:flutter/material.dart';

void main() => runApp(VSJApp());

class VSJApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Varanasi Software Junction',
      theme: ThemeData(
        primarySwatch: Colors.teal,
      ),
      home: VSJHomePage(title: 'Varanasi Software Junction'),
    );
  }
}

class VSJHomePage extends StatefulWidget {
  int mainaxisno = 0;
  int mainaxistotal = MainAxisAlignment.values.length;
  int crossaxisno = 0;
  int crossaxistotal = CrossAxisAlignment.values.length - 1;
  VSJHomePage({Key? key, required this.title}) : super(key: key);
  String getTitle() {
    return "VSJ - Main: ${MainAxisAlignment.values[mainaxisno].toString().replaceAll("MainAxisAlignment.", "")},  Cross: ${CrossAxisAlignment.values[crossaxisno].toString().replaceAll("CrossAxisAlignment.", "")}";
  }

  MainAxisAlignment mainaxisalignment = MainAxisAlignment.values[0];
  final String title;
  String display = "Varanasi Software Junction";

  @override
  _VSJPageState createState() => _VSJPageState();
}

class _VSJPageState extends State<VSJHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.getTitle()),
        centerTitle: true,
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: ElevatedButton(
                  child: const Text("MainAxis",style:TextStyle(fontSize: 10)),
                  onPressed: () {
                    widget.mainaxisno =
                        (widget.mainaxisno + 1) % widget.mainaxistotal;
                    widget.display = widget.getTitle();

                    setState(() {});
                  },
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: ElevatedButton(
                  child: const Text("Cross Axis",style:TextStyle(fontSize: 10)),
                  onPressed: () {
                    widget.crossaxisno =
                        (widget.crossaxisno + 1) % widget.crossaxistotal;
                    widget.display = widget.getTitle();

                    setState(() {});
                  },
                ),
              ),
            ],
          ),
          Expanded(
            child: ColoredBox(
              color: Colors.yellowAccent,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.values[widget.mainaxisno],
                crossAxisAlignment:
                    CrossAxisAlignment.values[widget.crossaxisno],
                children: <Widget>[
                  Container(
                      color: Colors.pinkAccent,
                      child: Icon(Icons.emoji_emotions,
                          size: 50, color: Colors.teal)),
                  Container(
                    color: Colors.blueAccent,
                    child: Icon(Icons.emoji_emotions_outlined,
                        size: 50, color: Colors.indigoAccent),
                  ),
                  Container(
                    color: Colors.purpleAccent,
                    child: Icon(Icons.emoji_emotions_sharp,
                        size: 50, color: Colors.teal),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
