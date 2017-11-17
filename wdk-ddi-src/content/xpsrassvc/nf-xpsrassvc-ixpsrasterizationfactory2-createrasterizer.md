---
UID: NF.xpsrassvc.IXpsRasterizationFactory2.CreateRasterizer
title: IXpsRasterizationFactory2::CreateRasterizer
author: windows-driver-content
description: The CreateRasterizer method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs.
old-location: print\ixpsrasterizationfactory2_createrasterizer.htm
ms.assetid: C31681A0-17C6-4255-9068-7486A2101AB7
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: xpsrassvc.h
req.include-header: Xpsrassvc.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IXpsRasterizationFactory2.CreateRasterizer
req.alt-loc: xpsrassvc.h
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
ms.keywords: IXpsRasterizationFactory2, CreateRasterizer, IXpsRasterizationFactory2::CreateRasterizer
req.iface: IXpsRasterizationFactory2
req.product: Windows 10 or later.
---

# IXpsRasterizationFactory2::CreateRasterizer method



## -description
<p>The <b>CreateRasterizer</b> method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the <a href="https://msdn.microsoft.com/a0493b5f-d6f7-4f69-9c6e-e112c29250c9">XPS Rasterization Service</a>. PWG Raster supports non-square DPIs.
</p>


## -syntax

````
HRESULT CreateRasterizer(
  [in, optional]  IXpsOMPage              *xpsPage,
  [in]            FLOAT                   dpiX,
  [in]            FLOAT                   dpiY,
  [in]            XPSRAS_RENDERING_MODE   nonTextRenderingMode,
  [in]            XPSRAS_RENDERING_MODE   textRenderingMode,
  [in]            XPSRAS_PIXEL_FORMAT     pixelFormat,
  [in]            XPSRAS_BACKGROUND_COLOR backgroundColor,
  [out, optional] IXpsRasterizer          **ppIXpsRasterizer
);
````


## -parameters
<dl>

### -param <i>*xpsPage</i> [in, optional]

<dd>
<p>Pointer to an <b>IXpsOMPage</b> object that represents the XPS fixed page to render. This object encapsulates a FixedPage section from an XPS document. </p>
</dd>

### -param <i>dpiX</i> [in]

<dd>
<p>Dots per inch which is applied to x dimension of the rasterized output bitmap. The DPI value is the resolution of the device that is to print or display the XPS fixed page.</p>
</dd>

### -param <i>dpiY</i> [in]

<dd>
<p>Dots per inch which is applied to y dimension of the rasterized output bitmap.</p>
</dd>

### -param <i>nonTextRenderingMode</i> [in]

<dd>
<p>Rendering mode for nontext items in the rasterized output. This parameter indicates whether to generate antialiased output. Set this parameter to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff564291">XPSRAS_RENDERING_MODE</a> enumeration values:</p>
<ul>
<li>
<p>XPSRAS_RENDERING_MODE_ANTIALIASED</p>
</li>
<li>
<p>XPSRAS_RENDERING_MODE_ALIASED</p>
</li>
</ul>
</dd>

### -param <i>textRenderingMode</i> [in]

<dd>
<p>Rendering mode for text in the rasterized output. This parameter indicates whether to generate antialiased output. Set this parameter to one of the following XPSRAS_RENDERING_MODE enumeration values:</p>
<ul>
<li>
<p>XPSRAS_RENDERING_MODE_ANTIALIASED</p>
</li>
<li>
<p>XPSRAS_RENDERING_MODE_ALIASED</p>
</li>
</ul>
</dd>

### -param <i>pixelFormat</i> [in]

<dd>
<p>Allows a caller to select the pixel format used by the IWICBitmap returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff556365">IXpsRasterizer::RasterizeRect</a>. Set this parameter to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/hh802469">XPSRAS_PIXEL_FORMAT</a> enumeration values:</p>
<ul>
<li>
<p>XPSRAS_PIXEL_FORMAT_32BPP_PBGRA_UINT_SRGB</p>
</li>
<li>
<p>XPSRAS_PIXEL_FORMAT_64BPP_PRGBA_HALF_SCRGB</p>
</li>
<li>
<p>XPSRAS_PIXEL_FORMAT_128BPP_PRGBA_FLOAT_SCRGB</p>
</li>
</ul>
</dd>

### -param <i>backgroundColor</i> [in]

<dd>
<p>Allows a caller to select background color. Set this parameter to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/dn897481">XPSRAS_BACKGROUND_COLOR</a> enumeration values:</p>
<ul>
<li>
<p>XPSRAS_BACKGROUND_COLOR_TRANSPARENT</p>
</li>
<li>
<p>XPSRAS_BACKGROUND_COLOR_OPAQUE</p>
</li>
</ul>
<p>The default background color is XPSRAS_BACKGROUND_COLOR_TRANSPARENT.</p>
</dd>

### -param <i>**ppIXpsRasterizer</i> [out, optional]

<dd>
<p>This parameter points to a location into which the method writes a pointer to the <a href="https://msdn.microsoft.com/1ef99120-2b3b-45aa-bcf7-16bcb9656089">IXpsRasterizer</a> interface of the newly created XPS rasterizer object. If the method fails, it writes <b>NULL</b> to this location and returns an error code.
</p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b>S_OK</b>. Otherwise, it returns an <b>HRESULT</b> error code.</p>

## -remarks


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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Xpsrassvc.h (include Xpsrassvc.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn937110">IXpsRasterizationFactory2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IXpsRasterizationFactory2::CreateRasterizer method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
