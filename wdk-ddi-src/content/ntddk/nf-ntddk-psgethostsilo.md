---
UID : NF:ntddk.PsGetHostSilo
title : PsGetHostSilo function
author : windows-driver-content
description : This routine returns the host silo.
old-location : kernel\psgethostsilo.htm
old-project : kernel
ms.assetid : 0B78562C-25DD-4CF2-9804-6DBEDE8B5F69
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : PsGetHostSilo routine [Kernel-Mode Driver Architecture], kernel.psgethostsilo, ntddk/PsGetHostSilo, PsGetHostSilo
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


# PsGetHostSilo function
This routine returns the host silo.

## Syntax

````
PESILO PsGetHostSilo(void);
````

## Parameters

This function has no parameters.

## Return Value

The host silo.


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