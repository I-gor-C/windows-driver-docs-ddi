---
UID: NC.netadapterpacket.PFN_NETPACKETGETTYPEDCONTEXT
title: PFN_NETPACKETGETTYPEDCONTEXT
author: windows-driver-content
description: 
ms.assetid: efd188aa-2bc0-448f-97d8-0e97738ce663
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netadapterpacket.h
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

# PFN_NETPACKETGETTYPEDCONTEXT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPACKETGETTYPEDCONTEXT PfnNetpacketgettypedcontext; 

// Definition

WDFAPI PfnNetpacketgettypedcontext 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NET_PACKET *NetPacket
	PCNET_CONTEXT_TYPE_INFO TypeInfo
)
{...}

PFN_NETPACKETGETTYPEDCONTEXT 


```

## -parameters

### -param DriverGlobals: 
### -param *NetPacket: 
### -param TypeInfo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also