---
UID: NE.d3dkmdt._D3DKMDT_GDISURFACETYPE
title: D3DKMDT_GDISURFACETYPE
author: windows-driver-content
description: The D3DKMDT_GDISURFACETYPE enumeration indicates the type of lockable surface that is used by the Desktop Window Manager (DWM) for redirection.
old-location: display\d3dkmdt_gdisurfacetype.htm
ms.assetid: b1c8fc0a-b877-4321-85b9-0c5c174ffc45
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_GDISURFACETYPE
req.alt-loc: d3dkmdt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# D3DKMDT_GDISURFACETYPE enumeration



## -description
<p>The D3DKMDT_GDISURFACETYPE enumeration indicates the type of lockable surface that is used by the Desktop Window Manager (DWM) for redirection.</p>


## -syntax

````
typedef enum _D3DKMDT_GDISURFACETYPE { 
  D3DKMDT_GDISURFACE_INVALID                          = 0,
  D3DKMDT_GDISURFACE_TEXTURE                          = 1,
  D3DKMDT_GDISURFACE_STAGING_CPUVISIBLE               = 2,
  D3DKMDT_GDISURFACE_STAGING                          = 3,
  D3DKMDT_GDISURFACE_LOOKUPTABLE                      = 4,
  D3DKMDT_GDISURFACE_EXISTINGSYSMEM                   = 5,
  D3DKMDT_GDISURFACE_TEXTURE_CPUVISIBLE               = 6,
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  D3DKMDT_GDISURFACE_TEXTURE_CROSSADAPTER             = 7,
  D3DKMDT_GDISURFACE_TEXTURE_CPUVISIBLE_CROSSADAPTER  = 8

#endif } D3DKMDT_GDISURFACETYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_GDISURFACE_INVALID"></a><a id="d3dkmdt_gdisurface_invalid"></a><b>D3DKMDT_GDISURFACE_INVALID</b>

<dd>
<p>The driver should not see this value.</p>
</dd>

### -field <a id="D3DKMDT_GDISURFACE_TEXTURE"></a><a id="d3dkmdt_gdisurface_texture"></a><b>D3DKMDT_GDISURFACE_TEXTURE</b>

<dd>
<p>Indicates that the surface has the following properties:</p>
<ul>
<li>
<p>It has a one-level texture.</p>
</li>
<li>
<p>It is not visible to the CPU, and the video memory manager will create it as a shared surface.</p>
</li>
<li>
<p>It is opened by a user-mode driver and used as a texture during DWM composition.</p>
</li>
<li>
<p>It is used by a user-mode driver as a render target for DirectX rendering.</p>
</li>
<li>
<p>It is used as a source or destination surface in GDI hardware-accelerated operations.</p>
</li>
</ul>
</dd>

### -field <a id="D3DKMDT_GDISURFACE_STAGING_CPUVISIBLE"></a><a id="d3dkmdt_gdisurface_staging_cpuvisible"></a><b>D3DKMDT_GDISURFACE_STAGING_CPUVISIBLE</b>

<dd>
<p>Indicates that the surface has the following properties:</p>
<ul>
<li>
<p>It is visible to the CPU and will be extensively used by the CPU. The allocation must be a linear format and in a cache-coherent GPU aperture segment.</p>
</li>
<li>
<p>It is used as a source surface in GDI hardware-accelerated operations.</p>
</li>
<li>
<p>It is used as a destination surface in bitblt (copy-only) GDI operations.</p>
</li>
<li>
<p>Its pitch must be returned by the display miniport driver.</p>
</li>
<li>
<p>Its pitch value and surface address must be aligned to the value of the <b>AlignmentShift</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a> structure (that is, <a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>-&gt;PresentationCaps.AlignmentShift).</p>
</li>
</ul>
</dd>

### -field <a id="D3DKMDT_GDISURFACE_STAGING"></a><a id="d3dkmdt_gdisurface_staging"></a><b>D3DKMDT_GDISURFACE_STAGING</b>

<dd>
<p>Indicates that the surface has the following properties:</p>
<ul>
<li>
<p>It is not visible to the CPU.</p>
</li>
<li>
<p>It is used as a source or destination surface in GDI hardware-accelerated operations.</p>
</li>
<li>
<p>It is used as a source or destination surface in GDI bitblt (copy-only) operations.</p>
</li>
</ul>
</dd>

### -field <a id="D3DKMDT_GDISURFACE_LOOKUPTABLE"></a><a id="d3dkmdt_gdisurface_lookuptable"></a><b>D3DKMDT_GDISURFACE_LOOKUPTABLE</b>

<dd>
<p>Indicates that the surface has the following properties:</p>
<ul>
<li>
<p>It is not visible to the CPU.</p>
</li>
<li>
<p>It is used only during processing of commands that are specified by the <b>ClearTypeBlend</b> and <b>OpCode</b>.DXGK_GDIOP_BITBLT (copy-only) members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562026">DXGK_RENDERKM_COMMAND</a> structure.</p>
</li>
<li>
<p>The format is defined by the D3DDDIFMT_A8 value of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a> enumeration.</p>
</li>
<li>
<p>The gamma lookup allocation is created one time and never changes after it is initialized. The allocation is initialized in D3DDDIFMT_A8 format by issuing a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562026">DXGK_RENDERKM_COMMAND</a>-&gt;Opcode.DXGK_GDIOP_BITBLT command from a D3DKMDT_GDISURFACE_STAGING_CPUVISIBLE surface.</p>
</li>
</ul>
</dd>

### -field <a id="D3DKMDT_GDISURFACE_EXISTINGSYSMEM"></a><a id="d3dkmdt_gdisurface_existingsysmem"></a><b>D3DKMDT_GDISURFACE_EXISTINGSYSMEM</b>

<dd>
<p>Indicates that the surface has the following properties:</p>
<ul>
<li>
<p>It is visible to the CPU. The allocation must be a linear format and in a cache-coherent GPU aperture segment.</p>
</li>
<li>
<p>Its pitch value and surface address must be aligned to the value of the <b>AlignmentShift</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a> structure (that is, <a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>-&gt;PresentationCaps.AlignmentShift).</p>
</li>
<li>
<p>The surface address is passed to the driver.</p>
</li>
<li>
<p>This value is used in the same way as the D3DKMDT_GDISURFACE_STAGING_CPUVISIBLE value.</p>
</li>
</ul>
</dd>

### -field <a id="D3DKMDT_GDISURFACE_TEXTURE_CPUVISIBLE"></a><a id="d3dkmdt_gdisurface_texture_cpuvisible"></a><b>D3DKMDT_GDISURFACE_TEXTURE_CPUVISIBLE</b>

<dd>
<p>Reserved for system use. Do not use this value in your driver.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3DKMDT_GDISURFACE_TEXTURE_CROSSADAPTER"></a><a id="d3dkmdt_gdisurface_texture_crossadapter"></a><b>D3DKMDT_GDISURFACE_TEXTURE_CROSSADAPTER</b>

<dd>
<p>Indicates that the surface has the following properties:</p>
<ul>
<li>
<p>It is not visible to the CPU, and the video memory manager will create it as a shared cross-adapter surface.</p>
</li>
<li>
<p>Its pitch must be returned by the display miniport driver in the <b>Pitch</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546021">D3DKMDT_GDISURFACEDATA</a> structure.</p>
</li>
<li>
<p>The pitch and height must have the required alignment for the cross-adapter resource. You can use the <b>D3DKMT_CROSS_ADAPTER_RESOURCE_PITCH_ALIGNMENT</b> and <b>D3DKMT_CROSS_ADAPTER_RESOURCE_HEIGHT_ALIGNMENT</b> constants to validate that the driver returns the correct pitch and height for the cross-adapter resource. These constants are defined in D3dukmdt.h.</p>
</li>
</ul>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <a id="D3DKMDT_GDISURFACE_TEXTURE_CPUVISIBLE_CROSSADAPTER"></a><a id="d3dkmdt_gdisurface_texture_cpuvisible_crossadapter"></a><b>D3DKMDT_GDISURFACE_TEXTURE_CPUVISIBLE_CROSSADAPTER</b>

<dd>
<p>Reserved for system use. Do not use this value in your driver.</p>
<p>Supported starting with Windows 8.1.</p>
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
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546021">D3DKMDT_GDISURFACEDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562026">DXGK_RENDERKM_COMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_GDISURFACETYPE enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
