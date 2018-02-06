---
UID: NC:d3d12umddi.PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030
title: PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030
author: windows-driver-content
description: Used to calculate a session policy size.
old-location: display\pfnd3d12ddi_calcprivatecryptosessionpolicysize_0030_.htm
old-project: display
ms.assetid: 5FAF1FBE-DCCA-4D92-BB8D-C014D488353B
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.pfnd3d12ddi_calcprivatecryptosessionpolicysize_0030_, PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030 entry point [Display Devices], PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030, d3d12umddi/PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3d12umddi.h
apiname:
-	PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030 callback function
Used to calculate a session policy size.

## Syntax

```
PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030 Pfnd3d12ddiCalcprivatecryptosessionpolicysize0030;

SIZE_T Pfnd3d12ddiCalcprivatecryptosessionpolicysize0030(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_CREATE_CRYPTO_SESSION_POLICY_0030 *pArgs,
  D3D12DDI_HCRYPTOSESSION_0030 hDrvCryptoSession
)
{...}
```

## Parameters

`hDrvDevice`

The hardware device being processed.

`*pArgs`

The arguments used to create a session policy.

`hDrvCryptoSession`

The information for the driver session.


## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h |