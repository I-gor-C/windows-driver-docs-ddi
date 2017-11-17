---
UID: NC.poscx.PFN_POSCXMARKPOSAPP
title: *PFN_POSCXMARKPOSAPP
author: windows-driver-content
description: 
ms.assetid: 9a83bf16-7d12-4dac-9ee2-0e7f667e7058
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

# *PFN_POSCXMARKPOSAPP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_POSCXMARKPOSAPP *PfnPoscxmarkposapp; 

// Definition

NTSTATUS *PfnPoscxmarkposapp 
(
	PPOSCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE device
	WDFFILEOBJECT fileObject
	BOOLEAN isPosApp
)
{...}

*PFN_POSCXMARKPOSAPP 


```

## -parameters

### -param DriverGlobals: 
### -param device: 
### -param fileObject: 
### -param isPosApp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also