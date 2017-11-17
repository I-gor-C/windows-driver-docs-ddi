---
UID: NC.sercx.PFN_SERCXGETRINGBUFFERUTILIZATION
title: PFN_SERCXGETRINGBUFFERUTILIZATION
author: windows-driver-content
description: 
ms.assetid: ae6f4357-5d6e-475c-a769-27ad04c0592a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# PFN_SERCXGETRINGBUFFERUTILIZATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXGETRINGBUFFERUTILIZATION PfnSercxgetringbufferutilization; 

// Definition

WDFAPI PfnSercxgetringbufferutilization 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PULONG BytesUsed
	PULONG BufferSize
)
{...}

PFN_SERCXGETRINGBUFFERUTILIZATION 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param BytesUsed: 
### -param BufferSize: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also