---
UID: NN:dbgeng.IDebugPlmClient2
title: IDebugPlmClient2
author: windows-driver-content
description: This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location: debugger\idebugplmclient2.htm
old-project: debugger
ms.assetid: 22AACAD1-292B-42D9-95F7-A3654E2077FB
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugplmclient2, IDebugPlmClient2 interface [Windows Debugging], IDebugPlmClient2 interface [Windows Debugging], described, IDebugPlmClient2, dbgeng/IDebugPlmClient2
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
-	IDebugPlmClient2
product: Windows
targetos: Windows
req.typenames: "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---

# IDebugPlmClient2 interface

This interface supports Process Lifecycle Management (PLM) for the debug client.

## Methods

<p>The <b>IDebugPlmClient2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugPlmClient2.LaunchPlmBgTaskForDebugWide](nf-dbgeng-idebugplmclient2-launchplmbgtaskfordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) background task. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |