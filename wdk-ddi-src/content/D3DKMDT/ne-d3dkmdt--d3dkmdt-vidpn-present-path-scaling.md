---
UID: NE.d3dkmdt._D3DKMDT_VIDPN_PRESENT_PATH_SCALING
title: D3DKMDT_VIDPN_PRESENT_PATH_SCALING
author: windows-driver-content
description: The D3DKMDT_VIDPN_PRESENT_PATH_SCALING enumeration is used to indicate the scaling transformation applied to content displayed on a VidPN present path.
old-location: display\d3dkmdt_vidpn_present_path_scaling.htm
ms.assetid: 4453534e-ce2b-4b0d-a93d-3d17185083fd
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_VIDPN_PRESENT_PATH_SCALING
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

# D3DKMDT_VIDPN_PRESENT_PATH_SCALING enumeration



## -description
<p>The D3DKMDT_VIDPN_PRESENT_PATH_SCALING enumeration is used to indicate the scaling transformation applied to content displayed on a VidPN present path.</p>


## -syntax

````
typedef enum _D3DKMDT_VIDPN_PRESENT_PATH_SCALING { 
  D3DKMDT_VPPS_UNINITIALIZED           = 0,
  D3DKMDT_VPPS_IDENTITY                = 1,
  D3DKMDT_VPPS_CENTERED                = 2,
  D3DKMDT_VPPS_STRETCHED               = 3,
  D3DKMDT_VPPS_ASPECTRATIOCENTEREDMAX  = 4,
  D3DKMDT_VPPS_CUSTOM                  = 5,
  D3DKMDT_VPPS_RESERVED1               = 253,
  D3DKMDT_VPPS_UNPINNED                = 254,
  D3DKMDT_VPPS_NOTSPECIFIED            = 255
} D3DKMDT_VIDPN_PRESENT_PATH_SCALING;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_VPPS_UNINITIALIZED"></a><a id="d3dkmdt_vpps_uninitialized"></a><b>D3DKMDT_VPPS_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_VIDPN_PRESENT_PATH_SCALING has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_VPPS_IDENTITY"></a><a id="d3dkmdt_vpps_identity"></a><b>D3DKMDT_VPPS_IDENTITY</b>

<dd>
<p>Indicates the identity transformation; the source content is presented with no change. Note that this transformation is available only if the path's source mode has the same spatial resolution as the path's target mode.</p>
</dd>

### -field <a id="D3DKMDT_VPPS_CENTERED"></a><a id="d3dkmdt_vpps_centered"></a><b>D3DKMDT_VPPS_CENTERED</b>

<dd>
<p>Indicates the centering transformation; the source content is presented unscaled, centered with respect to the spatial resolution of the target mode.</p>
</dd>

### -field <a id="D3DKMDT_VPPS_STRETCHED"></a><a id="d3dkmdt_vpps_stretched"></a><b>D3DKMDT_VPPS_STRETCHED</b>

<dd>
<p>Indicates that the source content is scaled to fit the path's target, and the aspect ratio of the source is not preserved.</p>
</dd>

### -field <a id="D3DKMDT_VPPS_ASPECTRATIOCENTEREDMAX"></a><a id="d3dkmdt_vpps_aspectratiocenteredmax"></a><b>D3DKMDT_VPPS_ASPECTRATIOCENTEREDMAX</b>

<dd>
<p>Indicates that the source content is scaled to fit the path's target while preserving the aspect ratio of the source.</p>
<p>This constant value is available beginning with Windows 7. See further information in the Remarks section.</p>
</dd>

### -field <a id="D3DKMDT_VPPS_CUSTOM"></a><a id="d3dkmdt_vpps_custom"></a><b>D3DKMDT_VPPS_CUSTOM</b>

<dd>
<p>Indicates that the path is capable of displaying one or more scaling modes that are not described by other constants of this enumeration.</p>
<p>This constant value is available beginning with Windows 7. See further information in the Remarks section.</p>
</dd>

### -field <a id="D3DKMDT_VPPS_RESERVED1"></a><a id="d3dkmdt_vpps_reserved1"></a><b>D3DKMDT_VPPS_RESERVED1</b>

<dd>
<p>Reserved for system use. Do not use this value. This value will never be passed to a driver.</p>
<p>This constant value is available beginning with Windows 7.</p>
</dd>

### -field <a id="D3DKMDT_VPPS_UNPINNED"></a><a id="d3dkmdt_vpps_unpinned"></a><b>D3DKMDT_VPPS_UNPINNED</b>

<dd>
<p>Indicates that no scaling transformation has been pinned for the VidPN present source.</p>
</dd>

### -field <a id="D3DKMDT_VPPS_NOTSPECIFIED"></a><a id="d3dkmdt_vpps_notspecified"></a><b>D3DKMDT_VPPS_NOTSPECIFIED</b>

<dd>
<p>Indicates that no transformation has been specified. See further information in the Remarks section.</p>
</dd>
</dl>

## -remarks
<p>The <b>Scaling</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a> structure is a value from the D3DKMDT_VIDPN_PRESENT_PATH_SCALING enumeration.</p>

<p>If D3DKMDT_VPPS_ASPECTRATIOCENTEREDMAX or D3DKMDT_VPPS_CUSTOM values are specified but the path is on a display miniport driver that does not support these values (which are available beginning with Windows 7), the driver's calls to <a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a> should return STATUS_GRAPHICS_VIDPN_MODALITY_NOT_SUPPORTED, and the operating system will apply the system default scaling. If a driver cannot support the requested scaling value on the specified path, its calls to <b>DxgkDdiCommitVidPn</b> should return STATUS_GRAPHICS_VIDPN_MODALITY_NOT_SUPPORTED.</p>

<p>The <b>Scaling</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a> structure is a value from the D3DKMDT_VIDPN_PRESENT_PATH_SCALING enumeration.</p>

<p>If D3DKMDT_VPPS_ASPECTRATIOCENTEREDMAX or D3DKMDT_VPPS_CUSTOM values are specified but the path is on a display miniport driver that does not support these values (which are available beginning with Windows 7), the driver's calls to <a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a> should return STATUS_GRAPHICS_VIDPN_MODALITY_NOT_SUPPORTED, and the operating system will apply the system default scaling. If a driver cannot support the requested scaling value on the specified path, its calls to <b>DxgkDdiCommitVidPn</b> should return STATUS_GRAPHICS_VIDPN_MODALITY_NOT_SUPPORTED.</p>

<p>The <b>Scaling</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a> structure is a value from the D3DKMDT_VIDPN_PRESENT_PATH_SCALING enumeration.</p>

<p>If D3DKMDT_VPPS_ASPECTRATIOCENTEREDMAX or D3DKMDT_VPPS_CUSTOM values are specified but the path is on a display miniport driver that does not support these values (which are available beginning with Windows 7), the driver's calls to <a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a> should return STATUS_GRAPHICS_VIDPN_MODALITY_NOT_SUPPORTED, and the operating system will apply the system default scaling. If a driver cannot support the requested scaling value on the specified path, its calls to <b>DxgkDdiCommitVidPn</b> should return STATUS_GRAPHICS_VIDPN_MODALITY_NOT_SUPPORTED.</p>

## -requirements
<table>
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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546712">D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_VIDPN_PRESENT_PATH_SCALING enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
