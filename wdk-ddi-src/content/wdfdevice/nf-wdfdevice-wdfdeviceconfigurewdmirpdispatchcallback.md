---
UID: NF.wdfdevice.WdfDeviceConfigureWdmIrpDispatchCallback
title: WdfDeviceConfigureWdmIrpDispatchCallback
author: windows-driver-content
description: The WdfDeviceConfigureWdmIrpDispatchCallback method registers a driver's EvtDeviceWdmIrpDispatch callback function.
old-location: wdf\wdfdeviceconfigurewdmirpdispatchcallback.htm
old-project: wdf
ms.assetid: 594E0FF1-A965-4CE4-A2EA-C9098685FCED
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDeviceConfigureWdmIrpDispatchCallback
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
req.alt-api: WdfDeviceConfigureWdmIrpDispatchCallback
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

# WdfDeviceConfigureWdmIrpDispatchCallback function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceConfigureWdmIrpDispatchCallback</b> method registers a driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md">EvtDeviceWdmIrpDispatch</a> callback function.</p>


## -syntax

````
NTSTATUS WdfDeviceConfigureWdmIrpDispatchCallback(
  _In_     WDFDEVICE                      Device,
  _In_opt_ WDFDRIVER                      Driver,
  _In_     UCHAR                          MajorFunction,
  _In_     PFN_WDFDEVICE_WDM_IRP_DISPATCH EvtDeviceWdmIrpDispatch,
  _In_opt_ WDFCONTEXT                     DriverContext
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>Driver</i> [in, optional]

<dd>
<p>A handle to the driver's framework driver object that the driver obtained from a previous call to <a href="..\wdfdriver\nf-wdfdriver-wdfdrivercreate.md">WdfDriverCreate</a> or <a href="..\wdfdriver\nf-wdfdriver-wdfgetdriver.md">WdfGetDriver</a>.  This parameter is optional.</p>
</dd>

### -param <i>MajorFunction</i> [in]

<dd>
<p>One of the following IRP major function codes: IRP_MJ_DEVICE_CONTROL, IRP_MJ_INTERNAL_DEVICE_CONTROL, IRP_MJ_READ, IRP_MJ_WRITE.</p>
</dd>

### -param <i>EvtDeviceWdmIrpDispatch</i> [in]

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md">EvtDeviceWdmIrpDispatch</a> callback function.</p>
</dd>

### -param <i>DriverContext</i> [in, optional]

<dd>
<p>An untyped pointer to driver-defined context information that the framework passes to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md">EvtDeviceWdmIrpDispatch</a> callback function. This parameter is optional and can be NULL.</p>
</dd>
</dl>

## -returns
<p>If the <b>WdfDeviceConfigureWdmIrpDispatchCallback</b> method encounters no errors, it returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid <i>MajorFunction</i> value was supplied.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Insufficient memory was available.</p>

<p> </p>

## -remarks
<p>A driver calls the <b>WdfDeviceConfigureWdmIrpDispatchCallback</b> method to register an <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md">EvtDeviceWdmIrpDispatch</a> callback function. The framework then calls <i>EvtDeviceWdmIrpDispatch</i> whenever it receives an I/O request packet (IRP) containing an IRP major function code that matches the <i>MajorFunction</i> parameter of this method.</p>

<p>A driver typically calls <b>WdfDeviceConfigureWdmIrpDispatchCallback</b> from its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function.</p>

<p>You must call <b>WdfDeviceConfigureWdmIrpDispatchCallback</b> once for each MJ function for which the driver wants to register a callback function. In other words, multiple calls are required for intercepting multiple MJ functions.</p>

<p>A driver might call the <b>WdfDeviceConfigureWdmIrpDispatchCallback</b> method for these reasons:<ul>
<li>To examine an IRP and assign it to  a specific queue based on domain-specific criteria, for example, direct all I/O associated with a file object to a particular queue.</li>
<li>To select on an individual request basis the need to call the <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a> callback function.</li>
</ul>
</p>

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
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmdispatchirp.md">WdfDeviceWdmDispatchIrp</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue.md">WdfDeviceWdmDispatchIrpToIoQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceConfigureWdmIrpDispatchCallback method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
