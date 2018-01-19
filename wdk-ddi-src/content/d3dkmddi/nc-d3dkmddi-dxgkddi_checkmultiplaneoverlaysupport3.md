---
UID : NC:d3dkmddi.DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3
title : DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3
author : windows-driver-content
description : The following new function is called to determine whether a specific multi-plane overlay configuration is supported.
old-location : display\dxgkddi_checkmultiplaneoverlaysupport3.htm
old-project : display
ms.assetid : 2EA7E8C4-51E0-4BDE-B69B-1A40FEB82952
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dkmddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3
req.alt-loc : d3dkmddi.h
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
req.typenames : DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 function
The following new function is called to determine whether a specific multi-plane overlay configuration is supported.

## Syntax

```
DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 DxgkddiCheckmultiplaneoverlaysupport3;

NTSTATUS DxgkddiCheckmultiplaneoverlaysupport3(
  IN_CONST_HANDLE hAdapter,
  IN_OUT_PDXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3 pCheckMultiPlaneOverlaySupport
)
{...}
```

## Parameters

`hAdapter`

Identifies the adapter containing the overlay hardware.

`pCheckMultiPlaneOverlaySupport`




## Return Value

DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 returns the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>If the routine has been successfully completed.

## Remarks

The kernel mode driver reports whether the specified configuration is supported.  The kernel mode driver should not raise or lower the available bandwidth in anticipation to this configuration getting set.

This function is always called at PASSIVE level.
</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |