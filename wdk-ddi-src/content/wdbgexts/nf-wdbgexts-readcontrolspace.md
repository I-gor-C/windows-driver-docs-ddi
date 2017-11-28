---
UID: NF.wdbgexts.ReadControlSpace
title: ReadControlSpace
author: windows-driver-content
description: The ReadControlSpace function reads the processor-specific control space into the array pointed to by buf.
old-location: debugger\readcontrolspace.htm
old-project: debugger
ms.assetid: 4b6955a5-ca03-418d-9eba-fdbe48599922
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ReadControlSpace
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ReadControlSpace
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
req.iface: 
req.product: Windows 10 or later.
---

# ReadControlSpace function



## -description
<p>The <b>ReadControlSpace</b> function reads the processor-specific control space into the array pointed to by <i>buf</i>.</p>


## -syntax

````
__inline VOID ReadControlSpace(
   USHORT processor,
   ULONG  address,
   PVOID  buf,
   ULONG  size
);
````


## -parameters
<dl>

### -param <i>processor</i> 

<dd>
<p>Specifies the number of the processor whose control space is to be read.</p>
</dd>

### -param <i>address</i> 

<dd>
<p>Specifies the address of the control space.</p>
</dd>

### -param <i>buf</i> 

<dd>
<p>Specifies the address of an array of bytes to hold the control space data.</p>
</dd>

### -param <i>size</i> 

<dd>
<p>Specifies the number of bytes in the array pointed to by <i>buf</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If you are writing 64-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553532">ReadControlSpace64</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

<p>If you are writing a WdbgExts extension, include <b>wdbgexts.h</b>. If you are writing a DbgEng extension that calls this function, include <b>wdbgexts.h</b> before <b>dbgeng.h</b> (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details).
</p>

<p>If you are writing 64-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553532">ReadControlSpace64</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

<p>If you are writing a WdbgExts extension, include <b>wdbgexts.h</b>. If you are writing a DbgEng extension that calls this function, include <b>wdbgexts.h</b> before <b>dbgeng.h</b> (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details).
</p>

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