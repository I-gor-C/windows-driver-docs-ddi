---
UID: NS.iddcx.IDDCX_METADATA~r1
title: IDDCX_METADATA
author: windows-driver-content
description: Gives information about the current provided surface and what is displayed on it.
old-location: display\iddcx_metadata.htm
old-project: display
ms.assetid: 7128e49d-71e9-4014-9f08-591cfaeba363
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_METADATA,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_METADATA
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDDCX_METADATA structure



## -description
<p>
                 Gives information about the current provided surface and what is displayed on it.</p>


## -syntax

````
typedef struct IDDCX_METADATA {
  UINT           Size;
  UINT           PresentationFrameNumber;
  UINT           DirtyRectCount;
  UINT           MoveRegionCount;
  BOOL           HwProtectedSurface;
  UINT64         PresentDisplayQPCTime;
  IDXGIResource* pSurface;
} IDDCX_METADATA, *IDDCX_METADATA;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>
                     Total size of the structure
                 </p>
</dd>

### -field <b>PresentationFrameNumber</b>

<dd>
<p>
                     Presentation frame number of this surface. If the frame number is the same as the previous frame, then it indicates that there has not been any image updates from the previous frame. This is an opportunity for the driver to re-encode the desktop image again to increase the visual quality. Once there are no more updates, the OS presents the same frame as many times indicated by the <a href="..\iddcx\ns-iddcx-iddcx-adapter-caps.md">IDDCX_ADAPTER_CAPS</a> value <b>StaticDesktopReencodeFrameCount</b> , then stops presenting until the next update
                 </p>
</dd>

### -field <b>DirtyRectCount</b>

<dd>
<p>
                      Number of dirty rects for this frame. Call <a href="..\iddcx\nf-iddcx-iddcxswapchaingetdirtyrects.md">IddCxSwapChainGetDirtyRects</a> to get the dirty rects
                 </p>
<div class="alert"><b>Note</b>   A zero <b>DirtyRectCount</b> and <b>MoveRegionCount</b> value indicates there were no desktop updates and the
    PresentationFrameNumber is the same as last frame</div>
<div> </div>
</dd>

### -field <b>MoveRegionCount</b>

<dd>
<p>
                     Number of move regions in this frame, call <a href="..\iddcx\nf-iddcx-iddcxswapchaingetmoveregions.md">IddCxSwapChainGetMoveRegions</a> to get the move regions
                 </p>
<div class="alert"><b>Note</b>   A zero <b>DirtyRectCount</b> and <b>MoveRegionCount</b> value indicates there were no desktop updates and the
    PresentationFrameNumber is the same as last frame</div>
<div> </div>
</dd>

### -field <b>HwProtectedSurface</b>

<dd>
<p>
                      Indicates if the provided surface is hardware protected or not
                 </p>
</dd>

### -field <b>PresentDisplayQPCTime</b>

<dd>
<p>
                     System QPC time of when this surface should be displayed on the indirect display monitor
                 </p>
</dd>

### -field <b>pSurface</b>

<dd>
<p>
                     DX surface that contains the image to encode and transmit. The driver can use this DX surface anytime until <a href="..\iddcx\nf-iddcx-iddcxswapchainreleaseandacquirebuffer.md">IddCxSwapChainReleaseAndAcquire</a> is called again</p>
<div class="alert"><b>Note</b>  This surface is always a A8R8G8B8 formated surface</div>
<div> </div>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>