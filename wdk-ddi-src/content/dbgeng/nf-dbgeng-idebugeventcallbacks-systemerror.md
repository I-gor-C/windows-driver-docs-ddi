---
UID: NF:dbgeng.IDebugEventCallbacks.SystemError
title: IDebugEventCallbacks::SystemError method
author: windows-driver-content
description: The SystemError callback method is called by the engine when a system error occurs in the target.
old-location: debugger\idebugeventcallbacks_systemerror.htm
old-project: Debugger
ms.assetid: 651f5207-36c8-4d46-8305-950efb2365bf
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: SystemError, IDebugEventCallbacks interface [Windows Debugging], SystemError method, SystemError method [Windows Debugging], dbgeng/IDebugEventCallbacks::SystemError, SystemError method [Windows Debugging], IDebugEventCallbacks interface, debugger.idebugeventcallbacks_systemerror, ComCallbacks_a84628b9-4376-4ca0-883f-835d19e13d73.xml, IDebugEventCallbacks, IDebugEventCallbacks::SystemError
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: dbgeng.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	dbgeng.h
apiname:
-	IDebugEventCallbacks.SystemError
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# SystemError method
The <b>SystemError</b> callback method is called by the engine when a system error occurs in the target.

## Syntax

````
HRESULT SystemError(
  [in] ULONG Error,
  [in] ULONG Level
);
````

## Parameters

`Error`

Specifies the error that caused the event.

`Level`

Specifies the severity of the error.


## Return Value

This method returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541651">DEBUG_STATUS_XXX</a> value, which indicates how the execution of the target should proceed after the engine processes this event.  For details on how the engine treats this value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.

## Remarks

This method is only called by the engine if the DEBUG_EVENT_SYSTEM_ERROR flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550737">IDebugEventCallbacks::GetInterestMask</a>.

For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** | dbgeng.h |