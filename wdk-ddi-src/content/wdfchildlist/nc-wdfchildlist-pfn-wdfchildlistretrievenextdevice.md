---
UID: NC.wdfchildlist.PFN_WDFCHILDLISTRETRIEVENEXTDEVICE
title: PFN_WDFCHILDLISTRETRIEVENEXTDEVICE
author: windows-driver-content
description: 
ms.assetid: bb824e60-4418-4819-a72f-ad1be69e62eb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfchildlist.h
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

# PFN_WDFCHILDLISTRETRIEVENEXTDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCHILDLISTRETRIEVENEXTDEVICE PfnWdfchildlistretrievenextdevice; 

// Definition

WDFAPI PfnWdfchildlistretrievenextdevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCHILDLIST ChildList
	PWDF_CHILD_LIST_ITERATOR Iterator
	WDFDEVICE *Device
	PWDF_CHILD_RETRIEVE_INFO Info
)
{...}

PFN_WDFCHILDLISTRETRIEVENEXTDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param ChildList: 
### -param Iterator: 
### -param *Device: 
### -param Info: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also