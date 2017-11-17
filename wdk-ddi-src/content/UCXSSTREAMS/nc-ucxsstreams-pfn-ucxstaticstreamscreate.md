---
UID: NC.ucxsstreams.PFN_UCXSTATICSTREAMSCREATE
title: PFN_UCXSTATICSTREAMSCREATE
author: windows-driver-content
description: 
ms.assetid: 2d48bfb2-f2bb-4ef8-9bd5-b235bd441638
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxsstreams.h
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

# PFN_UCXSTATICSTREAMSCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXSTATICSTREAMSCREATE PfnUcxstaticstreamscreate; 

// Definition

WDFAPI PfnUcxstaticstreamscreate 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXENDPOINT Endpoint
	PUCXSSTREAMS_INIT *StaticStreamsInit
	PWDF_OBJECT_ATTRIBUTES Attributes
	UCXSSTREAMS *StaticStreams
)
{...}

PFN_UCXSTATICSTREAMSCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Endpoint: 
### -param *StaticStreamsInit: 
### -param Attributes: 
### -param *StaticStreams: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also