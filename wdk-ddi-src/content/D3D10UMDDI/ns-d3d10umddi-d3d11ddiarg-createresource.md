---
UID: NS.d3d10umddi.D3D11DDIARG_CREATERESOURCE
title: D3D11DDIARG_CREATERESOURCE
author: windows-driver-content
description: Describes a resource to create.
old-location: display\d3d11ddiarg_createresource.htm
ms.assetid: 4cdc5d74-ef53-47aa-91ed-0b71dfe688dc
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDIARG_CREATERESOURCE is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11DDIARG_CREATERESOURCE
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
ms.keywords: D3D11DDIARG_CREATERESOURCE, D3D11DDIARG_CREATERESOURCE
req.iface: 
---

# D3D11DDIARG_CREATERESOURCE structure



## -description
<p>Describes a resource to create.</p>


## -syntax

````
typedef struct D3D11DDIARG_CREATERESOURCE {
  const D3D10DDI_MIPINFO               *pMipInfoList;
  const D3D10_DDIARG_SUBRESOURCE_UP    *pInitialDataUP;
  D3D10DDIRESOURCE_TYPE                ResourceDimension;
  UINT                                 Usage;
  UINT                                 BindFlags;
  UINT                                 MapFlags;
  UINT                                 MiscFlags;
  DXGI_FORMAT                          Format;
  DXGI_SAMPLE_DESC                     SampleDesc;
  UINT                                 MipLevels;
  UINT                                 ArraySize;
  DXGI_DDI_PRIMARY_DESC                *pPrimaryDesc;
  UINT                                 ByteStride;
#if D3D11DDI_MINOR_HEADER_VERSION >= 3
  D3D11_1DDI_VIDEO_DECODER_BUFFER_TYPE DecoderBufferType;
#endif 
} D3D11DDIARG_CREATERESOURCE;
````


## -struct-fields
<dl>

### -field <b>pMipInfoList</b>

<dd>
<p>[in] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff541845">D3D10DDI_MIPINFO</a> structures that contains dimensions for MIP levels. For resource formats where a single pixel or texel cannot be referenced directly with a byte address, the dimensions of the physical resource are typically larger or equal to the texel dimensions, in order to satisfy the necessary space requirements. For example, to create a fully mipped BC1 Texture2D, where the most detailed level is 8x8, the <b>pMipInfoList</b> array is:  { { 8, 8, 1, 8, 8, 1 }, { 4, 4, 1, 4, 4, 1 }, { 2, 2, 1, 4, 4, 1 }, { 1, 1, 1, 4, 4, 1 } }. </p>
</dd>

### -field <b>pInitialDataUP</b>

<dd>
<p>[in] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff541909">D3D10_DDIARG_SUBRESOURCE_UP</a> structures that provides initialization information for the resource's list of subresources.</p>
</dd>

### -field <b>ResourceDimension</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a> that indicates the resource type and dimensionality.</p>
</dd>

### -field <b>Usage</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff542008">D3D10_DDI_RESOURCE_USAGE</a> that indicates how the resource is used.</p>
</dd>

### -field <b>BindFlags</b>

<dd>
<p>[in] A valid bitwise OR of values of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541995">D3D10_DDI_RESOURCE_BIND_FLAG</a> that indicates how the resource is bound.</p>
</dd>

### -field <b>MapFlags</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541957">D3D10_DDI_MAP</a> that indicates the access level to map to the resource.</p>
</dd>

### -field <b>MiscFlags</b>

<dd>
<p>[in] A valid bitwise OR of values of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff542004">D3D10_DDI_RESOURCE_MISC_FLAG</a> that indicates miscellaneous information about the resource.</p>
</dd>

### -field <b>Format</b>

<dd>
<p>[in] A value of type <a href="direct3ddxgi.dxgi_format">DXGI_FORMAT</a> that indicates the pixel format of the resource.</p>
</dd>

### -field <b>SampleDesc</b>

<dd>
<p>[in] A value of type <a href="direct3ddxgi.dxgi_sample_desc">DXGI_SAMPLE_DESC</a> that describes the sample count and quality of the resource.</p>
</dd>

### -field <b>MipLevels</b>

<dd>
<p>[in] The number of MIP-map levels for the resource.</p>
</dd>

### -field <b>ArraySize</b>

<dd>
<p>[in] The number of array elements for a 2-D texture or 1-D texture. <b>ArraySize</b> must be set to 6 for a cube texture.</p>
<p>Beginning in Windows 8, if the driver must create a stereo back buffer, it should set the <b>ArraySize</b> member of the <b>D3D11DDIARG_CREATERESOURCE</b> structure to a value of 2.</p>
</dd>

### -field <b>pPrimaryDesc</b>

<dd>
<p>[in, out] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff557511">DXGI_DDI_PRIMARY_DESC</a> structure that describes a resource that is used as a primary.</p>
<p>The Microsoft Direct3D runtime sets <b>pPrimaryDesc</b> to a non-<b>NULL</b> value only if the D3D10_DDI_BIND_PRESENT bit is set in the <b>BindFlags</b> member; however, even if D3D10_DDI_BIND_PRESENT is set, the runtime does not always set <b>pPrimaryDesc</b> to non-<b>NULL</b>. Setting <b>pPrimaryDesc</b> to non-<b>NULL</b> indicates that the runtime will use the created resource as a primary (that is, the resource is scanned out to the display) and in flip-style present operations. </p>
<p>The user-mode display driver can return the DXGI_DDI_PRIMARY_DRIVER_FLAG_NO_SCANOUT flag in the <b>DriverFlags</b> member of DXGI_DDI_PRIMARY_DESC to prevent the runtime from performing flip-style present operations. </p>
<p>If <b>pPrimaryDesc</b> is set to <b>NULL</b>, the runtime will use the created resource in; copy-style (bit-block transfer) present operations. </p>
</dd>

### -field <b>ByteStride</b>

<dd>
<p>[in] The size, in bytes, from one scan line to the next scan line in the surface. </p>
</dd>

### -field <b>DecoderBufferType</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/hh451066">D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE</a> that indicates the  buffer type used by the video decoder.</p>
<p>If the driver does not check that D3D11DDI_MINOR_HEADER_VERSION &gt;= 3 before accessing this  structure member, it should access this member only when the D3D11_DDI_BIND_DECODER flag is set in the <b>BindFlags</b> member.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D11DDIARG_CREATERESOURCE is supported beginning with the Windows 7 operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/2dff9d2e-c497-422f-824b-a7101904fd67">CreateResource(D3D11)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541957">D3D10_DDI_MAP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541995">D3D10_DDI_RESOURCE_BIND_FLAG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542004">D3D10_DDI_RESOURCE_MISC_FLAG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542008">D3D10_DDI_RESOURCE_USAGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451066">D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541909">D3D10_DDIARG_SUBRESOURCE_UP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541845">D3D10DDI_MIPINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541810">D3D10DDIRESOURCE_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557511">DXGI_DDI_PRIMARY_DESC</a>
</dt>
<dt>
<a href="direct3ddxgi.dxgi_format">DXGI_FORMAT</a>
</dt>
<dt>
<a href="direct3ddxgi.dxgi_sample_desc">DXGI_SAMPLE_DESC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11DDIARG_CREATERESOURCE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
