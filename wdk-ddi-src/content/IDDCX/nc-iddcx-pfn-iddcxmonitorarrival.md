---
UID: NC.iddcx.PFN_IDDCXMONITORARRIVAL
title: *PFN_IDDCXMONITORARRIVAL
author: windows-driver-content
description: 
ms.assetid: 1e0c46d0-21db-48b8-b8a0-283e96f9e406
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: iddcx.h
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

# *PFN_IDDCXMONITORARRIVAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXMONITORARRIVAL *PfnIddcxmonitorarrival; 

// Definition

NTSTATUS *PfnIddcxmonitorarrival 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_MONITOR AdapterObject
	IDARG_OUT_MONITORARRIVAL *pOutArgs
)
{...}

*PFN_IDDCXMONITORARRIVAL 


```

## -parameters

### -param DriverGlobals: 
### -param AdapterObject: 
### -param *pOutArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also