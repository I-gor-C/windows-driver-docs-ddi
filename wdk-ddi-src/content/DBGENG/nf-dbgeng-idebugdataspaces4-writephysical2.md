---
UID: NF.dbgeng.IDebugDataSpaces4.WritePhysical2
title: IDebugDataSpaces4::WritePhysical2
author: windows-driver-content
description: The WritePhysical2 method writes data to the specified physical address in the target's memory.
old-location: debugger\writephysical2.htm
ms.assetid: 15a83343-b95b-4f79-b4f2-ed2ad60d170e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces4.WritePhysical2
req.alt-loc: dbgeng.h
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
ms.keywords: IDebugDataSpaces4, WritePhysical2, IDebugDataSpaces4::WritePhysical2
req.iface: IDebugDataSpaces4
---

# IDebugDataSpaces4::WritePhysical2 method



## -description
<p>The <b>WritePhysical2</b> method writes data to the specified physical address in the target's memory.</p>


## -syntax

````
HRESULT WritePhysical2(
  [in]            ULONG64 Offset,
  [in]            ULONG   Flags,
  [in]            PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesWritten
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the physical address of the memory to write the data to.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies the properties of the physical memory to be written to.  This must match the way the physical memory was advertised to the operating system on the target.  Possible values are listed in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_PHYSICAL_DEFAULT</p>
</td>
<td>
<p>Use the default memory caching.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_PHYSICAL_CACHED</p>
</td>
<td>
<p>The physical memory is cached.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_PHYSICAL_UNCACHED</p>
</td>
<td>
<p>The physical memory is uncached.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_PHYSICAL_WRITE_COMBINED</p>
</td>
<td>
<p>The physical memory is write-combined.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Specifies the data to write.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of the <i>Buffer</i> buffer.  This is the maximum number of bytes that will be written.</p>
</dd>

### -param <i>BytesWritten</i> [out, optional]

<dd>
<p>Receives the number of bytes written to the target's memory.  If <i>BytesWritten</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>This method is only available in kernel-mode debugging.</p>

<p>The flags DEBUG_PHYSICAL_CACHED, DEBUG_PHYSICAL_UNCACHED, and DEBUG_PHYSICAL_WRITE_COMBINED can only be used when the target is a live kernel target that is being debugged in the standard way (using a COM port, 1394 bus, or named pipe).</p>

<p>This method is only available in kernel-mode debugging.</p>

<p>The flags DEBUG_PHYSICAL_CACHED, DEBUG_PHYSICAL_UNCACHED, and DEBUG_PHYSICAL_WRITE_COMBINED can only be used when the target is a live kernel target that is being debugged in the standard way (using a COM port, 1394 bus, or named pipe).</p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550546">IDebugDataSpaces4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561432">WritePhysical</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561441">WritePhysical2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces4::WritePhysical2 method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
