---
UID: NC.ucxusbdevice.EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD
title: EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD
author: windows-driver-content
description: 
ms.assetid: 94d8fefd-bf4e-427e-a5e7-a343b00216ba
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

# EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD EvtUcxUsbdeviceDefaultEndpointAdd; 

// Definition

NTSTATUS EvtUcxUsbdeviceDefaultEndpointAdd 
(
	UCXCONTROLLER UcxController
	UCXUSBDEVICE UcxUsbDevice
	ULONG MaxPacketSize
	PUCXENDPOINT_INIT UcxEndpointInit
)
{...}

EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD PFN_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD


```

## -parameters

### -param UcxController: 
### -param UcxUsbDevice: 
### -param MaxPacketSize: 
### -param UcxEndpointInit: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also