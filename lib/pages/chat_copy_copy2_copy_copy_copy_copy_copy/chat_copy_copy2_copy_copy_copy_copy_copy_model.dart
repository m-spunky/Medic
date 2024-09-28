import '/flutter_flow/flutter_flow_util.dart';
import 'chat_copy_copy2_copy_copy_copy_copy_copy_widget.dart'
    show ChatCopyCopy2CopyCopyCopyCopyCopyWidget;
import 'package:flutter/material.dart';

class ChatCopyCopy2CopyCopyCopyCopyCopyModel
    extends FlutterFlowModel<ChatCopyCopy2CopyCopyCopyCopyCopyWidget> {
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
