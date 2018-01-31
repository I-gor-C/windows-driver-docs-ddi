---
UID : NF:printoem.OEMUpdateExternalFonts
title : OEMUpdateExternalFonts function
author : windows-driver-content
description : OEMUpdateExternalFonts function
old-location : print\oemupdateexternalfonts.htm
old-project : print
ms.assetid : 04b0a34f-0aec-4f42-8a2e-a29168a699e3
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : OEMUpdateExternalFonts function [Print Devices], printoem/OEMUpdateExternalFonts, print.oemupdateexternalfonts, OEMUpdateExternalFonts, print_obsoletefunctions_f42779e4-8a2d-45eb-801c-67e7e69cb96a.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : printoem.h
req.include-header : Printoem.h
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
req.typenames : STDVARIABLEINDEX
req.product : Windows 10 or later.
---


# OEMUpdateExternalFonts function


## Syntax

````
BOOL APIENTRY OEMUpdateExternalFonts(
   HANDLE hPrinter,
   HANDLE hHeap,
   PWSTR  pwstrCartridges
);
````

## Parameters

`hPrinter`



`hHeap`



`pwstrCartridges`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | printoem.h (include Printoem.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |