---
UID: NC.udecxurb.PFN_UDECXURBRETRIEVEBUFFER
title: *PFN_UDECXURBRETRIEVEBUFFER
author: windows-driver-content
description: 
ms.assetid: f4d5e2ac-5e1e-4168-9f79-6c6008d42684
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

# *PFN_UDECXURBRETRIEVEBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXURBRETRIEVEBUFFER *PfnUdecxurbretrievebuffer; 

// Definition

NTSTATUS *PfnUdecxurbretrievebuffer 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PUCHAR *TransferBuffer
	PULONG Length
)
{...}

*PFN_UDECXURBRETRIEVEBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param *TransferBuffer: 
### -param Length: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also