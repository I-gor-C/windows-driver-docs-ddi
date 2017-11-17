---
UID: NC.udecxurb.PFN_UDECXURBRETRIEVECONTROLSETUPPACKET
title: *PFN_UDECXURBRETRIEVECONTROLSETUPPACKET
author: windows-driver-content
description: 
ms.assetid: 106954d2-5e86-4550-99c1-f4454f489927
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxurb.h
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

# *PFN_UDECXURBRETRIEVECONTROLSETUPPACKET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXURBRETRIEVECONTROLSETUPPACKET *PfnUdecxurbretrievecontrolsetuppacket; 

// Definition

NTSTATUS *PfnUdecxurbretrievecontrolsetuppacket 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PWDF_USB_CONTROL_SETUP_PACKET SetupPacket
)
{...}

*PFN_UDECXURBRETRIEVECONTROLSETUPPACKET 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param SetupPacket: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also