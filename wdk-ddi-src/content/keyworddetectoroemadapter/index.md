---
UID: NA:
---

# Keyworddetectoroemadapter.h header

## -description

This header is used by Audio. For more information, see
- [Audio](../_audio/index.md)

Keyworddetectoroemadapter.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [__MIDL_IKeywordDetectorOemAdapter_0003 structure](ns-keyworddetectoroemadapter-__midl_ikeyworddetectoroemadapter_0003.md) | The KEYWORDSELECTOR struct is a triplet of IDs that uniquely select a particular keyword, language, and user combination. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [__MIDL_IKeywordDetectorOemAdapter_0002 enumeration](ne-keyworddetectoroemadapter-__midl_ikeyworddetectoroemadapter_0002.md) | The KEYWORDID enumeration identifies the phrase text/function of a keyword. The value is also be used in the Windows Biometric Service adapters. |

## Methods

| Title   | Description   |
| ---- |:---- |
| [IKeywordDetectorOemAdapter::BuildArmingPatternData method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-buildarmingpatterndata.md) | The BuildArmingPatternData method is called by the operating system to build OEM-specific pattern data that includes any keyword and user-specific model data for detection. |
| [IKeywordDetectorOemAdapter::ComputeAndAddUserModelData method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-computeandaddusermodeldata.md) | The ComputeAndAddUserModelData method is used by the training user experience to compute the user-specific information relative to the user-independent keyword. |
| [IKeywordDetectorOemAdapter::GetCapabilities method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-getcapabilities.md) | The GetCapabilities method returns the keywords and languages supported by the object. |
| [IKeywordDetectorOemAdapter::ParseDetectionResultData method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-parsedetectionresultdata.md) | The ParseDetectionResultData method is called by the operating system after handling a keyword detection event and after retrieving the result data from KSPROPERTY_SOUNDDETECTOR_MATCHRESULT. |
| [IKeywordDetectorOemAdapter::VerifyUserKeyword method](nf-keyworddetectoroemadapter-ikeyworddetectoroemadapter-verifyuserkeyword.md) | The VerifyUserKeyword method is used by the training user experience to verify that one instance of a spoken utterance, captured during training, matches a predefined keyword within some tolerance. |
