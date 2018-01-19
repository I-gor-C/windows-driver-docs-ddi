---
UID : NF:irb.AtaPortDebugPrint
title : AtaPortDebugPrint function
author : windows-driver-content
description : The AtaPortDebugPrint routine passes a message string to the kernel debugger for the debugger to print.
old-location : storage\ataportdebugprint.htm
old-project : storage
ms.assetid : 2a93d30f-4aa0-46b9-b9c7-cc15c62f3053
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : AtaPortDebugPrint
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : irb.h
req.include-header : Ata.h, Irb.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : AtaPortDebugPrint
req.alt-loc : ataport.lib,ataport.dll,pciidex.lib,pciidex.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ataport.lib; Pciidex.lib
req.dll : 
req.irql : 
req.typenames : IDE_POWER_STATE
---


# AtaPortDebugPrint function
The <b>AtaPortDebugPrint</b> routine passes a message string to the kernel debugger for the debugger to print.

## Syntax

````
VOID AtaPortDebugPrint(
   ULONG  DebugPrintLevel,
   PCCHAR DebugMessage
);
````

## Parameters

`DebugPrintLevel`

Determines how much debug information to display.

`DebugMessage`

A pointer to the debug message to display.

``




## Return Value

None

## Remarks

The verbosity of debug output is determined by <i>DebugPrintLevel</i> and a port driver-specific mask. Use the <b>nt!kd_idep_mask</b> command to set the desired level of verbosity. For more information about the kernel debugger, see the <a href="https://msdn.microsoft.com/e2490442-9d90-454b-95e0-db8c5d7fa19a">Using a Debugger</a> topic </p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | irb.h (include Ata.h, Irb.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |