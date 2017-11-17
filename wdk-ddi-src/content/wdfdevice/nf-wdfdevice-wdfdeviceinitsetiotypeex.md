---
UID: NF.wdfdevice.WdfDeviceInitSetIoTypeEx
title: WdfDeviceInitSetIoTypeEx
author: windows-driver-content
description: The WdfDeviceInitSetIoTypeEx method sets the method or preference for how a driver will access the data buffers that are included in read and write requests, as well as device I/O control requests, for a specified device.
old-location: wdf\wdfdeviceinitsetiotypeex.htm
ms.assetid: 3746D618-C92C-43AB-A45A-2188D572105D
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.13
req.umdf-ver: 2.0
req.alt-api: WdfDeviceInitSetIoTypeEx
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: 
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
ms.keywords: WdfDeviceInitSetIoTypeEx
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceInitSetIoTypeEx function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceInitSetIoTypeEx</b> method sets the method or preference for how a driver will access the data buffers that are included in read and write requests, as well as device I/O control requests, for a specified device.</p>


## -syntax

````
void WdfDeviceInitSetIoTypeEx(
  _In_ PWDFDEVICE_INIT     DeviceInit,
  _In_ PWDF_IO_TYPE_CONFIG IoTypeConfig
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure.</p>
</dd>

### -param <i>IoTypeConfig</i> [in]

<dd>
<p>Pointer to <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure initialized using WDF_IO_TYPE_CONFIG_INIT macro.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>If you are writing a driver using KMDF version 1.11 or earlier, you must instead use <a href="https://msdn.microsoft.com/library/windows/hardware/ff546128">WdfDeviceInitSetIoType</a>.</p>

<p><b>KMDF </b>A KMDF driver calls <b>WdfDeviceInitSetIoTypeEx</b> to set a buffer-access method for read and write requests. For device I/O control requests, the framework uses the buffer type that is encoded in the I/O control code (IOCTL).</p>

<p><b>UMDF </b>A UMDF driver calls <b>WdfDeviceInitSetIoTypeEx</b> to register preferences for read and write requests, as well as device I/O control requests.  The values that a UMDF driver provides to <b>WdfDeviceInitSetIoTypeEx</b> are only preferences, and are not guaranteed to be used by the framework.  Your driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/dn265602">WdfDeviceGetDeviceStackIoType</a> to determine the buffer access methods that UMDF has assigned to a device's read/write requests and I/O control requests. For I/O control requests, the access method that the framework uses might differ from the access method specified in the IOCTL and the access method requested by the driver.</p>

<p>If a driver calls <b>WdfDeviceInitSetIoTypeEx</b>, it must do so before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>.</p>

<p>If the driver does not call <b>WdfDeviceInitSetIoTypeEx</b>, the framework sets the driver's buffer-access method to <b>WdfDeviceIoBuffered</b>, for the specified device.</p>

<p>Calling <b>WdfDeviceInitSetIoTypeEx</b> from a KMDF filter driver has no effect. For KMDF filter drivers, the framework uses the I/O type that the next-lower driver in the driver stack specifies.</p>

<p>A UMDF filter driver can, however, register preferences for buffer-access method by calling <b>WdfDeviceInitSetIoTypeEx</b>.</p>

<p>All UMDF drivers in a driver stack must use the same method for accessing a device's buffers. If UMDF determines that some drivers prefer either buffered I/O or direct I/O for a device while other drivers prefer only buffered I/O for the device, UMDF uses buffered I/O for all drivers. If one or more of a stack's drivers prefer only buffered I/O while others prefer only direct I/O, UMDF logs an event to the system event log and does not start the driver stack.</p>

<p>For more information about buffer-access methods, see <a href="wdf.accessing_data_buffers_in_kmdf_drivers">Accessing Data Buffers</a>.</p>

<p>This method is the UMDF 2.0 equivalent of <a href="https://msdn.microsoft.com/7d79f34d-42aa-4ac7-a63d-2f17ee0dfcf0"> IWDFDeviceInitialize2::SetIoTypePreference</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure, sets the driver's buffer-access preferences to direct I/O, specifies that transfers smaller than 32 KB should use buffered I/O, and calls <b>WdfDeviceInitSetIoTypeEx</b>.</p>

<p>If you are writing a driver using KMDF version 1.11 or earlier, you must instead use <a href="https://msdn.microsoft.com/library/windows/hardware/ff546128">WdfDeviceInitSetIoType</a>.</p>

<p><b>KMDF </b>A KMDF driver calls <b>WdfDeviceInitSetIoTypeEx</b> to set a buffer-access method for read and write requests. For device I/O control requests, the framework uses the buffer type that is encoded in the I/O control code (IOCTL).</p>

<p><b>UMDF </b>A UMDF driver calls <b>WdfDeviceInitSetIoTypeEx</b> to register preferences for read and write requests, as well as device I/O control requests.  The values that a UMDF driver provides to <b>WdfDeviceInitSetIoTypeEx</b> are only preferences, and are not guaranteed to be used by the framework.  Your driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/dn265602">WdfDeviceGetDeviceStackIoType</a> to determine the buffer access methods that UMDF has assigned to a device's read/write requests and I/O control requests. For I/O control requests, the access method that the framework uses might differ from the access method specified in the IOCTL and the access method requested by the driver.</p>

<p>If a driver calls <b>WdfDeviceInitSetIoTypeEx</b>, it must do so before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>.</p>

<p>If the driver does not call <b>WdfDeviceInitSetIoTypeEx</b>, the framework sets the driver's buffer-access method to <b>WdfDeviceIoBuffered</b>, for the specified device.</p>

<p>Calling <b>WdfDeviceInitSetIoTypeEx</b> from a KMDF filter driver has no effect. For KMDF filter drivers, the framework uses the I/O type that the next-lower driver in the driver stack specifies.</p>

<p>A UMDF filter driver can, however, register preferences for buffer-access method by calling <b>WdfDeviceInitSetIoTypeEx</b>.</p>

<p>All UMDF drivers in a driver stack must use the same method for accessing a device's buffers. If UMDF determines that some drivers prefer either buffered I/O or direct I/O for a device while other drivers prefer only buffered I/O for the device, UMDF uses buffered I/O for all drivers. If one or more of a stack's drivers prefer only buffered I/O while others prefer only direct I/O, UMDF logs an event to the system event log and does not start the driver stack.</p>

<p>For more information about buffer-access methods, see <a href="wdf.accessing_data_buffers_in_kmdf_drivers">Accessing Data Buffers</a>.</p>

<p>This method is the UMDF 2.0 equivalent of <a href="https://msdn.microsoft.com/7d79f34d-42aa-4ac7-a63d-2f17ee0dfcf0"> IWDFDeviceInitialize2::SetIoTypePreference</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure, sets the driver's buffer-access preferences to direct I/O, specifies that transfers smaller than 32 KB should use buffered I/O, and calls <b>WdfDeviceInitSetIoTypeEx</b>.</p>

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
<p>1.13</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265602">WdfDeviceGetDeviceStackIoType</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7d79f34d-42aa-4ac7-a63d-2f17ee0dfcf0"> IWDFDeviceInitialize2::SetIoTypePreference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265643">WDF_IO_TYPE_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546128">WdfDeviceInitSetIoType</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitSetIoTypeEx method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
