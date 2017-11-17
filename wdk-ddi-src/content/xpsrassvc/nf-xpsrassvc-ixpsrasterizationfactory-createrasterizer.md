---
UID: NF.xpsrassvc.IXpsRasterizationFactory.CreateRasterizer
title: IXpsRasterizationFactory::CreateRasterizer
author: windows-driver-content
description: The CreateRasterize method creates an XPS rasterizer object.
old-location: print\ixpsrasterizationfactory_createrasterizer.htm
ms.assetid: 07d4f1ed-5dbe-47c1-96e8-dfe21e0c1d0d
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: xpsrassvc.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IXpsRasterizationFactory.CreateRasterizer
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
ms.keywords: IXpsRasterizationFactory, CreateRasterizer, IXpsRasterizationFactory::CreateRasterizer
req.iface: IXpsRasterizationFactory
req.product: Windows 10 or later.
---

# IXpsRasterizationFactory::CreateRasterizer method



## -description
<p>The <code>CreateRasterize</code> method creates an XPS rasterizer object.</p>


## -syntax

````
HRESULT CreateRasterizer(
  [in, optional]  IXpsOMPage            *xpsPage,
  [in]            FLOAT                 DPI,
  [in]            XPSRAS_RENDERING_MODE nonTextRenderingMode,
  [in]            XPSRAS_RENDERING_MODE textRenderingMode,
  [out, optional] IXpsRasterizer        **ppIXPSRasterizer
);
````


## -parameters
<dl>

### -param <i>xpsPage</i> [in, optional]

<dd>
<p>Pointer to an <b>IXpsOMPage</b> object that represents the XPS fixed page to render. This object encapsulates a FixedPage section from an XPS document. For more information about <b>IXpsOMPage</b>, see <a href="http://go.microsoft.com/fwlink/p/?linkid=146349">IXpsOMPage</a><u>.</u></p>
</dd>

### -param <i>DPI</i> [in]

<dd>
<p>Dots per inch in the rasterized output. This parameter applies to both the x and y dimensions of the output bitmap. The <i>DPI</i> value is the resolution of the device that is to print or display the XPS fixed page.</p>
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

### -param <i>ppIXPSRasterizer</i> [out, optional]

<dd>
<p>This parameter points to a location into which the method writes a pointer to the <a href="https://msdn.microsoft.com/1ef99120-2b3b-45aa-bcf7-16bcb9656089">IXpsRasterizer</a> interface of the newly created XPS rasterizer object. If the method fails, it writes <b>NULL</b> to this location and returns an error code.</p>
</dd>
</dl>

## -returns
<p><code>CreateRasterizer</code> returns S_OK if the call was successful. Otherwise, the method returns an error code. Possible error return values include:</p><dl>
<dt><b>E_POINTER</b></dt>
</dl><p>Parameter <i>xpsPage</i> or <i>ppIXPSRasterizer</i> is <b>NULL</b>.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameter <i>nonTextRenderingMode</i> or <i>textRenderingMode</i> is not a valid XPSRAS_RENDERING_MODE enumeration value.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>Out of memory.</p>

<p> </p>

<p></p>

## -remarks
<p>This method is supported in Windows 7 and later. It is not supported in versions of the Windows operating system before Windows 7.</p>

<p>Typically, an XPSDrv filter in an XPS pipeline calls this method to obtain an XPS rasterizer. It then uses the rasterizer to rasterize the XPS fixed page encapsulated by the object to which the parameter <i>xpsPage</i> points .</p>

<p>The parameter <i>DPI</i> specifies the printer resolution, which is assumed to be the same in both the horizontal and vertical dimensions. The width and height of the XPS fixed page, which can be obtained from the <b>IXpsOMPage::GetPageDimensions</b> method, are expressed in 1/96-inch units. Multiply these width and height values by <i>DPI</i>/96 to determine the width and height, in pixels, of the rasterized page. For more information about <b>IXpsOMPage::GetPageDimensions</b>, see <a href="http://go.microsoft.com/fwlink/p/?linkid=146350">IXpsOMPage</a>. For more information about how the XPS rasterizer object uses the DPI value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556365">IXpsRasterizer::RasterizeRect</a>.</p>

<p>If successful, the method creates an XPS rasterizer object and passes to the caller a counted reference to the object's <b>IXpsRasterizer</b> interface. When the object is no longer needed, the caller is responsible for releasing the object by calling the <a href="http://go.microsoft.com/fwlink/p/?linkid=98433">Release</a> method on the object's <b>IXpsRasterizer</b> interface.</p>

<p>If the method fails and <i>ppIXPSRasterizer</i> is non-<b>NULL</b>, the method sets *<i>ppIXPSRasterizer</i> = <b>NULL</b>.</p>

<p>For a code example that calls the <code>CreateRasterizer</code> method, see the XPSRasFilter sample in the WDK. This sample is located in the Src\Print\Xpsrasfilter folder in your WDK installation.</p>

<p>This method is supported in Windows 7 and later. It is not supported in versions of the Windows operating system before Windows 7.</p>

<p>Typically, an XPSDrv filter in an XPS pipeline calls this method to obtain an XPS rasterizer. It then uses the rasterizer to rasterize the XPS fixed page encapsulated by the object to which the parameter <i>xpsPage</i> points .</p>

<p>The parameter <i>DPI</i> specifies the printer resolution, which is assumed to be the same in both the horizontal and vertical dimensions. The width and height of the XPS fixed page, which can be obtained from the <b>IXpsOMPage::GetPageDimensions</b> method, are expressed in 1/96-inch units. Multiply these width and height values by <i>DPI</i>/96 to determine the width and height, in pixels, of the rasterized page. For more information about <b>IXpsOMPage::GetPageDimensions</b>, see <a href="http://go.microsoft.com/fwlink/p/?linkid=146350">IXpsOMPage</a>. For more information about how the XPS rasterizer object uses the DPI value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556365">IXpsRasterizer::RasterizeRect</a>.</p>

<p>If successful, the method creates an XPS rasterizer object and passes to the caller a counted reference to the object's <b>IXpsRasterizer</b> interface. When the object is no longer needed, the caller is responsible for releasing the object by calling the <a href="http://go.microsoft.com/fwlink/p/?linkid=98433">Release</a> method on the object's <b>IXpsRasterizer</b> interface.</p>

<p>If the method fails and <i>ppIXPSRasterizer</i> is non-<b>NULL</b>, the method sets *<i>ppIXPSRasterizer</i> = <b>NULL</b>.</p>

<p>For a code example that calls the <code>CreateRasterizer</code> method, see the XPSRasFilter sample in the WDK. This sample is located in the Src\Print\Xpsrasfilter folder in your WDK installation.</p>

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
<p>Available in Windows 7 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Xpsrassvc.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/1ef99120-2b3b-45aa-bcf7-16bcb9656089">IXpsRasterizer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556365">IXpsRasterizer::RasterizeRect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564291">XPSRAS_RENDERING_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IXpsRasterizationFactory::CreateRasterizer method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
