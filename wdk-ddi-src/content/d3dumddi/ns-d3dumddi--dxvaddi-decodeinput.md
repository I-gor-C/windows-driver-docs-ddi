---
UID: NS.d3dumddi._DXVADDI_DECODEINPUT
title: DXVADDI_DECODEINPUT
author: windows-driver-content
description: The DXVADDI_DECODEINPUT structure describes a render target format that is supported by a Microsoft DirectX Video Acceleration (DirectX VA) decode type.
old-location: display\dxvaddi_decodeinput.htm
old-project: display
ms.assetid: 6f62ce8d-058b-4838-bc7a-fae84c1b5111
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVADDI_DECODEINPUT, DXVADDI_DECODEINPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_DECODEINPUT
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

# DXVADDI_DECODEINPUT structure



## -description
<p>The DXVADDI_DECODEINPUT structure describes a render target format that is supported by a Microsoft DirectX Video Acceleration (DirectX VA) decode type. </p>


## -syntax

````
typedef struct _DXVADDI_DECODEINPUT {
  const GUID        *pGuid;
  DXVADDI_VIDEODESC VideoDesc;
} DXVADDI_DECODEINPUT;
````


## -struct-fields
<dl>

### -field <b>pGuid</b>

<dd>
<p>[in] A pointer to the GUID that represents the DirectX VA decode type.</p>
</dd>

### -field <b>VideoDesc</b>

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videodesc.md">DXVADDI_VIDEODESC</a> structure for the render target that is supported by the decode type that <b>pGuid</b> points to. </p>
</dd>
</dl>

## -remarks
<p>A pointer to the DXVADDI_DECODEINPUT structure is specified in the <b>pInfo</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a> structure--along with a D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFO value in the <b>Type</b> member of D3DDDIARG_GETCAPS--in a call to the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> function to retrieve information about the types of compressed buffers that are required to decode video. The compressed buffer information is returned in a pointer to a <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodebufferinfo.md">DXVADDI_DECODEBUFFERINFO</a> structure through the <b>pData</b> member of D3DDDIARG_GETCAPS.</p>

## -requirements
<table>
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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ne-d3dumddi--d3dddicaps-type.md">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodebufferinfo.md">DXVADDI_DECODEBUFFERINFO</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_DECODEINPUT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
