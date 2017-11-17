---
UID: NC.d3dkmddi.DXGKDDI_POWERRUNTIMESETDEVICEHANDLE
title: DXGKDDI_POWERRUNTIMESETDEVICEHANDLE
author: windows-driver-content
description: 
ms.assetid: 81c4cb40-91df-46f3-bfea-8421df484848
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

# DXGKDDI_POWERRUNTIMESETDEVICEHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_POWERRUNTIMESETDEVICEHANDLE DxgkddiPowerruntimesetdevicehandle; 

// Definition

NTSTATUS DxgkddiPowerruntimesetdevicehandle 
(
	IN_CONST_HANDLE DriverContext
	IN HANDLE PoDeviceHandle
)
{...}

DXGKDDI_POWERRUNTIMESETDEVICEHANDLE PDXGKDDI_POWERRUNTIMESETDEVICEHANDLE


```

## -parameters

### -param DriverContext: 
### -param PoDeviceHandle: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also