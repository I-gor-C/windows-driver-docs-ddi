---
UID: NN:dbgeng.IDebugClient6
title: IDebugClient6
author: windows-driver-content
description: This interface supports event context callbacks.
old-location: debugger\idebugclient6.htm
old-project: debugger
ms.assetid: 9F8DFF33-DE07-4061-9A9E-3C8172F75EB5
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugClient6, IDebugClient6 interface [Windows Debugging], IDebugClient6 interface [Windows Debugging], described, dbgeng/IDebugClient6, debugger.idebugclient6
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
-	IDebugClient6
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugClient6 interface

This interface supports event context callbacks.

## Methods

<p>The <b>IDebugClient6</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugClient6::SetEventContextCallbacks](nf-dbgeng-idebugclient6-seteventcontextcallbacks.md) | Registers an event callbacks object with this client. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |