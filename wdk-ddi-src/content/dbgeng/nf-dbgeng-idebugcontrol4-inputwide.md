---
UID: NF.dbgeng.IDebugControl4.InputWide
title: IDebugControl4::InputWide
author: windows-driver-content
description: The InputWide method requests an input string from the debugger engine.
old-location: debugger\inputwide.htm
old-project: debugger
ms.assetid: 79997d8c-4641-4953-a1a2-e5bde88cbc3f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl4, InputWide, IDebugControl4::InputWide
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
req.alt-api: IDebugControl4.InputWide
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
req.iface: IDebugControl4
---

# IDebugControl4::InputWide method



## -description
<p>The <b>InputWide</b>  method requests an input string from the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>.</p>


## -syntax

````
HRESULT InputWide(
  [out]           PWSTR  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG InputSize
);
````


## -parameters
<dl>

### -param <i>Buffer</i> [out]

<dd>
<p>Receives the input string from the engine.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size, in characters, of the buffer that <i>Buffer</i> specifies.</p>
</dd>

### -param <i>InputSize</i> [out, optional]

<dd>
<p>Receives the number of characters returned in <i>Buffer</i>.  If <i>InputSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the buffer was not big enough to hold the whole input string and it was truncated.</p>

<p> </p>

## -remarks
<p>For an overview of input in the debugger engine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>

<p>For an overview of input in the debugger engine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>

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