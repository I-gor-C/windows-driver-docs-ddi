---
UID: NF.storport.StorPortDebugPrint
title: StorPortDebugPrint
author: windows-driver-content
description: The StorPortDebugPrint routine prints a debug string to the kernel debugger, if the debugger is attached.
old-location: storage\storportdebugprint.htm
ms.assetid: 46845a10-c44b-4d11-b82e-986bfc066b97
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortDebugPrint
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
ms.keywords: StorPortDebugPrint
req.iface: 
req.product: Windows 10 or later.
---

# StorPortDebugPrint function



## -description
<p>The <b>StorPortDebugPrint</b> routine prints a debug string to the kernel debugger, if the debugger is attached.</p>


## -syntax

````
VOID StorPortDebugPrint(
   IN ULONG  DebugPrintLevel,
   IN PCCHAR DebugMessage
);
````


## -parameters
<dl>

### -param <i>DebugPrintLevel</i> 

<dd>
<p>Indicates the amount of debug information that will be displayed. </p>
</dd>

### -param <i>DebugMessage</i> 

<dd>
<p>Pointer to the debug message to be printed. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>To see these debug strings, the driver writer must set nt!Kd_STORMINIPORT_Mask. This follows the new system-wide debug print mechanism.</p>

<p>To see these debug strings, the driver writer must set nt!Kd_STORMINIPORT_Mask. This follows the new system-wide debug print mechanism.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
</table>