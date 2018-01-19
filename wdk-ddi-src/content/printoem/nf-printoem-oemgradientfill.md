---
UID : NF:printoem.OEMGradientFill
title : OEMGradientFill function
author : windows-driver-content
description : The OEMGradientFill function shades the specified primitives.
old-location : print\oemgradientfill.htm
old-project : print
ms.assetid : 8a25d44b-c83b-4454-858b-117dbb6cc4b7
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : OEMGradientFill
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
req.alt-api : OEMGradientFill
req.alt-loc : printoem.h
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
req.typenames : STDVARIABLEINDEX
req.product : Windows 10 or later.
---


# OEMGradientFill function
The <code>OEMGradientFill</code> function shades the specified primitives.

## Syntax

````
BOOL APIENTRY OEMGradientFill(
   SURFOBJ   *psoDest,
   CLIPOBJ   *pco,
   XLATEOBJ  *pxlo,
   TRIVERTEX *pVertex,
   ULONG     nVertex,
   PVOID     pMesh,
   ULONG     nMesh,
   RECTL     *prclExtents,
   POINTL    *pptlDitherOrg,
   ULONG     ulMode
);
````

## Parameters

`psoDest`



`pco`



`pxlo`



`pVertex`



`nVertex`



`pMesh`



`nMesh`



`prclExtents`



`pptlDitherOrg`



`ulMode`




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