---
UID: NF.dbgeng.IDebugSymbols2.ReadTypedDataPhysical
title: IDebugSymbols2::ReadTypedDataPhysical
author: windows-driver-content
description: The ReadTypedDataPhysical method reads the value of a variable from the target computer's physical memory.
old-location: debugger\readtypeddataphysical.htm
old-project: debugger
ms.assetid: 72562325-27f9-4e80-b03f-8926adad99c1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols2, ReadTypedDataPhysical, IDebugSymbols2::ReadTypedDataPhysical
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
req.alt-api: IDebugSymbols.ReadTypedDataPhysical,IDebugSymbols2.ReadTypedDataPhysical,IDebugSymbols3.ReadTypedDataPhysical
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
req.iface: IDebugSymbols2
---

# IDebugSymbols2::ReadTypedDataPhysical method



## -description
<p>The <b>ReadTypedDataPhysical</b> method reads the value of a variable from the target computer's physical memory.</p>


## -syntax

````
HRESULT ReadTypedDataPhysical(
  [in]            ULONG64 Offset,
  [in]            ULONG64 Module,
  [in]            ULONG   TypeId,
  [out]           PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesRead
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the physical address in the target computer's memory of the variable to be read.</p>
</dd>

### -param <i>Module</i> [in]

<dd>
<p>Specifies the base address of the module containing the type of the variable.</p>
</dd>

### -param <i>TypeId</i> [in]

<dd>
<p>Specifies the type ID of the type of the variable.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Receives the data that was read.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be read.</p>
</dd>

### -param <i>BytesRead</i> [out, optional]

<dd>
<p>Receives the number of bytes that were read.  If <i>BytesRead</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, the buffer <i>Buffer</i> was not large enough to hold all the data and it was truncated.</p>

<p> </p>

<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>This method is only available in kernel mode debugging.</p>

<p>The number of bytes this method attempts to read is the smaller of the size of the buffer and the size of the variable.</p>

<p>This is a convenience method.  The same result can be obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549457">GetTypeSize</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554313">ReadPhysical</a>.</p>

<p>For more information about types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558931">Types</a>.</p>

<p>This method is only available in kernel mode debugging.</p>

<p>The number of bytes this method attempts to read is the smaller of the size of the buffer and the size of the variable.</p>

<p>This is a convenience method.  The same result can be obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549457">GetTypeSize</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff554313">ReadPhysical</a>.</p>

<p>For more information about types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558931">Types</a>.</p>

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