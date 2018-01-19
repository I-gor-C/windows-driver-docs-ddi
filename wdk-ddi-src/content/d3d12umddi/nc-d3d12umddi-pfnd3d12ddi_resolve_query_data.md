---
UID : NC:d3d12umddi.PFND3D12DDI_RESOLVE_QUERY_DATA
title : PFND3D12DDI_RESOLVE_QUERY_DATA
author : windows-driver-content
description : The pfnResolveQueryData callback function transforms a previously stored query into an API defined format.
old-location : display\pfnd3d12ddi_resolve_query_data.htm
old-project : display
ms.assetid : 981053FF-9928-442F-B3B3-3B89AC61EEE4
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3D11_1DDI_GETCAPTUREHANDLEDATA, D3D11_1DDI_GETCAPTUREHANDLEDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d12umddi.h
req.include-header : D3d12umddi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnResolveQueryData
req.alt-loc : D3d12umddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_RESOLVE_QUERY_DATA callback function
The <i>pfnResolveQueryData</i> callback function transforms a previously stored query into an API defined format.

## Syntax

```
PFND3D12DDI_RESOLVE_QUERY_DATA Pfnd3d12ddiResolveQueryData;

void Pfnd3d12ddiResolveQueryData(
   D3D12DDI_HCOMMANDLIST,
   D3D12DDI_HQUERYHEAP,
   D3D12DDI_QUERY_TYPE,
  UINT StartElement,
  UINT ElementCount,
  D3D12DDI_HRESOURCE hDrvDestinationBuffer,
  UINT64 DestinationOffset
)
{...}
```

## Parameters

`D3D12DDI_HCOMMANDLIST`



`D3D12DDI_HQUERYHEAP`



`D3D12DDI_QUERY_TYPE`



`StartElement`

The value of the start element.

`ElementCount`

The element count.

`hDrvDestinationBuffer`

The handle of a destination buffer.

`DestinationOffset`

The destination offset.


## Return Value

This callback function does not return a value.

## Remarks

Resolve functionality is used by applications to transform a query result previously stored in a query heap into the API defined format.  The resolved data is stored in a buffer.  The results can then be consumed by a shader, predication, or mapped and read on the CPU.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |