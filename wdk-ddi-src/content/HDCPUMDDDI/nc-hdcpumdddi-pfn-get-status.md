---
UID: NC.hdcpumdddi.PFN_GET_STATUS
title: PFN_GET_STATUS
author: windows-driver-content
description: 
ms.assetid: 1cf3e5f1-8f24-4f0b-aaf3-2365448da012
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

# PFN_GET_STATUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_GET_STATUS PfnGetStatus; 

// Definition

VOID PfnGetStatus 
(
	PVOID pDriverContext
	HDCP_HANDSHAKE_STATE *pState
	BOOL *pfReceiver
	BOOL *pfRepeater
	HDCP_TRANSPORT_TYPE *pTransportType
	UINT *puLocalHdcpVersion
	UINT *puPeerHdcpVersion
)
{...}

PFN_GET_STATUS 


```

## -parameters

### -param pDriverContext: 
### -param *pState: 
### -param *pfReceiver: 
### -param *pfRepeater: 
### -param *pTransportType: 
### -param *puLocalHdcpVersion: 
### -param *puPeerHdcpVersion: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also