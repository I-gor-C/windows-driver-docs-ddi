---
UID: NC.iddcx.PFN_IDDCXMONITORQUERYHARDWARECURSOR
title: *PFN_IDDCXMONITORQUERYHARDWARECURSOR
author: windows-driver-content
description: 
ms.assetid: b345b72e-4209-400d-870d-05dd01d42ac7
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

# *PFN_IDDCXMONITORQUERYHARDWARECURSOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXMONITORQUERYHARDWARECURSOR *PfnIddcxmonitorqueryhardwarecursor; 

// Definition

NTSTATUS *PfnIddcxmonitorqueryhardwarecursor 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_MONITOR MonitorObject
	CONST IDARG_IN_QUERY_HWCURSOR *pInArgs
	IDARG_OUT_QUERY_HWCURSOR *pOutArgs
)
{...}

*PFN_IDDCXMONITORQUERYHARDWARECURSOR 


```

## -parameters

### -param DriverGlobals: 
### -param MonitorObject: 
### -param *pInArgs: 
### -param *pOutArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also