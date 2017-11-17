---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETREQUESTATTRIBUTES
title: PFN_WDFDEVICEINITSETREQUESTATTRIBUTES
author: windows-driver-content
description: 
ms.assetid: 80b8c4e4-6ea2-4636-9807-82cd52ef7892
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# PFN_WDFDEVICEINITSETREQUESTATTRIBUTES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETREQUESTATTRIBUTES PfnWdfdeviceinitsetrequestattributes; 

// Definition

WDFAPI PfnWdfdeviceinitsetrequestattributes 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_OBJECT_ATTRIBUTES RequestAttributes
)
{...}

PFN_WDFDEVICEINITSETREQUESTATTRIBUTES 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param RequestAttributes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also