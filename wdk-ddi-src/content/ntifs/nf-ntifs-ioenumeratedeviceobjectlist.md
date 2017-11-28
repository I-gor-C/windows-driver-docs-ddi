---
UID: NF.ntifs.IoEnumerateDeviceObjectList
title: IoEnumerateDeviceObjectList
author: windows-driver-content
description: The IoEnumerateDeviceObjectList routine enumerates a driver's device object list.
old-location: ifsk\ioenumeratedeviceobjectlist.htm
old-project: ifsk
ms.assetid: ce6cec58-2122-49c3-8c5c-172df2c4dd04
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IoEnumerateDeviceObjectList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Update Rollup for Windows 2000 Service Pack 4 (SP4) and on Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoEnumerateDeviceObjectList
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# IoEnumerateDeviceObjectList function



## -description
<p>The <b>IoEnumerateDeviceObjectList</b> routine enumerates a driver's device object list. </p>


## -syntax

````
NTSTATUS IoEnumerateDeviceObjectList(
  _In_  PDRIVER_OBJECT DriverObject,
  _Out_ PDEVICE_OBJECT *DeviceObjectList,
  _In_  ULONG          DeviceObjectListSize,
  _Out_ PULONG         ActualNumberDeviceObjects
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to the driver object for the driver. </p>
</dd>

### -param <i>DeviceObjectList</i> [out]

<dd>
<p>A pointer to a caller-allocated array that receives the device object pointers. This parameter can be <b>NULL</b>. </p>
</dd>

### -param <i>DeviceObjectListSize</i> [in]

<dd>
<p>Size, in bytes, of the <i>DeviceObjectList</i> array. Can be zero. </p>
</dd>

### -param <i>ActualNumberDeviceObjects</i> [out]

<dd>
<p>Actual number of device objects found in the driver object's device object list. Note that if the array at <i>DeviceObjectList</i> is too small, the number of device object pointers that are copied into the array will be less than <i>ActualNumberDeviceObjects</i>. </p>
</dd>
</dl>

## -returns
<p><b>IoEnumerateDeviceObjectList</b> can return one of the following: </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The call to <b>IoEnumerateDeviceObjectList</b> was successful. </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The array at <i>DeviceObjectList</i> is too small to hold the entire device object list. In this case, <b>IoEnumerateDeviceObjectList</b> copies as many device object pointers into the array as possible. </p>

<p> </p>

## -remarks
<p>A file system filter driver calls <b>IoEnumerateDeviceObjectList</b> to enumerate: </p>

<p>The device objects it has created. This is commonly done when the driver is preparing to unload. Note that a file system filter driver cannot safely be unloaded from a running system. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567117">ZwUnloadDriver</a>.</p>

<p>The device objects created by the base file system, so the filter knows the number of volumes to which it can attach.</p>

<p><b>IoEnumerateDeviceObjectList</b> returns all device objects created by the driver. This includes control device objects (CDO) as well as volume device objects (VDO). The two types of device objects can be distinguished by the fact that, by convention, CDOs are named and VDOs are not. </p>

<p>In the latter case, the filter driver typically calls <b>IoEnumerateDeviceObjectList</b> twice: once to get the number of device objects in the list, and once to get the device object list itself. In the first call, the caller should set the <i>DeviceObjectList</i> parameter to <b>NULL</b> and <i>DeviceObjectListSize</i> to zero. In the second call, <i>DeviceObjectList</i> should contain a pointer to an appropriately-sized pointer array, and <i>DeviceObjectListSize</i> should contain the size, in bytes, of that array. </p>

<p><b>IoEnumerateDeviceObjectList</b> increments the reference count on every device object in the list pointed to by <i>DeviceObjectList</i>. Thus every successful call to <b>IoEnumerateDeviceObjectList</b> must be matched by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>for each device object in the list. Failure to do so prevents the system from freeing or deleting these device objects because of an outstanding reference count. </p>

<p>A file system filter driver calls <b>IoEnumerateDeviceObjectList</b> to enumerate: </p>

<p>The device objects it has created. This is commonly done when the driver is preparing to unload. Note that a file system filter driver cannot safely be unloaded from a running system. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567117">ZwUnloadDriver</a>.</p>

<p>The device objects created by the base file system, so the filter knows the number of volumes to which it can attach.</p>

<p><b>IoEnumerateDeviceObjectList</b> returns all device objects created by the driver. This includes control device objects (CDO) as well as volume device objects (VDO). The two types of device objects can be distinguished by the fact that, by convention, CDOs are named and VDOs are not. </p>

<p>In the latter case, the filter driver typically calls <b>IoEnumerateDeviceObjectList</b> twice: once to get the number of device objects in the list, and once to get the device object list itself. In the first call, the caller should set the <i>DeviceObjectList</i> parameter to <b>NULL</b> and <i>DeviceObjectListSize</i> to zero. In the second call, <i>DeviceObjectList</i> should contain a pointer to an appropriately-sized pointer array, and <i>DeviceObjectListSize</i> should contain the size, in bytes, of that array. </p>

<p><b>IoEnumerateDeviceObjectList</b> increments the reference count on every device object in the list pointed to by <i>DeviceObjectList</i>. Thus every successful call to <b>IoEnumerateDeviceObjectList</b> must be matched by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>for each device object in the list. Failure to do so prevents the system from freeing or deleting these device objects because of an outstanding reference count. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>This routine is available on Update Rollup for Windows 2000 Service Pack 4 (SP4) and on Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548359">IoGetAttachedDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549145">IoGetAttachedDeviceReference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548379">IoGetLowerDeviceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567117">ZwUnloadDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoEnumerateDeviceObjectList routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
