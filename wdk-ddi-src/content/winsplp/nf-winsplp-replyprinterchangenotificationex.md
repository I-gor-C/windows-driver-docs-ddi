---
UID : NF:winsplp.ReplyPrinterChangeNotificationEx
title : ReplyPrinterChangeNotificationEx function
author : windows-driver-content
description : .
old-location : print\replyprinterchangenotificationex.htm
old-project : print
ms.assetid : A3A906C0-FA96-4008-B904-1DA333B59833
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : winsplp/ReplyPrinterChangeNotificationEx, print.replyprinterchangenotificationex, ReplyPrinterChangeNotificationEx, ReplyPrinterChangeNotificationEx function [Print Devices]
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


# ReplyPrinterChangeNotificationEx function


## Syntax

````
 WINAPI ReplyPrinterChangeNotificationEx(
  _In_  HANDLE    hNotify,
        DWORD     dwColor,
        DWORD     fdwFlags,
  _Out_ PDWORD    pdwResult,
  _In_  PVOID     pPrinterNotifyInfo
);
````

## Parameters

`hNotify`



`dwColor`



`fdwFlags`



`pdwResult`



`pPrinterNotifyInfo`




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