



import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

void main() {
  BlocOverrides.runZoned(
    () {
      return runApp(const VsjApp());
    },
    blocObserver: VsjBlocObserver(),
  );
}

class VsjBlocObserver extends BlocObserver {
  @override
  void onChange(BlocBase bloc, Change change) {
    super.onChange(bloc, change);
    print(change);
  }

  @override
  void onTransition(Bloc bloc, Transition transition) {
    super.onTransition(bloc, transition);
    print(transition);
  }
}

class VsjApp extends StatelessWidget {
  const VsjApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (_) => BankBloc(),
      child:
          const MaterialApp(debugShowCheckedModeBanner: false, home: VsjBank()),
    );
  }
}

class VsjBank extends StatelessWidget {
  const VsjBank({Key? key}) : super(key: key);
  static final BankAccount account = BankAccount();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('VSJ Bloc Demo'),
        centerTitle: true,
        backgroundColor: Colors.teal,
      ),
      body: Center(
        child: BlocBuilder<BankBloc, BankAccount>(
          builder: (context, account) {
            return Text('$account',
                style: const TextStyle(
                    color: Colors.blueAccent, fontWeight: FontWeight.bold));
          },
        ),
      ),
      floatingActionButton: Column(
        crossAxisAlignment: CrossAxisAlignment.end,
        mainAxisAlignment: MainAxisAlignment.end,
        children: <Widget>[
          ElevatedButton(
            child: const Text("Deposit   "),
            onPressed: () {
              context.read<BankBloc>().add(BankDepositPressed());
            },
          ),
          const SizedBox(height: 4),
          ElevatedButton(
            child: const Text("Withdraw"),
            onPressed: () {
              context.read<BankBloc>().add(BankWithdrawPressed());
            },
          ),
        ],
      ),
    );
  }
}

abstract class BankAccountEvent {}

/// Notifies bloc to increment balance.
class BankDepositPressed extends BankAccountEvent {}

/// Notifies bloc to decrement balance.
class BankWithdrawPressed extends BankAccountEvent {}

class BankBloc extends Bloc<BankAccountEvent, BankAccount> {
  BankBloc() : super(VsjBank.account) {
    on<BankDepositPressed>((event, emit) {
      state.balance += 10;
      state.prevnooftransactions = state.nooftransactions;
      state.nooftransactions += 1;
      emit(state);
    });

    on<BankWithdrawPressed>((event, emit) {
      state.balance -= 5;
      state.prevnooftransactions = state.nooftransactions;
      state.nooftransactions += 1;
      emit(state);
    });
  }
}

class BankAccount {
  int nooftransactions = 0;
  int prevnooftransactions = 0;
  int balance = 0;
  @override
  String toString() {
    return "Balance=$balance, Transactions=$nooftransactions";
  }

  @override
  bool operator ==(Object other) {
    if (other is! BankAccount) return false;
    BankAccount ac = other;
    print(prevnooftransactions == ac.nooftransactions);
    return prevnooftransactions == ac.nooftransactions;
  }

  @override
  int get hashCode => balance.hashCode ^ nooftransactions.hashCode;
}





