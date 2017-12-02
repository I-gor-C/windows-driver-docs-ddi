---
UID: NF.dbgeng.IDebugControl3.OutputCurrentState
title: IDebugControl3::OutputCurrentState
author: windows-driver-content
description: The OutputCurrentState method prints the current state of the current target to the debugger console.
old-location: debugger\outputcurrentstate.htm
old-project: debugger
ms.assetid: 3d176438-5551-48a4-b757-81c14d84c075
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl3, OutputCurrentState, IDebugControl3::OutputCurrentState
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
req.alt-api: IDebugControl.OutputCurrentState,IDebugControl2.OutputCurrentState,IDebugControl3.OutputCurrentState
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
req.iface: IDebugControl3
---

# IDebugControl3::OutputCurrentState method



## -description
<p>The <b>OutputCurrentState</b> method prints the current state of the current target to the debugger console.</p>


## -syntax

````
HRESULT OutputCurrentState(
  [in] ULONG OutputControl,
  [in] ULONG Flags
);
````


## -parameters
<dl>

### -param OutputControl [in]

<dd>
<p>Specifies which clients to send the output to.  For possible values see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541517">DEBUG_OUTCTL_XXX</a>.</p>
</dd>

### -param Flags [in]

<dd>
<p>Specifies the bit set that determines the information to print to the debugger console.  <i>Flags</i> can be any combination of values from the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_CURRENT_SYMBOL</p>
</td>
<td>
<p>Symbol string for the address of the current instruction.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CURRENT_DISASM</p>
</td>
<td>
<p>Disassembly of the current instruction.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CURRENT_REGISTERS</p>
</td>
<td>
<p>Current register values.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CURRENT_SOURCE_LINE</p>
</td>
<td>
<p>File name and line number of the source corresponding to the current instruction.</p>
</td>
</tr>
</table>
<p> </p>
<p>Alternatively, <i>Flags</i> can be set to DEBUG_CURRENT_DEFAULT.  This value includes all of the above flags.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Setting the flags contained in <i>Flags</i> merely allows the information to be printed.  The information will not always be printed (for example, it will not be printed if it is not available).</p>

<p>This is the same status information that is printed when breaking into the debugger.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558860">Target Information</a>.</p>

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