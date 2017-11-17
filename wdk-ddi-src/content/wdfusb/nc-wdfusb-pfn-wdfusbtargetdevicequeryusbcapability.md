---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICEQUERYUSBCAPABILITY
title: PFN_WDFUSBTARGETDEVICEQUERYUSBCAPABILITY
author: windows-driver-content
description: 
ms.assetid: 8a40aafb-3f72-4706-8570-c11bfd1491dc
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

# PFN_WDFUSBTARGETDEVICEQUERYUSBCAPABILITY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICEQUERYUSBCAPABILITY PfnWdfusbtargetdevicequeryusbcapability; 

// Definition

WDFAPI PfnWdfusbtargetdevicequeryusbcapability 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	CONST GUID
	ULONG CapabilityBufferLength
	PVOID CapabilityBuffer
	PULONG ResultLength
)
{...}

PFN_WDFUSBTARGETDEVICEQUERYUSBCAPABILITY 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param GUID: 
### -param CapabilityBufferLength: 
### -param CapabilityBuffer: 
### -param ResultLength: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also