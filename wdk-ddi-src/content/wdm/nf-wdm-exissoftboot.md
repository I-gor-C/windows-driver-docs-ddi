---
UID : NF:wdm.ExIsSoftBoot
title : ExIsSoftBoot function
author : windows-driver-content
description : Determines whether the system has gone through a soft restart.
old-location : kernel\exissoftboot.htm
old-project : kernel
ms.assetid : ff67bc75-b424-4278-b979-f67d118232aa
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : ExIsSoftBoot function [Kernel-Mode Driver Architecture], ExIsSoftBoot, wdm/ExIsSoftBoot, kernel.exissoftboot
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdm.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
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
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe (kernel mode)
req.irql : <=APC_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# ExIsSoftBoot function
Determines whether the system has gone through a soft restart.

## Syntax

````
 BOOLEAN  ExIsSoftBoot(
   VOID 
);
````

## Parameters

This function has no parameters.

## Return Value

TRUE indicates a soft restart; FALSE otherwise.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h |
| **Library** |  |
| **IRQL** | <=APC_LEVEL |
| **DDI compliance rules** |  |