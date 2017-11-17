---
UID: NC.poscx.PFN_POSCXGETPENDINGEVENT
title: *PFN_POSCXGETPENDINGEVENT
author: windows-driver-content
description: 
ms.assetid: 78ba289f-59bb-4083-a39a-b674bb91414f
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

# *PFN_POSCXGETPENDINGEVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_POSCXGETPENDINGEVENT *PfnPoscxgetpendingevent; 

// Definition

NTSTATUS *PfnPoscxgetpendingevent 
(
	PPOSCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE device
	WDFREQUEST request
)
{...}

*PFN_POSCXGETPENDINGEVENT 


```

## -parameters

### -param DriverGlobals: 
### -param device: 
### -param request: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also