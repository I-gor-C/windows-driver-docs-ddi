---
UID: NC.wdfrequest.PFN_WDFREQUESTFORWARDTOPARENTDEVICEIOQUEUE
title: PFN_WDFREQUESTFORWARDTOPARENTDEVICEIOQUEUE
author: windows-driver-content
description: 
ms.assetid: 740ab1f0-e318-418a-892c-c794b89f7810
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfrequest.h
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

# PFN_WDFREQUESTFORWARDTOPARENTDEVICEIOQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTFORWARDTOPARENTDEVICEIOQUEUE PfnWdfrequestforwardtoparentdeviceioqueue; 

// Definition

WDFAPI PfnWdfrequestforwardtoparentdeviceioqueue 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	WDFQUEUE ParentDeviceQueue
	PWDF_REQUEST_FORWARD_OPTIONS ForwardOptions
)
{...}

PFN_WDFREQUESTFORWARDTOPARENTDEVICEIOQUEUE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param ParentDeviceQueue: 
### -param ForwardOptions: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also