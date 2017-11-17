---
UID: NC.udecxusbdevice.PFN_UDECXUSBDEVICELINKPOWERENTRYCOMPLETE
title: *PFN_UDECXUSBDEVICELINKPOWERENTRYCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 55b150f5-abcb-423b-b019-28cc4b29ba73
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxusbdevice.h
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

# *PFN_UDECXUSBDEVICELINKPOWERENTRYCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXUSBDEVICELINKPOWERENTRYCOMPLETE *PfnUdecxusbdevicelinkpowerentrycomplete; 

// Definition

VOID *PfnUdecxusbdevicelinkpowerentrycomplete 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	UDECXUSBDEVICE UdecxUsbDevice
	NTSTATUS CompletionStatus
)
{...}

*PFN_UDECXUSBDEVICELINKPOWERENTRYCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param UdecxUsbDevice: 
### -param CompletionStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also