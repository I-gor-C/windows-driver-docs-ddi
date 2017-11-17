---
UID: NF.wpprecorder.WppRecorderLogSetIdentifier
title: WppRecorderLogSetIdentifier
author: windows-driver-content
description: The WppRecorderLogSetIdentifier method sets a string identifier for the recorder log.
old-location: devtest\wpprecorderlogsetidentifier.htm
ms.assetid: E2687B3C-2BCF-4764-99E0-4495296F14C4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: devtest
req.header: wpprecorder.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WppRecorderLogSetIdentifier
req.alt-loc: Wpprecorder.h
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
ms.keywords: WppRecorderLogSetIdentifier
req.iface: 
req.product: Windows 10 or later.
---

# WppRecorderLogSetIdentifier function



## -description
<p>The <b>WppRecorderLogSetIdentifier</b> method sets a string identifier for the recorder log.</p>


## -syntax

````
void WppRecorderLogSetIdentifier(
  [in] RECORDER_LOG RecorderLog,
  [in] PSTR         LogIdentifier
);
````


## -parameters
<dl>

### -param <i>RecorderLog</i> [in]

<dd>
<p>A recorder log handle returned in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/dn914615">WppRecorderLogCreate</a>.</p>
</dd>

### -param <i>LogIdentifier</i> [in]

<dd>
<p>A string identifier to set.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>Do not call <b>WppRecorderLogSetIdentifier</b> on the default log handle returned by <a href="https://msdn.microsoft.com/library/windows/hardware/dn895240">WppRecorderLogGetDefault</a>.</p>

<p>Do not call <b>WppRecorderLogSetIdentifier</b> on the default log handle returned by <a href="https://msdn.microsoft.com/library/windows/hardware/dn895240">WppRecorderLogGetDefault</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wpprecorder.h</dt>
</dl>
</td>
</tr>
</table>