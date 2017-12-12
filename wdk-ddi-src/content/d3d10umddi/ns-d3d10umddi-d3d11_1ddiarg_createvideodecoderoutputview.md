---
UID: NS.D3D10UMDDI.D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW
title: D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW
author: windows-driver-content
description: Describes the video decoder's output-view state.
old-location: display\d3d11_1ddiarg_createvideodecoderoutputview.htm
old-project: display
ms.assetid: 6DD555B1-01E8-48DE-B957-2752671B7EBB
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW, D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW
req.alt-loc: d3d10umddi.h
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
---

# D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW structure



## -description
Describes the video decoder's output-view state.



## -syntax

````
typedef struct _D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW {
  D3D10DDI_HRESOURCE hDrvResource;
  GUID               DecodeProfile;
  UINT               MipSlice;
  UINT               FirstArraySlice;
  UINT               ArraySize;
} D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW, *PD3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW;
````


## -struct-fields

### -field hDrvResource

A handle to the video decoder output resource.


### -field DecodeProfile

The decode profile to be used in conjunction with the encryption.


### -field MipSlice

The identifier of the MIP-map slice.


### -field FirstArraySlice

The identifier of the first array slice.


### -field ArraySize

The number of array slices for the texture.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 8

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2012

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>