---
UID : NF:printoem.OEMDownloadFontHeader
title : OEMDownloadFontHeader function
author : windows-driver-content
description : OEMDownloadFontHeader function
old-location : print\oemdownloadfontheader.htm
old-project : print
ms.assetid : 3865a206-840c-4acf-97be-86764cf522db
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : OEMDownloadFontHeader function [Print Devices], printoem/OEMDownloadFontHeader, OEMDownloadFontHeader, print.oemdownloadfontheader, print_obsoletefunctions_733001dd-14a7-43a6-b386-5be4b514ae0b.xml
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


# OEMDownloadFontHeader function


## Syntax

````
DWORD APIENTRY OEMDownloadFontHeader(
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