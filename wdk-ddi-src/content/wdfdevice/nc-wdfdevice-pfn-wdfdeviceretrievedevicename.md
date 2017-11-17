---
UID: NC.wdfdevice.PFN_WDFDEVICERETRIEVEDEVICENAME
title: PFN_WDFDEVICERETRIEVEDEVICENAME
author: windows-driver-content
description: 
ms.assetid: daaf2b91-3868-41f8-9738-bc04942dcc14
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

# PFN_WDFDEVICERETRIEVEDEVICENAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICERETRIEVEDEVICENAME PfnWdfdeviceretrievedevicename; 

// Definition

WDFAPI PfnWdfdeviceretrievedevicename 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	WDFSTRING String
)
{...}

PFN_WDFDEVICERETRIEVEDEVICENAME 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param String: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also