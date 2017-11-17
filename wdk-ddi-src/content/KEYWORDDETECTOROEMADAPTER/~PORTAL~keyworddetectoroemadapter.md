# Declarations in the keyworddetectoroemadapter header
This header Keyworddetectoroemadapter contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [IKeywordDetectorOemAdapterVtbl structure](ns-keyworddetectoroemadapter-ikeyworddetectoroemadaptervtbl.md) | TBD |
| [MIDL___MIDL_itf_keyworddetectoroemadapter_0000_0000_0001 structure](ns-keyworddetectoroemadapter---midl---midl-itf-keyworddetectoroemadapter-0000-0000-0001.md) | TBD |
| [MIDL_IKeywordDetectorOemAdapter_0003 structure](ns-keyworddetectoroemadapter---midl-ikeyworddetectoroemadapter-0003.md) | The KEYWORDSELECTOR struct is a triplet of IDs that uniquely select a particular keyword, language, and user combination. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IKeywordDetectorOemAdapter::ParseDetectionResultData method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-parsedetectionresultdata.md) | The ParseDetectionResultData method is called by the operating system after handling a keyword detection event and after retrieving the result data from KSPROPERTY_SOUNDDETECTOR_MATCHRESULT. |
| [IKeywordDetectorOemAdapter::GetCapabilities method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-getcapabilities.md) | The GetCapabilities method returns the keywords and languages supported by the object. |
| [IKeywordDetectorOemAdapter::VerifyUserKeyword method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-verifyuserkeyword.md) | The VerifyUserKeyword method is used by the training user experience to verify that one instance of a spoken utterance, captured during training, matches a predefined keyword within some tolerance. |
| [IKeywordDetectorOemAdapter::ComputeAndAddUserModelData method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-computeandaddusermodeldata.md) | The ComputeAndAddUserModelData method is used by the training user experience to compute the user-specific information relative to the user-independent keyword. |
| [IKeywordDetectorOemAdapter::BuildArmingPatternData method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-buildarmingpatterndata.md) | The BuildArmingPatternData method is called by the operating system to build OEM-specific pattern data that includes any keyword and user-specific model data for detection. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [MIDL_IKeywordDetectorOemAdapter_0002 enumeration](ne-keyworddetectoroemadapter---midl-ikeyworddetectoroemadapter-0002.md) | TBD |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IKeywordDetectorOemAdapter interface](nn-keyworddetectoroemadapter-ikeyworddetectoroemadapter~r1.md) | TBD |
| [IKeywordDetectorOemAdapter interface](nn-keyworddetectoroemadapter-ikeyworddetectoroemadapter.md) | TBD |

This header is used in these topics:

- [audio](..content/_audio)
