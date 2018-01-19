---
UID : NC:d3dkmthk.PDXGK_POWER_NOTIFICATION
title : PDXGK_POWER_NOTIFICATION
author : windows-driver-content
description : A callback providing notification that the graphics device will be undergoing a device power state transition.
old-location : display\pdxgk_power_notification.htm
old-project : display
ms.assetid : 11549B4E-7929-4957-9775-BF8AAF501D45
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
req.alt-api : "*PDXGK_POWER_NOTIFICATION"
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


# PDXGK_POWER_NOTIFICATION callback function
A callback providing notification that the graphics device will be undergoing a device power state transition.

## Syntax

```
PDXGK_POWER_NOTIFICATION PdxgkPowerNotification;

void PdxgkPowerNotification(
  PVOID GraphicsDeviceHandle,
  DEVICE_POWER_STATE NewGrfxPowerState,
  BOOLEAN PreNotification,
  PVOID PrivateHandle
)
{...}
```

## Parameters

`GraphicsDeviceHandle`

A handle to the graphics device.

`NewGrfxPowerState`

Indicates the new graphics power state.

`PreNotification`

Indicates that a notification should be provided.

`PrivateHandle`




## Return Value

This callback function does not return a value.


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