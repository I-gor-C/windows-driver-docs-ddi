---
UID: NF.dbgeng.IDebugDataSpaces2.WritePhysical
title: IDebugDataSpaces2::WritePhysical
author: windows-driver-content
description: The WritePhysical method writes data to the specified physical address in the target's memory.
old-location: debugger\writephysical3.htm
old-project: debugger
ms.assetid: ec691a7c-a569-49dd-af13-bfbf403be297
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugDataSpaces2, WritePhysical, IDebugDataSpaces2::WritePhysical
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
req.alt-api: IDebugDataSpaces.WritePhysical,IDebugDataSpaces2.WritePhysical,IDebugDataSpaces3.WritePhysical,IDebugDataSpaces4.WritePhysical
req.alt-loc: Dbgeng.h
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

# IDebugDataSpaces2::WritePhysical method



## -description
<p>The <b>WritePhysical</b> method writes data to the specified physical address in the target's memory.</p>


## -syntax

````
HRESULT WritePhysical(
  [in]            ULONG64 Offset,
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

### -param <i>Buffer</i> [in]

<dd>
<p>Specifies the data to write.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be written.</p>
</dd>

### -param <i>BytesWritten</i> [out, optional]

<dd>
<p>Receives the number of bytes written to the target's memory.  If <i>BytesWritten</i> is <b>NULL</b>, this information is not returned.</p>
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