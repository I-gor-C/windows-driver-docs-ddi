---
UID: NF.xpsrassvc.IXpsRasterizer.SetMinimalLineWidth
title: IXpsRasterizer::SetMinimalLineWidth
author: windows-driver-content
description: The SetMinimalLineWidth method allows the caller to set the minimum thickness (in pixels) of the lines that the device can render.
old-location: print\ixpsrasterizer_setminimallinewidth.htm
ms.assetid: daf84d1a-d499-4a6e-be87-39fd16f3d87d
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
req.alt-api: IXpsRasterizer.SetMinimalLineWidth
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
ms.keywords: IXpsRasterizer, SetMinimalLineWidth, IXpsRasterizer::SetMinimalLineWidth
req.iface: IXpsRasterizer
req.product: Windows 10 or later.
---

# IXpsRasterizer::SetMinimalLineWidth method



## -description
<p>The <code>SetMinimalLineWidth</code> method allows the caller to set the minimum thickness (in pixels) of the lines that the device can render. The default minimum thickness value is 1 pixel if <code>SetMinimalLineWidth</code> is not called. This minimum thickness value only applies to the Nominal Width Stroke as defined in the XPS Specification v1.0,  Sec 11.6.12. <b>IXpsRasterizer</b> requires that any Nominal Width Stroke is rasterized with either the width specified by its <b>StrokeThickness</b> attribute, or the pixel value set by <code>SetMinimalLineWidth</code> (1 pixel if <code>SetMinimalLineWidth</code> is not called), whichever is bigger.</p>


## -syntax

````
HRESULT STDMETHODCALLTYPE SetMinimalLineWidth(
  [in] INT width
);
````


## -parameters
<dl>

### -param <i>width</i> [in]

<dd>
<p>The minimum thickness (in pixels) of the lines the device is capable of rendering. The value should be greater than 1.</p>
</dd>
</dl>

## -returns
<p><code>SetMinimalLineWidth</code> always returns S_OK.</p>

## -remarks
<p>This method is supported in Windows 7 and later. It is not supported in versions of the Windows operating system before Windows 7.</p>

<p>This method is supported in Windows 7 and later. It is not supported in versions of the Windows operating system before Windows 7.</p>

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
<dt><a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ee719675.aspx">IWICBitmap</a></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556365">IXpsRasterizer::RasterizeRect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7616b5c7-a21f-4db1-923b-ebf2a039b5ec">IXpsRasterizerNotificationCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556350">IXpsRasterizationFactory::CreateRasterizer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IXpsRasterizer::SetMinimalLineWidth method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
