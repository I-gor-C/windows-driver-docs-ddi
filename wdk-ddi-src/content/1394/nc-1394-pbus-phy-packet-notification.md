---
UID: NC.1394.PBUS_PHY_PACKET_NOTIFICATION
title: PBUS_PHY_PACKET_NOTIFICATION
author: windows-driver-content
description: 
ms.assetid: 1f40b08a-0246-48f5-a1dc-7ccd1cc494c4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: 1394.h
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

# PBUS_PHY_PACKET_NOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PBUS_PHY_PACKET_NOTIFICATION PbusPhyPacketNotification; 

// Definition

void PbusPhyPacketNotification 
(
	PVOID Context
	ULONG GenerationCount
	ULARGE_INTEGER PhyPacket
)
{...}

PBUS_PHY_PACKET_NOTIFICATION 


```

## -parameters

### -param Context: 
### -param GenerationCount: 
### -param PhyPacket: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also