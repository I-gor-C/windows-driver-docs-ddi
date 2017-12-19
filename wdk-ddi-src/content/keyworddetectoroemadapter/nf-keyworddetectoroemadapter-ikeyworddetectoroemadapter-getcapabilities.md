---
UID: NF.keyworddetectoroemadapter.IKeywordDetectorOemAdapter.GetCapabilities
title: IKeywordDetectorOemAdapter::GetCapabilities method
author: windows-driver-content
description: The GetCapabilities method returns the keywords and languages supported by the object.
old-location: audio\ikeyworddetectoroemadapter_getcapabilities.htm
old-project: audio
ms.assetid: 5885E2BB-78DA-46F5-8330-DE8785C61946
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IKeywordDetectorOemAdapter, IKeywordDetectorOemAdapter::GetCapabilities, GetCapabilities
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: keyworddetectoroemadapter.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKeywordDetectorOemAdapter.GetCapabilities
req.alt-loc: KeywordDetectorOemAdapter.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: KeywordDetectorOemAdapter.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# IKeywordDetectorOemAdapter::GetCapabilities method



## -description
The <b>GetCapabilities</b> method returns the keywords and languages supported by the object.



## -syntax

````
HRESULT GetCapabilities(
  [in]  Bool         *SupportsUserModels,
  [out] KEYWORDID    **KeywordIds,
  [out] ULONG        *NumKeywords,
  [out] LANGID       **LangIds,
  [out] ULONG        *NumLanguages,
  [out] IMFMediaType **ppMediaType = 0
);
````


## -parameters

### -param SupportsUserModels [in]

A Boolean value that indicates whether user specific training is supported. 


### -param KeywordIds [out]

A pointer to an array of keyword IDs supported by the object. The object allocates the array by calling <a href="com.cotaskmemalloc">CoTaskMemAlloc</a>. The caller frees the memory by calling <a href="com.cotaskmemfree">CoTaskMemFree</a>.


### -param NumKeywords [out]

The number of keyword IDs in the <i>KeywordIds</i> array.


### -param LangIds [out]

A pointer to an array of language IDs supported by the object. The object allocates the array by calling <a href="com.cotaskmemalloc">CoTaskMemAlloc</a>. The caller frees the memory by calling <a href="com.cotaskmemfree">CoTaskMemFree</a>.


### -param NumLanguages [out]

The number of language IDs in the <i>LangIds</i> array.


### -param ppMediaType [out]

The audio format required by <a href="audio.ikeyworddetectoroemadapter_verifyuserkeyword">IKeywordDetectorOemAdapter::VerifyUserKeyword</a> and <a href="audio.ikeyworddetectoroemadapter_computeandaddusermodeldata">IKeywordDetectorOemAdapter::ComputeAndAddUserModelData</a>. 

The only valid values for the IMFMediaType are the following:

<ul>
<li>Type = Audio</li>
<li>Subtype = IEEE_FLOAT</li>
<li>Sampling Rate = 16 kHz</li>
<li>Bits = 32</li>
</ul>
Typically, the OEMDLL calls <a href="mf.mfcreatemediatype">MFCreateMediaType</a> and <a href="mf.mfinitmediatypefromwaveformatex">MFInitMediaTypeFromWaveFormatEx</a> to obtain an <a href="mf.imfmediatype">IMFMediaType</a> pointer to return to the caller.


## -returns
This method can return one of these values.
<dl>
<dt>S_OK</dt>
</dl>The function exited successfully.
<dl>
<dt>E_POINTER</dt>
</dl>The pointer for an output parameter is <b>NULL</b>.
<dl>
<dt>E_INVALIDARG</dt>
</dl>The pointer to the model data is <b>NULL</b>.

 


## -remarks
The information returned from this routine would normally not change for a given version of the OEMDLL or the user independent model data installed along with it.


The OEMDLL must have internal user independent models for the keywords and languages returned from this method.



## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>KeywordDetectorOemAdapter.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IDL

</th>
<td width="70%">
<dl>
<dt>KeywordDetectorOemAdapter.idl</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\keyworddetectoroemadapter\nn-keyworddetectoroemadapter-ikeyworddetectoroemadapter.md">IKeywordDetectorOemAdapter</a>
</dt>
<dt>
<a href="com.cotaskmemalloc">CoTaskMemAlloc</a>
</dt>
<dt>
<a href="com.cotaskmemfree">CoTaskMemFree</a>
</dt>
<dt>
<a href="audio.ikeyworddetectoroemadapter_verifyuserkeyword">IKeywordDetectorOemAdapter::VerifyUserKeyword</a>
</dt>
<dt>
<a href="audio.ikeyworddetectoroemadapter_computeandaddusermodeldata">IKeywordDetectorOemAdapter::ComputeAndAddUserModelData</a>
</dt>
<dt>
<a href="mf.mfcreatemediatype">MFCreateMediaType</a>
</dt>
<dt>
<a href="mf.mfinitmediatypefromwaveformatex">MFInitMediaTypeFromWaveFormatEx</a>
</dt>
<dt>
<a href="mf.imfmediatype">IMFMediaType</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IKeywordDetectorOemAdapter::GetCapabilities method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

