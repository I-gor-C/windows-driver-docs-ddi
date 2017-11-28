---
UID: NC.d3dumddi.PFND3DDDI_UPDATEOVERLAY
title: PFND3DDDI_UPDATEOVERLAY
author: windows-driver-content
description: The UpdateOverlay function reconfigures or moves an overlay that is being displayed.
old-location: display\updateoverlay.htm
old-project: display
ms.assetid: 80d7cc5c-51d8-4b91-9581-b073f9b0e68a
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
req.alt-api: UpdateOverlay
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

# PFND3DDDI_UPDATEOVERLAY callback



## -description
<p>The <i>UpdateOverlay</i> function reconfigures or moves an overlay that is being displayed.</p>


## -prototype

````
PFND3DDDI_UPDATEOVERLAY UpdateOverlay;

__checkReturn HRESULT APIENTRY UpdateOverlay(
  _In_       HANDLE                  hDevice,
  _In_ const D3DDDIARG_UPDATEOVERLAY *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543400">D3DDDIARG_UPDATEOVERLAY</a> structure that describes how to reconfigure the overlay.</p>
</dd>
</dl>

## -returns
<p><i>UpdateOverlay</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The overlay is successfully modified.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><i>UpdateOverlay</i> could not complete because of insufficient memory.</p><dl>
<dt><b>D3DDDIERR_NOTAVAILABLE</b></dt>
</dl><p><i>UpdateOverlay</i> could not complete because insufficient bandwidth was available or the requested overlay hardware was unavailable.</p><dl>
<dt><b>D3DDDIERR_UNSUPPORTEDOVERLAYFORMAT</b></dt>
</dl><p>The specified overlay format is not supported by the overlay hardware. </p><dl>
<dt><b>D3DDDIERR_UNSUPPORTEDOVERLAY</b></dt>
</dl><p>The overlay hardware is not supported for the specified size and display mode. </p>

<p> </p>

## -remarks
<p>Overlays are independent from the resources that are displayed by using the overlays.</p>

<p>Overlays are independent from the resources that are displayed by using the overlays.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543400">D3DDDIARG_UPDATEOVERLAY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_UPDATEOVERLAY callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
