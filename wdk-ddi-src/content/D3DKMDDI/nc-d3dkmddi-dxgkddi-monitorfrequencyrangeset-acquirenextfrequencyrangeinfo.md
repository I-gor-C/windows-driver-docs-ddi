---
UID: NC.d3dkmddi.DXGKDDI_MONITORFREQUENCYRANGESET_ACQUIRENEXTFREQUENCYRANGEINFO
title: DXGKDDI_MONITORFREQUENCYRANGESET_ACQUIRENEXTFREQUENCYRANGEINFO
author: windows-driver-content
description: 
ms.assetid: 333fe264-368a-47c2-8bda-e15cc3d45f16
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
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

# DXGKDDI_MONITORFREQUENCYRANGESET_ACQUIRENEXTFREQUENCYRANGEINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_MONITORFREQUENCYRANGESET_ACQUIRENEXTFREQUENCYRANGEINFO DxgkddiMonitorfrequencyrangesetAcquirenextfrequencyrangeinfo; 

// Definition

NTSTATUS DxgkddiMonitorfrequencyrangesetAcquirenextfrequencyrangeinfo 
(
	IN_CONST_D3DKMDT_HMONITORFREQUENCYRANGESET hMonitorFrequencyRangeSet
	IN_CONST_PD3DKMDT_MONITOR_FREQUENCY_RANGE_CONST pMonitorFrequencyRangeInfo
	DEREF_OUT_CONST_PPD3DKMDT_MONITOR_FREQUENCY_RANGE ppNextMonitorFrequencyRangeInfo
)
{...}

DXGKDDI_MONITORFREQUENCYRANGESET_ACQUIRENEXTFREQUENCYRANGEINFO 


```

## -parameters

### -param hMonitorFrequencyRangeSet: 
### -param pMonitorFrequencyRangeInfo: 
### -param ppNextMonitorFrequencyRangeInfo: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also