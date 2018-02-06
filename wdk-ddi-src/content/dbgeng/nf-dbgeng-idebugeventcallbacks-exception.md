---
UID: NF:dbgeng.IDebugEventCallbacks.Exception
title: IDebugEventCallbacks::Exception method
author: windows-driver-content
description: The Exception callback method is called by the engine when an exceptiondebugging event occurs in the target.
old-location: debugger\idebugeventcallbacks_exception.htm
old-project: debugger
ms.assetid: 93f915ab-1f9e-453c-b76e-8260eecd7298
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugeventcallbacks_exception, Exception method [Windows Debugging], IDebugEventCallbacks interface, Exception method [Windows Debugging], IDebugEventCallbacks, IDebugEventCallbacks::Exception, IDebugEventCallbacks interface [Windows Debugging], Exception method, ComCallbacks_46bf959d-52a9-4b0a-b074-d28b76de343d.xml, dbgeng/IDebugEventCallbacks::Exception, Exception
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
-	IDebugEventCallbacks.Exception
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# Exception method
The <b>Exception</b> callback method is called by the engine when an <a href="https://msdn.microsoft.com/0dd010e7-3e10-422a-adcb-8fe7df9e29ab">exception</a>debugging event occurs in the target.

## Syntax

````
HRESULT Exception(
  [in] PEXCEPTION_RECORD64 Exception,
  [in] ULONG               FirstChance
);
````

## Parameters

`Exception`

Specifies the nature of the exception.  EXCEPTION_RECORD64 is defined in winnt.h.

`FirstChance`

Specifies whether this exception has been previously encountered.  A nonzero value means that this is the first time the exception has been encountered ("first chance").  A zero value means that the exception has already been offered to all possible handlers, and each one declined to handle it ("second chance").


## Return Value

This method returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541651">DEBUG_STATUS_XXX</a> value, which indicates how the execution of the target should proceed after the engine processes this event.  For details on how the engine treats this value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.

## Remarks

This method is only called by the engine if the DEBUG_EVENT_EXCEPTION flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550737">IDebugEventCallbacks::GetInterestMask</a>.

Because the structure that <i>Exception</i> points to might be deleted after this method returns, implementations of <b>IDebugEventCallbacks</b> should not access this structure after returning.

For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** | dbgeng.h |