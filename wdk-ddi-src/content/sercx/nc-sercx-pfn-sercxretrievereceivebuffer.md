---
UID: NC.sercx.PFN_SERCXRETRIEVERECEIVEBUFFER
title: PFN_SERCXRETRIEVERECEIVEBUFFER
author: windows-driver-content
description: 
ms.assetid: 21b8244e-b089-43dd-a063-6262f31c823a
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

# PFN_SERCXRETRIEVERECEIVEBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXRETRIEVERECEIVEBUFFER PfnSercxretrievereceivebuffer; 

// Definition

WDFAPI PfnSercxretrievereceivebuffer 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	ULONG Length
	PSERCX_BUFFER_DESCRIPTOR BufferDescriptor
)
{...}

PFN_SERCXRETRIEVERECEIVEBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Length: 
### -param BufferDescriptor: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also