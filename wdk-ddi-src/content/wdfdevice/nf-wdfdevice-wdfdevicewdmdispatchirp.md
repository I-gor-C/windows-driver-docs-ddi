---
UID: NF.wdfdevice.WdfDeviceWdmDispatchIrp
title: WdfDeviceWdmDispatchIrp
author: windows-driver-content
description: The WdfDeviceWdmDispatchIrp method returns a dispatched IRP to the framework from EvtDeviceWdmIrpDispatch.
old-location: wdf\wdfdevicewdmdispatchirp.htm
old-project: wdf
ms.assetid: 362C6F7C-7B92-43A8-9BD0-F647FDD266E4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDeviceWdmDispatchIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.17
req.alt-api: WdfDeviceWdmDispatchIrp
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceWdmDispatchIrp function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceWdmDispatchIrp</b> method returns a dispatched IRP to the framework from <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md">EvtDeviceWdmIrpDispatch</a>.</p>


## -syntax

````
NTSTATUS WdfDeviceWdmDispatchIrp(
  _In_ WDFDEVICE   Device,
  _In_ PIRP          Irp,
  _In_ WDFCONTEXT   DispatchContext
);
````


## -parameters
<dl>

### -param <i> Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>   Irp</i> [in]

<dd>
<p>A pointer to an IRP structure.</p>
</dd>

### -param <i>  DispatchContext</i> [in]

<dd>
<p>The dispatch context parameter the driver received in <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md">EvtDeviceWdmIrpDispatch</a>  callback.</p>
</dd>
</dl>

## -returns
<p>The <b>WdfDeviceWdmDispatchIrp</b> method returns an NTSTATUS value that the framework or the driver provides as a result of processing the IRP. The driver must use this return value as the return value for the <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md">EvtDeviceWdmIrpDispatch</a> callback function that called <b>WdfDeviceWdmDispatchIrp</b>.</p>

<p>A bug check occurs if a KMDF  driver supplies an invalid object handle.  If a UMDF driver supplies an invalid handle, the driver host process terminates.</p>

## -remarks
<p>If your driver provides an <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md">EvtDeviceWdmIrpDispatch</a> callback function, you can call <b>WdfDeviceWdmDispatchIrp</b> from within the callback function to return the IRP to the framework for default processing instead of dispatching it to a specific queue.</p>

<p> For more information about specifying queues for IRPs as they arrive, see <a href="wdf.dispatching_irps_to_i_o_queues">Dispatching IRPs to I/O Queues</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.17</p>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md">EvtDeviceWdmIrpDispatch</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue.md">WdfDeviceWdmDispatchIrpToIoQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceWdmDispatchIrp method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
