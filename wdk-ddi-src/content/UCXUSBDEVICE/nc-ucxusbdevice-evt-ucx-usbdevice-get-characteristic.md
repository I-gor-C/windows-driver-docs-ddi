---
UID: NC.ucxusbdevice.EVT_UCX_USBDEVICE_GET_CHARACTERISTIC
title: EVT_UCX_USBDEVICE_GET_CHARACTERISTIC
author: windows-driver-content
description: 
ms.assetid: e212a873-817c-44f7-8c10-fd209556ff97
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

# EVT_UCX_USBDEVICE_GET_CHARACTERISTIC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_USBDEVICE_GET_CHARACTERISTIC EvtUcxUsbdeviceGetCharacteristic; 

// Definition

NTSTATUS EvtUcxUsbdeviceGetCharacteristic 
(
	UCXCONTROLLER UcxController
	UCXUSBDEVICE UcxUsbDevice
	PUCX_USBDEVICE_CHARACTERISTIC UcxUsbDeviceCharacteristic
)
{...}

EVT_UCX_USBDEVICE_GET_CHARACTERISTIC PFN_UCX_USBDEVICE_GET_CHARACTERISTIC


```

## -parameters

### -param UcxController: 
### -param UcxUsbDevice: 
### -param UcxUsbDeviceCharacteristic: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also