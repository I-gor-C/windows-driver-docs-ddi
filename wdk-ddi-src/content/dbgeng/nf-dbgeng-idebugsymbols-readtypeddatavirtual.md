---
UID: NF.dbgeng.IDebugSymbols.ReadTypedDataVirtual
title: IDebugSymbols::ReadTypedDataVirtual
author: windows-driver-content
description: The ReadTypedDataVirtual method reads the value of a variable in the target's virtual memory.
old-location: debugger\readtypeddatavirtual.htm
old-project: debugger
ms.assetid: 526bebd8-95af-4f6f-a381-eb60273d1af5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSymbols, ReadTypedDataVirtual, IDebugSymbols::ReadTypedDataVirtual
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
req.alt-api: IDebugSymbols.ReadTypedDataVirtual,IDebugSymbols2.ReadTypedDataVirtual,IDebugSymbols3.ReadTypedDataVirtual
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

# IDebugSymbols::ReadTypedDataVirtual method



## -description
<p>The <b>ReadTypedDataVirtual</b> method reads the value of a variable in the target's virtual memory.</p>


## -syntax

````
HRESULT ReadTypedDataVirtual(
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

### -param Offset [in]

<dd>
<p>Specifies the location in the target's virtual address space of the variable to read.</p>
</dd>

### -param Module [in]

<dd>
<p>Specifies the base address of the module containing the type of the variable.</p>
</dd>

### -param TypeId [in]

<dd>
<p>Specifies the type ID of the type.</p>
</dd>

### -param Buffer [out]

<dd>
<p>Receives the data that is read.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes to be read.</p>
</dd>

### -param BytesRead [out, optional]

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

<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p>

## -remarks
<p>The number of bytes this method attempts to read is the smaller of the size of the buffer and the size of the variable.</p>

<p>This is a convenience method.  The same result can be obtained by calling <a href="debugger.gettypesize2">GetTypeSize</a> and <a href="debugger.readvirtual">ReadVirtual</a>.</p>

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