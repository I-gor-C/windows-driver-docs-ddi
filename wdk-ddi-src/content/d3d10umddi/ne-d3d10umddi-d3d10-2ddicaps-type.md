---
UID: NE.d3d10umddi.D3D10_2DDICAPS_TYPE
title: D3D10_2DDICAPS_TYPE
author: windows-driver-content
description: The D3D10_2DDICAPS_TYPE enumeration type contains values that identify the type of capability information that is retrieved from a call to the driver's GetCaps(D3D10_2) function.
old-location: display\d3d10_2ddicaps_type.htm
old-project: display
ms.assetid: 2ca906d4-6d09-4624-a985-a47794acc959
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D10_2DDICAPS_TYPE is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_2DDICAPS_TYPE
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
req.iface: 
---

# D3D10_2DDICAPS_TYPE enumeration



## -description
<p>The D3D10_2DDICAPS_TYPE enumeration type contains values that identify the type of capability information that is retrieved from a call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a> function. </p>


## -syntax

````
enum D3D10_2DDICAPS_TYPE {
  D3D11DDICAPS_THREADING                       = 128, 
  D3D11DDICAPS_SHADER                          = 129, 
  D3D11DDICAPS_3DPIPELINESUPPORT               = 130, 
#if D3D11DDI_MINOR_HEADER_VERSION >= 3
  D3D11_1DDICAPS_D3D11_OPTIONS                 = 131, 
  D3D11_1DDICAPS_ARCHITECTURE_INFO             = 132, 
  D3D11_1DDICAPS_SHADER_MIN_PRECISION_SUPPORT  = 134, 
#endif 
#if D3D11DDI_MINOR_HEADER_VERSION >= 4
  D3DWDDM1_3DDICAPS_D3D11_OPTIONS1             = 136, 
  D3DWDDM1_3DDICAPS_MARKER                     = 137 

#endif 
};
````


## -enum-fields
<dl>

### -field <a id="D3D11DDICAPS_THREADING"></a><a id="d3d11ddicaps_threading"></a><b>D3D11DDICAPS_THREADING</b>

<dd>
<p>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure that describes the threading capabilities that the driver supports. </p>
</dd>

### -field <a id="D3D11DDICAPS_SHADER"></a><a id="d3d11ddicaps_shader"></a><b>D3D11DDICAPS_SHADER</b>

<dd>
<p>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542153">D3D11DDI_SHADER_CAPS</a> structure that describes the shader capabilities that the driver supports. </p>
</dd>

### -field <a id="D3D11DDICAPS_3DPIPELINESUPPORT"></a><a id="d3d11ddicaps_3dpipelinesupport"></a><b>D3D11DDICAPS_3DPIPELINESUPPORT</b>

<dd>
<p>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542134">D3D11DDI_3DPIPELINESUPPORT_CAPS</a> structure that describes the pipeline capabilities that the driver supports. </p>
</dd>

### -field <a id="D3D11_1DDICAPS_D3D11_OPTIONS"></a><a id="d3d11_1ddicaps_d3d11_options"></a><b>D3D11_1DDICAPS_D3D11_OPTIONS</b>

<dd>
<p>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406442">D3D11_1DDI_D3D11_OPTIONS_DATA</a>  structure that specifies options to provide data to the user-mode driver.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3D11_1DDICAPS_ARCHITECTURE_INFO"></a><a id="d3d11_1ddicaps_architecture_info"></a><b>D3D11_1DDICAPS_ARCHITECTURE_INFO</b>

<dd>
<p>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451150">D3DDDICAPS_ARCHITECTURE_INFO</a> structure that describes information about Direct3D 11.1 adapter architecture.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3D11_1DDICAPS_SHADER_MIN_PRECISION_SUPPORT"></a><a id="d3d11_1ddicaps_shader_min_precision_support"></a><b>D3D11_1DDICAPS_SHADER_MIN_PRECISION_SUPPORT</b>

<dd>
<p>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451154">D3DDDICAPS_SHADER_MIN_PRECISION_SUPPORT</a> structure that describes the precision support options for shaders in the user-mode display driver.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3DWDDM1_3DDICAPS_D3D11_OPTIONS1"></a><a id="d3dwddm1_3ddicaps_d3d11_options1"></a><b>D3DWDDM1_3DDICAPS_D3D11_OPTIONS1</b>

<dd>
<p>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn475744">D3DWDDM1_3DDI_D3D11_OPTIONS_DATA1</a> structure that describes the tiled resource support options in the user-mode display driver.</p>
<p>Supported starting with Windows 8. Used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDICAPS_MARKER"></a><a id="d3dwddm1_3ddicaps_marker"></a><b>D3DWDDM1_3DDICAPS_MARKER</b>

<dd>
<p>Supported starting with Windows 8. Used by WDDM 1.3 and later drivers.</p>
</dd>
</dl>

## -remarks
<p>To allow a driver to unify capability concepts, the values in the D3D10_2DDICAPS_TYPE enumeration are set up so they do not overlap with the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a> enumeration. </p>

<p>To allow a driver to unify capability concepts, the values in the D3D10_2DDICAPS_TYPE enumeration are set up so they do not overlap with the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a> enumeration. </p>

<p>To allow a driver to unify capability concepts, the values in the D3D10_2DDICAPS_TYPE enumeration are set up so they do not overlap with the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a> enumeration. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D10_2DDICAPS_TYPE is supported beginning with the Windows 7 operating system. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406442">D3D11_1DDI_D3D11_OPTIONS_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542134">D3D11DDI_3DPIPELINESUPPORT_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542153">D3D11DDI_SHADER_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451154">D3DDDICAPS_SHADER_MIN_PRECISION_SUPPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn475744">D3DWDDM1_3DDI_D3D11_OPTIONS_DATA1</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_2DDICAPS_TYPE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
