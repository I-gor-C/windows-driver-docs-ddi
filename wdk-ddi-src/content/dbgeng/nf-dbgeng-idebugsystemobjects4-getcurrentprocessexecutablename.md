---
UID : NF:dbgeng.IDebugSystemObjects4.GetCurrentProcessExecutableName
title : IDebugSystemObjects4::GetCurrentProcessExecutableName method
author : windows-driver-content
description : The GetCurrentProcessExecutableName method returns the name of executable file loaded in the current process.
old-location : debugger\getcurrentprocessexecutablename.htm
old-project : debugger
ms.assetid : ea968316-a53d-4ab1-966a-5c699ffb8f2a
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSystemObjects4, IDebugSystemObjects4::GetCurrentProcessExecutableName, GetCurrentProcessExecutableName
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
req.alt-api : IDebugSystemObjects.GetCurrentProcessExecutableName,IDebugSystemObjects2.GetCurrentProcessExecutableName,IDebugSystemObjects3.GetCurrentProcessExecutableName,IDebugSystemObjects4.GetCurrentProcessExecutableName
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


# GetCurrentProcessExecutableName method
The <b>GetCurrentProcessExecutableName</b>  method returns the name of executable file loaded in the current process.

## Syntax

````
HRESULT GetCurrentProcessExecutableName(
  [out, optional] PSTR   Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG ExeSize
);
````

## Parameters

`Buffer`

Receives the name of the executable file.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.

`BufferSize`

Specifies the size in characters of the buffer <i>Buffer</i>.

`ExeSize`

Receives the size in characters of the name of the executable file.  If <i>ExeSize</i> is <b>NULL</b>, this information is not returned.


## Return Value

This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.
<dl>
<dt><b>S_FALSE</b></dt>
</dl>The method was successful. However, the buffer was not large enough to hold the name of the executable file and it was truncated.

## Remarks

These methods are only available in user-mode debugging.

If the engine cannot determine the name of the executable file, it writes the string "?NoImage?" to the buffer.

For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

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