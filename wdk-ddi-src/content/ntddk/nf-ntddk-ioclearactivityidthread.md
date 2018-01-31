---
UID : NF:ntddk.IoClearActivityIdThread
title : IoClearActivityIdThread function
author : windows-driver-content
description : The IoClearActivityIdThread routine clears the activity ID of the current thread.
old-location : kernel\ioclearactivityidthread.htm
old-project : kernel
ms.assetid : 2F69FC2F-C336-4B51-8EFC-0A9AA22121B9
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : IoClearActivityIdThread, ntddk/IoClearActivityIdThread, kernel.ioclearactivityidthread, IoClearActivityIdThread routine [Kernel-Mode Driver Architecture]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntddk.h
req.include-header : Ntddk.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with  Windows 8.
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
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : Any level
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# IoClearActivityIdThread function
The IoClearActivityIdThread routine clears the activity ID of the current thread.

## Syntax

````
void IoClearActivityIdThread(
  _In_ LPCGUID OriginalId
);
````

## Parameters

`OriginalId`

The activity ID that was previously set on the thread.


## Return Value

None.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |
| **Library** |  |
| **IRQL** | Any level |
| **DDI compliance rules** |  |