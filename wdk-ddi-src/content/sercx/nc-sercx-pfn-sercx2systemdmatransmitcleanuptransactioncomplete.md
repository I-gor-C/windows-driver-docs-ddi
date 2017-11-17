---
UID: NC.sercx.PFN_SERCX2SYSTEMDMATRANSMITCLEANUPTRANSACTIONCOMPLETE
title: PFN_SERCX2SYSTEMDMATRANSMITCLEANUPTRANSACTIONCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 5dd0652f-092d-4ea8-b9f9-f603a5be24b8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# PFN_SERCX2SYSTEMDMATRANSMITCLEANUPTRANSACTIONCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2SYSTEMDMATRANSMITCLEANUPTRANSACTIONCOMPLETE PfnSercx2systemdmatransmitcleanuptransactioncomplete; 

// Definition

WDFAPI PfnSercx2systemdmatransmitcleanuptransactioncomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2SYSTEMDMATRANSMIT SystemDmaTransmit
)
{...}

PFN_SERCX2SYSTEMDMATRANSMITCLEANUPTRANSACTIONCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param SystemDmaTransmit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also