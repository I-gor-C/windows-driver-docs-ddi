---
UID: NC.nfccx.PFN_NFCCXSETLLCPCONFIG
title: *PFN_NFCCXSETLLCPCONFIG
author: windows-driver-content
description: 
ms.assetid: a2d60888-0b17-43d4-b72f-472dc64e6587
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

# *PFN_NFCCXSETLLCPCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NFCCXSETLLCPCONFIG *PfnNfccxsetllcpconfig; 

// Definition

NTSTATUS *PfnNfccxsetllcpconfig 
(
	PNFCCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PCNFC_CX_LLCP_CONFIG Config
)
{...}

*PFN_NFCCXSETLLCPCONFIG 


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