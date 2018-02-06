---
UID: NN:dbgeng.IDebugInputCallbacks
title: IDebugInputCallbacks
author: windows-driver-content
description: IDebugInputCallbacks interface
old-location: debugger\idebuginputcallbacks.htm
old-project: debugger
ms.assetid: 2122d970-1d1c-4ef0-b8f7-92ef6e4f0731
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebuginputcallbacks, IDebugInputCallbacks interface [Windows Debugging], IDebugInputCallbacks interface [Windows Debugging], described, IDebugInputCallbacks, dbgeng/IDebugInputCallbacks, ComCallbacks_9dd6d3d2-e92d-41bc-8276-fa8b7818a372.xml
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
-	IDebugInputCallbacks
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugInputCallbacks interface



## Methods

<p>The <b>IDebugInputCallbacks</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugInputCallbacks.EndInput](nf-dbgeng-idebuginputcallbacks-endinput.md) | The EndInput callback method is called by the engine to indicate that it is no longer waiting for input. |
| [dbgeng.IDebugInputCallbacks.StartInput](nf-dbgeng-idebuginputcallbacks-startinput.md) | The StartInput callback method is called by the engine to indicate that it is waiting for a line of input. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |