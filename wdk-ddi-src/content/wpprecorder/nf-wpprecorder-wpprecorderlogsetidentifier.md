---
UID: NF.wpprecorder.WppRecorderLogSetIdentifier
title: WppRecorderLogSetIdentifier
author: windows-driver-content
description: The WppRecorderLogSetIdentifier method sets a string identifier for the recorder log.
old-location: devtest\wpprecorderlogsetidentifier.htm
old-project: devtest
ms.assetid: E2687B3C-2BCF-4764-99E0-4495296F14C4
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: WppRecorderLogSetIdentifier
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
req.iface: 
req.product: Windows 10 or later.
---

# WppRecorderLogSetIdentifier function



## -description
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn895241">WppRecorderLogSetIdentifier</a> method sets a string identifier for the recorder log.</p>


## -syntax

````
NTSTATUS WppRecorderLogSetIdentifier(
   NULL RecorderLog,
   NULL LogIdentifier
);
````


## -parameters
<dl>

### -param <i>RecorderLog</i> 

<dd>
<p>A recorder log handle returned in a previous call to WppRecorderLogCreate.</p>
</dd>

### -param <i>LogIdentifier</i> 

<dd>
<p>A string identifier to set.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if completed successfully.</p>

## -remarks
<p>Do not call <a href="https://msdn.microsoft.com/library/windows/hardware/dn895241">WppRecorderLogSetIdentifier</a> on the default log handle returned by <a href="https://msdn.microsoft.com/library/windows/hardware/dn895240">WppRecorderLogGetDefault</a>.</p>

<p>Do not call <a href="https://msdn.microsoft.com/library/windows/hardware/dn895241">WppRecorderLogSetIdentifier</a> on the default log handle returned by <a href="https://msdn.microsoft.com/library/windows/hardware/dn895240">WppRecorderLogGetDefault</a>.</p>

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