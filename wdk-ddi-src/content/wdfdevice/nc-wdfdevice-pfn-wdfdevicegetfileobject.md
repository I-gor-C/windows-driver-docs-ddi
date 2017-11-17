---
UID: NC.wdfdevice.PFN_WDFDEVICEGETFILEOBJECT
title: PFN_WDFDEVICEGETFILEOBJECT
author: windows-driver-content
description: 
ms.assetid: 25b73527-e9e3-43d7-8d1c-551626f331c6
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

# PFN_WDFDEVICEGETFILEOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEGETFILEOBJECT PfnWdfdevicegetfileobject; 

// Definition

WDFAPI PfnWdfdevicegetfileobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PFILE_OBJECT FileObject
)
{...}

PFN_WDFDEVICEGETFILEOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param FileObject: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also