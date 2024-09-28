import '/flutter_flow/flutter_flow_util.dart';
import 'chat_copy_copy2_widget.dart' show ChatCopyCopy2Widget;
import 'package:flutter/material.dart';

class ChatCopyCopy2Model extends FlutterFlowModel<ChatCopyCopy2Widget> {
  ///  State fields for stateful widgets in this page.

  // State field(s) for TextField widget.
  FocusNode? textFieldFocusNode;
  TextEditingController? textController;
  String? Function(BuildContext, String?)? textControllerValidator;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    textFieldFocusNode?.dispose();
    textController?.dispose();
  }
}
