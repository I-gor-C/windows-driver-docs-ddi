---
UID : NF:printoem.OEMStrokeAndFillPath
title : OEMStrokeAndFillPath function
author : windows-driver-content
description : The OEMStrokeAndFillPath function concurrently strokes and fills a path.
old-location : print\oemstrokeandfillpath.htm
old-project : print
ms.assetid : f8a2df5d-426f-4872-8d54-55895c4fe6e3
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : OEMStrokeAndFillPath function [Print Devices], OEMStrokeAndFillPath, print.oemstrokeandfillpath, printoem/OEMStrokeAndFillPath, print_unidrv-pscript_rendering_e370d4e7-4593-46c7-87dd-93c963400290.xml
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


# OEMStrokeAndFillPath function
The <code>OEMStrokeAndFillPath</code> function concurrently strokes and fills a path.

## Syntax

````
BOOL APIENTRY OEMStrokeAndFillPath(
   SURFOBJ   *pso,
   PATHOBJ   *ppo,
   CLIPOBJ   *pco,
   XFORMOBJ  *pxo,
   BRUSHOBJ  *pboStroke,
   LINEATTRS *plineattrs,
   BRUSHOBJ  *pboFill,
   POINTL    *pptlBrushOrg,
   MIX       mixFill,
   FLONG     flOptions
);
````

## Parameters

`pso`



`ppo`



`pco`



`pxo`



`pboStroke`



`plineattrs`



`pboFill`



`pptlBrushOrg`



`mixFill`



`flOptions`




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