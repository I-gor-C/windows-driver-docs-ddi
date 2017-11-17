---
UID: NC.d3dkmddi.DXGKDDI_DESTROYDEVICE
title: DXGKDDI_DESTROYDEVICE
author: windows-driver-content
description: 
ms.assetid: 738dac48-cffa-4f29-8483-dc15e24de095
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

# DXGKDDI_DESTROYDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_DESTROYDEVICE DxgkddiDestroydevice; 

// Definition

NTSTATUS DxgkddiDestroydevice 
(
	IN_CONST_HANDLE hDevice
)
{...}

DXGKDDI_DESTROYDEVICE PDXGKDDI_DESTROYDEVICE


```

## -parameters

### -param hDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also