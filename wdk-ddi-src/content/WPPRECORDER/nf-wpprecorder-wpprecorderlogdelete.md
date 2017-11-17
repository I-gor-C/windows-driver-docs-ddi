---
UID: NF.wpprecorder.WppRecorderLogDelete
title: WppRecorderLogDelete
author: windows-driver-content
description: The WppRecorderLogDelete method deletes the specified recorder log.
old-location: devtest\wpprecorderlogdelete.htm
ms.assetid: AEE10756-7301-4B55-82A5-27CA595854EA
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
req.alt-api: WppRecorderLogDelete
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
ms.keywords: WppRecorderLogDelete
req.iface: 
req.product: Windows 10 or later.
---

# WppRecorderLogDelete function



## -description
<p>The <b>WppRecorderLogDelete</b> method deletes the specified recorder log.</p>


## -syntax

````
void WppRecorderLogDelete(
  [in] RECORDER_LOG RecorderLog
);
````


## -parameters
<dl>

### -param <i>RecorderLog</i> [in]

<dd>
<p>Handle to the recorder log to delete.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>When a thread enters this function, no threads can subsequently  log to this buffer.</p>

<p>When a thread enters this function, no threads can subsequently  log to this buffer.</p>

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