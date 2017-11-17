---
UID: NC.extsfns.PGET_PNP_TRIAGE_INFO
title: PGET_PNP_TRIAGE_INFO
author: windows-driver-content
description: 
ms.assetid: c2806c4d-ec08-4a47-a06f-6b405c1ff3ee
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# PGET_PNP_TRIAGE_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_PNP_TRIAGE_INFO PgetPnpTriageInfo; 

// Definition

HRESULT PgetPnpTriageInfo 
(
	IN PDEBUG_CLIENT Client
	OUT PDEBUG_PNP_TRIAGE_INFO pPNPTriageInfo
)
{...}

PGET_PNP_TRIAGE_INFO 


```

## -parameters

### -param Client: 
### -param pPNPTriageInfo: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also