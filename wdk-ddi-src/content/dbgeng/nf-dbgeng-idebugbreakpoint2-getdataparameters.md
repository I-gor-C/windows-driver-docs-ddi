---
UID: NF.dbgeng.IDebugBreakpoint2.GetDataParameters
title: IDebugBreakpoint2::GetDataParameters
author: windows-driver-content
description: The GetDataParameters method returns the parameters for a processor breakpoint.
old-location: debugger\getdataparameters.htm
old-project: debugger
ms.assetid: e281c67a-df97-464e-9996-b15c18172dc4
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugBreakpoint2, GetDataParameters, IDebugBreakpoint2::GetDataParameters
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
req.alt-api: IDebugBreakpoint.GetDataParameters,IDebugBreakpoint2.GetDataParameters
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

# IDebugBreakpoint2::GetDataParameters method



## -description
<p>The <b>GetDataParameters</b> method returns the parameters for a processor breakpoint.</p>


## -syntax

````
HRESULT GetDataParameters(
  [out] PULONG Size,
  [out] PULONG AccessType
);
````


## -parameters
<dl>

### -param <i>Size</i> [out]

<dd>
<p>The size, in bytes, of the memory block whose access triggers the breakpoint.  For more information about restrictions on the value of <i>Size</i> based on the processor type, see <a href="debugger.controlling_breakpoint_flags_and_parameters#valid_parameters_for_processor_breakpoints#valid_parameters_for_processor_breakpoints">Valid Parameters for Processor Breakpoints</a>.</p>
</dd>

### -param <i>AccessType</i> [out]

<dd>
<p>The type of access that triggers the breakpoint.  For a list of possible values, see <a href="debugger.controlling_breakpoint_flags_and_parameters#valid_parameters_for_processor_breakpoints#valid_parameters_for_processor_breakpoints">Valid Parameters for Processor Breakpoints</a>.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>The breakpoint is not a processor breakpoint.  For more information about the breakpoint type, see <a href="debugger.gettype">GetType</a>.</p>

<p> </p>

<p>This method can also return other error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>The <a href="debugger.getparameters">GetParameters</a> method also returns the information that is returned in <i>Size</i> and <i>AccessType</i>.</p>

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