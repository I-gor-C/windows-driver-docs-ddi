---
UID : NA:xpsrassvc
ms.assetid : 333d36bb-cab5-375c-9e40-5fba63531711
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# xpsrassvc.h header



xpsrassvc.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IXpsRasterizationFactory1](nn-xpsrassvc-ixpsrasterizationfactory1.md) | In Windows 8, the improvement of XPSRas to handle high precision colors has led to the development of a new interface, IXPSRasterizationFactory1. |
| [IXpsRasterizationFactory2](nn-xpsrassvc-ixpsrasterizationfactory2.md) | In Windows 10, the IXpsRasterizationFactory2 interface represents an object factory for creating components that can convert content from XPS to PWG Raster using the XPS Rasterization Service. PWG Raster supports non-square DPIs. |






## Enumerations
| Title | Description |
| ---- |:---- |
| [__MIDL___MIDL_itf_xpsrassvc_0000_0001_0001](ne-xpsrassvc-__midl___midl_itf_xpsrassvc_0000_0001_0001.md) | The XPSRAS_RENDERING_MODE enumeration specifies the rendering mode to be used by an XPS rasterizer. |
| [__MIDL___MIDL_itf_xpsrassvc_0000_0003_0001](ne-xpsrassvc-__midl___midl_itf_xpsrassvc_0000_0003_0001.md) | XPSRAS_PIXEL_FORMAT allows a caller to select the pixel format used by the IWICBitmap interface that is returned by the IXpsRasterizer::RasterizeRect method. XPSRAS_PIXEL_FORMAT is provided with Windows 8 and later versions of Windows. |
| [__MIDL___MIDL_itf_xpsrassvc_0000_0004_0001](ne-xpsrassvc-__midl___midl_itf_xpsrassvc_0000_0004_0001.md) | XPSRAS_BACKGROUND_COLOR specifies the background clear color to be used by an XPS rasterizer: |