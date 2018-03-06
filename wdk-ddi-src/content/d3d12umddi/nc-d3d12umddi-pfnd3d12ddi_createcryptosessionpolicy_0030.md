---
UID: NC:d3d12umddi.PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030
title: PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030
author: windows-driver-content
description: Used to create a crypto session policy.
old-location: display\pfnd3d12ddi_createcryptosessionpolicy_0030.htm
old-project: display
ms.assetid: BB3B2C57-CE5A-4E15-ABCB-4817C0234B62
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030, PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030 callback function [Display Devices], d3d12umddi/PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030, display.pfnd3d12ddi_createcryptosessionpolicy_0030
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	d3d12umddi.h
api_name:
-	PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030 callback function
Used to create a crypto session policy.

## Syntax

```
PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030 Pfnd3d12ddiCreatecryptosessionpolicy0030;

HRESULT Pfnd3d12ddiCreatecryptosessionpolicy0030(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_CREATE_CRYPTO_SESSION_POLICY_0030 *pArgs,
  D3D12DDI_HCRYPTOSESSION_0030 hDrvCryptoSession,
  D3D12DDI_HCRYPTOSESSIONPOLICY_0030 hDrvCryptoSessionPolicy,
  D3D12DDI_HRTPROTECTEDSESSION_0030 hRtProtectedSession
)
{...}
```

## Parameters

`hDrvDevice`

The hardware device being processed.

`*pArgs`

The arguments used to create a crypto session policy.

`hDrvCryptoSession`

Used to create a crypto session.

`hDrvCryptoSessionPolicy`

Used to create a crypto session policy.

`hRtProtectedSession`

Used to create a protected session.


## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h |