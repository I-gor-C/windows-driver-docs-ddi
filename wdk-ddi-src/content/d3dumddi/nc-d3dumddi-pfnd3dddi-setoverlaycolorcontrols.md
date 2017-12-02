---
UID: NC.d3dumddi.PFND3DDDI_SETOVERLAYCOLORCONTROLS
title: PFND3DDDI_SETOVERLAYCOLORCONTROLS
author: windows-driver-content
description: The SetOverlayColorControls function changes color-control settings for the given overlay.
old-location: display\setoverlaycolorcontrols.htm
old-project: display
ms.assetid: c2723c57-44eb-4866-9381-a3a341996989
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetOverlayColorControls
req.alt-loc: d3dumddi.h
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

# PFND3DDDI_SETOVERLAYCOLORCONTROLS callback



## -description
<p>The <i>SetOverlayColorControls</i> function changes color-control settings for the given overlay.</p>


## -prototype

````
PFND3DDDI_SETOVERLAYCOLORCONTROLS SetOverlayColorControls;

__checkReturn HRESULT APIENTRY SetOverlayColorControls(
  _In_       HANDLE                            hDevice,
  _In_ const D3DDDIARG_SETOVERLAYCOLORCONTROLS *pData
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param pData [in]

<dd>
<p> A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-setoverlaycolorcontrols.md">D3DDDIARG_SETOVERLAYCOLORCONTROLS</a> structure that describes parameters for changing an overlay's color-control settings.</p>
</dd>
</dl>

## -returns
<p><i>SetOverlayColorControls</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The color-control settings were successfully changed.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><i>SetOverlayColorControls</i> could not allocate the required memory for it to complete.</p>

<p> </p>

## -remarks
<p>The Microsoft Direct3D runtime calls the <i>SetOverlayColorControls</i> function to change the brightness, contrast, hue, saturation, sharpness, gamma, and color-enable settings that are associated with a specific overlay. </p>

<p>The runtime can also call <i>SetOverlayColorControls</i> for an overlay that is not yet visible. In this situation, when the <b>hOverlay</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-setoverlaycolorcontrols.md">D3DDDIARG_SETOVERLAYCOLORCONTROLS</a> structure pointed to by <i>pData</i> is set to <b>NULL</b>, the driver should store the supplied color-control settings and use them when an overlay that references the specified resource is created.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-setoverlaycolorcontrols.md">D3DDDIARG_SETOVERLAYCOLORCONTROLS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETOVERLAYCOLORCONTROLS callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
