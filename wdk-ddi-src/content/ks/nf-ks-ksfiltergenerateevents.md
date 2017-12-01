---
UID: NF.ks.KsFilterGenerateEvents
title: KsFilterGenerateEvents
author: windows-driver-content
description: The KsFilterGenerateEvents function generates events of an indicated type that are present in Filter's event list.
old-location: stream\ksfiltergenerateevents.htm
old-project: stream
ms.assetid: 62340660-3419-4da6-8d58-c2f82b4231ba
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsFilterGenerateEvents
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsFilterGenerateEvents
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
req.irql: <=DISPATCH_LEVEL (See Remarks section.)
req.iface: 
---

# KsFilterGenerateEvents function



## -description
<p>The<b> KsFilterGenerateEvents</b> function generates events of an indicated type that are present in <i>Filter</i>'s event list.</p>


## -syntax

````
void _inline KsFilterGenerateEvents(
  _In_           PKSFILTER                  Filter,
  _In_opt_ const GUID                       *EventSet,
  _In_           ULONG                      EventId,
  _In_           ULONG                      DataSize,
  _In_           PVOID                      Data,
  _In_opt_       PFNKSGENERATEEVENTCALLBACK CallBack,
  _In_opt_       PVOID                      CallBackContext
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--ksfilter.md">KSFILTER</a> structure on which to generate events. </p>
</dd>

### -param <i>EventSet</i> [in, optional]

<dd>
<p>A pointer to the event set GUID to match for determination of which events to generate. If this parameter is <b>NULL</b>, the event set GUID is not taken into account for determining matching events.</p>
</dd>

### -param <i>EventId</i> [in]

<dd>
<p>The event ID to match for determining which events to generate.</p>
</dd>

### -param <i>DataSize</i> [in]

<dd>
<p>The size of <i>Data</i> in bytes.</p>
</dd>

### -param <i>Data</i> [in]

<dd>
<p>A pointer to a data buffer. Specify if generating a data event.</p>
</dd>

### -param <i>CallBack</i> [in, optional]

<dd>
<p>A pointer to a caller-specified function that is called to determine whether a given event should be generated. If this is <b>NULL</b>, no callback verification is performed to determine whether an event should be generated (only <i>EventSet </i>and <i>EventId</i> are used). For more information, see the Remarks section below.</p>
</dd>

### -param <i>CallBackContext</i> [in, optional]

<dd>
<p>An optional pointer to a caller-specified context that is passed to the callback function <i>CallBack</i>. For more information, see the Remarks section below.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When calling this function, a minidriver must place <i>Data</i> and <i>CallBackContext</i> in a locked, nonpageable data segment. In addition, note that the <i>CallBack</i> is made at DISPATCH_LEVEL. The callback function must be in a locked segment and must be prepared to run at IRQL = DISPATCH_LEVEL. Note that there is an additional issue in DX8 <i>only</i>: <i>EventSet</i> must be in a locked data segment.</p>

<p>This is an inline function call to <a href="..\ks\nf-ks-ksgenerateevents.md">KsGenerateEvents</a> that performs the necessary typecasting. Minidrivers should usually call this version instead of directly calling <b>KsGenerateEvents</b>.</p>

<p>An event is generated if the following conditions hold:</p>

<p>The event is present in <i>Filter</i>'s event list and <i>EventId</i> matches the event's ID</p>

<p><i>EventSet</i> either matches the event's set GUID or is <b>NULL</b></p>

<p><i>CallBack</i> is either <b>NULL</b> or authorizes the match</p>

<p><i>CallBack</i> is a caller-specified callback used for additional match determination. It is prototyped as follows:</p>

<p>AVStream passes the contents of the <b>KsFilterGenerateEvents</b> routine's parameter <i>CallBackContext</i> in this callback's <i>Context</i> parameter. <i>EventEntry</i> is a pointer to a <a href="..\ks\ns-ks--ksevent-entry.md">KSEVENT_ENTRY</a> structure that specifies the event that would be generated. The callback function should return <b>TRUE</b> if this event should be generated.</p>

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
<p>&lt;=DISPATCH_LEVEL (See Remarks section.)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\nf-ks-ksaddevent.md">KsAddEvent</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgenerateevents.md">KsGenerateEvents</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspingenerateevents.md">KsPinGenerateEvents</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksevent-entry.md">KSEVENT_ENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterGenerateEvents function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
