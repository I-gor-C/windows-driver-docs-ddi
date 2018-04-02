---
UID: NN:dbgeng.IDebugPlmClient
title: IDebugPlmClient
author: windows-driver-content
description: This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location: debugger\idebugplmclient.htm
old-project: debugger
ms.assetid: 2D713354-4C93-4DC1-A3E9-7E6BC991FD08
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugPlmClient, IDebugPlmClient interface [Windows Debugging], IDebugPlmClient interface [Windows Debugging], described, dbgeng/IDebugPlmClient, debugger.idebugplmclient
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
-	IDebugPlmClient
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugPlmClient interface

This interface supports Process Lifecycle Management (PLM) for the debug client.

## Methods

<p>The <b>IDebugPlmClient</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugPlmClient::LaunchPlmPackageForDebugWide](nf-dbgeng-idebugplmclient-launchplmpackagefordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) application. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |