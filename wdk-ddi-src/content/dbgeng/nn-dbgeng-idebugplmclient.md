---
UID : NN:dbgeng.IDebugPlmClient
title : IDebugPlmClient
author : windows-driver-content
description : This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location : debugger\idebugplmclient.htm
old-project : debugger
ms.assetid : 2D713354-4C93-4DC1-A3E9-7E6BC991FD08
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : debugger.idebugplmclient, IDebugPlmClient interface [Windows Debugging], IDebugPlmClient interface [Windows Debugging], described, IDebugPlmClient, dbgeng/IDebugPlmClient
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : dbgeng.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugPlmClient interface

This interface supports Process Lifecycle Management (PLM) for the debug client.

## Methods

<p>The <b>IDebugPlmClient</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugPlmClient.LaunchPlmPackageForDebugWide](nf-dbgeng-idebugplmclient-launchplmpackagefordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) application. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **DLL** |  |