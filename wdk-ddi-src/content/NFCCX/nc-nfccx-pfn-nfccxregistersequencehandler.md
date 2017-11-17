---
UID: NC.nfccx.PFN_NFCCXREGISTERSEQUENCEHANDLER
title: *PFN_NFCCXREGISTERSEQUENCEHANDLER
author: windows-driver-content
description: 
ms.assetid: dcd389ff-d3ac-4669-8240-720250102cfb
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

# *PFN_NFCCXREGISTERSEQUENCEHANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NFCCXREGISTERSEQUENCEHANDLER *PfnNfccxregistersequencehandler; 

// Definition

NTSTATUS *PfnNfccxregistersequencehandler 
(
	PNFCCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	NFC_CX_SEQUENCE Sequence
	PFN_NFC_CX_SEQUENCE_HANDLER EvtNfcCxSequenceHandler
)
{...}

*PFN_NFCCXREGISTERSEQUENCEHANDLER 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Sequence: 
### -param EvtNfcCxSequenceHandler: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also