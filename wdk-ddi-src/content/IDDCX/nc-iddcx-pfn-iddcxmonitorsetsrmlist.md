---
UID: NC.iddcx.PFN_IDDCXMONITORSETSRMLIST
title: *PFN_IDDCXMONITORSETSRMLIST
author: windows-driver-content
description: 
ms.assetid: d6e21138-2f34-4577-afe7-da336eda9055
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

# *PFN_IDDCXMONITORSETSRMLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXMONITORSETSRMLIST *PfnIddcxmonitorsetsrmlist; 

// Definition

NTSTATUS *PfnIddcxmonitorsetsrmlist 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_MONITOR MonitorObject
	IDARG_IN_SETSRMLIST *pInArgs
)
{...}

*PFN_IDDCXMONITORSETSRMLIST 


```

## -parameters

### -param DriverGlobals: 
### -param MonitorObject: 
### -param *pInArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also