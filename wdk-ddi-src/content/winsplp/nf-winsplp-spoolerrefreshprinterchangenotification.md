---
UID : NF:winsplp.SpoolerRefreshPrinterChangeNotification
title : SpoolerRefreshPrinterChangeNotification function
author : windows-driver-content
description : .
old-location : print\spoolerrefreshprinterchangenotification.htm
old-project : print
ms.assetid : 86D8D605-3620-4F43-B4A5-6AF568265E92
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : SpoolerRefreshPrinterChangeNotification
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
req.alt-api : SpoolerRefreshPrinterChangeNotification
req.alt-loc : Winsplp.h
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
req.typenames : NOTIFICATION_CONFIG_FLAGS
req.product : Windows 10 or later.
---


# SpoolerRefreshPrinterChangeNotification function


## Syntax

````
BOOL WINAPI SpoolerRefreshPrinterChangeNotification(
  _In_        HANDLE                    hPrinter,
  _In_        DWORD                     dwColor,
  _In_        PPRINTER_NOTIFY_OPTIONS   pOptions,
  _Inout_opt_ PPRINTER_NOTIFY_INFO      ppInfo
);
````

## Parameters

`hPrinter`



`dwColor`



`pOptions`



`ppInfo`




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