---
UID: NF.wdfdevice.WdfDeviceInitSetRemoveLockOptions
title: WdfDeviceInitSetRemoveLockOptions function
author: windows-driver-content
description: The WdfDeviceInitSetRemoveLockOptions method causes the framework to acquire a remove lock before delivering an IRP of any type to the driver.
old-location: wdf\wdfdeviceinitsetremovelockoptions.htm
old-project: wdf
ms.assetid: 0BCF4141-BE4E-42C0-8986-BE039B27F5D5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDeviceInitSetRemoveLockOptions
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WdfDeviceInitSetRemoveLockOptions
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceInitSetRemoveLockOptions function



## -description
<p class="CCE_Message">[Applies to KMDF only]

   The <b>WdfDeviceInitSetRemoveLockOptions</b> method causes the framework to acquire a remove lock before delivering an IRP of any type to the driver.


## -syntax

````
void WdfDeviceInitSetRemoveLockOptions(
  _In_ PWDFDEVICE_INIT          DeviceInit,
  _In_ PWDF_REMOVE_LOCK_OPTIONS Options
);
````


## -parameters

### -param DeviceInit [in]

A caller-supplied pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.

### -param Options [in]

A pointer to a <a href="wdf.wdf_remove_lock_options">WDF_REMOVE_LOCK_OPTIONS</a> structure.

## -returns
This method does not return a value.

## -remarks
By default, the framework acquires a remove lock before it delivers IRPs of the following major types to the driver:

<dl>
<dd>IRP_MJ_PNP</dd>
<dd>IRP_MJ_POWER</dd>
<dd>IRP_MJ_SYSTEM_CONTROL</dd>
</dl>

When the IRP completes, the framework releases the remove lock.

Starting in KMDF 1.11, the driver can optionally call <b>WdfDeviceInitSetRemoveLockOptions</b> to cause the framework to acquire a remove lock before delivering all IRP types, not just those listed above.

If your driver has kernel-mode clients that send I/O unsynchronized with the PnP state of your device, you may experience crashes due to I/O IRPs arriving after the framework device object has been removed. In this case, you can call <b>WdfDeviceInitSetRemoveLockOptions</b> to prevent the device object from being removed until I/O has completed.

Typically, a driver calls <b>WdfDeviceInitSetRemoveLockOptions</b> from within its <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback function, just before calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>.

After a driver calls <b>WdfDeviceInitSetRemoveLockOptions</b>, the setting remains in effect for the lifetime of the framework device object.

For more information about remove locks, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565504">Using Remove Locks</a>.

This code example initializes a <a href="wdf.wdf_remove_lock_options">WDF_REMOVE_LOCK_OPTIONS</a> structure and calls <b>WdfDeviceInitSetRemoveLockOptions</b>.

## -requirements
<table>
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
Minimum KMDF version
</th>
<td width="70%">
1.11
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_remove_lock_options">WDF_REMOVE_LOCK_OPTIONS</a>
</dt>
<dt>
<a href="wdf.wdf_remove_lock_options_init">WDF_REMOVE_LOCK_OPTIONS_INIT</a>
</dt>
<dt>
<a href="wdf.wdf_remove_lock_options_flags">WDF_REMOVE_LOCK_OPTIONS_FLAGS</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitSetRemoveLockOptions method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
