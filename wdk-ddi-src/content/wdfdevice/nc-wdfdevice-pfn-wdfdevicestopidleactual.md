---
UID: NC.wdfdevice.PFN_WDFDEVICESTOPIDLEACTUAL
title: *PFN_WDFDEVICESTOPIDLEACTUAL
author: windows-driver-content
description: 
ms.assetid: a246a835-4615-488f-afe8-86f865aa2352
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# *PFN_WDFDEVICESTOPIDLEACTUAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFDEVICESTOPIDLEACTUAL *PfnWdfdevicestopidleactual; 

// Definition

NTSTATUS *PfnWdfdevicestopidleactual 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	BOOLEAN WaitForD0
	PVOID Tag
	LONG Line
	PCCH File
)
{...}

*PFN_WDFDEVICESTOPIDLEACTUAL 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param WaitForD0: 
### -param Tag: 
### -param Line: 
### -param File: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also