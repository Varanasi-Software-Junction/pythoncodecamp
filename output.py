



class VsjCubit extends Cubit<int> {
  VsjCubit(int startvalue) : super(startvalue);
  void double() => emit(state + state);
  void triple() => emit(state + state + state);
}
/*
 * Create Objects like this
final v0 = VsjCubit(0); // state starts at 0
final v10 = VsjCubit(10); // state starts at 10 
 */



