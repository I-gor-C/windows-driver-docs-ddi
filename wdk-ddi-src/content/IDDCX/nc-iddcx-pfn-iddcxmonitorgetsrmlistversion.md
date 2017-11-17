---
UID: NC.iddcx.PFN_IDDCXMONITORGETSRMLISTVERSION
title: *PFN_IDDCXMONITORGETSRMLISTVERSION
author: windows-driver-content
description: 
ms.assetid: 0c2a91e5-39de-4505-a0c3-4c9d746e19d6
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

# *PFN_IDDCXMONITORGETSRMLISTVERSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXMONITORGETSRMLISTVERSION *PfnIddcxmonitorgetsrmlistversion; 

// Definition

NTSTATUS *PfnIddcxmonitorgetsrmlistversion 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_MONITOR MonitorObject
	IDARG_IN_GETSRMLISTVERSION *pInArgs
	IDARG_OUT_GETSRMLISTVERSION *pOutArgs
)
{...}

*PFN_IDDCXMONITORGETSRMLISTVERSION 


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