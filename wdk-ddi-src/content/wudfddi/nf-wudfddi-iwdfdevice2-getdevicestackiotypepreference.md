---
UID: NF.wudfddi.IWDFDevice2.GetDeviceStackIoTypePreference
title: IWDFDevice2::GetDeviceStackIoTypePreference
author: windows-driver-content
description: The GetDeviceStackIoTypePreference method retrieves the buffer access methods that the framework is using for a device.
old-location: wdf\iwdfdevice2_getdevicestackiotypepreference.htm
old-project: wdf
ms.assetid: 3a1f6432-3f61-4502-ac98-fa984539f88e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDevice2, GetDeviceStackIoTypePreference, IWDFDevice2::GetDeviceStackIoTypePreference
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
req.alt-api: IWDFDevice2.GetDeviceStackIoTypePreference
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
req.iface: IWDFDevice2
req.product: Windows 10 or later.
---

# IWDFDevice2::GetDeviceStackIoTypePreference method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetDeviceStackIoTypePreference</b> method retrieves the buffer access methods that the framework is using for a device.</p>


## -syntax

````
void GetDeviceStackIoTypePreference(
  [out] WDF_DEVICE_IO_TYPE *ReadWritePreference,
  [out] WDF_DEVICE_IO_TYPE *IoControlPreference
);
````


## -parameters
<dl>

### -param <i>ReadWritePreference</i> [out]

<dd>
<p>A pointer to a driver-allocated location that receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551255">WDF_DEVICE_IO_TYPE</a>-typed value. This value identifies the buffer access method that the framework is using for a device's read and write requests.</p>
</dd>

### -param <i>IoControlPreference</i> [out]

<dd>
<p>A pointer to a driver-allocated location that receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551255">WDF_DEVICE_IO_TYPE</a>-typed value. This value that identifies the buffer access method that the framework is using for a device's I/O control requests.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>If your driver calls <b>GetDeviceStackIoTypePreference</b> before the PnP manager has loaded all of the device's drivers, the values that <b>GetDeviceStackIoTypePreference</b> retrieves might not be the values that it actually uses.</p>

<p>For more information about how the framework chooses a buffer access method, see <a href="wdf.accessing_data_buffers_in_umdf_drivers#how_umdf_chooses_a_buffer_access_method_for_an_i_o_request#how_umdf_chooses_a_buffer_access_method_for_an_i_o_request">How UMDF Chooses a Buffer Access Method for an I/O Request</a>.</p>

<p>The following code example retrieves the buffer access methods that the framework is using for a device.</p>

<p>If your driver calls <b>GetDeviceStackIoTypePreference</b> before the PnP manager has loaded all of the device's drivers, the values that <b>GetDeviceStackIoTypePreference</b> retrieves might not be the values that it actually uses.</p>

<p>For more information about how the framework chooses a buffer access method, see <a href="wdf.accessing_data_buffers_in_umdf_drivers#how_umdf_chooses_a_buffer_access_method_for_an_i_o_request#how_umdf_chooses_a_buffer_access_method_for_an_i_o_request">How UMDF Chooses a Buffer Access Method for an I/O Request</a>.</p>

<p>The following code example retrieves the buffer access methods that the framework is using for a device.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556969">IWDFDeviceInitialize2::SetIoTypePreference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice2::GetDeviceStackIoTypePreference method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
