---
UID: NF.d3dkmthk.D3DKMTSubmitCommand
title: D3DKMTSubmitCommand function
author: windows-driver-content
description: D3DKMTSubmitCommand is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing.
old-location: display\d3dkmtsubmitcommand.htm
old-project: display
ms.assetid: E726B4AC-F003-45B3-B467-F123DBE60D87
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DKMTSubmitCommand
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTSubmitCommand
req.alt-loc: GDI32.dll,API-MS-Win-DX-D3DKMT-L1-1-1.dll,GDI32.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: GDI32.lib
req.dll: GDI32.dll
req.irql: 
---

# D3DKMTSubmitCommand function



## -description
<b>D3DKMTSubmitCommand</b> is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing. These contexts generate commands directly from user mode, manage their own command buffer pool and don’t make use of the allocation or patch location list.
This function replaces the old <a href="display.dxgkddirenderkm">Render</a> function for such contexts and must be used in its place. Contexts that operate in legacy patch mode must continue to use the old <i>Render</i> function.
Although the user mode driver doesn’t generate patch locations, it must still generate a list of primaries, which are being written to. The video memory manager uses the allocation list to determine which primary allocations are being referenced for write by each command buffer. This information is used to synchronize rendering to the primaries with <i>flip</i> operations.
Some kernel mode drivers need information from their user mode driver on how to submit a particular direct memory access (DMA) buffer to their GPU. In Windows Display Driver Model (WDDM) 1.0, this information was sent by the user mode driver to the kernel mode driver through the command buffer. Since DMA buffer are built directly by the user mode driver and submitted to the GPU without modification they can’t be used to send information to the kernel driver anymore. To enable the transfer of information between the user mode and kernel mode drivers, an explicit private driver data buffer has been added to be sent along with a submission. <div class="alert"><b>Note</b>  This private driver data is unidirectional and the kernel mode driver can’t return information to the user mode driver through this buffer.</div>
<div> </div>



## -syntax

````
NTSTATUS APIENTRY D3DKMTSubmitCommand(
  _In_ const D3DKMT_SUBMITCOMMAND *pData
);
````


## -parameters

### -param pData [in]

A pointer to a <a href="display.d3dkmt_submitcommand">D3DKMT_SUBMITCOMMAND</a> structure that describes the operation.

## -returns
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The device context was successfully created.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>Parameters were validated and determined to be incorrect.

 

This function might also return other <b>NTSTATUS</b> values.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2016
</td>
</tr>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>GDI32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>GDI32.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dkmt_submitcommand">D3DKMT_SUBMITCOMMAND</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTSubmitCommand function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
