---
UID: NC.d3dkmddi.DXGKDDI_QUERYVIDPNHWCAPABILITY
title: DXGKDDI_QUERYVIDPNHWCAPABILITY
author: windows-driver-content
description: 
ms.assetid: 90d86c7f-2728-47e9-ab1c-638beda2bb32
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

# DXGKDDI_QUERYVIDPNHWCAPABILITY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_QUERYVIDPNHWCAPABILITY DxgkddiQueryvidpnhwcapability; 

// Definition

NTSTATUS DxgkddiQueryvidpnhwcapability 
(
	IN_CONST_HANDLE i_hAdapter
	INOUT_PDXGKARG_QUERYVIDPNHWCAPABILITY io_pVidPnHWCaps
)
{...}

DXGKDDI_QUERYVIDPNHWCAPABILITY PDXGKDDI_QUERYVIDPNHWCAPABILITY


```

## -parameters

### -param i_hAdapter: 
### -param io_pVidPnHWCaps: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also