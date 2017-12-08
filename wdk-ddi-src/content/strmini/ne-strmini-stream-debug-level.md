---
UID: NE.strmini.STREAM_DEBUG_LEVEL
title: STREAM_DEBUG_LEVEL
author: windows-driver-content
description: The STREAM_DEBUG_LEVEL enumeration lists incrementally increasing levels of debugger output.
old-location: stream\stream_debug_level.htm
old-project: stream
ms.assetid: 42d70c1f-5cce-4097-849d-a5aa05b669b5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STREAM_DEBUG_LEVEL
req.alt-loc: strmini.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# STREAM_DEBUG_LEVEL enumeration



## -description
<p>The STREAM_DEBUG_LEVEL enumeration lists incrementally increasing levels of debugger output.</p>


## -syntax

````
typedef enum  { 
  DebugLevelFatal    = 0,
  DebugLevelError    = 1,
  DebugLevelWarning  = 2,
  DebugLevelInfo     = 3,
  DebugLevelTrace    = 4,
  DebugLevelVerbose  = 5,
  DebugLevelMaximum  = 6
} STREAM_DEBUG_LEVEL;
````


## -enum-fields
<dl>

### -field DebugLevelFatal

<dd>
<p>Display only information about nonrecoverable system failure.</p>
</dd>

### -field DebugLevelError

<dd>
<p>Display information about serious but recoverable error.</p>
</dd>

### -field DebugLevelWarning

<dd>
<p>Display warnings</p>
</dd>

### -field DebugLevelInfo

<dd>
<p>Display status information. System must remain responsive.</p>
</dd>

### -field DebugLevelTrace

<dd>
<p>Display trace information. System need not remain responsive</p>
</dd>

### -field DebugLevelVerbose

<dd>
<p>Display verbose trace information. System need not remain responsive.</p>
</dd>

### -field DebugLevelMaximum

<dd>
<p>Display maximum information.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\strmini\nf-strmini-streamclassdebugprint.md">StreamClassDebugPrint</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20STREAM_DEBUG_LEVEL enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
