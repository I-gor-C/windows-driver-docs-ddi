---
UID : NC:dispmprt.DXGKDDI_RESET_DEVICE
title : DXGKDDI_RESET_DEVICE
author : windows-driver-content
description : The DxgkDdiResetDevice function sets a display adapter to VGA character mode (80 x 50).
old-location : display\dxgkddiresetdevice.htm
old-project : display
ms.assetid : e757e63d-6d78-4b20-9471-290f56c1bcde
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.dxgkddiresetdevice, DxgkDdiResetDevice callback function [Display Devices], DxgkDdiResetDevice, DXGKDDI_RESET_DEVICE, DXGKDDI_RESET_DEVICE, dispmprt/DxgkDdiResetDevice, DmFunctions_70e9fe99-65be-47a5-bb9a-fac4e10d3ae9.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : dispmprt.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
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
req.irql : Any level (see Remarks section)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PSYMBOL_INFO_EX, SYMBOL_INFO_EX"
---


# DXGKDDI_RESET_DEVICE function
The <i>DxgkDdiResetDevice</i> function sets a display adapter to VGA character mode (80 x 50).

## Syntax

```
DXGKDDI_RESET_DEVICE DxgkddiResetDevice;

void DxgkddiResetDevice(
  IN_CONST_PVOID MiniportDeviceContext
)
{...}
```

## Parameters

`MiniportDeviceContext`

A handle to a context block associated with a display adapter. The display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_add_device.md">DxgkDdiAddDevice</a> function previously provided this handle to the DirectX graphics kernel subsystem.


## Return Value

None

## Remarks

The HAL calls this function so it can display information on the screen during hibernation, bug checks, and the like.

<i>DxgkDdiResetDevice</i> can be called at any IRQL, so it must be in nonpageable memory. <i>DxgkDdiResetDevice</i> must not call any code that is in pageable memory and must not manipulate any data that is in pageable memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dispmprt.h |
| **Library** |  |
| **IRQL** | Any level (see Remarks section) |
| **DDI compliance rules** |  |