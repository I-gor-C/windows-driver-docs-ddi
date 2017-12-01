---
UID: NC.d3dkmddi.DXGKDDI_VIDPN_GETTOPOLOGY
title: DXGKDDI_VIDPN_GETTOPOLOGY
author: windows-driver-content
description: The pfnGetTopology function returns a handle to the VidPN topology object contained by a specified VidPN object.
old-location: display\dxgk_vidpn_interface_pfngettopology.htm
old-project: display
ms.assetid: 2bc43cd0-97a2-4120-8e6f-425664d3d28c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnGetTopology
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

# DXGKDDI_VIDPN_GETTOPOLOGY callback



## -description
<p>The <b>pfnGetTopology</b> function returns a handle to the VidPN topology object contained by a specified VidPN object.</p>


## -prototype

````
DXGKDDI_VIDPN_GETTOPOLOGY pfnGetTopology;

NTSTATUS APIENTRY pfnGetTopology(
  _In_  const D3DKMDT_HVIDPN               hVidPn,
  _Out_       D3DKMDT_HVIDPNTOPOLOGY       *phVidPnTopology,
  _Out_ const DXGK_VIDPNTOPOLOGY_INTERFACE **ppVidPnTopologyInterface
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPn</i> [in]

<dd>
<p>[in] A handle to a VidPN object. The VidPN manager previously provided this handle to the display miniport driver by calling <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a>, <a href="display.dxgkddiissupportedvidpn">DxgkDdiIsSupportedVidPn</a>, or <a href="display.dxgkddirecommendfunctionalvidpn">DxgkDdiRecommendFunctionalVidPn</a>.</p>
</dd>

### -param <i>phVidPnTopology</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a handle to the VidPN topology object.</p>
</dd>

### -param <i>ppVidPnTopologyInterface</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-vidpntopology-interface.md">DXGK_VIDPNTOPOLOGY_INTERFACE</a> structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter the VidPN topology object.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnGetTopology</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN</b></dt>
</dl><p>The handle supplied in <i>hVidPn</i> was invalid.</p>

<p> </p>

## -remarks
<p>The display miniport driver does not need to release the handle that it receives in <i>phVidPnTopology</i>.</p>

<p>The lifetime of the DXGK_VIDPNTOPOLOGY_INTERFACE structure returned in <i>ppVidPnTopologyInterface</i> is owned by the operating system. Using this ownership scheme, the operating system can migrate to newer implementations at run time without breaking clients of the interface. </p>

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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
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
<a href="display.vidpn_topology_interface">VidPN Topology Interface</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-vidpntopology-interface.md">DXGK_VIDPNTOPOLOGY_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPN_GETTOPOLOGY callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
