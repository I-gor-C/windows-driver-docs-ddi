---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCYCLEPORT
title: PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCYCLEPORT
author: windows-driver-content
description: 
ms.assetid: 76808967-a293-4c17-8206-4496c765be4e
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

# PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCYCLEPORT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCYCLEPORT PfnWdfusbtargetdeviceformatrequestforcycleport; 

// Definition

WDFAPI PfnWdfusbtargetdeviceformatrequestforcycleport 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	WDFREQUEST Request
)
{...}

PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCYCLEPORT 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also