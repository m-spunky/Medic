import '/flutter_flow/flutter_flow_util.dart';
import 'home_page_medic_widget.dart' show HomePageMedicWidget;
import 'package:flutter/material.dart';

class HomePageMedicModel extends FlutterFlowModel<HomePageMedicWidget> {
  ///  State fields for stateful widgets in this page.

  // State field(s) for PlacePicker widget.
  FFPlace placePickerValue = const FFPlace();
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
