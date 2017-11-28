---
UID: NF.wdfiotarget.WdfIoTargetWdmGetTargetFileHandle
title: WdfIoTargetWdmGetTargetFileHandle
author: windows-driver-content
description: The WdfIoTargetWdmGetTargetFileHandle method returns a handle to the file that is associated with a specified remote I/O target.
old-location: wdf\wdfiotargetwdmgettargetfilehandle.htm
old-project: wdf
ms.assetid: 3312e6ca-bf2c-4a53-bd86-d36d708ed596
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfIoTargetWdmGetTargetFileHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.15
req.alt-api: WdfIoTargetWdmGetTargetFileHandle
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoTargetWdmGetTargetFileHandle function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfIoTargetWdmGetTargetFileHandle</b> method returns a handle to the file that is associated with a specified remote I/O target.</p>


## -syntax

````
HANDLE WdfIoTargetWdmGetTargetFileHandle(
  _In_ WDFIOTARGET IoTarget
);
````


## -parameters
<dl>

### -param <i>IoTarget</i> [in]

<dd>
<p>A handle to a remote I/O target object. This handle was obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>.</p>
</dd>
</dl>

## -returns
<p>If the driver specified an object name when it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>, <b>WdfIoTargetWdmGetTargetFileHandle</b> returns the file handle that is associated with the specified I/O target. Otherwise <b>WdfIoTargetWdmGetTargetFileHandle</b> returns <b>NULL</b>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>For KMDF, the returned file handle is a kernel-mode handle that is valid in an arbitrary thread context. For information about how a driver can use this file handle, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564923">Using a File Handle</a>. </p>

<p>The file handle that the <b>WdfIoTargetWdmGetTargetFileHandle</b> method returns is valid until the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548586">WdfIoTargetClose</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548589">WdfIoTargetCloseForQueryRemove</a>, or until the remote I/O target object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> function for the remote I/O target object, and if the object is deleted before the remote I/O target is closed, the pointer is valid until the <i>EvtCleanupCallback</i> function returns.</p>

<p>If the driver attempts to access the WDM device object after it has been removed, the driver can cause the system to crash.  The <a href="http://go.microsoft.com/fwlink/p/?linkid=251907">toastmon</a> sample demonstrates how the driver can provide an <a href="..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-query-remove.md">EvtIoTargetQueryRemove</a> callback function so that it is notified if the I/O target is removed.</p>

<p>For UMDF, <b>WdfIoTargetWdmGetTargetFileHandle</b> returns a Win32 HANDLE valid only in the current process.</p>

<p>If the driver specifies NULL for <i>FileName</i> when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/dn265641">WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE</a>,  <b>WdfIoTargetWdmGetTargetFileHandle</b> returns a non-NULL handle.</p>

<p>For more information about <b>WdfIoTargetWdmGetTargetFileHandle</b>, see <a href="wdf.obtaining_information_about_a_general_i_o_target">Obtaining Information About a General I/O Target</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example obtains a handle to the file that is associated with a specified remote I/O target.</p>

<p>A legacy UMDF driver (version 1.<i>x</i>)  calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff558841">IWDFDevice::RetrieveDeviceName</a> to get the name of the underlying kernel-mode device and then open a handle to it with <b>CreateFile</b>. The driver then sends I/O directly to the device using <b>DeviceIoControl</b>.</p>

<p>Starting in UMDF 2.15, the driver opens the local I/O target by file and retrieves its handle. The framework opens and closes the file handle. The file handle remains valid within the contract of <b>WdfIoTargetWdmGetTargetFileHandle</b>.</p>

<p>For KMDF, the returned file handle is a kernel-mode handle that is valid in an arbitrary thread context. For information about how a driver can use this file handle, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564923">Using a File Handle</a>. </p>

<p>The file handle that the <b>WdfIoTargetWdmGetTargetFileHandle</b> method returns is valid until the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548586">WdfIoTargetClose</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548589">WdfIoTargetCloseForQueryRemove</a>, or until the remote I/O target object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> function for the remote I/O target object, and if the object is deleted before the remote I/O target is closed, the pointer is valid until the <i>EvtCleanupCallback</i> function returns.</p>

<p>If the driver attempts to access the WDM device object after it has been removed, the driver can cause the system to crash.  The <a href="http://go.microsoft.com/fwlink/p/?linkid=251907">toastmon</a> sample demonstrates how the driver can provide an <a href="..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-query-remove.md">EvtIoTargetQueryRemove</a> callback function so that it is notified if the I/O target is removed.</p>

<p>For UMDF, <b>WdfIoTargetWdmGetTargetFileHandle</b> returns a Win32 HANDLE valid only in the current process.</p>

<p>If the driver specifies NULL for <i>FileName</i> when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/dn265641">WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE</a>,  <b>WdfIoTargetWdmGetTargetFileHandle</b> returns a non-NULL handle.</p>

<p>For more information about <b>WdfIoTargetWdmGetTargetFileHandle</b>, see <a href="wdf.obtaining_information_about_a_general_i_o_target">Obtaining Information About a General I/O Target</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example obtains a handle to the file that is associated with a specified remote I/O target.</p>

<p>A legacy UMDF driver (version 1.<i>x</i>)  calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff558841">IWDFDevice::RetrieveDeviceName</a> to get the name of the underlying kernel-mode device and then open a handle to it with <b>CreateFile</b>. The driver then sends I/O directly to the device using <b>DeviceIoControl</b>.</p>

<p>Starting in UMDF 2.15, the driver opens the local I/O target by file and retrieves its handle. The framework opens and closes the file handle. The file handle remains valid within the contract of <b>WdfIoTargetWdmGetTargetFileHandle</b>.</p>

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
<p>2.15</p>
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
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548686">WdfIoTargetWdmGetTargetFileObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetWdmGetTargetFileHandle method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
