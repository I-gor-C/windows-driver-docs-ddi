---
UID: NF.dbgeng.IDebugOutputCallbacksWide.Output
title: IDebugOutputCallbacksWide::Output
author: windows-driver-content
description: The Output callback method is called by the engine to send output from the client to the IDebugOutputCallbacksWide object that is registered with the client.
old-location: debugger\idebugoutputcallbackswide_output.htm
old-project: debugger
ms.assetid: b57661c3-a18f-45ed-b7fc-f6471753566e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugOutputCallbacksWide, Output, IDebugOutputCallbacksWide::Output
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
req.alt-api: IDebugOutputCallbacksWide.Output
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
req.iface: IDebugOutputCallbacksWide
---

# IDebugOutputCallbacksWide::Output method



## -description
<p>The <b>Output</b> callback method is called by the engine to send output from the client to the  <b>IDebugOutputCallbacksWide</b> object that is registered with the client.</p>


## -syntax

````
HRESULT Output(
  [in] ULONG  Mask,
  [in] PCWSTR Text
);
````


## -parameters
<dl>

### -param <i>Mask</i> [in]

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541518">DEBUG_OUTPUT_XXX</a> bit flags that indicate the nature of the output.</p>
</dd>

### -param <i>Text</i> [in]

<dd>
<p>Specifies the output that is being sent.</p>
</dd>
</dl>

## -returns
<p>The return value is ignored by the engine unless it indicates a remote procedure call error; in this case the client, with which this <b>IDebugEventCallbacksWide</b> object is registered, is disabled.</p>

## -remarks
<p>The engine calls this method only if the supplied value of <i>Mask</i> is allowed by the client's output control.</p>

<p>For more information about debugger engine output, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>

<p>The engine calls this method only if the supplied value of <i>Mask</i> is allowed by the client's output control.</p>

<p>For more information about debugger engine output, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>

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