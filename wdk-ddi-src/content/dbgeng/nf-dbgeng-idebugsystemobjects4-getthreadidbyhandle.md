---
UID : NF:dbgeng.IDebugSystemObjects4.GetThreadIdByHandle
title : IDebugSystemObjects4::GetThreadIdByHandle method
author : windows-driver-content
description : The GetThreadIdByHandle method returns the engine thread ID for the specified thread. The thread is specified by its system handle.
old-location : debugger\getthreadidbyhandle.htm
old-project : debugger
ms.assetid : 80962f29-9a11-456b-b083-bd0f4e26e954
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSystemObjects4, IDebugSystemObjects4::GetThreadIdByHandle, GetThreadIdByHandle
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
req.alt-api : IDebugSystemObjects.GetThreadIdByHandle,IDebugSystemObjects2.GetThreadIdByHandle,IDebugSystemObjects3.GetThreadIdByHandle,IDebugSystemObjects4.GetThreadIdByHandle
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


# GetThreadIdByHandle method
The <b>GetThreadIdByHandle</b> method returns the engine thread ID for the specified thread.  The thread is specified by its system handle.

## Syntax

````
HRESULT GetThreadIdByHandle(
  [in]  ULONG64 Handle,
  [out] PULONG  Id
);
````

## Parameters

`Handle`

Specifies the system handle of the thread whose thread ID is requested.

`Id`

Receives the engine thread ID.


## Return Value

This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

## Remarks

In kernel-mode debugging, because the handle is an artificial handle for a processor,  this method returns the engine thread ID for the virtual thread representing that processor.

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