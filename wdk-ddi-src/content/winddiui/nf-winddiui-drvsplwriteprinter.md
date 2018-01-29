---
UID : NF:winddiui.DrvSplWritePrinter
title : DrvSplWritePrinter function
author : windows-driver-content
description : .
old-location : print\drvsplwriteprinter.htm
old-project : print
ms.assetid : c42bb90a-3c38-4c0c-b523-10e740a027c4
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : winddiui/DrvSplWritePrinter, print_interface-graphics_a59ea0df-c5d8-4a84-8b57-21dfa4f382c4.xml, DrvSplWritePrinter function [Print Devices], print.drvsplwriteprinter, DrvSplWritePrinter
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : winddiui.h
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
req.typenames : "*PWINBIO_VERSION, WINBIO_VERSION"
req.product : Windows 10 or later.
---


# DrvSplWritePrinter function


## Syntax

````
BOOL WINAPI DrvSplWritePrinter(
   HANDLE  hDriver,
   LPVOID  pBuf,
   DWORD   cbBuf,
   LPDWORD pcWritten
);
````

## Parameters

`hDriver`



`pBuf`



`cbBuf`



`pcWritten`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | winddiui.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |