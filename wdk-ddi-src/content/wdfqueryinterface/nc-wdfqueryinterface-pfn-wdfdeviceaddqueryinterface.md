---
UID: NC.wdfqueryinterface.PFN_WDFDEVICEADDQUERYINTERFACE
title: PFN_WDFDEVICEADDQUERYINTERFACE
author: windows-driver-content
description: 
ms.assetid: c3581161-07eb-4170-9824-c3248a3400f4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfqueryinterface.h
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

# PFN_WDFDEVICEADDQUERYINTERFACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEADDQUERYINTERFACE PfnWdfdeviceaddqueryinterface; 

// Definition

WDFAPI PfnWdfdeviceaddqueryinterface 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_QUERY_INTERFACE_CONFIG InterfaceConfig
)
{...}

PFN_WDFDEVICEADDQUERYINTERFACE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param InterfaceConfig: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also