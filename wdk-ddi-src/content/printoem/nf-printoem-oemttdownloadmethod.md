---
UID : NF:printoem.OEMTTDownloadMethod
title : OEMTTDownloadMethod function
author : windows-driver-content
description : OEMTTDownloadMethod function
old-location : print\oemttdownloadmethod.htm
old-project : print
ms.assetid : 0807622e-0ed9-419a-8917-bba4b1b2a475
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : printoem/OEMTTDownloadMethod, print.oemttdownloadmethod, print_obsoletefunctions_cae8b020-17a2-4345-8d48-3138eeba2a1d.xml, OEMTTDownloadMethod, OEMTTDownloadMethod function [Print Devices]
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


# OEMTTDownloadMethod function


## Syntax

````
DWORD APIENTRY OEMTTDownloadMethod(
   PDEVOBJ     pdevobj,
   PUNIFONTOBJ pUFObj
);
````

## Parameters

`pdevobj`



`pUFObj`




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