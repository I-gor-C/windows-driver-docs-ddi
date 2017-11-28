---
UID: NS.dxgiddi.DXGI_DDI_BASE_CALLBACKS
title: DXGI_DDI_BASE_CALLBACKS
author: windows-driver-content
description: The DXGI_DDI_BASE_CALLBACKS structure contains pointers to Microsoft Direct3D 10 runtime callback functions that the user-mode display driver can use.
old-location: display\dxgi_ddi_base_callbacks.htm
old-project: display
ms.assetid: dd1690e2-7eef-4086-a3e1-9ca456b79a6f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_DDI_BASE_CALLBACKS, DXGI_DDI_BASE_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_BASE_CALLBACKS
req.alt-loc: dxgiddi.h
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

# DXGI_DDI_BASE_CALLBACKS structure



## -description
<p>The DXGI_DDI_BASE_CALLBACKS structure contains pointers to Microsoft Direct3D 10 runtime callback functions that the user-mode display driver can use.</p>


## -syntax

````
typedef struct DXGI_DDI_BASE_CALLBACKS {
  PFNDDXGIDDI_PRESENTCB                    pfnPresentCb;
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WIN8)
  PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAYCB pfnPresentMultiplaneOverlayCb;
#endif 
} DXGI_DDI_BASE_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>pfnPresentCb</b>

<dd>
<p>A pointer to the <a href="..\dxgiddi\nc-dxgiddi-pfnddxgiddi-presentcb.md">pfnPresentCbDXGI</a> function.</p>
</dd>

### -field <b>pfnPresentMultiplaneOverlayCb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh780324">pfnPresentMultiPlaneOverlayCb (DXGI)</a> function. Supported starting with Windows 8.1.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541664">D3D10DDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557485">DXGI_DDI_BASE_ARGS</a>
</dt>
<dt>
<a href="..\dxgiddi\nc-dxgiddi-pfnddxgiddi-presentcb.md">pfnPresentCbDXGI</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh780324">pfnPresentMultiPlaneOverlayCb (DXGI)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_BASE_CALLBACKS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
