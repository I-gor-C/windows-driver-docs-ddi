# Keyworddetectoroemadapter.h header


This header is used by Audio. For more information, see
- [Audio](../_audio/index.md)

Keyworddetectoroemadapter.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [IKeywordDetectorOemAdapter::BuildArmingPatternData method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-buildarmingpatterndata.md) | The BuildArmingPatternData method is called by the operating system to build OEM-specific pattern data that includes any keyword and user-specific model data for detection. |
| [IKeywordDetectorOemAdapter::ComputeAndAddUserModelData method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-computeandaddusermodeldata.md) | The ComputeAndAddUserModelData method is used by the training user experience to compute the user-specific information relative to the user-independent keyword. |
| [IKeywordDetectorOemAdapter::GetCapabilities method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-getcapabilities.md) | The GetCapabilities method returns the keywords and languages supported by the object. |
| [IKeywordDetectorOemAdapter::ParseDetectionResultData method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-parsedetectionresultdata.md) | The ParseDetectionResultData method is called by the operating system after handling a keyword detection event and after retrieving the result data from KSPROPERTY_SOUNDDETECTOR_MATCHRESULT. |
| [IKeywordDetectorOemAdapter::VerifyUserKeyword method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-verifyuserkeyword.md) | The VerifyUserKeyword method is used by the training user experience to verify that one instance of a spoken utterance, captured during training, matches a predefined keyword within some tolerance. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [MIDL_IKeywordDetectorOemAdapter_0003 structure](ns-keyworddetectoroemadapter---midl-ikeyworddetectoroemadapter-0003.md) | The KEYWORDSELECTOR struct is a triplet of IDs that uniquely select a particular keyword, language, and user combination. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IKeywordDetectorOemAdapter interface](nn-keyworddetectoroemadapter-ikeyworddetectoroemadapter.md) | IKeywordDetectorOemAdapter is a Component Object Model (COM) interface for interacting with the Voice Activation Driver Interface. The IKeywordDetectorOemAdapter interface is supported in Windows 10 and later versions of Windows. |
| [IKeywordDetectorOemAdapter interface](nn-keyworddetectoroemadapter-ikeyworddetectoroemadapter~r1.md) | IKeywordDetectorOemAdapter is a Component Object Model (COM) interface for interacting with the Voice Activation Driver Interface. The IKeywordDetectorOemAdapter interface is supported in Windows 10 and later versions of Windows. |
