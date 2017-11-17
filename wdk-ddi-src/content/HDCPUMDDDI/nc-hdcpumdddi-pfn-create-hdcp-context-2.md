---
UID: NC.hdcpumdddi.PFN_CREATE_HDCP_CONTEXT_2
title: PFN_CREATE_HDCP_CONTEXT_2
author: windows-driver-content
description: 
ms.assetid: f0e7e90e-f0ff-4c89-a264-93bc8cc6502c
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

# PFN_CREATE_HDCP_CONTEXT_2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_CREATE_HDCP_CONTEXT_2 PfnCreateHdcpContext2; 

// Definition

HRESULT PfnCreateHdcpContext2 
(
	PVOID pOSContext
	PHDCP_CALLBACKS pCallbacks
	HDCP_ENDPOINT_TYPE EndpointType
	HDCP_AUTHENTICATION_TYPE AuthenticationType
	LUID AdapterLuid
	PVOID *ppDriverContext
)
{...}

PFN_CREATE_HDCP_CONTEXT_2 


```

## -parameters

### -param pOSContext: 
### -param pCallbacks: 
### -param EndpointType: 
### -param AuthenticationType: 
### -param AdapterLuid: 
### -param *ppDriverContext: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also