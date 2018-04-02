---
UID: NF:dbgeng.IDebugEventCallbacksWide.SystemError
title: IDebugEventCallbacksWide::SystemError method
author: windows-driver-content
description: The SystemError callback method is called by the engine when a system error occurs in the target.
old-location: debugger\idebugeventcallbackswide_systemerror.htm
old-project: debugger
ms.assetid: 938eacb5-7939-43ed-a854-046708fc9c79
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugEventCallbacksWide, IDebugEventCallbacksWide interface [Windows Debugging], SystemError method, IDebugEventCallbacksWide::SystemError, SystemError method [Windows Debugging], SystemError method [Windows Debugging], IDebugEventCallbacksWide interface, SystemError,IDebugEventCallbacksWide.SystemError, dbgeng/IDebugEventCallbacksWide::SystemError, debugger.idebugeventcallbackswide_systemerror
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugEventCallbacksWide.SystemError
product:
- Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IDebugEventCallbacksWide::SystemError method
The <b>SystemError</b> callback method is called by the engine when a system error occurs in the target.

## Syntax

```
HRESULT SystemError(
  ULONG Error,
  ULONG Level
);
```

## Parameters

`Error`

Specifies the error that caused the event.

`Level`

Specifies the severity of the error.


## Return Value

This method returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541651">DEBUG_STATUS_XXX</a> value, which indicates how the execution of the target should proceed after the engine processes this event.  For details on how the engine treats this value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.

## Remarks

This method is only called by the engine if the DEBUG_EVENT_SYSTEM_ERROR flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550625">IDebugEventCallbacksWide::GetInterestMask</a>.

For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | dbgeng.h (include Dbgeng.h) |