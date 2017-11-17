---
UID: NC.sercx.PFN_SERCXRETRIEVETRANSMITBUFFER
title: PFN_SERCXRETRIEVETRANSMITBUFFER
author: windows-driver-content
description: 
ms.assetid: 43d3bc13-c2e9-490e-a5b7-7e3e248a2a17
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

# PFN_SERCXRETRIEVETRANSMITBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXRETRIEVETRANSMITBUFFER PfnSercxretrievetransmitbuffer; 

// Definition

WDFAPI PfnSercxretrievetransmitbuffer 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	ULONG Length
	PSERCX_BUFFER_DESCRIPTOR BufferDescriptor
)
{...}

PFN_SERCXRETRIEVETRANSMITBUFFER 


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