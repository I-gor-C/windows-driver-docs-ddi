---
UID: NC.pfhook.PacketFilterExtensionPtr
title: PacketFilterExtensionPtr
author: windows-driver-content
description: 
ms.assetid: 51f3422e-05ba-4a1c-9aab-88f0c3662363
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: pfhook.h
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

# PacketFilterExtensionPtr callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PacketFilterExtensionPtr Packetfilterextensionptr; 

// Definition

PF_FORWARD_ACTION Packetfilterextensionptr 
(
	unsigned char *PacketHeader
	 unsigned char *Packet
	 unsigned int PacketLength
	 unsigned int RecvInterfaceIndex
	 unsigned int SendInterfaceIndex
	IPAddr RecvLinkNextHop
	IPAddr SendLinkNextHop
)
{...}

PacketFilterExtensionPtr 


```

## -parameters

### -param *PacketHeader: 
### -param *Packet: 
### -param PacketLength: 
### -param RecvInterfaceIndex: 
### -param SendInterfaceIndex: 
### -param RecvLinkNextHop: 
### -param SendLinkNextHop: 



## -returns

Returns PF_FORWARD_ACTION that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also