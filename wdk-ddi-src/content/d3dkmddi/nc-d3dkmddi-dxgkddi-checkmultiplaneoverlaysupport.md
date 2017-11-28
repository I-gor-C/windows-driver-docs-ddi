---
UID: NC.d3dkmddi.DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT
title: DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT
author: windows-driver-content
description: Called by the Microsoft DirectX graphics kernel subsystem to check the details of hardware support for multiplane overlays.
old-location: display\dxgkddicheckmultiplaneoverlaysupport.htm
old-project: display
ms.assetid: 8332DD64-B75E-40A4-9D98-3406187150F2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiCheckMultiPlaneOverlaySupport
req.alt-loc: d3dkmddi.h
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
req.iface: 
---

# DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT callback



## -description
<p>Called by the Microsoft DirectX graphics kernel subsystem to check the details of hardware support for multiplane overlays.</p>


## -prototype

````
DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT DxgkDdiCheckMultiPlaneOverlaySupport;

_Check_return_ NTSTATUS APIENTRY DxgkDdiCheckMultiPlaneOverlaySupport(
  _In_    const HANDLE                                hAdapter,
  _Inout_       DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT *pCheckMultiPlaneOverlaySupport
)
{ ... }
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>A handle to a context block that is associated with a display adapter. The display miniport driver previously provided this handle to the DirectX graphics kernel subsystem in the <i>MiniportDeviceContext</i> output parameter of the <a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a> function.</p>
</dd>

### -param <i>pCheckMultiPlaneOverlaySupport</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn305131">DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT</a> structure that provides details on hardware support for multiplane overlays.</p>
</dd>
</dl>

## -returns
<p>Returns <b>STATUS_SUCCESS</b> if it succeeds; otherwise it returns one of the error codes defined in Ntstatus.h.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn305131">DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
