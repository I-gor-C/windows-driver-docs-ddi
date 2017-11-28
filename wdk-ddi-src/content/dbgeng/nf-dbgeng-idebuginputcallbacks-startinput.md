---
UID: NF.dbgeng.IDebugInputCallbacks.StartInput
title: IDebugInputCallbacks::StartInput
author: windows-driver-content
description: The StartInput callback method is called by the engine to indicate that it is waiting for a line of input.
old-location: debugger\idebuginputcallbacks_startinput.htm
old-project: debugger
ms.assetid: 4ac3764e-6482-49de-aac8-3b540561d201
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugInputCallbacks, StartInput, IDebugInputCallbacks::StartInput
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
req.alt-api: IDebugInputCallbacks.StartInput
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
req.iface: IDebugInputCallbacks
---

# IDebugInputCallbacks::StartInput method



## -description
<p>The <b>StartInput</b> callback method is called by the engine to indicate that it is waiting for a line of input.</p>


## -syntax

````
HRESULT StartInput(
  [in] ULONG BufferSize
);
````


## -parameters
<dl>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the number of characters requested.  Any input longer than this size will be truncated.</p>
</dd>
</dl>

## -returns
<p>The return value is ignored by the engine unless it indicates a remote procedure call error; in this case the client, with which this <b>IDebugEventCallbacks</b> object is registered, is disabled.</p>

## -remarks
<p>This method indicates that the engine is waiting for a line of input from any client.  This can occur if, for example, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550962">Input</a> method was called on a client.</p>

<p>After calling this method, the engine waits until it receives some input.  When it does receive input, it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550791">IDebugInputCallbacks::EndInput</a> to inform all the <b>IDebugInputCallbacks</b> objects that are registered with clients that it is no longer waiting for input.</p>

<p>The <b>IDebugInputCallbacks</b> object can provide the engine with a line of input by calling either the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554600">ReturnInput</a> or <b>ReturnInputWide</b> methods.</p>

<p>For more information about debugger engine input, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>

<p>This method indicates that the engine is waiting for a line of input from any client.  This can occur if, for example, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550962">Input</a> method was called on a client.</p>

<p>After calling this method, the engine waits until it receives some input.  When it does receive input, it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550791">IDebugInputCallbacks::EndInput</a> to inform all the <b>IDebugInputCallbacks</b> objects that are registered with clients that it is no longer waiting for input.</p>

<p>The <b>IDebugInputCallbacks</b> object can provide the engine with a line of input by calling either the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554600">ReturnInput</a> or <b>ReturnInputWide</b> methods.</p>

<p>For more information about debugger engine input, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>

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