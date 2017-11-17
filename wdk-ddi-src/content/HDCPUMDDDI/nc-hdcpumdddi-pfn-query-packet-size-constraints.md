---
UID: NC.hdcpumdddi.PFN_QUERY_PACKET_SIZE_CONSTRAINTS
title: PFN_QUERY_PACKET_SIZE_CONSTRAINTS
author: windows-driver-content
description: 
ms.assetid: effc0dcb-361c-4116-b716-b47704e6d042
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hdcpumdddi.h
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

# PFN_QUERY_PACKET_SIZE_CONSTRAINTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_QUERY_PACKET_SIZE_CONSTRAINTS PfnQueryPacketSizeConstraints; 

// Definition

VOID PfnQueryPacketSizeConstraints 
(
	UINT *pcbMinPacketSize
	UINT *pcbMaxPacketSize
)
{...}

PFN_QUERY_PACKET_SIZE_CONSTRAINTS 


```

## -parameters

### -param *pcbMinPacketSize: 
### -param *pcbMaxPacketSize: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also