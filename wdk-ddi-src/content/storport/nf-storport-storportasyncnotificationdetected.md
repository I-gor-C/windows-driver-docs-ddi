---
UID: NF.storport.StorPortAsyncNotificationDetected
title: StorPortAsyncNotificationDetected
author: windows-driver-content
description: A storage miniport driver calls StorPortAsyncNotificationDetected to notify the Storport driver of a storage device status change event.
old-location: storage\storportasyncnotificationdetected.htm
old-project: storage
ms.assetid: 558F652C-6D1A-4BAF-9C2C-3F4FE24651D2
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortAsyncNotificationDetected
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortAsyncNotificationDetected
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any
req.iface: 
req.product: Windows 10 or later.
---

# StorPortAsyncNotificationDetected function



## -description
<p>A storage miniport driver calls <b>StorPortAsyncNotificationDetected</b> to  notify the Storport driver of a storage device status change event.</p>
<p>The notification is queued as a work item for deferred processing at DISPATCH_LEVEL or lower IRQL.</p>


## -syntax

````
ULONG StorPortAsyncNotificationDetected(
  _In_ PVOID         HwDeviceExtension,
       PSTOR_ADDRESS Address,
       ULONGLONG     Flags
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>A pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls <a href="..\storport\nf-storport-storportinitialize.md">StorPortInitialize</a>. The port driver frees this memory when it removes the device.</p>
</dd>

### -param Address 

<dd>
<p>The address of the storage device with a status change event.</p>
</dd>

### -param Flags 

<dd>
<p>The status notifications to indicate to Storport.</p>
<p>
<p>The Flags parameter contains a bitwise OR combination of status notifications. All status values can be set with the single <b>RAID_ASYNC_NOTIFY_SUPPORTED_FLAGS</b> value.</p>
</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="RAID_ASYNC_NOTIFY_FLAG_MEDIA_STATUS"></a><a id="raid_async_notify_flag_media_status"></a><dl>

### -param RAID_ASYNC_NOTIFY_FLAG_MEDIA_STATUS

</dl>
</td>
<td width="60%">
<p>Notify Storport that a media change occurred.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="RAID_ASYNC_NOTIFY_FLAG_DEVICE_STATUS"></a><a id="raid_async_notify_flag_device_status"></a><dl>

### -param RAID_ASYNC_NOTIFY_FLAG_DEVICE_STATUS

</dl>
</td>
<td width="60%">
<p>Notify Storport that the functional status of the storage device has changed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="RAID_ASYNC_NOTIFY_FLAG_DEVICE_OPERATION"></a><a id="raid_async_notify_flag_device_operation"></a><dl>

### -param RAID_ASYNC_NOTIFY_FLAG_DEVICE_OPERATION

</dl>
</td>
<td width="60%">
<p>Notify Storport that an operational role of the storage device has changed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>A status value indicating the result of the notification. This can be one of these values:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The state change notification is scheduled for processing.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The address type invalid.</p>

<p>-or-</p>

<p><i>HwDeviceExtension</i> is <b>NULL</b>.</p>

<p>-or-</p>

<p><i>Flags</i> contains an undefined value.</p><dl>
<dt><b>STOR_STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The storage device unit cannot be found at <i>address</i>.</p>

<p>-or-</p>

<p>The storage device does not support asynchronous notifications.</p><dl>
<dt><b>STOR_STATUS_BUSY</b></dt>
</dl><p>A prior notification is in process and this one cannot be scheduled.</p>

<p> </p>

## -remarks
<p>A miniport can detect status events in its <a href="storage.hwstorinterrupt">HwStorInterrupt</a> routine and call <b>StorPortAsyncNotificationDetected</b> to queue and process the status change notification later at a lower IRQL. </p>

<p>When processed by Storport, the status event notification is forwarded to the storage class driver to initiate any necessary system response actions.</p>

<p>If the <i>Flags</i> parameter is 0, Storport will indicate all status values in its notification to the storage class driver.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any</p>
</td>
</tr>
</table>