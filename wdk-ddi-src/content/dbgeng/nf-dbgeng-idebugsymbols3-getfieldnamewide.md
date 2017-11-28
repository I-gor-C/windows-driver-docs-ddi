---
UID: NF.dbgeng.IDebugSymbols3.GetFieldNameWide
title: IDebugSymbols3::GetFieldNameWide
author: windows-driver-content
description: The GetFieldNameWide method returns the name of a field within a structure.
old-location: debugger\getfieldnamewide.htm
old-project: debugger
ms.assetid: e27c6af5-c9fa-4fe6-ad39-82ea59a0f27b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, GetFieldNameWide, IDebugSymbols3::GetFieldNameWide
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
req.alt-api: IDebugSymbols3.GetFieldNameWide
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
req.iface: IDebugSymbols3
---

# IDebugSymbols3::GetFieldNameWide method



## -description
<p>The <b>GetFieldNameWide</b>  method returns the name of a field within a structure.</p>


## -syntax

````
HRESULT GetFieldNameWide(
  [in]            ULONG64 Module,
  [in]            ULONG   TypeId,
  [in]            ULONG   FieldIndex,
  [out, optional] PWSTR   NameBuffer,
  [in]            ULONG   NameBufferSize,
  [out, optional] PULONG  NameSize
);
````


## -parameters
<dl>

### -param <i>Module</i> [in]

<dd>
<p>Specifies the base address of the module in which the structure was defined.</p>
</dd>

### -param <i>TypeId</i> [in]

<dd>
<p>Specifies the type ID of the structure.</p>
</dd>

### -param <i>FieldIndex</i> [in]

<dd>
<p>Specifies the index of the desired field within the structure. </p>
</dd>

### -param <i>NameBuffer</i> [out, optional]

<dd>
<p>Receives the field's name.  If <i>NameBuffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>NameBufferSize</i> [in]

<dd>
<p>Specifies the size in characters of the buffer <i>NameBuffer</i>.</p>
</dd>

### -param <i>NameSize</i> [out, optional]

<dd>
<p>Receives the size in characters of the field's name.  If <i>NameSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, <i>NameBuffer</i> was not large enough to hold the field's name and it was truncated.</p>

<p> </p>

## -remarks
<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

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