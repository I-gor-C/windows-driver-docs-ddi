---
UID : NC:61883.PCMP_NOTIFY_ROUTINE
title : PCMP_NOTIFY_ROUTINE
author : windows-driver-content
description : This routine is called for plug notification.
old-location : ieee\pcmp_notify_routine.htm
old-project : IEEE
ms.assetid : 0576D73A-0A36-4AB7-952C-19B56FD246D8
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _TOPOLOGY_MAP, TOPOLOGY_MAP, *PTOPOLOGY_MAP
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : 61883.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : CmpNotifyRoutine
req.alt-loc : 61883.h
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
req.typenames : TOPOLOGY_MAP, *PTOPOLOGY_MAP
---


# PCMP_NOTIFY_ROUTINE callback function
This routine is called for plug notification.

## Syntax

```
PCMP_NOTIFY_ROUTINE PcmpNotifyRoutine;

void PcmpNotifyRoutine(
  PCMP_NOTIFY_INFO NotifyInfo
)
{...}
```

## Parameters

`NotifyInfo`

Specifies the notification information.


## Return Value

This callback does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | 61883.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |