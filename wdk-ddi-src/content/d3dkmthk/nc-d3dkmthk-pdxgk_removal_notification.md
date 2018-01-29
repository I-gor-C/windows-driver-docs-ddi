---
UID : NC:d3dkmthk.PDXGK_REMOVAL_NOTIFICATION
title : PDXGK_REMOVAL_NOTIFICATION
author : windows-driver-content
description : A callback indicating that the graphics device is being removed.
old-location : display\pdxgk_removal_notification.htm
old-project : display
ms.assetid : F9AA5859-8E8A-491D-B149-F42E418A64DC
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.pdxgk_removal_notification, *PDXGK_REMOVAL_NOTIFICATION callback function [Display Devices], *PDXGK_REMOVAL_NOTIFICATION, d3dkmthk/*PDXGK_REMOVAL_NOTIFICATION
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_TARGETMODE_DETAIL_TIMING
---


# PDXGK_REMOVAL_NOTIFICATION callback function
A callback indicating that the graphics device is being removed.

## Syntax

```
PDXGK_REMOVAL_NOTIFICATION PdxgkRemovalNotification;

void PdxgkRemovalNotification(
  PVOID GraphicsDeviceHandle,
  PVOID PrivateHandle
)
{...}
```

## Parameters

`GraphicsDeviceHandle`

A handle to the graphics device.

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