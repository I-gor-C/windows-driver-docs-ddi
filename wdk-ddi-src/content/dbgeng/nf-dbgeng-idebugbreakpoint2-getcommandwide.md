---
UID: NF.dbgeng.IDebugBreakpoint2.GetCommandWide
title: IDebugBreakpoint2::GetCommandWide method
author: windows-driver-content
description: The GetCommand method returns the command string that is executed when a breakpoint is triggered.
old-location: debugger\getcommandwide.htm
old-project: Debugger
ms.assetid: 050a4243-6ad8-4aa4-8ffb-40fe9fc07b51
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugBreakpoint2, IDebugBreakpoint2::GetCommandWide, GetCommandWide
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugBreakpoint2.GetCommandWide
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
---

# IDebugBreakpoint2::GetCommandWide method



## -description
The <b>GetCommand</b>  method returns the command string that is executed when a breakpoint is triggered.



## -syntax

````
HRESULT GetCommandWide(
  [out, optional] PWSTR  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG CommandSize
);
````


## -parameters

### -param Buffer [out, optional]

The command string that is executed when the breakpoint is triggered.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.


### -param BufferSize [in]

The size, in characters, of the buffer that <i>Buffer</i> points to.


### -param CommandSize [out, optional]

The size of the command string.  If <i>CommandSize</i> is <b>NULL</b>, this information is not returned.


## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.
<dl>
<dt><b>S_FALSE</b></dt>
</dl>The method was successful, but the buffer was not large enough to hold the command string and so the command string was truncated to fit.

 

This method can also return error values.  For more information, see <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a>.


## -remarks
The command string is a list of debugger commands that are separated by semicolons.  These commands are executed every time that the breakpoint is triggered.  The commands are executed before the engine informs any event callbacks that the breakpoint has been triggered.

The <a href="debugger.getparameters">GetParameters</a> method also returns the size of the breakpoint's command, <i>CommandSize</i>.

For more information about breakpoint properties, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>