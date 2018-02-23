---
UID: NN:dbgeng.IDebugPlmClient3
title: IDebugPlmClient3
author: windows-driver-content
description: This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location: debugger\idebugplmclient3.htm
old-project: Debugger
ms.assetid: 5B0580FF-0829-406A-B511-C0CD91A08D5F
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: debugger.idebugplmclient3, IDebugPlmClient3 interface [Windows Debugging], IDebugPlmClient3 interface [Windows Debugging], described, IDebugPlmClient3, dbgeng/IDebugPlmClient3
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
-	IDebugPlmClient3
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugPlmClient3 interface

This interface supports Process Lifecycle Management (PLM) for the debug client.

## Methods

<p>The <b>IDebugPlmClient3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugPlmClient3.ActivateAndDebugPlmBgTaskWide](nf-dbgeng-idebugplmclient3-activateanddebugplmbgtaskwide.md) | Launches and attaches to a Process Lifecycle Management (PLM) background task. |
| [dbgeng.IDebugPlmClient3.DisablePlmPackageDebugWide](nf-dbgeng-idebugplmclient3-disableplmpackagedebugwide.md) | Disables a Process Lifecycle Management (PLM) package debug. |
| [dbgeng.IDebugPlmClient3.EnablePlmPackageDebugWide](nf-dbgeng-idebugplmclient3-enableplmpackagedebugwide.md) | Enables a Process Lifecycle Management (PLM) package debug. |
| [dbgeng.IDebugPlmClient3.LaunchAndDebugPlmAppWide](nf-dbgeng-idebugplmclient3-launchanddebugplmappwide.md) | Launches and attaches to a Process Lifecycle Management (PLM) application. |
| [dbgeng.IDebugPlmClient3.QueryPlmPackageList](nf-dbgeng-idebugplmclient3-queryplmpackagelist.md) | Query a Process Lifecycle Management (PLM) package list. |
| [dbgeng.IDebugPlmClient3.QueryPlmPackageWide](nf-dbgeng-idebugplmclient3-queryplmpackagewide.md) | Query a Process Lifecycle Management (PLM) package. |
| [dbgeng.IDebugPlmClient3.ResumePlmPackageWide](nf-dbgeng-idebugplmclient3-resumeplmpackagewide.md) | Resumes a Process Lifecycle Management (PLM) package. |
| [dbgeng.IDebugPlmClient3.SuspendPlmPackageWide](nf-dbgeng-idebugplmclient3-suspendplmpackagewide.md) | Suspends a Process Lifecycle Management (PLM) package. |
| [dbgeng.IDebugPlmClient3.TerminatePlmPackageWide](nf-dbgeng-idebugplmclient3-terminateplmpackagewide.md) | Ends a Process Lifecycle Management (PLM) package. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |