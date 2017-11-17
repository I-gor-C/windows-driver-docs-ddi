---
UID: NC.ucxusbdevice.EVT_UCX_USBDEVICE_RESUME
title: EVT_UCX_USBDEVICE_RESUME
author: windows-driver-content
description: 
ms.assetid: 0698c376-7f96-43f1-968d-54b2374d2ca6
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

# EVT_UCX_USBDEVICE_RESUME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_USBDEVICE_RESUME EvtUcxUsbdeviceResume; 

// Definition

VOID EvtUcxUsbdeviceResume 
(
	UCXCONTROLLER UcxController
	UCXUSBDEVICE UcxUsbDevice
)
{...}

EVT_UCX_USBDEVICE_RESUME PFN_UCX_USBDEVICE_RESUME


```

## -parameters

### -param UcxController: 
### -param UcxUsbDevice: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also