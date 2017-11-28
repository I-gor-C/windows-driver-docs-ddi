---
UID: NF.wudfddi.IWDFDevice.PostEvent
title: IWDFDevice::PostEvent
author: windows-driver-content
description: The PostEvent method asynchronously notifies applications that are waiting for the specified event from a driver.
old-location: wdf\iwdfdevice_postevent.htm
old-project: wdf
ms.assetid: 3df25c91-d421-48fe-958c-48bce3bc78b8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDevice, PostEvent, IWDFDevice::PostEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDevice.PostEvent
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
req.iface: IWDFDevice
req.product: Windows 10 or later.
---

# IWDFDevice::PostEvent method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>PostEvent</b> method asynchronously notifies applications that are waiting for the specified event from a driver.</p>


## -syntax

````
HRESULT PostEvent(
  [in] REFGUID        EventGuid,
  [in] WDF_EVENT_TYPE EventType,
  [in] BYTE           *pbData,
  [in] DWORD          cbDataSize
);
````


## -parameters
<dl>

### -param <i>EventGuid</i> [in]

<dd>
<p>The GUID for the event. The GUID is determined by the application and the driver and is opaque to the framework.</p>
</dd>

### -param <i>EventType</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn265637">WDF_EVENT_TYPE</a>-typed value that identifies the type of event. In the current version of UMDF, the driver must set <i>EventType</i> to <b>WdfEventBroadcast</b> (1). <b>WdfEventBroadcast</b> indicates that the event is broadcast. Applications can subscribe to <b>WdfEventBroadcast</b>-type events. To receive broadcast events, the application must register for notification through the Microsoft Win32 <b>RegisterDeviceNotification</b> function. <b>WdfEventBroadcast</b>-type events are exposed as DBT_CUSTOMEVENT-type events to applications.</p>
</dd>

### -param <i>pbData</i> [in]

<dd>
<p>A pointer to a buffer that contains data that is associated with the event. <b>NULL</b> is a valid value. </p>
</dd>

### -param <i>cbDataSize</i> [in]

<dd>
<p>The size, in bytes, of data that <i>pbData</i> points to. Zero is a valid size value if <i>pbData</i> is set to <b>NULL</b>. </p>
<p>The maximum size of the event data is slightly less than MAXUSHORT (64 KB). The precise upper limit is (0xFFFF - <a href="https://msdn.microsoft.com/library/windows/hardware/ff545727">FIELD_OFFSET</a>(<a href="https://msdn.microsoft.com/library/windows/hardware/ff564596">TARGET_DEVICE_CUSTOM_NOTIFICATION</a>, CustomDataBuffer)). </p>
</dd>
</dl>

## -returns
<p><b>PostEvent</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The event data was successfully sent to the operating system.</p><dl>
<dt><b>HRESULT_FROM_WIN32(ERROR_NOT_ENOUGH_MEMORY)</b></dt>
</dl><p>The data size that the <i>cbDataSize</i> parameter specifies is larger than the maximum allowable size. </p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The <i>EventType</i> parameter is not set to <b>WdfEventBroadcast</b> (1). </p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
<a href="wdf.iwdfdevice_postevent">PostEvent</a> could not allocate memory that was required for it to complete.</p>

<p> </p>

<p><b>PostEvent</b> might also return other HRESULT values.</p>

## -remarks
<p>When the driver calls <b>IWDFDevice::PostEvent</b> to notify the requesting application about an event, UMDF sends the event to the operating system. The operating system sends the event on to the requesting application in an asynchronous operation. If the operating system initially returns no error, the driver receives no error (S_OK). However, later, if the operating system receives an error while it attempts to deliver the event (possibly because of a low memory condition), the operating system is unable to inform the driver about the error. Because of the asynchronous nature of this event notification, delivery of the event to the requesting application is not guaranteed. If event information is lost on its way up to the requesting application, the application should be able to recover from the lost event. </p>

<p>For information about creating device events, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF Drivers</a>.</p>

<p>When the driver calls <b>IWDFDevice::PostEvent</b> to notify the requesting application about an event, UMDF sends the event to the operating system. The operating system sends the event on to the requesting application in an asynchronous operation. If the operating system initially returns no error, the driver receives no error (S_OK). However, later, if the operating system receives an error while it attempts to deliver the event (possibly because of a low memory condition), the operating system is unable to inform the driver about the error. Because of the asynchronous nature of this event notification, delivery of the event to the requesting application is not guaranteed. If event information is lost on its way up to the requesting application, the application should be able to recover from the lost event. </p>

<p>For information about creating device events, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF Drivers</a>.</p>

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
<p>1.5</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556917">IWDFDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545727">FIELD_OFFSET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564596">TARGET_DEVICE_CUSTOM_NOTIFICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265606">WdfDevicePostEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice::PostEvent method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
