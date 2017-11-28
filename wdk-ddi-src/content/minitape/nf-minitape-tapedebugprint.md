---
UID: NF.minitape.TapeDebugPrint
title: TapeDebugPrint
author: windows-driver-content
description: The TapeDebugPrint routine prints the indicated string.
old-location: storage\tapedebugprint.htm
old-project: storage
ms.assetid: d06e4308-f1a9-4acd-bc25-b3fd53129064
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: TapeDebugPrint
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: minitape.h
req.include-header: Minitape.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TapeDebugPrint
req.alt-loc: Tape.lib,Tape.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Tape.lib
req.dll: 
req.irql: 
req.iface: 
---

# TapeDebugPrint function



## -description
<p>The <b>TapeDebugPrint</b> routine prints the indicated string.</p>


## -syntax

````
VOID TapeDebugPrint(
   ULONG  DebugPrintLevel,
   PCCHAR DebugMessage
);
````


## -parameters
<dl>

### -param <i>DebugPrintLevel</i> 

<dd>
<p>Determines whether the string is printed or not. If this parameter has a value less than or equal to the tape class global variable <b>TapeClassDebug</b>, <b>TapeDebugPrint</b> prints the message, otherwise nothing is printed. If this parameter has a value of zero, <b>TapeClassDebug</b> always prints the message. </p>
</dd>

### -param <i>DebugMessage</i> 

<dd>
<p>Pointer to the string to be printed.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Minitape.h (include Minitape.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Tape.lib</dt>
</dl>
</td>
</tr>
</table>