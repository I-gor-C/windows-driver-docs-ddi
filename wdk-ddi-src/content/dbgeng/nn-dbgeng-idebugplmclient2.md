---
UID: NN:dbgeng.IDebugPlmClient2
title: IDebugPlmClient2
author: windows-driver-content
description: This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location: debugger\idebugplmclient2.htm
old-project: debugger
ms.assetid: 22AACAD1-292B-42D9-95F7-A3654E2077FB
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IDebugPlmClient2, IDebugPlmClient2 interface [Windows Debugging], IDebugPlmClient2 interface [Windows Debugging], described, dbgeng/IDebugPlmClient2, debugger.idebugplmclient2
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugPlmClient2
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugPlmClient2 interface

This interface supports Process Lifecycle Management (PLM) for the debug client.

## Methods

<p>The <b>IDebugPlmClient2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugPlmClient2::LaunchPlmBgTaskForDebugWide](nf-dbgeng-idebugplmclient2-launchplmbgtaskfordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) background task. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |