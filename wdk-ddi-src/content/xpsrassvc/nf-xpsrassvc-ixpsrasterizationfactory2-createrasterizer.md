---
UID: NF:xpsrassvc.IXpsRasterizationFactory2.CreateRasterizer
title: IXpsRasterizationFactory2::CreateRasterizer method
author: windows-driver-content
description: The CreateRasterizer method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs.
old-location: print\ixpsrasterizationfactory2_createrasterizer.htm
old-project: print
ms.assetid: C31681A0-17C6-4255-9068-7486A2101AB7
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: CreateRasterizer method [Print Devices], CreateRasterizer method [Print Devices], IXpsRasterizationFactory2 interface, CreateRasterizer,IXpsRasterizationFactory2.CreateRasterizer, IXpsRasterizationFactory2, IXpsRasterizationFactory2 interface [Print Devices], CreateRasterizer method, IXpsRasterizationFactory2::CreateRasterizer, print.ixpsrasterizationfactory2_createrasterizer, xpsrassvc/IXpsRasterizationFactory2::CreateRasterizer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: xpsrassvc.h
req.include-header: Xpsrassvc.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	xpsrassvc.h
api_name:
-	IXpsRasterizationFactory2.CreateRasterizer
product: Windows
targetos: Windows
req.typenames: XPSRAS_BACKGROUND_COLOR
req.product: Windows 10 or later.
---


# IXpsRasterizationFactory2::CreateRasterizer method
The <b>CreateRasterizer</b> method creates an XPS rasterizer object that can convert content from XPS to PWG Raster using the <a href="https://msdn.microsoft.com/a0493b5f-d6f7-4f69-9c6e-e112c29250c9">XPS Rasterization Service</a>. PWG Raster supports non-square DPIs.

## Syntax

```
HRESULT CreateRasterizer(
  IXpsOMPage              *xpsPage,
  FLOAT                   DPIX,
  FLOAT                   DPIY,
  XPSRAS_RENDERING_MODE   nonTextRenderingMode,
  XPSRAS_RENDERING_MODE   textRenderingMode,
  XPSRAS_PIXEL_FORMAT     pixelFormat,
  XPSRAS_BACKGROUND_COLOR backgroundColor,
  IXpsRasterizer          **ppIXpsRasterizer
);
```

## Parameters

`xpsPage`



`DPIX`



`DPIY`



`nonTextRenderingMode`

Rendering mode for nontext items in the rasterized output. This parameter indicates whether to generate antialiased output. Set this parameter to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff564291">XPSRAS_RENDERING_MODE</a> enumeration values:

<ul>
<li>
XPSRAS_RENDERING_MODE_ANTIALIASED

</li>
<li>
XPSRAS_RENDERING_MODE_ALIASED

</li>
</ul>

`textRenderingMode`

Rendering mode for text in the rasterized output. This parameter indicates whether to generate antialiased output. Set this parameter to one of the following XPSRAS_RENDERING_MODE enumeration values:

<ul>
<li>
XPSRAS_RENDERING_MODE_ANTIALIASED

</li>
<li>
XPSRAS_RENDERING_MODE_ALIASED

</li>
</ul>

`pixelFormat`

Allows a caller to select the pixel format used by the IWICBitmap returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff556365">IXpsRasterizer::RasterizeRect</a>. Set this parameter to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/hh802469">XPSRAS_PIXEL_FORMAT</a> enumeration values:

<ul>
<li>
XPSRAS_PIXEL_FORMAT_32BPP_PBGRA_UINT_SRGB

</li>
<li>
XPSRAS_PIXEL_FORMAT_64BPP_PRGBA_HALF_SCRGB

</li>
<li>
XPSRAS_PIXEL_FORMAT_128BPP_PRGBA_FLOAT_SCRGB

</li>
</ul>

`backgroundColor`

Allows a caller to select background color. Set this parameter to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/dn897481">XPSRAS_BACKGROUND_COLOR</a> enumeration values:

<ul>
<li>
XPSRAS_BACKGROUND_COLOR_TRANSPARENT

</li>
<li>
XPSRAS_BACKGROUND_COLOR_OPAQUE

</li>
</ul>
The default background color is XPSRAS_BACKGROUND_COLOR_TRANSPARENT.

`ppIXpsRasterizer`




## Return Value

If this method succeeds, it returns <b>S_OK</b>. Otherwise, it returns an <b>HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10  |
| **Target Platform** | Desktop |
| **Header** | xpsrassvc.h (include Xpsrassvc.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn937110">IXpsRasterizationFactory2</a>