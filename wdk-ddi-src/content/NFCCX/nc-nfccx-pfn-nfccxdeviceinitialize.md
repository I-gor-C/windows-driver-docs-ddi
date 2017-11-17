---
UID: NC.nfccx.PFN_NFCCXDEVICEINITIALIZE
title: *PFN_NFCCXDEVICEINITIALIZE
author: windows-driver-content
description: 
ms.assetid: 1f2e9154-7e04-44d5-8098-06b1ccd48c0b
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

# *PFN_NFCCXDEVICEINITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NFCCXDEVICEINITIALIZE *PfnNfccxdeviceinitialize; 

// Definition

NTSTATUS *PfnNfccxdeviceinitialize 
(
	PNFCCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

*PFN_NFCCXDEVICEINITIALIZE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also