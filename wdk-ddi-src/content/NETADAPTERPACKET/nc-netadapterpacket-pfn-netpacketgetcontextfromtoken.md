---
UID: NC.netadapterpacket.PFN_NETPACKETGETCONTEXTFROMTOKEN
title: PFN_NETPACKETGETCONTEXTFROMTOKEN
author: windows-driver-content
description: 
ms.assetid: 4c3b4c71-4e0f-4ff8-ae19-293f034585aa
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

# PFN_NETPACKETGETCONTEXTFROMTOKEN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETPACKETGETCONTEXTFROMTOKEN PfnNetpacketgetcontextfromtoken; 

// Definition

WDFAPI PfnNetpacketgetcontextfromtoken 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NET_PACKET *NetPacket
	PNET_PACKET_CONTEXT_TOKEN Token
)
{...}

PFN_NETPACKETGETCONTEXTFROMTOKEN 


```

## -parameters

### -param DriverGlobals: 
### -param *NetPacket: 
### -param Token: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also