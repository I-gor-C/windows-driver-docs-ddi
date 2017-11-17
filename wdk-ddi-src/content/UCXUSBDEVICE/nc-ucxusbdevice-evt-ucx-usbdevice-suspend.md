---
UID: NC.ucxusbdevice.EVT_UCX_USBDEVICE_SUSPEND
title: EVT_UCX_USBDEVICE_SUSPEND
author: windows-driver-content
description: 
ms.assetid: 1bb61994-2996-466e-a58c-f4ce347b5064
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxusbdevice.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# EVT_UCX_USBDEVICE_SUSPEND callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_USBDEVICE_SUSPEND EvtUcxUsbdeviceSuspend; 

// Definition

VOID EvtUcxUsbdeviceSuspend 
(
	UCXCONTROLLER UcxController
	UCXUSBDEVICE UcxUsbDevice
)
{...}

EVT_UCX_USBDEVICE_SUSPEND PFN_UCX_USBDEVICE_SUSPEND


```

## -parameters

### -param UcxController: 
### -param UcxUsbDevice: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also