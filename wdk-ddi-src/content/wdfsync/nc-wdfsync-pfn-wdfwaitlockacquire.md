---
UID: NC.wdfsync.PFN_WDFWAITLOCKACQUIRE
title: *PFN_WDFWAITLOCKACQUIRE
author: windows-driver-content
description: 
ms.assetid: 1b459fbe-556c-4c18-b6d4-b66eb9195058
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfsync.h
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

# *PFN_WDFWAITLOCKACQUIRE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFWAITLOCKACQUIRE *PfnWdfwaitlockacquire; 

// Definition

NTSTATUS *PfnWdfwaitlockacquire 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	_Requires_lock_not_held_(_Curr_)WDFWAITLOCK Lock
	PLONGLONG Timeout
)
{...}

*PFN_WDFWAITLOCKACQUIRE 


```

## -parameters

### -param DriverGlobals: 
### -param Lock: 
### -param Timeout: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also