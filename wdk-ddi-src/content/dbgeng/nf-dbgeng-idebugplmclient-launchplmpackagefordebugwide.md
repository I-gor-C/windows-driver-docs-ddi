---
UID: NF:dbgeng.IDebugPlmClient.LaunchPlmPackageForDebugWide
title: IDebugPlmClient::LaunchPlmPackageForDebugWide method
author: windows-driver-content
description: Launches a suspended Process Lifecycle Management (PLM) application.
old-location: debugger\idebugplmclient_launchplmpackagefordebugwide.htm
old-project: debugger
ms.assetid: DE11B4A5-5AE3-4369-AF6D-6CE34B9AAFAB
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugPlmClient, IDebugPlmClient interface [Windows Debugging], LaunchPlmPackageForDebugWide method, IDebugPlmClient::LaunchPlmPackageForDebugWide, LaunchPlmPackageForDebugWide method [Windows Debugging], LaunchPlmPackageForDebugWide method [Windows Debugging], IDebugPlmClient interface, LaunchPlmPackageForDebugWide,IDebugPlmClient.LaunchPlmPackageForDebugWide, dbgeng/IDebugPlmClient::LaunchPlmPackageForDebugWide, debugger.idebugplmclient_launchplmpackagefordebugwide
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
-	IDebugPlmClient.LaunchPlmPackageForDebugWide
product:
- Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IDebugPlmClient::LaunchPlmPackageForDebugWide method
Launches a suspended Process Lifecycle Management (PLM) application.

## Syntax

```
HRESULT LaunchPlmPackageForDebugWide(
  ULONG64 Server,
  ULONG   Timeout,
  PCWSTR  PackageFullName,
  PCWSTR  AppName,
  PCWSTR  Arguments,
  PULONG  ProcessId,
  PULONG  ThreadId
);
```

## Parameters

`Server`

The server of the application.

`Timeout`

A time-out value.

`PackageFullName`

A pointer to the package name.

`AppName`

A pointer to the application name.

`Arguments`

A pointer an arguments string.

`ProcessId`

A pointer to a process ID output.

`ThreadId`

A pointer to a thread ID output.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/2D713354-4C93-4DC1-A3E9-7E6BC991FD08">IDebugPlmClient</a>