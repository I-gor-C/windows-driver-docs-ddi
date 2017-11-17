---
UID: NC.udecxurb.PFN_UDECXURBCOMPLETEWITHNTSTATUS
title: *PFN_UDECXURBCOMPLETEWITHNTSTATUS
author: windows-driver-content
description: 
ms.assetid: e59b64d1-1a9c-4290-bbe9-f2cd6a965096
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxurb.h
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

# *PFN_UDECXURBCOMPLETEWITHNTSTATUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXURBCOMPLETEWITHNTSTATUS *PfnUdecxurbcompletewithntstatus; 

// Definition

VOID *PfnUdecxurbcompletewithntstatus 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	NTSTATUS NtStatus
)
{...}

*PFN_UDECXURBCOMPLETEWITHNTSTATUS 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param NtStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also