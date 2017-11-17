---
UID: NC.nfccx.PFN_NFCCXSETRFDISCOVERYCONFIG
title: *PFN_NFCCXSETRFDISCOVERYCONFIG
author: windows-driver-content
description: 
ms.assetid: 42ebd282-3a09-4a05-b110-946adc1f623d
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

# *PFN_NFCCXSETRFDISCOVERYCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NFCCXSETRFDISCOVERYCONFIG *PfnNfccxsetrfdiscoveryconfig; 

// Definition

NTSTATUS *PfnNfccxsetrfdiscoveryconfig 
(
	PNFCCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PCNFC_CX_RF_DISCOVERY_CONFIG Config
)
{...}

*PFN_NFCCXSETRFDISCOVERYCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Config: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also