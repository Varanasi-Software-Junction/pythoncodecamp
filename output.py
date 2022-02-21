import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

Future<void> main() async {
  final cubit = VsjCubit(5);
  final subscription = cubit.stream.listen(print);
  while(true)
  {
  cubit.double();
  cubit.triple();
  await Future.delayed(Duration(seconds: 5));
  cubit.triple();
  cubit.double();
  await Future.delayed(Duration(seconds: 5));
  }
  //await subscription.cancel();
  //await cubit.close();
  print("Done");
}

class VsjCubit extends Cubit<int> {
  VsjCubit(int startvalue) : super(startvalue);
  void double() => emit(state + state);
  void triple() => emit(state + state + state);
  //To observe the change override the onChange method.
  @override
  void onChange(Change<int> change) {
    print(change);
    super.onChange(change);
  }
}
/*
 * Create Objects like this
final v0 = VsjCubit(0); // state starts at 0
final v10 = VsjCubit(10); // state starts at 10 
 */
