---
UID: NF.wdfdevice.WdfDeviceGetIoTarget
title: WdfDeviceGetIoTarget
author: windows-driver-content
description: The WdfDeviceGetIoTarget method returns a handle to a function or filter driver's local I/O target, for a specified device.
old-location: wdf\wdfdevicegetiotarget.htm
old-project: wdf
ms.assetid: a0749324-8b4e-4b82-8c51-b1b8883d521e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceGetIoTarget
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceGetIoTarget
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceGetIoTarget function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceGetIoTarget</b> method returns a handle to a function or filter driver's <a href="wdf.general_i_o_targets">local I/O target</a>, for a specified device.</p>


## -syntax

````
WDFIOTARGET WdfDeviceGetIoTarget(
  _In_ WDFDEVICE Device
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>WdfDeviceGetIoTarget</b> returns a handle to a framework I/O target object. If the specified framework device object represents a PDO, the method returns <b>NULL</b>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>When a UMDF driver sends a driver-created request to a local I/O target, the request has no associated file object. Some lower targets, such as a HIDClass-enumerated raw PDO, fail requests that have no associated file object. In this situation, a UMDF driver can specify <b>WdfIoTargetOpenLocalTargetByFile</b> to create an I/O target that represents the lower stack (just like a local target) using a file handle. As a result, any driver-created requests sent to this I/O target are associated with the file object corresponding to the handle opened.

 To do so, call the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265641">WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE</a> function before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>.</p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example obtains a handle to a specified device's local I/O target.</p>

<p>When a UMDF driver sends a driver-created request to a local I/O target, the request has no associated file object. Some lower targets, such as a HIDClass-enumerated raw PDO, fail requests that have no associated file object. In this situation, a UMDF driver can specify <b>WdfIoTargetOpenLocalTargetByFile</b> to create an I/O target that represents the lower stack (just like a local target) using a file handle. As a result, any driver-created requests sent to this I/O target are associated with the file object corresponding to the handle opened.

 To do so, call the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265641">WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE</a> function before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>.</p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example obtains a handle to a specified device's local I/O target.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>