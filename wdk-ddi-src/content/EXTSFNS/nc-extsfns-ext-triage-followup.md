---
UID: NC.extsfns.EXT_TRIAGE_FOLLOWUP
title: EXT_TRIAGE_FOLLOWUP
author: windows-driver-content
description: 
ms.assetid: d01917f1-3206-4b3d-8d3c-5d02278e47ae
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

# EXT_TRIAGE_FOLLOWUP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_TRIAGE_FOLLOWUP ExtTriageFollowup; 

// Definition

DWORD ExtTriageFollowup 
(
	PDEBUG_CLIENT4 Client
	PCSTR SymbolName
	OUT PDEBUG_TRIAGE_FOLLOWUP_INFO OwnerInfo
)
{...}

EXT_TRIAGE_FOLLOWUP 


```

## -parameters

### -param Client: 
### -param SymbolName: 
### -param OwnerInfo: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also