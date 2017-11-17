---
UID: NC.udecxwdfdevice.PFN_UDECXINITIALIZEWDFDEVICEINIT
title: *PFN_UDECXINITIALIZEWDFDEVICEINIT
author: windows-driver-content
description: 
ms.assetid: f688c642-8e49-4e84-a14e-8dcd23c25f69
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxwdfdevice.h
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

# *PFN_UDECXINITIALIZEWDFDEVICEINIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXINITIALIZEWDFDEVICEINIT *PfnUdecxinitializewdfdeviceinit; 

// Definition

NTSTATUS *PfnUdecxinitializewdfdeviceinit 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT WdfDeviceInit
)
{...}

*PFN_UDECXINITIALIZEWDFDEVICEINIT 


```

## -parameters

### -param DriverGlobals: 
### -param WdfDeviceInit: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also