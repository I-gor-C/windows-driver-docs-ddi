---
UID: NC.d3dumddi.PFND3DDDI_QUERYRESIDENCYCB
title: PFND3DDDI_QUERYRESIDENCYCB
author: windows-driver-content
description: The pfnQueryResidencyCb function queries the residency status of a resource or list of allocations.
old-location: display\pfnqueryresidencycb.htm
old-project: display
ms.assetid: 707ba050-e70c-49f8-aac0-0bcc8fe9bf8b
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
req.alt-api: pfnQueryResidencyCb
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

# PFND3DDDI_QUERYRESIDENCYCB callback



## -description
<p>The <b>pfnQueryResidencyCb</b> function queries the residency status of a resource or list of allocations.</p>


## -prototype

````
PFND3DDDI_QUERYRESIDENCYCB pfnQueryResidencyCb;

__checkReturn HRESULT APIENTRY pfnQueryResidencyCb(
  _In_          HANDLE                  hDevice,
  _Inout_ const D3DDDICB_QUERYRESIDENCY *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in, out]

<dd>
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-queryresidency.md">D3DDDICB_QUERYRESIDENCY</a> structure that describes the residency status of a resource or list of allocations.</p>
</dd>
</dl>

## -returns
<p><b>pfnQueryResidencyCb</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The residency status was successfully returned.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks
<p>The user-mode display driver can call the <b>pfnQueryResidencyCb</b> function to query the residency status of allocations either through a resource or through a list of allocations. If the driver queries the residency status of allocations through a resource, all of the allocations that belong to the resource are queried. Typically, the user-mode display driver queries the residency of a resource or list of allocations after the Microsoft Direct3D runtime calls the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryresourceresidency.md">QueryResourceResidency</a> or <a href="display.queryresourceresidencydxgi">QueryResourceResidencyDXGI</a> function to determine the residency of a resource. However, the user-mode display driver can query the residency of a resource or list of allocations at any time. </p>

<p>The following code example shows how to query for residency status.</p>

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
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-queryresidency.md">D3DDDICB_QUERYRESIDENCY</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicecallbacks.md">D3DDDI_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryresourceresidency.md">QueryResourceResidency</a>
</dt>
<dt>
<a href="display.queryresourceresidencydxgi">QueryResourceResidencyDXGI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_QUERYRESIDENCYCB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
