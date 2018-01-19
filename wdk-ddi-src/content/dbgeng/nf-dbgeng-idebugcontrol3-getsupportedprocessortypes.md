---
UID : NF:dbgeng.IDebugControl3.GetSupportedProcessorTypes
title : IDebugControl3::GetSupportedProcessorTypes method
author : windows-driver-content
description : The GetSupportedProcessorTypes method returns the processor types supported by the debugger engine.
old-location : debugger\getsupportedprocessortypes.htm
old-project : debugger
ms.assetid : b1a69c60-67e8-46b0-8f2e-7da2c4860ea6
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugControl3, IDebugControl3::GetSupportedProcessorTypes, GetSupportedProcessorTypes
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
req.alt-api : IDebugControl.GetSupportedProcessorTypes,IDebugControl2.GetSupportedProcessorTypes,IDebugControl3.GetSupportedProcessorTypes
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


# GetSupportedProcessorTypes method
The <b>GetSupportedProcessorTypes</b> method returns the processor types supported by the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>.

## Syntax

````
HRESULT GetSupportedProcessorTypes(
  [in]  ULONG  Start,
  [in]  ULONG  Count,
  [out] PULONG Types
);
````

## Parameters

`Start`

Specifies the index of the first processor type to return.  The supported processor types are indexed by the numbers zero through the number of supported processor types minus one.  The number of supported processor types can be found using <a href="https://msdn.microsoft.com/library/windows/hardware/ff547966">GetNumberSupportedProcessorTypes</a>.

`Count`

Specifies the number of processor types to return.

`Types`

Receives the list of processor types.  The number of elements this array holds is <i>Count</i>.  For a description of the processor types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545572">GetActualProcessorType</a>.


## Return Value

This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

## Remarks

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558860">Target Information</a>.

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

## See Also

<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547966">GetNumberSupportedProcessorTypes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548169">GetProcessorTypeNames</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetSupportedProcessorTypes method%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>