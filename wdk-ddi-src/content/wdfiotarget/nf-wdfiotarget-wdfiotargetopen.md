---
UID: NF.wdfiotarget.WdfIoTargetOpen
title: WdfIoTargetOpen
author: windows-driver-content
description: The WdfIoTargetOpen method opens a remote I/O target so the driver can send I/O requests to it.
old-location: wdf\wdfiotargetopen.htm
ms.assetid: 6ea2e6dd-9794-4214-8fb1-db563f49b33a
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfIoTargetOpen
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WdfIoTargetOpen
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoTargetOpen function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfIoTargetOpen</b> method opens a remote I/O target so the driver can send I/O requests to it.</p>


## -syntax

````
NTSTATUS WdfIoTargetOpen(
  _In_ WDFIOTARGET                IoTarget,
  _In_ PWDF_IO_TARGET_OPEN_PARAMS OpenParams
);
````


## -parameters
<dl>

### -param <i>IoTarget</i> [in]

<dd>
<p>A handle to an I/O target object that was obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>.</p>
</dd>

### -param <i>OpenParams</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>WdfIoTargetOpen</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The specified I/O target is already open.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Available system resources were insufficient to complete the operation.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The size of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure that <i>OpenParams</i> specified was incorrect.</p><dl>
<dt><b>STATUS_NO_SUCH_DEVICE</b></dt>
</dl><p>The <i>TargetFileObject</i> member of the caller's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure specified an invalid file object.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The device name that is identified in the <i>OpenParams</i> parameter cannot be found.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Drivers can open remote I/O targets by supplying a Unicode string that represents an <a href="https://msdn.microsoft.com/b30e7475-7f94-4993-b373-8e4a8b1bcb4c">object name</a> or by supplying a pointer to a Windows Driver Model (WDM) <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure. (Framework-based drivers typically do not have pointers to other drivers' DEVICE_OBJECT structures.)</p>

<p>To obtain a device interface name prior to calling <b>WdfIoTargetOpen</b>, a UMDF driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/hh780224">CM_Register_Notification</a> to register for interface arrival and removal notification. Then it can open the remote target using
the interface symbolic name that it receives in the interface notification callback routine.  The driver should continue to listen for the removal notification while the handle is open. If the target driver fails, the UMDF driver must close the handle.</p>

<p> If the interface already exists, a UMDF driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff538463">CM_Get_Device_Interface_List</a>, possibly calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff538471">CM_Get_Device_Interface_List_Size</a> first to determine the required buffer size.</p>

<p>If you want your driver to use its local I/O target, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a> instead of <b>WdfIoTargetOpen</b>.</p>

<p>If a call to <b>WdfIoTargetOpen</b> fails, the driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a> to delete the I/O target object.</p>

<p>For more information about <b>WdfIoTargetOpen</b>, see <a href="wdf.initializing_a_general_i_o_target">Initializing a General I/O Target</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following example creates an I/O target object, initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure, and opens a remote I/O target by specifying a device's symbolic link name.</p>

<p>Drivers can open remote I/O targets by supplying a Unicode string that represents an <a href="https://msdn.microsoft.com/b30e7475-7f94-4993-b373-8e4a8b1bcb4c">object name</a> or by supplying a pointer to a Windows Driver Model (WDM) <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure. (Framework-based drivers typically do not have pointers to other drivers' DEVICE_OBJECT structures.)</p>

<p>To obtain a device interface name prior to calling <b>WdfIoTargetOpen</b>, a UMDF driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/hh780224">CM_Register_Notification</a> to register for interface arrival and removal notification. Then it can open the remote target using
the interface symbolic name that it receives in the interface notification callback routine.  The driver should continue to listen for the removal notification while the handle is open. If the target driver fails, the UMDF driver must close the handle.</p>

<p> If the interface already exists, a UMDF driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff538463">CM_Get_Device_Interface_List</a>, possibly calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff538471">CM_Get_Device_Interface_List_Size</a> first to determine the required buffer size.</p>

<p>If you want your driver to use its local I/O target, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a> instead of <b>WdfIoTargetOpen</b>.</p>

<p>If a call to <b>WdfIoTargetOpen</b> fails, the driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a> to delete the I/O target object.</p>

<p>For more information about <b>WdfIoTargetOpen</b>, see <a href="wdf.initializing_a_general_i_o_target">Initializing a General I/O Target</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following example creates an I/O target object, initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a> structure, and opens a remote I/O target by specifying a device's symbolic link name.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552377">WDF_IO_TARGET_OPEN_PARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548586">WdfIoTargetClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetOpen method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
