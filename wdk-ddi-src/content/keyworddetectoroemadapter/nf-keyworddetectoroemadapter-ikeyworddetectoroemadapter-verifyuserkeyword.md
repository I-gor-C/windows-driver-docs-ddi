---
UID: NF.keyworddetectoroemadapter.IKeywordDetectorOemAdapter.VerifyUserKeyword
title: IKeywordDetectorOemAdapter::VerifyUserKeyword
author: windows-driver-content
description: The VerifyUserKeyword method is used by the training user experience to verify that one instance of a spoken utterance, captured during training, matches a predefined keyword within some tolerance.
old-location: audio\ikeyworddetectoroemadapter_verifyuserkeyword.htm
old-project: audio
ms.assetid: AFF679B6-B389-4EA2-8834-9B1B47412B7D
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IKeywordDetectorOemAdapter, VerifyUserKeyword, IKeywordDetectorOemAdapter::VerifyUserKeyword
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: keyworddetectoroemadapter.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKeywordDetectorOemAdapter.VerifyUserKeyword
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
req.iface: IKeywordDetectorOemAdapter
---

# IKeywordDetectorOemAdapter::VerifyUserKeyword method



## -description
<p>The <b>VerifyUserKeyword</b> method is used by the training user experience  to verify that one instance of a spoken utterance, captured during training, matches a predefined keyword within some tolerance.</p>


## -syntax

````
HRESULT VerifyUserKeyword(
  [in] IStream        *ModelData,
  [in] KEYWORDID      KeywordId,
  [in] LANGID         LangId,
  [in] LONG           KeywordEndBytePos,
  [in] IMFMediaBuffer *UserRecording = 0
);
````


## -parameters
<dl>

### -param <i>ModelData</i> [in]

<dd>
<p>A pointer to an <b>IStream</b> object bound to model data for a given stored model. On the initial call this will be empty.</p>
</dd>

### -param <i>KeywordId</i> [in]

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn957510">KEYWORDID</a> in the  <i>UserRecording</i> parameter.</p>
</dd>

### -param <i>LangId</i> [in]

<dd>
<p>The <b>LANGID</b> of the spoken language in the <i>UserRecording</i> parameter. </p>
</dd>

### -param <i>KeywordEndBytePos</i> [in]

<dd>
<p>Indicates the end of the keyword in the UserRecording.</p>
</dd>

### -param <i>UserRecording</i> [in]

<dd>
<p>A pointer to the buffer containing the raw data in the appropriate <a href="mf.imfmediatype">IMFMediaType</a> format.</p>
<p>The user recording must have the following attributes:</p>
<ul>
<li>Type = Audio</li>
<li>Subtype = IEEE_FLOAT</li>
<li>Sampling Rate = 16 kHz</li>
<li>Bits = 32</li>
</ul>
</dd>
</dl>

## -returns
<p>This method can return one of these values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p> The function exited successfully.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>User keyword training is not supported for the device.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>One or more of the following conditions are true:</p><dl>
<dt><b>E_NO_MATCH</b></dt>
</dl><p>The user recording didn't contain the specified keyword.</p>

<p> </p>

## -remarks
<p>Note that audio is processed in a unique way for voice activation training. The following table summarizes the differences between voice activation training and the regular voice recognition usage. </p>

<p> </p>

<p></p>

<p>Note that audio is processed in a unique way for voice activation training. The following table summarizes the differences between voice activation training and the regular voice recognition usage. </p>

<p> </p>

<p></p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>KeywordDetectorOemAdapter.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IDL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957504">IKeywordDetectorOemAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957510">KEYWORDID</a>
</dt>
<dt>
<a href="mf.imfmediatype">IMFMediaType</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IKeywordDetectorOemAdapter::VerifyUserKeyword method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
