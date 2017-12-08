---
UID: NF.dbgeng.IDebugDataSpaces2.WriteIo
title: IDebugDataSpaces2::WriteIo
author: windows-driver-content
description: The WriteIo method writes to the system and bus I/O memory.
old-location: debugger\writeio.htm
old-project: debugger
ms.assetid: 3bc84b15-7c13-4ad9-b9a1-6abd5a7389eb
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugDataSpaces2, WriteIo, IDebugDataSpaces2::WriteIo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces.WriteIo,IDebugDataSpaces2.WriteIo,IDebugDataSpaces3.WriteIo,IDebugDataSpaces4.WriteIo
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
req.iface: IDebugDataSpaces2
---

# IDebugDataSpaces2::WriteIo method



## -description
<p>The <b>WriteIo</b> method writes to the system and bus I/O memory.</p>


## -syntax

````
HRESULT WriteIo(
  [in]            ULONG   InterfaceType,
  [in]            ULONG   BusNumber,
  [in]            ULONG   AddressSpace,
  [in]            ULONG64 Offset,
  [in]            PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesWritten
);
````


## -parameters
<dl>

### -param InterfaceType [in]

<dd>
<p>Specifies the interface type of the I/O bus.  This parameter may take values in the INTERFACE_TYPE enumeration defined in wdm.h.</p>
</dd>

### -param BusNumber [in]

<dd>
<p>Specifies the system-assigned number of the bus.  This is usually zero, unless the system has more than one bus of the same interface type.</p>
</dd>

### -param AddressSpace [in]

<dd>
<p>Set to one.</p>
</dd>

### -param Offset [in]

<dd>
<p>Specifies the location of the requested data.</p>
</dd>

### -param Buffer [in]

<dd>
<p>Specifies the data to write to the I/O bus.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be written.</p>
</dd>

### -param BytesWritten [out, optional]

<dd>
<p>Receives the number of bytes written to I/O bus.  If <i>BytesWritten</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>This method is only available in kernel-mode debugging.</p>

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