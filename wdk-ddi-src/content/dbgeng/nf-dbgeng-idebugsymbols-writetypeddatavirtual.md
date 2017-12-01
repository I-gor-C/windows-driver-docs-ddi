---
UID: NF.dbgeng.IDebugSymbols.WriteTypedDataVirtual
title: IDebugSymbols::WriteTypedDataVirtual
author: windows-driver-content
description: The WriteTypedDataVirtual method writes data to the target's virtual address space. The number of bytes written is the size of the specified type.
old-location: debugger\writetypeddatavirtual.htm
old-project: debugger
ms.assetid: c7a3854b-2405-4e20-8c6c-4e0c0d43987e
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols, WriteTypedDataVirtual, IDebugSymbols::WriteTypedDataVirtual
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
req.alt-api: IDebugSymbols.WriteTypedDataVirtual,IDebugSymbols2.WriteTypedDataVirtual,IDebugSymbols3.WriteTypedDataVirtual
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
req.iface: IDebugSymbols
---

# IDebugSymbols::WriteTypedDataVirtual method



## -description
<p>The <b>WriteTypedDataVirtual</b> method writes data to the target's virtual address space.  The number of bytes written is the size of the specified type.</p>


## -syntax

````
HRESULT WriteTypedDataVirtual(
  [in]            ULONG64 Offset,
  [in]            ULONG64 Module,
  [in]            ULONG   TypeId,
  [in]            PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesWritten
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space where the data will be written.</p>
</dd>

### -param <i>Module</i> [in]

<dd>
<p>Specifies the base address of the module containing the type.</p>
</dd>

### -param <i>TypeId</i> [in]

<dd>
<p>Specifies the type ID of the type.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Specifies the buffer containing the data to be written.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes to be written.</p>
</dd>

### -param <i>BytesWritten</i> [out, optional]

<dd>
<p>Receives the number of bytes that were written.  If <i>BytesWritten</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  All the bytes in the buffer <i>Buffer</i> were written.  However, the buffer was smaller than the size of the type specified. </p>

<p> </p>

## -remarks
<p>This is a convenience method.  The same result can be obtained by calling <a href="debugger.gettypesize2">GetTypeSize</a> and <a href="debugger.writevirtual">WriteVirtual</a>.</p>

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