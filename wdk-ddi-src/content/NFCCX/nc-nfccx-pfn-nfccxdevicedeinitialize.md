---
UID: NC.nfccx.PFN_NFCCXDEVICEDEINITIALIZE
title: *PFN_NFCCXDEVICEDEINITIALIZE
author: windows-driver-content
description: 
ms.assetid: 3efd8292-fe0f-4d46-a809-319658797fcc
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

# *PFN_NFCCXDEVICEDEINITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NFCCXDEVICEDEINITIALIZE *PfnNfccxdevicedeinitialize; 

// Definition

NTSTATUS *PfnNfccxdevicedeinitialize 
(
	PNFCCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

*PFN_NFCCXDEVICEDEINITIALIZE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also