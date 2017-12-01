---
UID: NS.d3dumddi._DXVADDI_DECODEBUFFERINFO
title: DXVADDI_DECODEBUFFERINFO
author: windows-driver-content
description: The DXVADDI_DECODEBUFFERINFO structure describes information about a particular type of compressed buffer that is required for a video decoding scenario.
old-location: display\dxvaddi_decodebufferinfo.htm
old-project: display
ms.assetid: e0a0ad31-86c1-44bd-b069-70442973a539
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVADDI_DECODEBUFFERINFO, DXVADDI_DECODEBUFFERINFO
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
req.alt-api: DXVADDI_DECODEBUFFERINFO
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

# DXVADDI_DECODEBUFFERINFO structure



## -description
<p>The DXVADDI_DECODEBUFFERINFO structure describes information about a particular type of compressed buffer that is required for a video decoding scenario. </p>


## -syntax

````
typedef struct _DXVADDI_DECODEBUFFERINFO {
  D3DDDIFORMAT CompressedBufferType;
  UINT         CreationWidth;
  UINT         CreationHeight;
  D3DDDI_POOL  CreationPool;
} DXVADDI_DECODEBUFFERINFO;
````


## -struct-fields
<dl>

### -field <b>CompressedBufferType</b>

<dd>
<p>[out] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the buffer.</p>
</dd>

### -field <b>CreationWidth</b>

<dd>
<p>[out] The width of the data in the buffer as the number of units of bits. For example, AYUV data is specified in 32-bit units, IA44/AI44 data is specified in 8-bit units, and DPXD data is specified in 2-bit units.</p>
<p>The driver must assign a value to <b>CreationWidth</b> that is a multiple of 2 and does not exceed 65535.</p>
</dd>

### -field <b>CreationHeight</b>

<dd>
<p>[out] The height of the data in the buffer as the number of units of bits. For example, AYUV data is specified in 32-bit units, IA44/AI44 data is specified in 8-bit units, and DPXD data is specified in 2-bit units.</p>
<p>The driver must assign a value to <b>CreationHeight</b> that does not exceed 65535.</p>
</dd>

### -field <b>CreationPool</b>

<dd>
<p>[out] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-pool.md">D3DDDI_POOL</a>-typed value that indicates the type of memory that the buffer exists in.</p>
</dd>
</dl>

## -remarks
<p>A pointer to the <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodeinput.md">DXVADDI_DECODEINPUT</a> structure is specified in the <b>pInfo</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a> structure--along with a D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFO value in the <b>Type</b> member of D3DDDIARG_GETCAPS--in a call to the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> function to retrieve information about the types of compressed buffers that are required to accelerate a particular DirectX VA video decode type. The information about the types of compressed buffers is returned in an array of DXVADDI_DECODEBUFFERINFO structures through the <b>pData</b> member of D3DDDIARG_GETCAPS.</p>

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
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-decodeinput.md">DXVADDI_DECODEINPUT</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_DECODEBUFFERINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
