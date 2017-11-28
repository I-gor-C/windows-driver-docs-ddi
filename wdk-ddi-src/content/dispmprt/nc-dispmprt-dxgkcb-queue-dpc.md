---
UID: NC.dispmprt.DXGKCB_QUEUE_DPC
title: DXGKCB_QUEUE_DPC
author: windows-driver-content
description: The DxgkCbQueueDpc function queues a deferred procedure call (DPC) for execution at IRQL DISPATCH_LEVEL.
old-location: display\dxgkcbqueuedpc.htm
old-project: display
ms.assetid: c8c26675-8b87-4818-ad51-4e0a341965d0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkCbQueueDpc
req.alt-loc: dispmprt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: IDebugSystemObjects4
---

# DXGKCB_QUEUE_DPC callback



## -description
<p>The <b>DxgkCbQueueDpc</b> function queues a deferred procedure call (DPC) for execution at IRQL  DISPATCH_LEVEL.</p>


## -prototype

````
DXGKCB_QUEUE_DPC DxgkCbQueueDpc;

BOOLEAN DxgkCbQueueDpc(
  _In_ HANDLE DeviceHandle
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceHandle</i> [in]

<dd>
<p>A handle that represents a display adapter. The display miniport driver previously obtained this handle in the <b>DeviceHandle</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560942">DXGKRNL_INTERFACE</a> structure that was passed to <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>.</p>
</dd>
</dl>

## -returns
<p><b>DxgkCbQueueDpc</b> returns <b>TRUE</b> if the DPC is successfully queued; otherwise it returns <b>FALSE</b>.</p>

## -remarks
<p>This function queues a DPC object for the display miniport and calls the <a href="display.dxgkddidpcroutine">DxgkDdiDpcRoutine</a> function when the interrupt service routine (ISR) requests it. </p>

<p>There can only be one callback to this function scheduled per device at any one time. If a callback is already scheduled for a device, a second call to <b>DxgkCbQueueDpc</b> will not have any effect and will return <b>FALSE</b>.</p>

<p>For more information on the use of this function, see these topics:</p>

<p>This function queues a DPC object for the display miniport and calls the <a href="display.dxgkddidpcroutine">DxgkDdiDpcRoutine</a> function when the interrupt service routine (ISR) requests it. </p>

<p>There can only be one callback to this function scheduled per device at any one time. If a callback is already scheduled for a device, a second call to <b>DxgkCbQueueDpc</b> will not have any effect and will return <b>FALSE</b>.</p>

<p>For more information on the use of this function, see these topics:</p>

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
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb-queue-dpc.md">DxgkCbQueueDpc</a>
</dt>
<dt>
<a href="display.dxgkddidpcroutine">DxgkDdiDpcRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_QUEUE_DPC callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
