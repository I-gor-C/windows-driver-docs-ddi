---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICESENDCONTROLTRANSFERSYNCHRONOUSLY
title: PFN_WDFUSBTARGETDEVICESENDCONTROLTRANSFERSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: 339e694a-f305-4764-9633-1d7e5b66e65d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBTARGETDEVICESENDCONTROLTRANSFERSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICESENDCONTROLTRANSFERSYNCHRONOUSLY PfnWdfusbtargetdevicesendcontroltransfersynchronously; 

// Definition

WDFAPI PfnWdfusbtargetdevicesendcontroltransfersynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	WDFREQUEST Request
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
	PWDF_USB_CONTROL_SETUP_PACKET SetupPacket
	PWDF_MEMORY_DESCRIPTOR MemoryDescriptor
	PULONG BytesTransferred
)
{...}

PFN_WDFUSBTARGETDEVICESENDCONTROLTRANSFERSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Request: 
### -param RequestOptions: 
### -param SetupPacket: 
### -param MemoryDescriptor: 
### -param BytesTransferred: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also