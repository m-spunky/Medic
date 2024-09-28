import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: const FirebaseOptions(
            apiKey: "AIzaSyATFKgSquvO6_aTfOxbxGsPHHr3AZnUQTo",
            authDomain: "demo1-6nugji.firebaseapp.com",
            projectId: "demo1-6nugji",
            storageBucket: "demo1-6nugji.appspot.com",
            messagingSenderId: "902387129372",
            appId: "1:902387129372:web:83bb44f7e8edbe27d2d3d9"));
  } else {
    await Firebase.initializeApp();
  }
}
