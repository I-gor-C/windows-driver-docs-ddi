---
UID: NC.d3dumddi.PFND3DDDI_SUBMITCOMMANDCB
title: PFND3DDDI_SUBMITCOMMANDCB
author: windows-driver-content
description: pfnSubmitCommandCb is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing.
old-location: display\pfnsubmitcommandcb.htm
old-project: display
ms.assetid: 60300845-9050-4D0A-83D1-76A45EA823C1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnSubmitCommandCb
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

# PFND3DDDI_SUBMITCOMMANDCB callback



## -description
<p><b>pfnSubmitCommandCb</b> is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing. These contexts generate commands directly from user mode, manage their own command buffer pool and don’t make use of allocation or patch location list.</p>
<p><b>pfnSubmitCommandCb</b> replaces the old <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rendercb.md">pfnRenderCb</a> for such contexts and must be used in its place. Contexts that operate in legacy patch mode must continue to use the old <i>pfnRenderCb</i>.</p>
<p>Although the user mode driver doesn’t generate patch locations it must still generate a list of the primaries that  are being written to. The video memory manager uses the allocation list to determine which primary allocations are being referenced for write by each command buffer. This information is used to synchronize rendering to the primaries with <i>Flip</i> operations.</p>
<p>Some kernel mode drivers need information from their user mode driver on how to submit a particular direct memory access (DMA) buffer to their GPU. In Windows Display Driver Model (WDDM) 1.0, this information was sent by the user mode driver to the kernel mode driver through the command buffer. Since DMA buffer are built directly by the user mode driver and submitted to the GPU without modification they can’t be used to send information to the kernel driver anymore. As a result, we are adding an explicit private driver data buffer to be sent along with a submission. Note that this private driver data is unidirectional and the kernel mode driver can’t return information to the user mode driver through this buffer.</p>


## -prototype

````
PFND3DDDI_SUBMITCOMMANDCB pfnSubmitCommandCb;

HRESULT APIENTRY CALLBACK* pfnSubmitCommandCb(
  _In_       HANDLE                 hDevice,
  _In_ const D3DDDICB_SUBMITCOMMAND *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device.</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-submitcommand.md">D3DDDICB_SUBMITCOMMAND</a> structure that describes the operation to perform.</p>
</dd>
</dl>

## -returns
<p>If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks


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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rendercb.md">pfnRenderCb</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-submitcommand.md">D3DDDICB_SUBMITCOMMAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SUBMITCOMMANDCB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
