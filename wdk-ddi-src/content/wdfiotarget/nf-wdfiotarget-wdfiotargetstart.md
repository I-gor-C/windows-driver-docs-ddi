---
UID: NF.wdfiotarget.WdfIoTargetStart
title: WdfIoTargetStart
author: windows-driver-content
description: The WdfIoTargetStart method starts sending queued requests to a local or remote I/O target.
old-location: wdf\wdfiotargetstart.htm
old-project: wdf
ms.assetid: 0d270910-f0ff-4305-bd68-caa36d3a02c5
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfIoTargetStart
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfIoTargetStart
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, FailD0EntryIoTargetState, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoTargetStart function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfIoTargetStart</b> method starts sending queued requests to a local or remote I/O target.</p>


## -syntax

````
NTSTATUS WdfIoTargetStart(
  _In_ WDFIOTARGET IoTarget
);
````


## -parameters
<dl>

### -param <i>IoTarget</i> [in]

<dd>
<p>A handle to a local or remote I/O target object that was obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>, or from a method that a specialized I/O target provides.</p>
</dd>
</dl>

## -returns
<p><b>WdfIoTargetStart</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The device has been removed.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>If your driver can detect recoverable device errors, you might want your driver to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> to temporarily stop sending requests, then later call <b>WdfIoTargetStart</b> to resume sending requests.</p>

<p>Additionally, if a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a> callback function must call <b>WdfIoTargetStart</b> to start the reader.</p>

<p>Your driver must call <b>WdfIoTargetStart</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> synchronously. After the driver calls one of these functions, it must not call the other function before the first one returns.</p>

<p>For more information about <b>WdfIoTargetStart</b>, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example shows how an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a> callback function can call <b>WdfIoTargetStart</b>, if the driver uses a continuous reader for a USB pipe. </p>

<p>If your driver can detect recoverable device errors, you might want your driver to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> to temporarily stop sending requests, then later call <b>WdfIoTargetStart</b> to resume sending requests.</p>

<p>Additionally, if a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a> callback function must call <b>WdfIoTargetStart</b> to start the reader.</p>

<p>Your driver must call <b>WdfIoTargetStart</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> synchronously. After the driver calls one of these functions, it must not call the other function before the first one returns.</p>

<p>For more information about <b>WdfIoTargetStart</b>, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example shows how an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a> callback function can call <b>WdfIoTargetStart</b>, if the driver uses a continuous reader for a USB pipe. </p>

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
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfiotarget.h (include Wdf.h)</dt>
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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975077">FailD0EntryIoTargetState</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetStart method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
