---
UID: NC.iddcx.PFN_IDDCXDEVICEINITCONFIG
title: *PFN_IDDCXDEVICEINITCONFIG
author: windows-driver-content
description: 
ms.assetid: 94e113fe-148e-4353-b319-b5ff1df55018
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: iddcx.h
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

# *PFN_IDDCXDEVICEINITCONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXDEVICEINITCONFIG *PfnIddcxdeviceinitconfig; 

// Definition

NTSTATUS *PfnIddcxdeviceinitconfig 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	CONST IDD_CX_CLIENT_CONFIG *Config
)
{...}

*PFN_IDDCXDEVICEINITCONFIG 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param *Config: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also