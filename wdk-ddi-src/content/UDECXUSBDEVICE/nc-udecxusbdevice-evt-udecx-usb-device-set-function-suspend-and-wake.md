---
UID: NC.udecxusbdevice.EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE
title: EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE
author: windows-driver-content
description: 
ms.assetid: e4290981-54d1-4489-bd52-e03da1aea6f8
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

# EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE EvtUdecxUsbDeviceSetFunctionSuspendAndWake; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtUdecxUsbDeviceSetFunctionSuspendAndWake 
(
	WDFDEVICE UdecxWdfDevice
	UDECXUSBDEVICE UdecxUsbDevice
	ULONG Interface
	UDECX_USB_DEVICE_FUNCTION_POWER FunctionPower
)
{...}

EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE PFN_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE


```

## -parameters

### -param UdecxWdfDevice: 
### -param UdecxUsbDevice: 
### -param Interface: 
### -param FunctionPower: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also