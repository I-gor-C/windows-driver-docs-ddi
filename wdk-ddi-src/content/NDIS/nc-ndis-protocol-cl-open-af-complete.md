---
UID: NC.ndis.PROTOCOL_CL_OPEN_AF_COMPLETE
title: PROTOCOL_CL_OPEN_AF_COMPLETE
author: windows-driver-content
description: 
ms.assetid: 4c80178f-ff6b-4f5f-942f-37e39b51ea07
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# PROTOCOL_CL_OPEN_AF_COMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PROTOCOL_CL_OPEN_AF_COMPLETE ProtocolClOpenAfComplete; 

// Definition

VOID ProtocolClOpenAfComplete 
(
	NDIS_STATUS Status
	NDIS_HANDLE ProtocolAfContext
	NDIS_HANDLE NdisAfHandle
)
{...}

PROTOCOL_CL_OPEN_AF_COMPLETE PPROTOCOL_CL_OPEN_AF_COMPLETE


```

## -parameters

### -param Status: 
### -param ProtocolAfContext: 
### -param NdisAfHandle: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also