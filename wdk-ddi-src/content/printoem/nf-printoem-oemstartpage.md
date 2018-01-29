---
UID : NF:printoem.OEMStartPage
title : OEMStartPage function
author : windows-driver-content
description : The OEMStartPage function is called by GDI when it is ready to start sending the contents of a physical page to the driver for rendering.
old-location : print\oemstartpage.htm
old-project : print
ms.assetid : 86cee994-2dfe-4eaf-906b-ce6d9051399e
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : OEMStartPage function [Print Devices], printoem/OEMStartPage, print.oemstartpage, OEMStartPage, print_unidrv-pscript_rendering_df5731ee-40be-45e1-8dbb-b7893ec27622.xml
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


# OEMStartPage function
The <code>OEMStartPage</code> function is called by GDI when it is ready to start sending the contents of a physical page to the driver for rendering.

## Syntax

````
BOOL APIENTRY OEMStartPage(
   SURFOBJ *pso
);
````

## Parameters

`pso`




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