---
UID : NF:dbgeng.IDebugBreakpoint2.SetDataParameters
title : IDebugBreakpoint2::SetDataParameters method
author : windows-driver-content
description : The SetDataParameters method sets the parameters for a processor breakpoint.
old-location : debugger\setdataparameters.htm
old-project : debugger
ms.assetid : 66878652-be29-479f-8e00-a9d8ab1b0db7
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugBreakpoint2, IDebugBreakpoint2::SetDataParameters, SetDataParameters
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IDebugBreakpoint.SetDataParameters,IDebugBreakpoint2.SetDataParameters
req.alt-loc : dbgeng.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---


# SetDataParameters method
The <b>SetDataParameters</b> method sets the parameters for a processor breakpoint.

## Syntax

````
HRESULT SetDataParameters(
  [in] ULONG Size,
  [in] ULONG AccessType
);
````

## Parameters

`Size`

The size, in bytes, of the memory block whose access triggers the breakpoint.  For more information about restrictions on the value of <i>Size</i> based on the processor type, see <a href="debugger.controlling_breakpoint_flags_and_parameters#valid_parameters_for_processor_breakpoints#valid_parameters_for_processor_breakpoints">Valid Parameters for Processor Breakpoints</a>.

`AccessType`

The type of access that triggers the breakpoint. For a list of possible value, see <a href="debugger.controlling_breakpoint_flags_and_parameters#valid_parameters_for_processor_breakpoints#valid_parameters_for_processor_breakpoints">Valid Parameters for Processor Breakpoints</a>.


## Return Value

<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.
<dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl>The breakpoint is not a processor breakpoint.  For more information about the breakpoint type, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a>.

 

This method can also return other error values.  For more information, see <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a>.

## Remarks

For more information about breakpoint properties, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539284">Controlling Breakpoint Flags and Parameters</a>.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |