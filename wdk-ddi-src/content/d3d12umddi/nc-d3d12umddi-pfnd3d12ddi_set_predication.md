---
UID: NC:d3d12umddi.PFND3D12DDI_SET_PREDICATION
title: PFND3D12DDI_SET_PREDICATION
author: windows-driver-content
description: The pfnSetPredication callback function denotes that subsequent video operations and resource manipulation commands are not actually performed if the resulting predicate data of the predicate is equal to the operation specified.
old-location: display\pfnd3d12ddi_set_predication.htm
old-project: display
ms.assetid: C5830688-4FC6-4D3F-82EB-15354B28C5F1
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D12DDI_SET_PREDICATION, d3d12umddi/pfnSetPredication, display.pfnd3d12ddi_set_predication, pfnSetPredication, pfnSetPredication callback function [Display Devices]
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
-	pfnSetPredication
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_SET_PREDICATION callback function
The <i>pfnSetPredication</i> callback function denotes that subsequent video operations and resource manipulation commands are not actually performed if the resulting predicate data of the predicate is equal to the operation specified.

## Syntax

```
PFND3D12DDI_SET_PREDICATION Pfnd3d12ddiSetPredication;

void Pfnd3d12ddiSetPredication(
   D3D12DDI_HCOMMANDLIST,
   D3D12DDI_HRESOURCE,
   UINT64,
   D3D12DDI_PREDICATION_OP
)
{...}
```

## Parameters

`D3D12DDI_HCOMMANDLIST`



`D3D12DDI_HRESOURCE`



`UINT64`



`D3D12DDI_PREDICATION_OP`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |

## See Also

<a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi_predication_op.md">D3D12DDI_PREDICATION_OP</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D12DDI_SET_PREDICATION callback function%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>