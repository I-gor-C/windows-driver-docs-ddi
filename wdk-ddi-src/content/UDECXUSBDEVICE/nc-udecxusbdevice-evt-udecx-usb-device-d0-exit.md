---
UID: NC.udecxusbdevice.EVT_UDECX_USB_DEVICE_D0_EXIT
title: EVT_UDECX_USB_DEVICE_D0_EXIT
author: windows-driver-content
description: 
ms.assetid: 55b0a890-20b9-4457-95b3-dabea1bc31f2
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

# EVT_UDECX_USB_DEVICE_D0_EXIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UDECX_USB_DEVICE_D0_EXIT EvtUdecxUsbDeviceD0Exit; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtUdecxUsbDeviceD0Exit 
(
	WDFDEVICE UdecxWdfDevice
	UDECXUSBDEVICE UdecxUsbDevice
	UDECX_USB_DEVICE_WAKE_SETTING WakeSetting
)
{...}

EVT_UDECX_USB_DEVICE_D0_EXIT PFN_UDECX_USB_DEVICE_D0_EXIT


```

## -parameters

### -param UdecxWdfDevice: 
### -param UdecxUsbDevice: 
### -param WakeSetting: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also