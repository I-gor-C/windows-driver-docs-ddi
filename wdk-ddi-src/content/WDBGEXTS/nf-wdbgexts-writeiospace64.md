---
UID: NF.wdbgexts.WriteIoSpace64
title: WriteIoSpace64
author: windows-driver-content
description: The WriteIoSpace64 function writes to the system I/O locations.
old-location: debugger\writeiospace64.htm
ms.assetid: c750d3de-8481-42d5-a290-00e49d5fe82b
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WriteIoSpace64
req.alt-loc: wdbgexts.h
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
ms.keywords: WriteIoSpace64
req.iface: 
req.product: Windows 10 or later.
---

# WriteIoSpace64 function



## -description
<p>The <b>WriteIoSpace64</b> function writes to the system I/O locations. </p>


## -syntax

````
VOID  WriteIoSpace64(
   ULONG64 address,
   ULONG   data,
   PULONG  size
);
````


## -parameters
<dl>

### -param <i>address</i> 

<dd>
<p>Specifies the I/O address to write to.</p>
</dd>

### -param <i>data</i> 

<dd>
<p>Specifies the address of a variable that holds the data to write. This must be at least the number of bytes contained in <i>size</i>.</p>
</dd>

### -param <i>size</i> 

<dd>
<p>Specifies the address of a variable that contains the number of bytes to write. <i>Size</i> must be 1, 2, or 4. After the data is written, <i>size</i> will contain the number of bytes actually written.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If you are writing 32-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff561406">WriteIoSpace</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

<p>For a WdbgExts extension, include wdbgexts.h. For a DbgEng extension, include wdbgexts.h before dbgeng.h. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details.</p>

<p>If you are writing 32-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff561406">WriteIoSpace</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

<p>For a WdbgExts extension, include wdbgexts.h. For a DbgEng extension, include wdbgexts.h before dbgeng.h. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details.</p>

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
<dt>Wdbgexts.h (include Wdbgexts.h, Wdbgexts.h, or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>