---
UID: NC.nfccx.PFN_NFCCXRELEASEHARDWARECONTROL
title: *PFN_NFCCXRELEASEHARDWARECONTROL
author: windows-driver-content
description: 
ms.assetid: 7f2505be-b6c4-4f61-8b8f-1e3c482516c7
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

# *PFN_NFCCXRELEASEHARDWARECONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_NFCCXRELEASEHARDWARECONTROL *PfnNfccxreleasehardwarecontrol; 

// Definition

NTSTATUS *PfnNfccxreleasehardwarecontrol 
(
	PNFCCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

*PFN_NFCCXRELEASEHARDWARECONTROL 


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