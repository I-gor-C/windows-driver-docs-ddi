---
UID : NF:dbgeng.IDebugSystemObjects4.GetCurrentProcessSystemId
title : IDebugSystemObjects4::GetCurrentProcessSystemId method
author : windows-driver-content
description : The GetCurrentProcessSystemId method returns the system process ID of the current process.
old-location : debugger\getcurrentprocesssystemid.htm
old-project : debugger
ms.assetid : 850f2f86-af0d-414a-99d7-d081753c591f
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSystemObjects4, IDebugSystemObjects4::GetCurrentProcessSystemId, GetCurrentProcessSystemId
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
req.alt-api : IDebugSystemObjects.GetCurrentProcessSystemId,IDebugSystemObjects2.GetCurrentProcessSystemId,IDebugSystemObjects3.GetCurrentProcessSystemId,IDebugSystemObjects4.GetCurrentProcessSystemId
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


# GetCurrentProcessSystemId method
The <b>GetCurrentProcessSystemId</b> method returns the system process ID of the current process.

## Syntax

````
HRESULT GetCurrentProcessSystemId(
  [out] PULONG SysId
);
````

## Parameters

`SysId`

Receives the system process ID.


## Return Value

This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.
<dl>
<dt><b>E_NOTIMPL</b></dt>
</dl>The target is a kernel-mode target.

## Remarks

This method is only available in user-mode debugging.

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