---
UID: NE.wdfdevice._WDF_DEVICE_IO_TYPE
title: WDF_DEVICE_IO_TYPE
author: windows-driver-content
description: The WDF_DEVICE_IO_TYPE enumeration is used to specify a method for accessing data buffers.
old-location: wdf\wdf_device_io_type.htm
ms.assetid: 0ad08e4f-7a9b-4052-888e-ae01c9c105c8
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_DEVICE_IO_TYPE
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
ms.keywords: WDF_REL_TIMEOUT_IN_US
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_IO_TYPE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_DEVICE_IO_TYPE</b> enumeration is used to specify a <a href="https://msdn.microsoft.com/f95a0aec-65f9-44c9-8ae5-11bb4d832752">method for accessing data buffers</a>.</p>


## -syntax

````
typedef enum _WDF_DEVICE_IO_TYPE { 
  WdfDeviceIoUndefined         = 0,
  WdfDeviceIoNeither           = 1,
  WdfDeviceIoBuffered          = 2,
  WdfDeviceIoDirect            = 3,
  WdfDeviceIoBufferedOrDirect  = 4
} WDF_DEVICE_IO_TYPE, *PWDF_DEVICE_IO_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfDeviceIoUndefined"></a><a id="wdfdeviceioundefined"></a><a id="WDFDEVICEIOUNDEFINED"></a><b>WdfDeviceIoUndefined</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="WdfDeviceIoNeither"></a><a id="wdfdeviceioneither"></a><a id="WDFDEVICEIONEITHER"></a><b>WdfDeviceIoNeither</b>

<dd>
<p><b>UMDF </b>This value is not used by UMDF drivers. A UMDF driver can access device I/O control requests that specify the METHOD_NEITHER buffer access method by setting the <b>UmdfMethodNeitherAction</b> INF directive and using <b>WdfDeviceIoBuffered</b> or <b>WdfDeviceIoDirect</b>. For more information, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives in INF Files</a>.</p>
<p><b>KMDF </b>Neither buffered nor direct I/O will be used to access data buffers.</p>
</dd>

### -field <a id="WdfDeviceIoBuffered"></a><a id="wdfdeviceiobuffered"></a><a id="WDFDEVICEIOBUFFERED"></a><b>WdfDeviceIoBuffered</b>

<dd>
<p>Buffered I/O will be used to access data buffers.</p>
</dd>

### -field <a id="WdfDeviceIoDirect"></a><a id="wdfdeviceiodirect"></a><a id="WDFDEVICEIODIRECT"></a><b>WdfDeviceIoDirect</b>

<dd>
<p>Direct I/O will be used to access data buffers.</p>
</dd>

### -field <a id="WdfDeviceIoBufferedOrDirect"></a><a id="wdfdeviceiobufferedordirect"></a><a id="WDFDEVICEIOBUFFEREDORDIRECT"></a><b>WdfDeviceIoBufferedOrDirect</b>

<dd>
<p>This value is not used by KMDF drivers.</p>
<p><b>UMDF </b>Buffered I/O or direct I/O will be used to access data buffers.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_DEVICE_IO_TYPE</b> enumeration is used to specify buffer access method types in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure is used  as input to <a href="https://msdn.microsoft.com/library/windows/hardware/dn265604">WdfDeviceInitSetIoTypeEx</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546128">WdfDeviceInitSetIoType</a>.</p>

<p>The <b>WDF_DEVICE_IO_TYPE</b> enumeration is used to specify buffer access method types in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure is used  as input to <a href="https://msdn.microsoft.com/library/windows/hardware/dn265604">WdfDeviceInitSetIoTypeEx</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546128">WdfDeviceInitSetIoType</a>.</p>

<p>The <b>WDF_DEVICE_IO_TYPE</b> enumeration is used to specify buffer access method types in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a> structure is used  as input to <a href="https://msdn.microsoft.com/library/windows/hardware/dn265604">WdfDeviceInitSetIoTypeEx</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546128">WdfDeviceInitSetIoType</a>.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265642">WDF_IO_TYPE_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546128">WdfDeviceInitSetIoType</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265604">WdfDeviceInitSetIoTypeEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_IO_TYPE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
