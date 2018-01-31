---
UID : NF:dbgeng.IDebugPlmClient.LaunchPlmPackageForDebugWide
title : IDebugPlmClient::LaunchPlmPackageForDebugWide method
author : windows-driver-content
description : Launches a suspended Process Lifecycle Management (PLM) application.
old-location : debugger\idebugplmclient_launchplmpackagefordebugwide.htm
old-project : debugger
ms.assetid : DE11B4A5-5AE3-4369-AF6D-6CE34B9AAFAB
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : IDebugPlmClient::LaunchPlmPackageForDebugWide, LaunchPlmPackageForDebugWide method [Windows Debugging], IDebugPlmClient interface, LaunchPlmPackageForDebugWide method [Windows Debugging], IDebugPlmClient, dbgeng/IDebugPlmClient::LaunchPlmPackageForDebugWide, debugger.idebugplmclient_launchplmpackagefordebugwide, IDebugPlmClient interface [Windows Debugging], LaunchPlmPackageForDebugWide method, LaunchPlmPackageForDebugWide
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
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


# LaunchPlmPackageForDebugWide method
Launches a suspended Process Lifecycle Management (PLM) application.

## Syntax

````
HRESULT LaunchPlmPackageForDebugWide(
  [in]           ULONG64 Server,
  [in]           ULONG   Timeout,
  [in]           PCWSTR  PackageFullName,
  [in]           PCWSTR  AppName,
  [in, optional] PCWSTR  Arguments,
  [out]          PULONG  ProcessId,
  [out]          PULONG  ThreadId
);
````

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
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugplmclient.md">IDebugPlmClient</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugPlmClient::LaunchPlmPackageForDebugWide method%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>