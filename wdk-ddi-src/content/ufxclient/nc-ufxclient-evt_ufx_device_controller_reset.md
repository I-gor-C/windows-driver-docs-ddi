---
UID: NC:ufxclient.EVT_UFX_DEVICE_CONTROLLER_RESET
title: EVT_UFX_DEVICE_CONTROLLER_RESET
author: windows-driver-content
description: The client driver's implementation to reset the function controller to its initial state.
old-location: buses\evt_ufx_device_controller_reset.htm
old-project: usbref
ms.assetid: 37CE6358-68F8-49E2-8B3E-126D5D135ADF
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: EVT_UFX_DEVICE_CONTROLLER_RESET, EvtUfxDeviceControllerReset, EvtUfxDeviceControllerReset callback function [Buses], PFN_UFX_DEVICE_CONTROLLER_RESET, PFN_UFX_DEVICE_CONTROLLER_RESET callback function pointer [Buses], buses.evt_ufx_device_controller_reset, ufxclient/EvtUfxDeviceControllerReset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ufxclient.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	Ufxclient.h
api_name:
-	PFN_UFX_DEVICE_CONTROLLER_RESET
product: Windows
targetos: Windows
req.typenames: UFX_HARDWARE_FAILURE_CONTEXT, *PUFX_HARDWARE_FAILURE_CONTEXT
req.product: Windows 10 or later.
---


# EVT_UFX_DEVICE_CONTROLLER_RESET callback function
The client driver's implementation to reset the function controller to its initial state.

## Syntax

```
EVT_UFX_DEVICE_CONTROLLER_RESET EvtUfxDeviceControllerReset;

void EvtUfxDeviceControllerReset(
  UFXDEVICE ,
  PUFX_HARDWARE_FAILURE_CONTEXT 
)
{...}
```

## Parameters

`Arg1`



`Arg1`




## Return Value

This callback function does not return a value.

## Remarks

The client driver for the function host controller registers its <i>EVT_UFX_DEVICE_CONTROLLER_RESET</i> implementation with the USB function class extension (UFX) by calling the <a href="..\ufxclient\nf-ufxclient-ufxdevicecreate.md">UfxDeviceCreate</a> method.

The client driver indicates completion of this event by calling the <a href="..\ufxclient\nf-ufxclient-ufxdeviceeventcomplete.md">UfxDeviceEventComplete</a> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ufxclient.h |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\ufxclient\nf-ufxclient-ufxdeviceeventcomplete.md">UfxDeviceEventComplete</a>



<a href="..\ufxclient\nf-ufxclient-ufxdevicecreate.md">UfxDeviceCreate</a>