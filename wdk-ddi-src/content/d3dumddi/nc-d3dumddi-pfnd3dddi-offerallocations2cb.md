---
UID: NC.d3dumddi.PFND3DDDI_OFFERALLOCATIONS2CB
title: PFND3DDDI_OFFERALLOCATIONS2CB
author: windows-driver-content
description: Called by the user-mode display driver to offer video memory allocations for reuse.
old-location: display\pfnofferallocations2cb.htm
old-project: display
ms.assetid: 4A8123D3-3A7D-4716-BD02-DD6533DB22F6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnOfferAllocations2Cb
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

# PFND3DDDI_OFFERALLOCATIONS2CB callback



## -description
<p>Called by the user-mode display driver   to offer  video memory allocations for reuse.</p>


## -prototype

````
PFND3DDDI_OFFERALLOCATIONS2CB pfnOfferAllocations2Cb;

__checkReturn HRESULT CALLBACK pfnOfferAllocations2Cb(
  _In_       HANDLE                     hDevice,
  _In_ const D3DDDICB_OFFERALLOCATIONS2 *pData
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p> A handle to the display device (graphics context). The Direct3D runtime passed the user-mode driver this handle as the <b>hDevice</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-createdevice.md">D3DDDIARG_CREATEDEVICE</a> structure at device creation.</p>
</dd>

### -param pData [in]

<dd>
<p> A pointer to a <a href="display.d3dddicb_offerallocations2">D3DDDICB_OFFERALLOCATIONS2</a> structure  that defines the video memory allocations that the driver offers.</p>
</dd>
</dl>

## -returns
<p>
      Returns one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The  allocations were successfully offered.</p><dl>
<dt><b>D3DDDIERR_DEVICEREMOVED</b></dt>
</dl><p>
         The video memory manager or display miniport driver could not complete the operation because either a Plug and Play (PnP) Stop event or a Timeout Detection and Recovery (TDR) event occurred.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>An invalid parameter was supplied.</p>

<p> </p>

## -remarks
<p>The user-mode display driver calls <b>pfnOfferAllocations2Cb</b> to notify the Microsoft DirectX graphics kernel subsystem that, after it completes any previously submitted render operations,  it can offer the allocations' memory for other processes to use.</p>

<p>After the driver calls <b>pfnOfferAllocations2Cb</b> to offer an allocation to reuse, it must call <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reclaimallocations3cb.md">pfnReclaimAllocations3Cb</a>  before it locks the allocation or submits it for rendering operations.</p>

<p><b>pfnOfferAllocations2Cb</b> functions identically to <a href="display.pfnofferallocationscb">pfnOfferAllocationsCb</a>, except that it takes flags into account through the pData parameter.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-createdevice.md">D3DDDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="display.d3dddicb_offerallocations2">D3DDDICB_OFFERALLOCATIONS2</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicecallbacks.md">D3DDDI_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="display.pfnofferresources">pfnOfferResources</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reclaimallocations3cb.md">pfnReclaimAllocations3Cb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_OFFERALLOCATIONS2CB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
