---
UID: NF.keyworddetectoroemadapter.IKeywordDetectorOemAdapter.ComputeAndAddUserModelData
title: IKeywordDetectorOemAdapter::ComputeAndAddUserModelData
author: windows-driver-content
description: The ComputeAndAddUserModelData method is used by the training user experience to compute the user-specific information relative to the user-independent keyword.
old-location: audio\ikeyworddetectoroemadapter_computeandaddusermodeldata.htm
ms.assetid: 4E810EAD-3864-44C1-9845-60DAB288BB48
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: keyworddetectoroemadapter.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKeywordDetectorOemAdapter.ComputeAndAddUserModelData
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
ms.keywords: IKeywordDetectorOemAdapter, ComputeAndAddUserModelData, IKeywordDetectorOemAdapter::ComputeAndAddUserModelData
req.iface: IKeywordDetectorOemAdapter
---

# IKeywordDetectorOemAdapter::ComputeAndAddUserModelData method



## -description
<p>The <b>ComputeAndAddUserModelData</b> method is used by the training user experience to compute the user-specific information relative to the user-independent keyword. The DLL updates the <i>ModelData</i> parameter with the results. </p>


## -syntax

````
HRESULT ComputeAndAddUserModelData(
  [in] IStream         *ModelData,
  [in] KEYWORDSELECTOR KeywordSelector,
  [in] LONG            KeywordEndBytePos,
  [in] IMFMediaBuffer  **UserRecordings,
  [in] ULONG           NumUserRecordings = 0
);
````


## -parameters
<dl>

### -param <i>ModelData</i> [in]

<dd>
<p>A pointer to the <b>IStream</b> object bound to model data. It is modified by this call.</p>
</dd>

### -param <i>KeywordSelector</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn957511">KEYWORDSELECTOR</a> struct that uniquely identifies this model.</p>
</dd>

### -param <i>KeywordEndBytePos</i> [in]

<dd>
<p>Indicates the end of the keyword in the UserRecording.</p>
</dd>

### -param <i>UserRecordings</i> [in]

<dd>
<p>A pointer to an array of pointers to the previously verified user recordings of the keyword.</p>
</dd>

### -param <i>NumUserRecordings</i> [in]

<dd>
<p>The number of recordings.</p>
</dd>
</dl>

## -returns
<p>This method can return one of these values.</p><dl>
<dt>S_OK</dt>
</dl><p>The function exited successfully.</p><dl>
<dt>E_NOTIMPL</dt>
</dl><p>User keyword training is not supported by the device.</p><dl>
<dt>E_INVALIDARG</dt>
</dl><p>Either the <i>KeywordId</i> or <i>LangId</i> parameters are invalid.</p><dl>
<dt>HRESULT_FROM_WIN32(ERROR_GEN_FAILURE)</dt>
</dl><p>The processing was unable to complete.</p>

<p> </p>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957511">KEYWORDSELECTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IKeywordDetectorOemAdapter::ComputeAndAddUserModelData method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
