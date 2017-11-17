---
UID: NC.iddcx.PFN_IDDCXMONITORCREATE
title: *PFN_IDDCXMONITORCREATE
author: windows-driver-content
description: 
ms.assetid: 77a1cb59-4115-426f-84e8-382971de1c85
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

# *PFN_IDDCXMONITORCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXMONITORCREATE *PfnIddcxmonitorcreate; 

// Definition

NTSTATUS *PfnIddcxmonitorcreate 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_ADAPTER AdapterObject
	CONST IDARG_IN_MONITORCREATE *pInArgs
	IDARG_OUT_MONITORCREATE *pOutArgs
)
{...}

*PFN_IDDCXMONITORCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param AdapterObject: 
### -param *pInArgs: 
### -param *pOutArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also