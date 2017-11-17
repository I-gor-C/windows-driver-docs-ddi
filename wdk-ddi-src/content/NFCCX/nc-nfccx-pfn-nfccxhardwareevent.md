---
UID: NC.nfccx.PFN_NFCCXHARDWAREEVENT
title: *PFN_NFCCXHARDWAREEVENT
author: windows-driver-content
description: 
ms.assetid: 275c1dcd-6c18-42fe-9e92-159e7589f0fb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: nfccx.h
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

# *PFN_NFCCXHARDWAREEVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NFCCXHARDWAREEVENT *PfnNfccxhardwareevent; 

// Definition

NTSTATUS *PfnNfccxhardwareevent 
(
	PNFCCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PNFC_CX_HARDWARE_EVENT HardwareEvent
)
{...}

*PFN_NFCCXHARDWAREEVENT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param HardwareEvent: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also