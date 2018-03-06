---
UID: NC:d3d12umddi.PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021
title: PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021
author: windows-driver-content
description: The pfnShaderCacheGetValueCb callback function gets a shader cache value.
old-location: display\pfnd3d12ddi_shadercachegetvalue_cb_0021.htm
old-project: display
ms.assetid: EFC9E2D0-1995-4FE9-840C-7B33081AEF2F
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021, d3d12umddi/pfnShaderCacheGetValueCb, display.pfnd3d12ddi_shadercachegetvalue_cb_0021, pfnShaderCacheGetValueCb, pfnShaderCacheGetValueCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
-	D3d12umddi.h
api_name:
-	pfnShaderCacheGetValueCb
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021 callback function
The <i>pfnShaderCacheGetValueCb</i> callback function gets a shader cache value.

## Syntax

```
PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021 Pfnd3d12ddiShadercachegetvalueCb0021;

HRESULT Pfnd3d12ddiShadercachegetvalueCb0021(
  D3D12DDI_HRTDEVICE hRTDevice,
  D3D12DDI_HRTPIPELINESTATE hRTPSO,
  const D3D12DDI_SHADERCACHE_HASH *pPrecomputedHash,
  const void *pKey,
  SIZE_T KeyLen,
  void *pValue,
  SIZE_T *pValueLen
)
{...}
```

## Parameters

`hRTDevice`

The handle of the device for the driver to use when it calls back into the runtime.

`hRTPSO`

The handle of a PSO.

`*pPrecomputedHash`

A hash value.

`*pKey`

A pointer to a key.

`KeyLen`

The length of the key.

`*pValue`

A pointer to an output value.

`*pValueLen`

The length of the output value.


## Return Value

If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.

## Remarks

Access this callback by using the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi_shadercache_callbacks_0021.md">D3D12DDI_SHADERCACHE_CALLBACKS_0021</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |

## See Also

<a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi_shadercache_callbacks_0021.md">D3D12DDI_SHADERCACHE_CALLBACKS_0021</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021 callback function%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>