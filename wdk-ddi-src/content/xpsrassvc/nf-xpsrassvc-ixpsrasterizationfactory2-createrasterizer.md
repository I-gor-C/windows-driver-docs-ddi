---
UID: NF.xpsrassvc.IXpsRasterizationFactory2.CreateRasterizer
title: IXpsRasterizationFactory2::CreateRasterizer
author: windows-driver-content
description: The CreateRasterizer method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs.
old-location: print\ixpsrasterizationfactory2_createrasterizer.htm
old-project: print
ms.assetid: C31681A0-17C6-4255-9068-7486A2101AB7
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IXpsRasterizationFactory2, CreateRasterizer, IXpsRasterizationFactory2::CreateRasterizer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
req.iface: IXpsRasterizationFactory2
req.product: Windows 10 or later.
---

# IXpsRasterizationFactory2::CreateRasterizer method



## -description
<p>The <b>CreateRasterizer</b> method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the <a href="print.xps_rasterization_service_reference">XPS Rasterization Service</a>. PWG Raster supports non-square DPIs.
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

### -param *xpsPage [in, optional]

<dd>
<p>Pointer to an <b>IXpsOMPage</b> object that represents the XPS fixed page to render. This object encapsulates a FixedPage section from an XPS document. </p>
</dd>

### -param dpiX [in]

<dd>
<p>Dots per inch which is applied to x dimension of the rasterized output bitmap. The DPI value is the resolution of the device that is to print or display the XPS fixed page.</p>
</dd>

### -param dpiY [in]

<dd>
<p>Dots per inch which is applied to y dimension of the rasterized output bitmap.</p>
</dd>

### -param nonTextRenderingMode [in]

<dd>
<p>Rendering mode for nontext items in the rasterized output. This parameter indicates whether to generate antialiased output. Set this parameter to one of the following <a href="print.xpsras_rendering_mode_enumeration">XPSRAS_RENDERING_MODE</a> enumeration values:</p>
<ul>
<li>
<p>XPSRAS_RENDERING_MODE_ANTIALIASED</p>
</li>
<li>
<p>XPSRAS_RENDERING_MODE_ALIASED</p>
</li>
</ul>
</dd>

### -param textRenderingMode [in]

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

### -param pixelFormat [in]

<dd>
<p>Allows a caller to select the pixel format used by the IWICBitmap returned by <a href="print.ixpsrasterizer_rasterizerect">IXpsRasterizer::RasterizeRect</a>. Set this parameter to one of the following <a href="print.xpsras_pixel_format">XPSRAS_PIXEL_FORMAT</a> enumeration values:</p>
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

### -param backgroundColor [in]

<dd>
<p>Allows a caller to select background color. Set this parameter to one of the following <a href="print.xpsras_background_color">XPSRAS_BACKGROUND_COLOR</a> enumeration values:</p>
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

### -param **ppIXpsRasterizer [out, optional]

<dd>
<p>This parameter points to a location into which the method writes a pointer to the <a href="print.ixpsrasterizer_interface">IXpsRasterizer</a> interface of the newly created XPS rasterizer object. If the method fails, it writes <b>NULL</b> to this location and returns an error code.
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
<a href="..\xpsrassvc\nn-xpsrassvc-ixpsrasterizationfactory2.md">IXpsRasterizationFactory2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IXpsRasterizationFactory2::CreateRasterizer method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
