---
UID: NF.dbgeng.IDebugBreakpoint2.SetCommandWide
title: IDebugBreakpoint2::SetCommandWide
author: windows-driver-content
description: The SetCommandWide method sets the command that is executed when a breakpoint is triggered.
old-location: debugger\setcommandwide.htm
old-project: debugger
ms.assetid: 3edab087-01e4-4cd4-82d3-38d67962c93c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugBreakpoint2, SetCommandWide, IDebugBreakpoint2::SetCommandWide
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
req.alt-api: IDebugBreakpoint2.SetCommandWide
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
req.iface: IDebugBreakpoint2
---

# IDebugBreakpoint2::SetCommandWide method



## -description
<p>The <b>SetCommandWide</b> method sets the command that is executed when a breakpoint is triggered.</p>


## -syntax

````
HRESULT SetCommandWide(
  [in] PCWSTR Command
);
````


## -parameters
<dl>

### -param Command [in]

<dd>
<p>The command string that is executed when the breakpoint is triggered.</p>
</dd>
</dl>

## -returns
<p><b>SetCommandWide</b> might return one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The command string is a list of debugger commands that are separated by semicolons.  These commands are executed every time that the breakpoint is triggered.  The commands are executed before the engine informs any event callbacks that the breakpoint has been triggered.</p>

<p>If the command string includes an execution command such as <b>G (Go)</b>, this command should be the last command in the <i>Command</i> string.  If a command causes the target to resume execution, the rest of the command string is ignored.</p>

<p>For more information about breakpoint properties, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.</p>

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