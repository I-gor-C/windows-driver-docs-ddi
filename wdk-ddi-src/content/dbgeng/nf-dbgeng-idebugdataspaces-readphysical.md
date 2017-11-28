---
UID: NF.dbgeng.IDebugDataSpaces.ReadPhysical
title: IDebugDataSpaces::ReadPhysical
author: windows-driver-content
description: The ReadPhysical method reads the target's memory from the specified physical address.
old-location: debugger\readphysical3.htm
old-project: debugger
ms.assetid: 8df51985-9208-46ce-8802-6bc5ec707ab2
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugDataSpaces, ReadPhysical, IDebugDataSpaces::ReadPhysical
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
req.alt-api: IDebugDataSpaces.ReadPhysical,IDebugDataSpaces2.ReadPhysical,IDebugDataSpaces3.ReadPhysical,IDebugDataSpaces4.ReadPhysical
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
req.iface: IDebugDataSpaces
---

# IDebugDataSpaces::ReadPhysical method



## -description
<p>The <b>ReadPhysical</b> method reads the target's memory from the specified physical address.</p>


## -syntax

````
HRESULT ReadPhysical(
  [in]            ULONG64 Offset,
  [out]           PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesRead
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the physical address of the memory to read.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Receives the memory that is read.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be read.</p>
</dd>

### -param <i>BytesRead</i> [out, optional]

<dd>
<p>Receives the number of bytes read from the target's memory.  If <i>BytesRead</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>This method is only available in kernel-mode debugging.</p>

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