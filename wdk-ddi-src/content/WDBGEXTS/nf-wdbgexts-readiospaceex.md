---
UID: NF.wdbgexts.ReadIoSpaceEx
title: ReadIoSpaceEx
author: windows-driver-content
description: The ReadIoSpaceEx function is an extended version of ReadIoSpace.
old-location: debugger\readiospaceex.htm
ms.assetid: de0681e6-c716-4879-8e07-daacc092d18f
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
req.alt-api: ReadIoSpaceEx
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
ms.keywords: ReadIoSpaceEx
req.iface: 
req.product: Windows 10 or later.
---

# ReadIoSpaceEx function



## -description
<p>The <b>ReadIoSpaceEx</b> function is an extended version of <a href="https://msdn.microsoft.com/library/windows/hardware/ff553574">ReadIoSpace</a>. It reads not only the system I/O locations, but also I/O locations on a bus. <b>ReadIoSpace</b> works like <b>ReadIoSpaceEx</b>, except that it defaults <i>interfacetype</i> to ISA, <i>busnumber</i> to zero, and <i>addressspace</i> to 1.</p>


## -syntax

````
__inline VOID ReadIoSpaceEx(
   ULONG  address,
   PULONG data,
   PULONG size,
   ULONG  interfacetype,
   ULONG  busnumber,
   ULONG  addressspace
);
````


## -parameters
<dl>

### -param <i>address</i> 

<dd>
<p>Specifies the I/O address to read from.</p>
</dd>

### -param <i>data</i> 

<dd>
<p>Specifies the address of a variable to hold the data read. This must be at least the number of bytes contained in <i>size</i>.</p>
</dd>

### -param <i>size</i> 

<dd>
<p>Specifies the address of a variable that contains the number of bytes to read. <i>Size</i> must be 1, 2, or 4. After the data is read, <i>size</i> will contain the number of bytes actually read.</p>
</dd>

### -param <i>interfacetype</i> 

<dd>
<p>Specifies the type of interface on which the extended I/O space exists. Possible values include ISA, EISA, and MCA. For more information, see ntddk.h, which is available as part of Windows Driver Kit.</p>
</dd>

### -param <i>busnumber</i> 

<dd>
<p>Specifies the number of the bus on which the extended I/O space exists. This is typically zero, unless there is more than one bus of a given type.</p>
</dd>

### -param <i>addressspace</i> 

<dd>
<p>This is typically 1.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If you are writing 64-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553583">ReadIoSpaceEx64</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

<p>If you are writing a WdbgExts extension, include <b>wdbgexts.h</b>. If you are writing a DbgEng extension that calls this function, include <b>wdbgexts.h</b> before <b>dbgeng.h</b> (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details).
</p>

<p>If you are writing 64-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff553583">ReadIoSpaceEx64</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

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