---
UID: NC.fwpsk.FWPS_CALLOUT_CLASSIFY_FN3
title: FWPS_CALLOUT_CLASSIFY_FN3
author: windows-driver-content
description: 
ms.assetid: cf0ce6b1-a090-449e-9a7d-809cd6f5ea48
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: fwpsk.h
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

# FWPS_CALLOUT_CLASSIFY_FN3 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FWPS_CALLOUT_CLASSIFY_FN3 FwpsCalloutClassifyFn3; 

// Definition

void FwpsCalloutClassifyFn3 
(
	const FWPS_INCOMING_VALUES0 *inFixedValues
	 const FWPS_INCOMING_METADATA_VALUES0 *inMetaValues
	 void *layerData
	 const void *classifyContext
	 const FWPS_FILTER3 *filter
	UINT64 flowContext
	FWPS_CLASSIFY_OUT0 *classifyOut
)
{...}

FWPS_CALLOUT_CLASSIFY_FN3 


```

## -parameters

### -param *inFixedValues: 
### -param *inMetaValues: 
### -param *layerData: 
### -param *classifyContext: 
### -param *filter: 
### -param flowContext: 
### -param *classifyOut: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also