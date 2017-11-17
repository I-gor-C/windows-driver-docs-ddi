---
UID: NC.d3d12umddi.PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030
title: PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030
author: windows-driver-content
description: 
ms.assetid: dd6761b7-6c6a-48f9-92c9-4af6c3e2dc66
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
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

# PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030 Pfnd3d12ddiCalcprivatecryptosessionpolicysize0030; 

// Definition

SIZE_T Pfnd3d12ddiCalcprivatecryptosessionpolicysize0030 
(
	D3D12DDI_HDEVICE hDrvDevice
	CONST D3D12DDIARG_CREATE_CRYPTO_SESSION_POLICY_0030 *pArgs
	D3D12DDI_HCRYPTOSESSION_0030 hDrvCryptoSession
)
{...}

PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030 


```

## -parameters

### -param hDrvDevice: 
### -param *pArgs: 
### -param hDrvCryptoSession: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also