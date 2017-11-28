---
UID: NC.d3d12umddi.PFND3D12DDI_VIDEO_GETCAPS
title: PFND3D12DDI_VIDEO_GETCAPS
author: windows-driver-content
description: The pfnGetCaps callback function defines an entry point for video specific caps.
old-location: display\pfnd3d12ddi_video_getcaps.htm
old-project: display
ms.assetid: 6875B754-115F-481D-8D46-2A383BA6B5E7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
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
req.alt-api: pfnGetCaps
req.alt-loc: D3d12umddi.h
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
req.iface: 
---

# PFND3D12DDI_VIDEO_GETCAPS callback



## -description
<p>The <i>pfnGetCaps</i> callback function defines an entry point for video specific caps.</p>


## -prototype

````
PFND3D12DDI_VIDEO_GETCAPS pfnGetCaps;

HRESULT APIENTRY* pfnGetCaps(
             D3D12DDI_HDEVICE          hDrvDevice,
  _In_ const D3D12DDIARG_VIDEO_GETCAPS *pArgs
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDrvDevice</i> 

<dd>
<p>The handle of a device.</p>
</dd>

### -param <i>pArgs</i> [in]

<dd>
<p> Values used to get capabilities.</p>
</dd>
</dl>

## -returns
<p>If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks
<p>Access this function though the <a href="display.d3d12ddi_video_decode_support_data">D3D12DDI_VIDEO_DECODE_SUPPORT_DATA</a> structure.</p>

<p>The following list describes the mapping of D3D12DDICAPS_TYPE_VIDEO_0010 type to the meaning of the pInfo, pData, and DataSize parameters.</p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_SUPPORT</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_PROFILES</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_FORMATS </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_CONVERSION_SUPPORT </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_BITSTREAM_ENCRYPTION_SCHEMES</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_PROCESS_SUPPORT </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_PROCESS_MAX_INPUT_STREAMS </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_PROCESS_REFERENCE_INFO </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_0032_DECODER_HEAP_SIZE</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_PROFILE_COUNT</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_PROFILE_FORMAT_COUNT</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_BITSTREAM_ENCRYPTION_SCHEME_COUNT</p>

<p> </p>

<p>Access this function though the <a href="display.d3d12ddi_video_decode_support_data">D3D12DDI_VIDEO_DECODE_SUPPORT_DATA</a> structure.</p>

<p>The following list describes the mapping of D3D12DDICAPS_TYPE_VIDEO_0010 type to the meaning of the pInfo, pData, and DataSize parameters.</p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_SUPPORT</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_PROFILES</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_FORMATS </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_CONVERSION_SUPPORT </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_BITSTREAM_ENCRYPTION_SCHEMES</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_PROCESS_SUPPORT </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_PROCESS_MAX_INPUT_STREAMS </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_PROCESS_REFERENCE_INFO </p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_0032_DECODER_HEAP_SIZE</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_PROFILE_COUNT</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_PROFILE_FORMAT_COUNT</p>

<p> </p>

<p>D3D12DDICAPS_TYPE_VIDEO_DECODE_BITSTREAM_ENCRYPTION_SCHEME_COUNT</p>

<p> </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3d12ddi_video_decode_support_data">D3D12DDI_VIDEO_DECODE_SUPPORT_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D12DDI_VIDEO_GETCAPS callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
