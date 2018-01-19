---
UID : NF:winddiui.DrvSplEndPage
title : DrvSplEndPage function
author : windows-driver-content
description : .
old-location : print\drvsplendpage.htm
old-project : print
ms.assetid : 09c3db82-7890-48c8-a91f-3d1f3f01ef84
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : DrvSplEndPage
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
req.alt-api : DrvSplEndPage
req.alt-loc : winddiui.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : WINBIO_VERSION, *PWINBIO_VERSION
req.product : Windows 10 or later.
---


# DrvSplEndPage function


## Syntax

````
BOOL WINAPI DrvSplEndPage(
   HANDLE hDriver
);
````

## Parameters

`hDriver`




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