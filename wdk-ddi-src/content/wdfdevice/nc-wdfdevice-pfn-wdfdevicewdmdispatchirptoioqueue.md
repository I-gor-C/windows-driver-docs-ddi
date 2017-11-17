---
UID: NC.wdfdevice.PFN_WDFDEVICEWDMDISPATCHIRPTOIOQUEUE
title: PFN_WDFDEVICEWDMDISPATCHIRPTOIOQUEUE
author: windows-driver-content
description: 
ms.assetid: 0add1ccf-e55e-47a4-9ac6-7929043beb36
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

# PFN_WDFDEVICEWDMDISPATCHIRPTOIOQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEWDMDISPATCHIRPTOIOQUEUE PfnWdfdevicewdmdispatchirptoioqueue; 

// Definition

WDFAPI PfnWdfdevicewdmdispatchirptoioqueue 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PIRP Irp
	WDFQUEUE Queue
	ULONG Flags
)
{...}

PFN_WDFDEVICEWDMDISPATCHIRPTOIOQUEUE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Irp: 
### -param Queue: 
### -param Flags: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also