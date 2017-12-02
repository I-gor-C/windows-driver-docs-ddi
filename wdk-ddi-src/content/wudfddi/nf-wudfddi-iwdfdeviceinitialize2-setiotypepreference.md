---
UID: NF.wudfddi.IWDFDeviceInitialize2.SetIoTypePreference
title: IWDFDeviceInitialize2::SetIoTypePreference
author: windows-driver-content
description: The SetIoTypePreference method specifies your preferences for how UMDF and the driver access the data buffers of a device's I/O requests.
old-location: wdf\iwdfdeviceinitialize2_setiotypepreference.htm
old-project: wdf
ms.assetid: 7d79f34d-42aa-4ac7-a63d-2f17ee0dfcf0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFDeviceInitialize2, SetIoTypePreference, IWDFDeviceInitialize2::SetIoTypePreference
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFDeviceInitialize2.SetIoTypePreference
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFDeviceInitialize2
req.product: Windows 10 or later.
---

# IWDFDeviceInitialize2::SetIoTypePreference method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>SetIoTypePreference</b> method specifies your preferences for how UMDF and the driver access the data buffers of a device's I/O requests.</p>


## -syntax

````
void SetIoTypePreference(
  [in] WDF_DEVICE_IO_BUFFER_RETRIEVAL RetrievalMode,
  [in] WDF_DEVICE_IO_TYPE             ReadWritePreference,
  [in] WDF_DEVICE_IO_TYPE             IoControlPreference
);
````


## -parameters
<dl>

### -param RetrievalMode [in]

<dd>
<p>A <a href="..\wudfddi_types\ne-wudfddi-types--wdf-device-io-buffer-retrieval.md">WDF_DEVICE_IO_BUFFER_RETRIEVAL</a>-typed value that specifies the buffer retrieval mode that you prefer UMDF to use to make an I/O request's buffers available to the driver.</p>
</dd>

### -param ReadWritePreference [in]

<dd>
<p>A <a href="..\wudfddi_types\ne-wudfddi-types--wdf-device-io-type.md">WDF_DEVICE_IO_TYPE</a>-typed value that specifies the buffer access method that you prefer UMDF to use for the data buffers of read and write requests. </p>
</dd>

### -param IoControlPreference [in]

<dd>
<p>A WDF_DEVICE_IO_TYPE-typed value that specifies the buffer access method that you prefer UMDF to use for the data buffers of device I/O control requests. </p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>If a driver calls <b>SetIoTypePreference</b> for a device, it must do so from its <a href="wdf.idriverentry_ondeviceadd">IDriverEntry::OnDeviceAdd</a> callback function, before the driver calls <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a>.</p>

<p>If the driver does not call <b>SetIoTypePreference</b>, UMDF sets the <i>RetrievalMode</i> parameter to <b>WdfDeviceIoBufferRetrievalCopyImmediately</b> and it sets the buffer access method to <b>WdfDeviceIoBuffered</b> for read, write, and device I/O control requests.</p>

<p>UMDF might not use the preferences that the driver specifies when it calls <b>SetIoTypePreference</b>. For more information about how UMDF chooses a retrieval mode and buffer access method, see <a href="wdf.accessing_data_buffers_in_umdf_drivers#specifying_a_buffer_retrieval_mode#specifying_a_buffer_retrieval_mode">Specifying a Buffer Retrieval Mode</a> and <a href="wdf.accessing_data_buffers_in_umdf_drivers#how_umdf_chooses_a_buffer_access_method_for_an_i_o_request#how_umdf_chooses_a_buffer_access_method_for_an_i_o_request">How UMDF Chooses a Buffer Access Method for an I/O Request</a><u>.</u></p>

<p>A driver cannot set the buffer access method to <b>WdfDeviceIoDirect</b> or <b>WdfDeviceIoBufferedOrDirect</b> unless it also sets the <i>RetrievalMode</i> parameter to <b>WdfDeviceIoBufferRetrievalDeferred</b>.</p>

<p>For more information about accessing an I/O request's data buffers, see <a href="wdf.accessing_data_buffers_in_umdf_drivers">Accessing Data Buffers in UMDF-Based Drivers</a>.</p>

<p>The following code example shows a segment of a driver's <a href="wdf.idriverentry_ondeviceadd">IDriverEntry::OnDeviceAdd</a> callback function. The segment obtains the <a href="..\wudfddi\nn-wudfddi-iwdfdeviceinitialize2.md">IWDFDeviceInitialize2</a> interface and then calls <b>SetIoTypePreference</b>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfdeviceinitialize2.md">IWDFDeviceInitialize2</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest2_geteffectiveiotype">IWDFIoRequest2::GetEffectiveIoType</a>
</dt>
<dt>
<a href="..\wudfddi_types\ne-wudfddi-types--wdf-device-io-buffer-retrieval.md">WDF_DEVICE_IO_BUFFER_RETRIEVAL</a>
</dt>
<dt>
<a href="..\wudfddi_types\ne-wudfddi-types--wdf-device-io-type.md">WDF_DEVICE_IO_TYPE (UMDF)</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetiotypeex.md">WdfDeviceInitSetIoTypeEx</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetiotype.md">WdfDeviceInitSetIoType</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDeviceInitialize2::SetIoTypePreference method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
