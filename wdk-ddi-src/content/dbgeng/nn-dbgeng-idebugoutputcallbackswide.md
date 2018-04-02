---
UID: NN:dbgeng.IDebugOutputCallbacksWide
title: IDebugOutputCallbacksWide
author: windows-driver-content
description: IDebugOutputCallbacksWide interface
old-location: debugger\idebugoutputcallbackswide.htm
old-project: debugger
ms.assetid: 2f0c10f7-009a-4108-ad23-d6b6e2e1257e
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugOutputCallbacksWide, IDebugOutputCallbacksWide interface [Windows Debugging], IDebugOutputCallbacksWide interface [Windows Debugging], described, dbgeng/IDebugOutputCallbacksWide, debugger.idebugoutputcallbackswide
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
-	IDebugOutputCallbacksWide
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugOutputCallbacksWide interface



## Methods

<p>The <b>IDebugOutputCallbacksWide</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugOutputCallbacksWide::Output](nf-dbgeng-idebugoutputcallbackswide-output.md) | The Output callback method is called by the engine to send output from the client to the IDebugOutputCallbacksWide object that is registered with the client. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550801">IDebugOutputCallbacks</a>