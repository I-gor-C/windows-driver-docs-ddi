---
UID: NF.mcd.ChangerClassDebugPrint
title: ChangerClassDebugPrint function
author: windows-driver-content
description: The ChangerClassDebugPrint function prints debugging information.
old-location: storage\changerclassdebugprint.htm
old-project: storage
ms.assetid: 452377f1-a926-4f43-8168-bea11622902e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ChangerClassDebugPrint
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mcd.h
req.include-header: Mcd.h, Ntddchgr.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ChangerClassDebugPrint
req.alt-loc: Mcd.lib,Mcd.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Mcd.lib
req.dll: 
req.irql: 
---

# ChangerClassDebugPrint function



## -description
The <b>ChangerClassDebugPrint</b> function prints debugging information. 


## -syntax

````
VOID ChangerClassDebugPrint(
   ULONG  DebugPrintLevel,
   PCCHAR DebugMessage
);
````


## -parameters

### -param DebugPrintLevel 

Indicates how verbose debug information should be. Caller must assign this parameter an integer value between zero and three, where three specifies the highest level of verbosity and zero the lowest. 

### -param DebugMessage 

Caller can specify a message to be included with the debugging information that is printed by assigning a printable ASCII character string to this parameter.

## -returns
None

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Mcd.lib</dt>
</dl>
</td>
</tr>
</table>