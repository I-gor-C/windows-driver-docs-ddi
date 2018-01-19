---
UID : NC:d3d12umddi.PFND3D12DDI_VIDEO_GET_BITSTREAM_ENCRYPTION_SCHEME_COUNT_0020
title : PFND3D12DDI_VIDEO_GET_BITSTREAM_ENCRYPTION_SCHEME_COUNT_0020
author : windows-driver-content
description : The pfnGetBitstreamEncryptionSchemeCount callback function retrieves the number of encryption schemes supported for a decode profile.
old-location : display\pfnd3d12ddi_video_get_decode_bitstream_encryption_scheme_count.htm
old-project : display
ms.assetid : BD3DFB48-9470-45CC-93BC-A918FD43DC3F
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3D11_1DDI_GETCAPTUREHANDLEDATA, D3D11_1DDI_GETCAPTUREHANDLEDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d12umddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnGetBitstreamEncryptionSchemeCount
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


# PFND3D12DDI_VIDEO_GET_BITSTREAM_ENCRYPTION_SCHEME_COUNT_0020 callback function
The <i>pfnGetBitstreamEncryptionSchemeCount</i> callback function retrieves the number of encryption schemes supported for a decode profile.

## Syntax

```
PFND3D12DDI_VIDEO_GET_BITSTREAM_ENCRYPTION_SCHEME_COUNT_0020 Pfnd3d12ddiVideoGetBitstreamEncryptionSchemeCount0020;

UINT Pfnd3d12ddiVideoGetBitstreamEncryptionSchemeCount0020(
   D3D12DDI_HDEVICE,
  UINT NodeIndex,
  REFGUID DecodeProfile
)
{...}
```

## Parameters

`D3D12DDI_HDEVICE`



`NodeIndex`

The physical adapter of the device to which this operation applies.

`DecodeProfile`

The decode profile GUID to retrieve the count of supported encryption GUIDs.


## Return Value

This function retrieves the number of encryption schemes supported for a decode profile.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |