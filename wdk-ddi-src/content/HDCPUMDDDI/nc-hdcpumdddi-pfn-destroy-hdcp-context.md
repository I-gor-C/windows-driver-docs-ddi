---
UID: NC.hdcpumdddi.PFN_DESTROY_HDCP_CONTEXT
title: PFN_DESTROY_HDCP_CONTEXT
author: windows-driver-content
description: 
ms.assetid: a24a0640-3f45-4568-a0ea-e4cbfb019abd
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

# PFN_DESTROY_HDCP_CONTEXT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_DESTROY_HDCP_CONTEXT PfnDestroyHdcpContext; 

// Definition

VOID PfnDestroyHdcpContext 
(
	PVOID pDriverContext
)
{...}

PFN_DESTROY_HDCP_CONTEXT 


```

## -parameters

### -param pDriverContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also