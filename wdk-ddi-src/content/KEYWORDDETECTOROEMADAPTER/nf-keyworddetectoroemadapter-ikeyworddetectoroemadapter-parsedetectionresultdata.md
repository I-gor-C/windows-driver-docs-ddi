---
UID: NF.keyworddetectoroemadapter.IKeywordDetectorOemAdapter.ParseDetectionResultData
title: IKeywordDetectorOemAdapter::ParseDetectionResultData
author: windows-driver-content
description: The ParseDetectionResultData method is called by the operating system after handling a keyword detection event and after retrieving the result data from KSPROPERTY_SOUNDDETECTOR_MATCHRESULT.
old-location: audio\ikeyworddetectoroemadapter_parsedetectionresultdata.htm
ms.assetid: 97C92A85-BE00-4B95-80D1-20FE7A31BCA9
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
req.alt-api: IKeywordDetectorOemAdapter.ParseDetectionResultData
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
ms.keywords: IKeywordDetectorOemAdapter, ParseDetectionResultData, IKeywordDetectorOemAdapter::ParseDetectionResultData
req.iface: IKeywordDetectorOemAdapter
---

# IKeywordDetectorOemAdapter::ParseDetectionResultData method



## -description
<p>The <b>ParseDetectionResultData</b> method is called by the operating system after handling a keyword detection event and after retrieving the result data from <a href="https://msdn.microsoft.com/library/windows/hardware/dn932150">KSPROPERTY_SOUNDDETECTOR_MATCHRESULT</a>. The operating system passes the OEM-specific match result data to this method in order to get the results of a keyword detection.  The OEMDLL processes the results and returns information about the matched keyword, the language associated with the matched keyword, and the matched user (if any).</p>


## -syntax

````
HRESULT ParseDetectionResultData(
  [in]  IStream                     *ModelData,
  [in]  SOUNDDETECTOR_PATTERNHEADER *Result,
  [out] KEYWORDID                   *KeywordId,
  [out] LANGID                      *LangId,
  [out] BOOL                        *pIsUserMatch,
  [out] LONGLONG                    *KeywordStartPerformanceCounter,
  [out] LONGLONG                    *KeywordEndPerformanceCounter = 0
);
````


## -parameters
<dl>

### -param <i>ModelData</i> [in]

<dd>
<p>A pointer to <b>IStream</b> bound to model data for the arming pattern.

</p>
</dd>

### -param <i>Result</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/dn957513">SOUNDDETECTOR_PATTERNHEADER</a> from the DDI.
</p>
</dd>

### -param <i>KeywordId</i> [out]

<dd>
<p>Identifies a keyword function. The driver may return 0 to indicate no match.</p>
</dd>

### -param <i>LangId</i> [out]

<dd>
<p>Identifies a language.</p>
</dd>

### -param <i>pIsUserMatch</i> [out]

<dd>
<p>Indicates if the user matched.</p>
</dd>

### -param <i>KeywordStartPerformanceCounter</i> [out]

<dd>
<p>Optionally returns the start time of the keyword in terms of the Windows performance counter. The OEMDLL should return 0 if this is not available.</p>
</dd>

### -param <i>KeywordEndPerformanceCounter</i> [out]

<dd>
<p>Optionally returns the end time of the keyword in terms of the Windows performance counter. The OEMDLL should return 0 if this is not available.</p>
</dd>
</dl>

## -returns
<p>This method can return one of these values.</p><dl>
<dt>S_OK</dt>
</dl><p>The function exited successfully. </p><dl>
<dt>E_POINTER</dt>
</dl><p> The <i>ModelData</i> pointer is <b>NULL</b>.</p><dl>
<dt>E_INVALIDARG</dt>
</dl><p> The <i>KeywordId</i> or <i>LangId</i> parameters are invalid.</p><dl>
<dt>HRESULT_FROM_WIN32(ERROR_GEN_FAILURE)</dt>
</dl><p> The processing was unable to complete.</p><dl>
<dt>E_HW_RESET</dt>
</dl><p>The hardware reset due to an internal fault.</p>

<p> </p>

## -remarks
<p>If the driver includes any portion of the spoken keyword in the burst keyword/command stream from its keyword detector pin, then the driver must return a valid value for <i>KeywordEndTime</i>. Otherwise the driver may optionally return 0.
</p>

<p>If the driver returns <i>KeywordStartTime</i> or <i>KeywordEndTime</i>, the returned values must be consistent with the time stamps returned from the driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/dn946533">IMiniportWaveRTInputStream::GetReadPacket</a> routine.
</p>

<p>The driver may return valid values for <i>KeywordStartTime</i> and <i>KeywordEndTime</i> regardless of whether the driver includes any portion of the spoken keyword in the burst keyword/command stream.
</p>

<p>If the caller receives <b>E_HW_RESET</b>, no keyword was detected by the hardware and the state was lost. A re-arm will be required to get back to a monitoring state.</p>

<p>If the driver includes any portion of the spoken keyword in the burst keyword/command stream from its keyword detector pin, then the driver must return a valid value for <i>KeywordEndTime</i>. Otherwise the driver may optionally return 0.
</p>

<p>If the driver returns <i>KeywordStartTime</i> or <i>KeywordEndTime</i>, the returned values must be consistent with the time stamps returned from the driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/dn946533">IMiniportWaveRTInputStream::GetReadPacket</a> routine.
</p>

<p>The driver may return valid values for <i>KeywordStartTime</i> and <i>KeywordEndTime</i> regardless of whether the driver includes any portion of the spoken keyword in the burst keyword/command stream.
</p>

<p>If the caller receives <b>E_HW_RESET</b>, no keyword was detected by the hardware and the state was lost. A re-arm will be required to get back to a monitoring state.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn932150">KSPROPERTY_SOUNDDETECTOR_MATCHRESULT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957513">SOUNDDETECTOR_PATTERNHEADER</a>
</dt>
<dt>
<a href="com.cotaskmemalloc">CoTaskMemAlloc</a>
</dt>
<dt>
<a href="com.cotaskmemfree">CoTaskMemFree</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn946533">IMiniportWaveRTInputStream::GetReadPacket</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IKeywordDetectorOemAdapter::ParseDetectionResultData method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
