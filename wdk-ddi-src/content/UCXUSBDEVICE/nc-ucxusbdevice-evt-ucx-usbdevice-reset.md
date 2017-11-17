---
UID: NC.ucxusbdevice.EVT_UCX_USBDEVICE_RESET
title: EVT_UCX_USBDEVICE_RESET
author: windows-driver-content
description: 
ms.assetid: da5ce221-7ccb-4742-a426-185e03cf2acc
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

# EVT_UCX_USBDEVICE_RESET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_USBDEVICE_RESET EvtUcxUsbdeviceReset; 

// Definition

VOID EvtUcxUsbdeviceReset 
(
	UCXCONTROLLER UcxController
	WDFREQUEST Request
)
{...}

EVT_UCX_USBDEVICE_RESET PFN_UCX_USBDEVICE_RESET


```

## -parameters

### -param UcxController: 
### -param Request: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also