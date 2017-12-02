---
UID: NF.wdbgexts.WritePhysicalWithFlags
title: WritePhysicalWithFlags
author: windows-driver-content
description: The WritePhysicalWithFlags function writes to physical memory.
old-location: debugger\writephysicalwithflags.htm
old-project: debugger
ms.assetid: ae679f76-2e26-43f2-a097-1e158fbc0cc7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WritePhysicalWithFlags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WritePhysicalWithFlags
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

# WritePhysicalWithFlags function



## -description
<p>The <b>WritePhysicalWithFlags</b> function writes to physical memory.</p>


## -syntax

````
VOID WritePhysicalWithFlags(
   ULONG64 address,
   PVOID   buf,
   ULONG   size,
   ULONG   flags,
   PULONG  sizew
);
````


## -parameters
<dl>

### -param address 

<dd>
<p>Specifies the physical address to write.</p>
</dd>

### -param buf 

<dd>
<p>Specifies the address of an array of bytes to hold the data that is  written.</p>
</dd>

### -param size 

<dd>
<p>Specifies the number of bytes to write. </p>
</dd>

### -param flags 

<dd>
<p>Specifies the properties of the physical memory to be written to.  This must match the way the physical memory was advertised to the operating system on the target.  Possible values are listed in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>PHYS_FLAG_DEFAULT</p>
</td>
<td>
<p>Use the default memory caching.</p>
</td>
</tr>
<tr>
<td>
<p>PHYS_FLAG_CACHED</p>
</td>
<td>
<p>The physical memory is cached.</p>
</td>
</tr>
<tr>
<td>
<p>PHYS_FLAG_UNCACHED</p>
</td>
<td>
<p>The physical memory is uncached.</p>
</td>
</tr>
<tr>
<td>
<p>PHYS_FLAG_WRITE_COMBINED</p>
</td>
<td>
<p>The physical memory is write-combined.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param sizew 

<dd>
<p>Receives the number of bytes actually written.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
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
<dt>Wdbgexts.h (include Wdbgexts.h or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdbgexts\nf-wdbgexts-writephysical.md">WritePhysical</a>
</dt>
<dt>
<a href="..\wdbgexts\nf-wdbgexts-readphysicalwithflags.md">ReadPhysicalWithFlags</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20WritePhysicalWithFlags function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
