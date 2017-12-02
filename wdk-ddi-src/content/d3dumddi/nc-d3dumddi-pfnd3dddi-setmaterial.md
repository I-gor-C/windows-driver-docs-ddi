---
UID: NC.d3dumddi.PFND3DDDI_SETMATERIAL
title: PFND3DDDI_SETMATERIAL
author: windows-driver-content
description: The SetMaterial function sets the material properties that devices on the system use to create the required effect during rendering.
old-location: display\setmaterial.htm
old-project: display
ms.assetid: e1273478-a450-44fa-95d5-ee86cb3a46b2
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
req.alt-api: SetMaterial
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

# PFND3DDDI_SETMATERIAL callback



## -description
<p>The <i>SetMaterial</i> function sets the material properties that devices on the system use to create the required effect during rendering.</p>


## -prototype

````
PFND3DDDI_SETMATERIAL SetMaterial;

__checkReturn HRESULT APIENTRY SetMaterial(
  _In_       HANDLE                hDevice,
  _In_ const D3DDDIARG_SETMATERIAL *pData
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
<p> A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-setmaterial.md">D3DDDIARG_SETMATERIAL</a> structure that describes the material properties that are used for rendering.</p>
</dd>
</dl>

## -returns
<p><i>SetMaterial</i> returns S_OK or an appropriate error result if the material properties are not successfully set.</p>

## -remarks
<p>Material properties detail a material's diffuse reflection, ambient reflection, light emission, and specular highlighting characteristics. The Microsoft Direct3D runtime uses the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-setmaterial.md">D3DDDIARG_SETMATERIAL</a> structure to pass all of the material property information to the user-mode display driver. Material properties affect the colors that the Direct3D runtime uses to rasterize polygons that use the material. With the exception of the specular property, each of the properties is described as an RGBA color that represents how much of the red, green, and blue parts of a given type of light it reflects and an alpha blending factor (the alpha component of the RGBA color). The material's specular property is described in two parts: color and power. For more information about material properties, see the Microsoft Windows SDK documentation.</p>

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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-setmaterial.md">D3DDDIARG_SETMATERIAL</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETMATERIAL callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
