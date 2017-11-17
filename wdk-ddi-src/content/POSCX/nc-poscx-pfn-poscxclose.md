---
UID: NC.poscx.PFN_POSCXCLOSE
title: *PFN_POSCXCLOSE
author: windows-driver-content
description: 
ms.assetid: dedcec24-da38-4818-9f5d-205f8768dc47
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: poscx.h
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

# *PFN_POSCXCLOSE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_POSCXCLOSE *PfnPoscxclose; 

// Definition

NTSTATUS *PfnPoscxclose 
(
	PPOSCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE device
	WDFFILEOBJECT fileObject
)
{...}

*PFN_POSCXCLOSE 


```

## -parameters

### -param DriverGlobals: 
### -param device: 
### -param fileObject: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also