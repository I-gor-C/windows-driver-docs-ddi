---
UID : NF:printoem.OEMBitBlt
title : OEMBitBlt function
author : windows-driver-content
description : The OEMBitBlt function provides general bit-block transfer capabilities between device-managed surfaces, between GDI-managed standard-format bitmaps, or between a device-managed surface and a GDI-managed standard-format bitmap.
old-location : print\oembitblt.htm
old-project : print
ms.assetid : d47e1bdb-2c91-4f73-b742-5312d989781a
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : OEMBitBlt
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
req.alt-api : OEMBitBlt
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


# OEMBitBlt function
The <code>OEMBitBlt</code> function provides general bit-block transfer capabilities between <a href="wdkgloss.d#wdkgloss.device-managed_surface#wdkgloss.device-managed_surface"><i>device-managed surfaces</i></a>, between GDI-managed standard-format bitmaps, or between a device-managed surface and a GDI-managed standard-format bitmap.

## Syntax

````
BOOL  APIENTRY OEMBitBlt(
   SURFOBJ  *psoTrg,
   SURFOBJ  *psoSrc,
   SURFOBJ  *psoMask,
   CLIPOBJ  *pco,
   XLATEOBJ *pxlo,
   RECTL    *prclTrg,
   POINTL   *pptlSrc,
   POINTL   *pptlMask,
   BRUSHOBJ *pbo,
   POINTL   *pptlBrush,
   ROP4     rop4
);
````

## Parameters

`psoTrg`



`psoSrc`



`psoMask`



`pco`



`pxlo`



`prclTrg`



`pptlSrc`



`pptlMask`



`pbo`



`pptlBrush`



`rop4`




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