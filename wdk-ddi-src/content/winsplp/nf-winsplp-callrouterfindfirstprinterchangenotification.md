---
UID : NF:winsplp.CallRouterFindFirstPrinterChangeNotification
title : CallRouterFindFirstPrinterChangeNotification function
author : windows-driver-content
description : "."
old-location : print\callrouterfindfirstprinterchangenotification.htm
old-project : print
ms.assetid : 7B974255-2FCB-4EFE-B33F-9856E0A09FC4
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : winsplp/CallRouterFindFirstPrinterChangeNotification, CallRouterFindFirstPrinterChangeNotification, CallRouterFindFirstPrinterChangeNotification function [Print Devices], print.callrouterfindfirstprinterchangenotification
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : winsplp.h
req.include-header : 
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
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : NOTIFICATION_CONFIG_FLAGS
req.product : Windows 10 or later.
---


# CallRouterFindFirstPrinterChangeNotification function


## Syntax

````
DWORD WINAPI CallRouterFindFirstPrinterChangeNotification(
  _In_ HANDLE                  hPrinterRPC,
       DWORD                   fdwFilterFlags,
       DWORD                   fdwOptions,
  _In_ HANDLE                  hNotify,
  _In_ PPRINTER_NOTIFY_OPTIONS pPrinterNotifyOptions
);
````

## Parameters

`hPrinterRPC`



`fdwFilterFlags`



`fdwOptions`



`hNotify`



`pPrinterNotifyOptions`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | winsplp.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |