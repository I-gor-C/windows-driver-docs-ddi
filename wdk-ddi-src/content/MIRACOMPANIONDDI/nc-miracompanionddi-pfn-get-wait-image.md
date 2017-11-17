---
UID: NC.miracompanionddi.PFN_GET_WAIT_IMAGE
title: PFN_GET_WAIT_IMAGE
author: windows-driver-content
description: 
ms.assetid: ff4254a9-d06e-4c5d-9117-e4a24d344fbf
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: miracompanionddi.h
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

# PFN_GET_WAIT_IMAGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_GET_WAIT_IMAGE PfnGetWaitImage; 

// Definition

HRESULT PfnGetWaitImage 
(
	void const *pSessionContext
	UINT unTimeoutInMs
	UINT *punWidth
	UINT *punHeight
	BYTE **ppbImage
)
{...}

PFN_GET_WAIT_IMAGE 


```

## -parameters

### -param *pSessionContext: 
### -param unTimeoutInMs: 
### -param *punWidth: 
### -param *punHeight: 
### -param **ppbImage: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also