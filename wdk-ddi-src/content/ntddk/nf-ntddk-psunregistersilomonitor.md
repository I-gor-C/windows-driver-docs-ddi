---
UID : NF:ntddk.PsUnregisterSiloMonitor
title : PsUnregisterSiloMonitor function
author : windows-driver-content
description : This routine unregisters a server silo monitor.
old-location : kernel\psunregistersilomonitor.htm
old-project : kernel
ms.assetid : B1B85AD5-F626-4177-8218-428B617A97F6
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : ntddk/PsUnregisterSiloMonitor, PsUnregisterSiloMonitor routine [Kernel-Mode Driver Architecture], PsUnregisterSiloMonitor, kernel.psunregistersilomonitor
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntddk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1607
req.target-min-winversvr : Windows Server 2016
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
req.typenames : WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# PsUnregisterSiloMonitor function
This routine unregisters a server silo monitor.

## Syntax

````
void PsUnregisterSiloMonitor(
  _In_ _Post_invalid_ PSILO_MONITOR Monitor
);
````

## Parameters

`Monitor`

The server silo monitor to unregister.


## Return Value

This routine does not return a value.

## Remarks

The monitor will not receive further notifications after this routine completes.
    
If the monitor allocated a silo context slot, this routine will not complete until all silo contexts have been removed from slot.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |