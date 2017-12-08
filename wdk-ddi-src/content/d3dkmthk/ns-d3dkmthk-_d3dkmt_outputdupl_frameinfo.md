---
UID: NS.D3DKMTHK._D3DKMT_OUTPUTDUPL_FRAMEINFO
title: _D3DKMT_OUTPUTDUPL_FRAMEINFO
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outputdupl_frameinfo.htm
old-project: display
ms.assetid: e35389b2-52aa-4481-a5d7-6c45c795885f
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_OUTPUTDUPL_FRAMEINFO, D3DKMT_OUTPUTDUPL_FRAMEINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OUTPUTDUPL_FRAMEINFO
req.alt-loc: D3dkmthk.h
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

# _D3DKMT_OUTPUTDUPL_FRAMEINFO structure



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef struct _D3DKMT_OUTPUTDUPL_FRAMEINFO {
  LARGE_INTEGER                      LastPresentTime;
  LARGE_INTEGER                      LastMouseUpdateTime;
  UINT                               AccumulatedFrames;
  BOOL                               RectsCoalesced;
  BOOL                               ProtectedContentMaskedOut;
  D3DKMT_OUTPUTDUPL_POINTER_POSITION PointerPosition;
  UINT                               TotalMetadataBufferSize;
  UINT                               PointerShapeBufferSize;
} D3DKMT_OUTPUTDUPL_FRAMEINFO;
````


## -struct-fields

### -field LastPresentTime


### -field LastMouseUpdateTime


### -field AccumulatedFrames


### -field RectsCoalesced


### -field ProtectedContentMaskedOut


### -field PointerPosition


### -field TotalMetadataBufferSize


### -field PointerShapeBufferSize


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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>