---
UID: NN:dbgeng.IDebugOutputCallbacks
title: IDebugOutputCallbacks
author: windows-driver-content
description: IDebugOutputCallbacks interface
old-location: debugger\idebugoutputcallbacks.htm
old-project: debugger
ms.assetid: 6b29e15c-3a9d-4d96-8b72-22064526ca75
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: ComCallbacks_ed6ca0bd-5599-426d-b089-18a12311eba0.xml, IDebugOutputCallbacks, IDebugOutputCallbacks interface [Windows Debugging], IDebugOutputCallbacks interface [Windows Debugging], described, dbgeng/IDebugOutputCallbacks, debugger.idebugoutputcallbacks
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
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
-	IDebugOutputCallbacks
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugOutputCallbacks interface



## Methods

<p>The <b>IDebugOutputCallbacks</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugOutputCallbacks::Output](nf-dbgeng-idebugoutputcallbacks-output.md) | The Output callback method is called by the engine to send output from the client to the IDebugOutputCallbacks object that is registered with the client. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550804">IDebugOutputCallbacksWide</a>