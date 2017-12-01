---
UID: NF.dbgeng.IDebugInputCallbacks.EndInput
title: IDebugInputCallbacks::EndInput
author: windows-driver-content
description: The EndInput callback method is called by the engine to indicate that it is no longer waiting for input.
old-location: debugger\idebuginputcallbacks_endinput.htm
old-project: debugger
ms.assetid: e22b616c-51f6-4687-95b0-eb833ceb9ec3
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugInputCallbacks, EndInput, IDebugInputCallbacks::EndInput
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
req.alt-api: IDebugInputCallbacks.EndInput
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

# IDebugInputCallbacks::EndInput method



## -description
<p>The <b>EndInput</b> callback method is called by the engine to indicate that it is no longer waiting for input.</p>


## -syntax

````
HRESULT EndInput();
````


## -parameters


## -returns
<p>This method's return value is ignored by the engine.</p>

<p>This method's return value is ignored by the engine.</p>

<p>This method's return value is ignored by the engine.</p>

## -remarks
<p>Even if the engine has not called <a href="debugger.idebuginputcallbacks_startinput">IDebugInputCallbacks::StartInput</a> for this <a href="..\dbgeng\nn-dbgeng-idebuginputcallbacks.md">IDebugInputCallbacks</a> object, the engine will call <b>EndInput</b> if another IDebugInputCallbacks object returned an error from the <b>IDebugInputCallbacks::StartInput</b> method.</p>

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