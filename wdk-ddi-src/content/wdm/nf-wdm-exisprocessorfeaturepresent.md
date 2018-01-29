---
UID : NF:wdm.ExIsProcessorFeaturePresent
title : ExIsProcessorFeaturePresent function
author : windows-driver-content
description : The ExIsProcessorFeaturePresent routine queries for the existence of a specified processor feature.
old-location : kernel\exisprocessorfeaturepresent.htm
old-project : kernel
ms.assetid : d8c4d1d7-3510-48c4-b1a6-062157f4632e
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : kernel.exisprocessorfeaturepresent, wdm/ExIsProcessorFeaturePresent, ExIsProcessorFeaturePresent routine [Kernel-Mode Driver Architecture], k102_4dccea04-24a3-4465-97bc-67bb58cee3b1.xml, ExIsProcessorFeaturePresent
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows 2000.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : IrqlExPassive, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# ExIsProcessorFeaturePresent function
The <b>ExIsProcessorFeaturePresent</b> routine queries for the existence of a specified processor feature.

## Syntax

````
BOOLEAN ExIsProcessorFeaturePresent(
  _In_ ULONG ProcessorFeature
);
````

## Parameters

`ProcessorFeature`

Specifies one of the following constant values:


## Return Value

<b>ExIsProcessorFeaturePresent</b> returns <b>TRUE</b> if the specified processor feature is present; otherwise, it returns <b>FALSE</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** | IrqlExPassive, PowerIrpDDis, HwStorPortProhibitedDDIs |