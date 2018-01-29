---
UID : NF:ntddk.PsIsHostSilo
title : PsIsHostSilo function
author : windows-driver-content
description : This routine will check if the supplied Silo is the host silo.
old-location : kernel\psishostsilo.htm
old-project : kernel
ms.assetid : 4C6D85F2-C9B8-425D-A307-5609E1C1465B
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : ntddk/PsIsHostSilo, PsIsHostSilo routine [Kernel-Mode Driver Architecture], kernel.psishostsilo, PsIsHostSilo
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
req.typenames : "*PWHEA_RAW_DATA_FORMAT, WHEA_RAW_DATA_FORMAT"
---


# PsIsHostSilo function
This routine  will check if the supplied <i>Silo</i> is the host silo.

## Syntax

````
BOOLEAN PsIsHostSilo(
  _In_ PESILO Silo
);
````

## Parameters

`Silo`

The  silo to evaluate.


## Return Value

Returns <b>true</b> if the specified silo is the host silo; otherwise, <b>false</b>.


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