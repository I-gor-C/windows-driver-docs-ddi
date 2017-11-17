---
UID: NC.udecxusbdevice.EVT_UDECX_USB_DEVICE_POST_ENUMERATION_RESET
title: EVT_UDECX_USB_DEVICE_POST_ENUMERATION_RESET
author: windows-driver-content
description: 
ms.assetid: 09fe2056-84a7-4380-a324-7828ad0452b7
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxusbdevice.h
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

# EVT_UDECX_USB_DEVICE_POST_ENUMERATION_RESET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UDECX_USB_DEVICE_POST_ENUMERATION_RESET EvtUdecxUsbDevicePostEnumerationReset; 

// Definition

_IRQL_requires_same_ VOID EvtUdecxUsbDevicePostEnumerationReset 
(
	WDFDEVICE UdecxWdfDevice
	UDECXUSBDEVICE UdecxUsbDevice
	WDFREQUEST Request
	BOOLEAN AllDevicesReset
)
{...}

EVT_UDECX_USB_DEVICE_POST_ENUMERATION_RESET PFN_UDECX_USB_DEVICE_POST_ENUMERATION_RESET


```

## -parameters

### -param UdecxWdfDevice: 
### -param UdecxUsbDevice: 
### -param Request: 
### -param AllDevicesReset: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also