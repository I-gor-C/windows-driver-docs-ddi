---
UID: NC.udecxusbdevice.EVT_UDECX_USB_DEVICE_D0_ENTRY
title: EVT_UDECX_USB_DEVICE_D0_ENTRY
author: windows-driver-content
description: 
ms.assetid: b32cb4cb-c5cb-4928-aea5-867a736c609f
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

# EVT_UDECX_USB_DEVICE_D0_ENTRY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UDECX_USB_DEVICE_D0_ENTRY EvtUdecxUsbDeviceD0Entry; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtUdecxUsbDeviceD0Entry 
(
	WDFDEVICE UdecxWdfDevice
	UDECXUSBDEVICE UdecxUsbDevice
)
{...}

EVT_UDECX_USB_DEVICE_D0_ENTRY PFN_UDECX_USB_DEVICE_D0_ENTRY


```

## -parameters

### -param UdecxWdfDevice: 
### -param UdecxUsbDevice: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also