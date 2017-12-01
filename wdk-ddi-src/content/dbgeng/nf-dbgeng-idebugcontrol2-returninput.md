---
UID: NF.dbgeng.IDebugControl2.ReturnInput
title: IDebugControl2::ReturnInput
author: windows-driver-content
description: The ReturnInput method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input.
old-location: debugger\returninput.htm
old-project: debugger
ms.assetid: 1f4c63da-8583-4382-a208-8279b4fe0906
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, ReturnInput, IDebugControl2::ReturnInput
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
req.alt-api: IDebugControl.ReturnInput,IDebugControl2.ReturnInput,IDebugControl3.ReturnInput
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
req.iface: IDebugControl2
---

# IDebugControl2::ReturnInput method



## -description
<p>The <b>ReturnInput</b>  method is used by <b>IDebugInputCallbacks</b> objects to send an input string to the engine following a request for input.</p>


## -syntax

````
HRESULT ReturnInput(
  [in] PCSTR Buffer
);
````


## -parameters
<dl>

### -param <i>Buffer</i> [in]

<dd>
<p>Specifies the input string being sent to the engine.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The engine had already received the input it requested. The input string in <i>Buffer</i> was not received by the engine.</p>

<p> </p>

<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
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