---
UID: NE.wudfddi_types._WDF_DEVICE_IO_TYPE
title: WDF_DEVICE_IO_TYPE
author: windows-driver-content
description: The WDF_DEVICE_IO_TYPE enumeration is used to specify a method for accessing data buffers.
old-location: wdf\wdf_device_io_type__umdf_.htm
ms.assetid: 52733647-d577-4507-a5ad-5f56f3a9f8a2
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi_types.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: WDF_DEVICE_IO_TYPE
req.alt-loc: Wudfddi_types.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: WRITE_REGISTER_USHORT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_IO_TYPE enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
      The <b>WDF_DEVICE_IO_TYPE</b> enumeration is used to specify a method for <a href="wdf.accessing_data_buffers_in_umdf_drivers">accessing data buffers</a>.</p>


## -syntax

````
typedef enum _WDF_DEVICE_IO_TYPE { 
  WdfDeviceIoUndefined         = 0x00,
  WdfDeviceIoNeither           = 0x01,
  WdfDeviceIoBuffered          = 0x02,
  WdfDeviceIoDirect            = 0x03,
  WdfDeviceIoBufferedOrDirect  = 0x04,
  WdfDeviceIoMaximum           = 0x5
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
<p>Reserved for system use.</p>
</dd>

### -field <a id="WdfDeviceIoBuffered"></a><a id="wdfdeviceiobuffered"></a><a id="WDFDEVICEIOBUFFERED"></a><b>WdfDeviceIoBuffered</b>

<dd>
<p>UMDF and the driver use <a href="wdf.accessing_data_buffers_in_umdf_drivers">buffered I/O</a> to access data buffers.</p>
</dd>

### -field <a id="WdfDeviceIoDirect"></a><a id="wdfdeviceiodirect"></a><a id="WDFDEVICEIODIRECT"></a><b>WdfDeviceIoDirect</b>

<dd>
<p>UMDF and the driver use <a href="wdf.accessing_data_buffers_in_umdf_drivers">direct I/O</a> to access data buffers.</p>
</dd>

### -field <a id="WdfDeviceIoBufferedOrDirect"></a><a id="wdfdeviceiobufferedordirect"></a><a id="WDFDEVICEIOBUFFEREDORDIRECT"></a><b>WdfDeviceIoBufferedOrDirect</b>

<dd>
<p>UMDF and the driver can use either buffered I/O or direct I/O to access data buffers. </p>
</dd>

### -field <a id="WdfDeviceIoMaximum"></a><a id="wdfdeviceiomaximum"></a><a id="WDFDEVICEIOMAXIMUM"></a><b>WdfDeviceIoMaximum</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_DEVICE_IO_TYPE</b> enumeration is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556969">IWDFDeviceInitialize2::SetIoTypePreference</a> and as output from <a href="https://msdn.microsoft.com/library/windows/hardware/ff558994">IWDFIoRequest2::GetEffectiveIoType</a>.</p>

<p>You should use the following guidelines when choosing an I/O type for your driver:</p>

<p>Buffered I/O provides the best security and reliability, because applications and drivers access separate copies of the data. In addition, buffered I/O provides the best performance if most of the data transfers are relatively small (typically two memory pages or less). </p>

<p>Direct I/O provides the best performance if most I/O requests transfer large amounts of data. However, applications and drivers access a single copy of the data. Therefore, the driver must copy application-specified parameters to local driver memory before it validates the parameters to ensure that the application does not modify the parameters after validation. If the driver must validate large amounts of application data, buffered I/O might be a better choice because the driver does not have to copy the data before validating it.</p>

<p>Typically, a filter driver that can reside in several driver stacks and performs little processing of application data can support both buffered I/O and direct I/O and therefore can specify <b>WdfDeviceIoBufferedOrDirect</b>. However, if the driver validates application-specified parameters it must copy them first when direct I/O is used.</p>

<p>For more information about accessing an I/O request's data buffers, see <a href="wdf.accessing_data_buffers_in_umdf_drivers">Accessing Data Buffers in UMDF-Based Drivers</a>.</p>

<p>For the KMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551255">WDF_DEVICE_IO_TYPE</a>.</p>

<p>The <b>WDF_DEVICE_IO_TYPE</b> enumeration is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556969">IWDFDeviceInitialize2::SetIoTypePreference</a> and as output from <a href="https://msdn.microsoft.com/library/windows/hardware/ff558994">IWDFIoRequest2::GetEffectiveIoType</a>.</p>

<p>You should use the following guidelines when choosing an I/O type for your driver:</p>

<p>Buffered I/O provides the best security and reliability, because applications and drivers access separate copies of the data. In addition, buffered I/O provides the best performance if most of the data transfers are relatively small (typically two memory pages or less). </p>

<p>Direct I/O provides the best performance if most I/O requests transfer large amounts of data. However, applications and drivers access a single copy of the data. Therefore, the driver must copy application-specified parameters to local driver memory before it validates the parameters to ensure that the application does not modify the parameters after validation. If the driver must validate large amounts of application data, buffered I/O might be a better choice because the driver does not have to copy the data before validating it.</p>

<p>Typically, a filter driver that can reside in several driver stacks and performs little processing of application data can support both buffered I/O and direct I/O and therefore can specify <b>WdfDeviceIoBufferedOrDirect</b>. However, if the driver validates application-specified parameters it must copy them first when direct I/O is used.</p>

<p>For more information about accessing an I/O request's data buffers, see <a href="wdf.accessing_data_buffers_in_umdf_drivers">Accessing Data Buffers in UMDF-Based Drivers</a>.</p>

<p>For the KMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551255">WDF_DEVICE_IO_TYPE</a>.</p>

<p>The <b>WDF_DEVICE_IO_TYPE</b> enumeration is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556969">IWDFDeviceInitialize2::SetIoTypePreference</a> and as output from <a href="https://msdn.microsoft.com/library/windows/hardware/ff558994">IWDFIoRequest2::GetEffectiveIoType</a>.</p>

<p>You should use the following guidelines when choosing an I/O type for your driver:</p>

<p>Buffered I/O provides the best security and reliability, because applications and drivers access separate copies of the data. In addition, buffered I/O provides the best performance if most of the data transfers are relatively small (typically two memory pages or less). </p>

<p>Direct I/O provides the best performance if most I/O requests transfer large amounts of data. However, applications and drivers access a single copy of the data. Therefore, the driver must copy application-specified parameters to local driver memory before it validates the parameters to ensure that the application does not modify the parameters after validation. If the driver must validate large amounts of application data, buffered I/O might be a better choice because the driver does not have to copy the data before validating it.</p>

<p>Typically, a filter driver that can reside in several driver stacks and performs little processing of application data can support both buffered I/O and direct I/O and therefore can specify <b>WdfDeviceIoBufferedOrDirect</b>. However, if the driver validates application-specified parameters it must copy them first when direct I/O is used.</p>

<p>For more information about accessing an I/O request's data buffers, see <a href="wdf.accessing_data_buffers_in_umdf_drivers">Accessing Data Buffers in UMDF-Based Drivers</a>.</p>

<p>For the KMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551255">WDF_DEVICE_IO_TYPE</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi_types.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556969">IWDFDeviceInitialize2::SetIoTypePreference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558994">IWDFIoRequest2::GetEffectiveIoType</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561399">WDF_DEVICE_IO_BUFFER_RETRIEVAL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_IO_TYPE (UMDF) enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
