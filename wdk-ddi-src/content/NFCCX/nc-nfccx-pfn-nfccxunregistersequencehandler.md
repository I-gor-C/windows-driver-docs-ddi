---
UID: NC.nfccx.PFN_NFCCXUNREGISTERSEQUENCEHANDLER
title: *PFN_NFCCXUNREGISTERSEQUENCEHANDLER
author: windows-driver-content
description: 
ms.assetid: 3ec04d0d-e1f4-45f7-a370-caeb1d1e8b13
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

# *PFN_NFCCXUNREGISTERSEQUENCEHANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NFCCXUNREGISTERSEQUENCEHANDLER *PfnNfccxunregistersequencehandler; 

// Definition

NTSTATUS *PfnNfccxunregistersequencehandler 
(
	PNFCCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	NFC_CX_SEQUENCE Sequence
)
{...}

*PFN_NFCCXUNREGISTERSEQUENCEHANDLER 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Sequence: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also