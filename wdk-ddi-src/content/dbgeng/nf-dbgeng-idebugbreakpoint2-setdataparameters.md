---
UID: NF.dbgeng.IDebugBreakpoint2.SetDataParameters
title: IDebugBreakpoint2::SetDataParameters
author: windows-driver-content
description: The SetDataParameters method sets the parameters for a processor breakpoint.
old-location: debugger\setdataparameters.htm
old-project: debugger
ms.assetid: 66878652-be29-479f-8e00-a9d8ab1b0db7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugBreakpoint2, SetDataParameters, IDebugBreakpoint2::SetDataParameters
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
req.alt-api: IDebugBreakpoint.SetDataParameters,IDebugBreakpoint2.SetDataParameters
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

# IDebugBreakpoint2::SetDataParameters method



## -description
<p>The <b>SetDataParameters</b> method sets the parameters for a processor breakpoint.</p>


## -syntax

````
HRESULT SetDataParameters(
  [in] ULONG Size,
  [in] ULONG AccessType
);
````


## -parameters
<dl>

### -param Size [in]

<dd>
<p>The size, in bytes, of the memory block whose access triggers the breakpoint.  For more information about restrictions on the value of <i>Size</i> based on the processor type, see <a href="debugger.controlling_breakpoint_flags_and_parameters#valid_parameters_for_processor_breakpoints#valid_parameters_for_processor_breakpoints">Valid Parameters for Processor Breakpoints</a>.</p>
</dd>

### -param AccessType [in]

<dd>
<p>The type of access that triggers the breakpoint. For a list of possible value, see <a href="debugger.controlling_breakpoint_flags_and_parameters#valid_parameters_for_processor_breakpoints#valid_parameters_for_processor_breakpoints">Valid Parameters for Processor Breakpoints</a>.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>The breakpoint is not a processor breakpoint.  For more information about the breakpoint type, see <a href="debugger.gettype">GetType</a>.</p>

<p> </p>

<p>This method can also return other error values.  For more information, see <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a>.</p>

## -remarks
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