---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICEALLOCANDQUERYSTRING
title: PFN_WDFUSBTARGETDEVICEALLOCANDQUERYSTRING
author: windows-driver-content
description: 
ms.assetid: 264b4097-0cc2-439b-b844-e4f69ea74012
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

# PFN_WDFUSBTARGETDEVICEALLOCANDQUERYSTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICEALLOCANDQUERYSTRING PfnWdfusbtargetdeviceallocandquerystring; 

// Definition

WDFAPI PfnWdfusbtargetdeviceallocandquerystring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	PWDF_OBJECT_ATTRIBUTES StringMemoryAttributes
	WDFMEMORY *StringMemory
	PUSHORT NumCharacters
	UCHAR StringIndex
	USHORT LangID
)
{...}

PFN_WDFUSBTARGETDEVICEALLOCANDQUERYSTRING 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param StringMemoryAttributes: 
### -param *StringMemory: 
### -param NumCharacters: 
### -param StringIndex: 
### -param LangID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also