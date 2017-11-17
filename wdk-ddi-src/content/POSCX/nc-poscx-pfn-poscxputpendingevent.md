---
UID: NC.poscx.PFN_POSCXPUTPENDINGEVENT
title: *PFN_POSCXPUTPENDINGEVENT
author: windows-driver-content
description: 
ms.assetid: 755c4073-4795-4991-849d-7a669c8d0117
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

# *PFN_POSCXPUTPENDINGEVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_POSCXPUTPENDINGEVENT *PfnPoscxputpendingevent; 

// Definition

NTSTATUS *PfnPoscxputpendingevent 
(
	PPOSCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE device
	ULONG deviceInterfaceTag
	ULONG eventType
	size_t rawEventDataSize
	PVOID rawEventDataPtr
	POS_CX_EVENT_ATTRIBUTES eventAttr
)
{...}

*PFN_POSCXPUTPENDINGEVENT 


```

## -parameters

### -param DriverGlobals: 
### -param device: 
### -param deviceInterfaceTag: 
### -param eventType: 
### -param rawEventDataSize: 
### -param rawEventDataPtr: 
### -param eventAttr: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also