---
UID: NE.wdfdevice._WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS
title: WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS
author: windows-driver-content
description: The WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS enumeration type defines flags that the driver can specify when it calls WdfDeviceWdmDispatchIrpToIoQueue.
old-location: wdf\wdf_dispatch_irp_to_io_queue_flags.htm
old-project: wdf
ms.assetid: 6A205F51-990F-4721-B4C7-B96E944D2A54
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS
req.alt-loc: wdfdevice.h
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
req.product: Windows 10 or later.
---

# WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS</b> enumeration type defines flags that the driver can specify when it calls  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451105">WdfDeviceWdmDispatchIrpToIoQueue</a>.</p>


## -syntax

````
typedef enum _WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS { 
  WDF_DISPATCH_IRP_TO_IO_QUEUE_NO_FLAGS                     = 0x00000000,
  WDF_DISPATCH_IRP_TO_IO_QUEUE_INVOKE_INCALLERCTX_CALLBACK  = 0x00000001,
  WDF_DISPATCH_IRP_TO_IO_QUEUE_PREPROCESSED_IRP             = 0x00000002
} WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WDF_DISPATCH_IRP_TO_IO_QUEUE_NO_FLAGS"></a><a id="wdf_dispatch_irp_to_io_queue_no_flags"></a><b>WDF_DISPATCH_IRP_TO_IO_QUEUE_NO_FLAGS</b>

<dd>
<p>No flags are set.</p>
</dd>

### -field <a id="WDF_DISPATCH_IRP_TO_IO_QUEUE_INVOKE_INCALLERCTX_CALLBACK"></a><a id="wdf_dispatch_irp_to_io_queue_invoke_incallerctx_callback"></a><b>WDF_DISPATCH_IRP_TO_IO_QUEUE_INVOKE_INCALLERCTX_CALLBACK</b>

<dd>
<p>Specifies that the framework should call the <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a> callback function before inserting the request into the queue.</p>
</dd>

### -field <a id="WDF_DISPATCH_IRP_TO_IO_QUEUE_PREPROCESSED_IRP"></a><a id="wdf_dispatch_irp_to_io_queue_preprocessed_irp"></a><b>WDF_DISPATCH_IRP_TO_IO_QUEUE_PREPROCESSED_IRP</b>

<dd>
<p>Specifies that the IRP was preprocessed by the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function.  Accordingly, the framework adjusts the IRP's stack location to the next entry before inserting it into the queue.</p>
</dd>
</dl>

## -remarks
<p> For more information about specifying queues for IRPs as they arrive, see <a href="wdf.dispatching_irps_to_i_o_queues">Dispatching IRPs to I/O Queues</a>.</p>

<p> For more information about specifying queues for IRPs as they arrive, see <a href="wdf.dispatching_irps_to_i_o_queues">Dispatching IRPs to I/O Queues</a>.</p>

<p> For more information about specifying queues for IRPs as they arrive, see <a href="wdf.dispatching_irps_to_i_o_queues">Dispatching IRPs to I/O Queues</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451105">WdfDeviceWdmDispatchIrpToIoQueue</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md">EvtDeviceWdmIrpPreprocess</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
