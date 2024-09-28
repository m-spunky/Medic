import '/flutter_flow/flutter_flow_calendar.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/form_field_controller.dart';
import 'appointment_medic_widget.dart' show AppointmentMedicWidget;
import 'package:flutter/material.dart';
import 'package:mask_text_input_formatter/mask_text_input_formatter.dart';

class AppointmentMedicModel extends FlutterFlowModel<AppointmentMedicWidget> {
  ///  State fields for stateful widgets in this page.

  final formKey1 = GlobalKey<FormState>();
  final formKey2 = GlobalKey<FormState>();
  // State field(s) for sheduleDateCalendar widget.
  DateTimeRange? sheduleDateCalendarSelectedDay;
  // State field(s) for fullName widget.
  FocusNode? fullNameFocusNode1;
  TextEditingController? fullNameTextController1;
  String? Function(BuildContext, String?)? fullNameTextController1Validator;
  String? _fullNameTextController1Validator(BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Please enter the patients full name.';
    }

    return null;
  }

  // State field(s) for age widget.
  FocusNode? ageFocusNode1;
  TextEditingController? ageTextController1;
  String? Function(BuildContext, String?)? ageTextController1Validator;
  String? _ageTextController1Validator(BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Please enter an age for the patient.';
    }

    return null;
  }

  // State field(s) for dateOfBirth widget.
  FocusNode? dateOfBirthFocusNode1;
  TextEditingController? dateOfBirthTextController1;
  final dateOfBirthMask1 = MaskTextInputFormatter(mask: '##/##/####');
  String? Function(BuildContext, String?)? dateOfBirthTextController1Validator;
  String? _dateOfBirthTextController1Validator(
      BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Please enter the date of birth of the patient.';
    }

    return null;
  }

  // State field(s) for ChoiceChips widget.
  FormFieldController<List<String>>? choiceChipsValueController1;
  String? get choiceChipsValue1 =>
      choiceChipsValueController1?.value?.firstOrNull;
  set choiceChipsValue1(String? val) =>
      choiceChipsValueController1?.value = val != null ? [val] : [];
  // State field(s) for description widget.
  FocusNode? descriptionFocusNode1;
  TextEditingController? descriptionTextController1;
  String? Function(BuildContext, String?)? descriptionTextController1Validator;
  String? _descriptionTextController1Validator(
      BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Field is required';
    }

    return null;
  }

  DateTime? datePicked1;
  DateTime? datePicked2;
  // State field(s) for Calendar widget.
  DateTimeRange? calendarSelectedDay;
  // State field(s) for fullName widget.
  FocusNode? fullNameFocusNode2;
  TextEditingController? fullNameTextController2;
  String? Function(BuildContext, String?)? fullNameTextController2Validator;
  String? _fullNameTextController2Validator(BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Please enter the patients full name.';
    }

    return null;
  }

  // State field(s) for age widget.
  FocusNode? ageFocusNode2;
  TextEditingController? ageTextController2;
  String? Function(BuildContext, String?)? ageTextController2Validator;
  String? _ageTextController2Validator(BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Please enter an age for the patient.';
    }

    return null;
  }

  // State field(s) for dateOfBirth widget.
  FocusNode? dateOfBirthFocusNode2;
  TextEditingController? dateOfBirthTextController2;
  final dateOfBirthMask2 = MaskTextInputFormatter(mask: '##/##/####');
  String? Function(BuildContext, String?)? dateOfBirthTextController2Validator;
  String? _dateOfBirthTextController2Validator(
      BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Please enter the date of birth of the patient.';
    }

    return null;
  }

  // State field(s) for ChoiceChips widget.
  FormFieldController<List<String>>? choiceChipsValueController2;
  String? get choiceChipsValue2 =>
      choiceChipsValueController2?.value?.firstOrNull;
  set choiceChipsValue2(String? val) =>
      choiceChipsValueController2?.value = val != null ? [val] : [];
  // State field(s) for description widget.
  FocusNode? descriptionFocusNode2;
  TextEditingController? descriptionTextController2;
  String? Function(BuildContext, String?)? descriptionTextController2Validator;
  DateTime? datePicked3;
  DateTime? datePicked4;

  @override
  void initState(BuildContext context) {
    sheduleDateCalendarSelectedDay = DateTimeRange(
      start: DateTime.now().startOfDay,
      end: DateTime.now().endOfDay,
    );
    fullNameTextController1Validator = _fullNameTextController1Validator;
    ageTextController1Validator = _ageTextController1Validator;
    dateOfBirthTextController1Validator = _dateOfBirthTextController1Validator;
    descriptionTextController1Validator = _descriptionTextController1Validator;
    calendarSelectedDay = DateTimeRange(
      start: DateTime.now().startOfDay,
      end: DateTime.now().endOfDay,
    );
    fullNameTextController2Validator = _fullNameTextController2Validator;
    ageTextController2Validator = _ageTextController2Validator;
    dateOfBirthTextController2Validator = _dateOfBirthTextController2Validator;
  }

  @override
  void dispose() {
    fullNameFocusNode1?.dispose();
    fullNameTextController1?.dispose();

    ageFocusNode1?.dispose();
    ageTextController1?.dispose();

    dateOfBirthFocusNode1?.dispose();
    dateOfBirthTextController1?.dispose();

    descriptionFocusNode1?.dispose();
    descriptionTextController1?.dispose();

    fullNameFocusNode2?.dispose();
    fullNameTextController2?.dispose();

    ageFocusNode2?.dispose();
    ageTextController2?.dispose();

    dateOfBirthFocusNode2?.dispose();
    dateOfBirthTextController2?.dispose();

    descriptionFocusNode2?.dispose();
    descriptionTextController2?.dispose();
  }
}
