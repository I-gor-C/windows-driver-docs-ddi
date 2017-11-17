---
UID: NC.sercx.PFN_SERCXPROGRESSRECEIVE
title: PFN_SERCXPROGRESSRECEIVE
author: windows-driver-content
description: 
ms.assetid: 544c3fb7-f5b9-419d-92e5-06250282ae22
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

# PFN_SERCXPROGRESSRECEIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXPROGRESSRECEIVE PfnSercxprogressreceive; 

// Definition

WDFAPI PfnSercxprogressreceive 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	ULONG BytesReceived
	SERCX_STATUS ReceiveStatus
)
{...}

PFN_SERCXPROGRESSRECEIVE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param BytesReceived: 
### -param ReceiveStatus: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also