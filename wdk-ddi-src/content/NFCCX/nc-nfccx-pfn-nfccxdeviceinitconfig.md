---
UID: NC.nfccx.PFN_NFCCXDEVICEINITCONFIG
title: *PFN_NFCCXDEVICEINITCONFIG
author: windows-driver-content
description: 
ms.assetid: 7a028e6f-9d40-476a-8335-8f30c4504ac3
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

# *PFN_NFCCXDEVICEINITCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NFCCXDEVICEINITCONFIG *PfnNfccxdeviceinitconfig; 

// Definition

NTSTATUS *PfnNfccxdeviceinitconfig 
(
	PNFCCX_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PNFC_CX_CLIENT_CONFIG Config
)
{...}

*PFN_NFCCXDEVICEINITCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param Config: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also