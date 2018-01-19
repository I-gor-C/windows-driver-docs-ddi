---
UID : NF:dbgeng.IDebugSystemObjects4.GetCurrentThreadHandle
title : IDebugSystemObjects4::GetCurrentThreadHandle method
author : windows-driver-content
description : The GetCurrentThreadHandle method returns the system handle for the current thread.
old-location : debugger\getcurrentthreadhandle.htm
old-project : debugger
ms.assetid : edbda821-8016-48db-a2f5-7f615428da0c
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSystemObjects4, IDebugSystemObjects4::GetCurrentThreadHandle, GetCurrentThreadHandle
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
req.alt-api : IDebugSystemObjects.GetCurrentThreadHandle,IDebugSystemObjects2.GetCurrentThreadHandle,IDebugSystemObjects3.GetCurrentThreadHandle,IDebugSystemObjects4.GetCurrentThreadHandle
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


# GetCurrentThreadHandle method
The <b>GetCurrentThreadHandle</b> method returns the system handle for the current thread.

## Syntax

````
HRESULT GetCurrentThreadHandle(
  [out] PULONG64 Handle
);
````

## Parameters

`Handle`

Receives the current thread's system handle.


## Return Value

This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

## Remarks

In kernel-mode debugging, an artificial handle is created because the threads are virtual threads.

For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.  For details on system handles, see <a href="wdkgloss.h#wdkgloss.handle#wdkgloss.handle"><i>Handles</i></a>.</p>

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