---
UID: NF.dbgeng.IDebugSymbols3.GetConstantNameWide
title: IDebugSymbols3::GetConstantNameWide
author: windows-driver-content
description: The GetConstantNameWide method returns the name of the specified constant.
old-location: debugger\getconstantnamewide.htm
old-project: debugger
ms.assetid: 743d2f83-905b-4bc9-8e23-b330c3ca7629
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols3, GetConstantNameWide, IDebugSymbols3::GetConstantNameWide
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
req.alt-api: IDebugSymbols3.GetConstantNameWide
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

# IDebugSymbols3::GetConstantNameWide method



## -description
<p>The <b>GetConstantNameWide</b>  method returns the name of the specified constant.</p>


## -syntax

````
HRESULT GetConstantNameWide(
  [in]            ULONG64 Module,
  [in]            ULONG   TypeId,
  [in]            ULONG64 Value,
  [out, optional] PWSTR   NameBuffer,
  [in]            ULONG   NameBufferSize,
  [out, optional] PULONG  NameSize
);
````


## -parameters
<dl>

### -param <i>Module</i> [in]

<dd>
<p>Specifies the base address of the module in which the constant was defined.</p>
</dd>

### -param <i>TypeId</i> [in]

<dd>
<p>Specifies the type ID of the constant.</p>
</dd>

### -param <i>Value</i> [in]

<dd>
<p>Specifies the value of the constant.</p>
</dd>

### -param <i>NameBuffer</i> [out, optional]

<dd>
<p>Receives the constant's name.  If <i>NameBuffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>NameBufferSize</i> [in]

<dd>
<p>Specifies the size in characters of the buffer <i>NameBuffer</i>.</p>
</dd>

### -param <i>NameSize</i> [out, optional]

<dd>
<p>Receives the size in characters of the constant's name.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the buffer was not large enough for the constant's name and it was truncated.</p>

<p> </p>

## -remarks
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