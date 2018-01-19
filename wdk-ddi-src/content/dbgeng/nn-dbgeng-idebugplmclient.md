---
UID : NN:dbgeng.IDebugPlmClient
title : IDebugPlmClient
author : windows-driver-content
description : This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location : debugger\idebugplmclient.htm
old-project : debugger
ms.assetid : 2D713354-4C93-4DC1-A3E9-7E6BC991FD08
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSystemObjects4, IDebugSystemObjects4::SetImplicitThreadDataOffset, SetImplicitThreadDataOffset
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
req.alt-api : IDebugPlmClient
req.alt-loc : dbgeng.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
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