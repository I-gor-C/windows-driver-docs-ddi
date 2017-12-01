---
UID: NC.d3dkmddi.DXGKCB_NOTIFY_DPC
title: DXGKCB_NOTIFY_DPC
author: windows-driver-content
description: The DxgkCbNotifyDpc function informs the graphics processing unit (GPU) scheduler about a graphics hardware update at deferred-procedure-call (DPC) time.
old-location: display\dxgkcbnotifydpc.htm
old-project: display
ms.assetid: 3df3f7d4-3721-46f5-b9e3-19bd3d870292
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
req.alt-api: DxgkCbNotifyDpc
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
req.irql: DISPATCH_LEVEL
req.iface: 
---

# DXGKCB_NOTIFY_DPC callback



## -description
<p>The <b>DxgkCbNotifyDpc</b> function informs the graphics processing unit (GPU) scheduler about a graphics hardware update at deferred-procedure-call (DPC) time.</p>


## -prototype

````
DXGKCB_NOTIFY_DPC DxgkCbNotifyDpc;

VOID APIENTRY DxgkCbNotifyDpc(
  _In_ const HANDLE hAdapter
)
{ ... }
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>[in] A handle to the adapter object for the GPU. The driver receives the handle from the <b>DeviceHandle</b> member of the <a href="display.dxgkrnl_interface">DXGKRNL_INTERFACE</a> structure in a call to its <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The display miniport driver's DPC callback routine calls the <b>DxgkCbNotifyDpc</b> function to inform the GPU scheduler about an update to a fence through a direct memory access (DMA) stream to the graphics hardware. </p>

<p>The following code example shows how to notify the GPU scheduler about the DMA or V-Sync interrupt.</p>

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
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb-queue-dpc.md">DxgkCbQueueDpc</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-notify-interrupt.md">DxgkCbNotifyInterrupt</a>
</dt>
<dt>
<a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>
</dt>
<dt>
<a href="display.dxgkrnl_interface">DXGKRNL_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_NOTIFY_DPC callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
