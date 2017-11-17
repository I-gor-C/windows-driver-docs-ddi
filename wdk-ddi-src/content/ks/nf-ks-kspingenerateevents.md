---
UID: NF.ks.KsPinGenerateEvents
title: KsPinGenerateEvents
author: windows-driver-content
description: The KsPinGenerateEvents function generates events of an indicated type that are present in Pin's event list.
old-location: stream\kspingenerateevents.htm
ms.assetid: c2137849-aff0-4bf7-abab-b92e17aaef70
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPinGenerateEvents
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: <=DISPATCH_LEVEL (See Remarks)
ms.keywords: KsPinGenerateEvents
req.iface: 
---

# KsPinGenerateEvents function



## -description
<p>The<b> KsPinGenerateEvents</b> function generates events of an indicated type that are present in <i>Pin</i>'s event list.</p>


## -syntax

````
void _inline KsPinGenerateEvents(
  _In_           PKSPIN                     Pin,
  _In_opt_ const GUID                       *EventSet,
  _In_           ULONG                      EventId,
  _In_           ULONG                      DataSize,
  _In_opt_       PVOID                      Data,
  _In_opt_       PFNKSGENERATEEVENTCALLBACK CallBack,
  _In_opt_       PVOID                      CallBackContext
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure on which to generate events. </p>
</dd>

### -param <i>EventSet</i> [in, optional]

<dd>
<p>A pointer to the event set GUID to match to determine which events to generate. If this parameter is <b>NULL</b>, set GUID is not taken into account for determining matching events.</p>
</dd>

### -param <i>EventId</i> [in]

<dd>
<p>The event ID to match to determine which events to generate.</p>
</dd>

### -param <i>DataSize</i> [in]

<dd>
<p>The size in bytes of the data with which to generate the data event.</p>
</dd>

### -param <i>Data</i> [in, optional]

<dd>
<p>A pointer to a data buffer. Specify if generating a data event.</p>
</dd>

### -param <i>CallBack</i> [in, optional]

<dd>
<p>A pointer to a caller-specified function that is called to determine whether a given event should be generated. If <b>NULL</b>, no callback verification is performed to determine whether an event should be generated (only <i>EventSet </i>and <i>EventId</i> are used). Prototype as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>  BOOLEAN CallBack
(IN PVOID Context,
    IN PKSEVENT_ENTRY EventEntry); </pre>
</td>
</tr>
</table></span></div>
<p><b>KsPinGenerateEvents</b> passes the <i>CallBackContext</i> parameter unchanged as the <i>Context</i> parameter for the callback. The callback function returns <b>TRUE</b> if <i>EventEntry</i> should be generated. Otherwise, it returns <b>FALSE</b>. </p>
</dd>

### -param <i>CallBackContext</i> [in, optional]

<dd>
<p>A pointer to a caller-specified context that is passed to the callback function <i>CallBack</i>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When calling this function, a minidriver must place <i>Data</i> and <i>CallBackContext</i> in a locked, nonpageable data segment. The <i>CallBack</i> is made at DISPATCH_LEVEL. The callback function must be in a locked segment and must be prepared to run at IRQL = DISPATCH_LEVEL. Note that there is an additional issue in DX8 <i>only</i>: <i>EventSet</i> must be in a locked data segment.</p>

<p>This is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562597">KsGenerateEvents</a>, which performs the necessary typecasting. Minidrivers should usually call this version instead of directly calling <b>KsGenerateEvents</b>.</p>

<p>An event is generated if the following three conditions hold:</p>

<p>The event is present in <i>Pin's </i>event list and <i>EventId </i>matches the event's ID.</p>

<p><i>EventSet</i> either matches the event's set GUID or is <b>NULL</b>.</p>

<p><i>CallBack </i>is either <b>NULL</b> or authorizes the match.</p>

<p>For more information, see <a href="NULL">Event Handling in AVStream</a> and <a href="NULL">KS Events</a>. </p>

<p>When calling this function, a minidriver must place <i>Data</i> and <i>CallBackContext</i> in a locked, nonpageable data segment. The <i>CallBack</i> is made at DISPATCH_LEVEL. The callback function must be in a locked segment and must be prepared to run at IRQL = DISPATCH_LEVEL. Note that there is an additional issue in DX8 <i>only</i>: <i>EventSet</i> must be in a locked data segment.</p>

<p>This is an inline function call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562597">KsGenerateEvents</a>, which performs the necessary typecasting. Minidrivers should usually call this version instead of directly calling <b>KsGenerateEvents</b>.</p>

<p>An event is generated if the following three conditions hold:</p>

<p>The event is present in <i>Pin's </i>event list and <i>EventId </i>matches the event's ID.</p>

<p><i>EventSet</i> either matches the event's set GUID or is <b>NULL</b>.</p>

<p><i>CallBack </i>is either <b>NULL</b> or authorizes the match.</p>

<p>For more information, see <a href="NULL">Event Handling in AVStream</a> and <a href="NULL">KS Events</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL (See Remarks)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560931">KsAddEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562597">KsGenerateEvents</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562541">KsFilterGenerateEvents</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561853">KSEVENT_ENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGenerateEvents function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
