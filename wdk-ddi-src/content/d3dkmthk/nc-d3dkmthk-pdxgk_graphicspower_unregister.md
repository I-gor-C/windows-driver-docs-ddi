---
UID : NC:d3dkmthk.PDXGK_GRAPHICSPOWER_UNREGISTER
title : PDXGK_GRAPHICSPOWER_UNREGISTER
author : windows-driver-content
description : A callback to un-register itself with the graphics driver.
old-location : display\pdxgk_graphicspower_unregister.htm
old-project : display
ms.assetid : A925D5D3-EF79-4C14-BE1C-188C255DDF8E
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_TARGETMODE_DETAIL_TIMING, DXGK_TARGETMODE_DETAIL_TIMING
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dkmthk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PDXGK_GRAPHICSPOWER_UNREGISTER
req.alt-loc : d3dkmthk.h
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
req.typenames : DXGK_TARGETMODE_DETAIL_TIMING
---


# PDXGK_GRAPHICSPOWER_UNREGISTER callback function
A callback to un-register itself with the graphics driver.

## Syntax

```
PDXGK_GRAPHICSPOWER_UNREGISTER PdxgkGraphicspowerUnregister;

NTSTATUS PdxgkGraphicspowerUnregister(
  PVOID DeviceHandle,
  PVOID PrivateHandle
)
{...}
```

## Parameters

`DeviceHandle`

A handle to the graphics device.

`PrivateHandle`

A handle to the graphics device.


## Return Value

Return STATUS_SUCCESS if the call succeeds.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |