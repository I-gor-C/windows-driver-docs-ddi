---
UID: NS.wdfdevice._WDF_PNPPOWER_EVENT_CALLBACKS
title: WDF_PNPPOWER_EVENT_CALLBACKS
author: windows-driver-content
description: The WDF_PNPPOWER_EVENT_CALLBACKS structure contains pointers to a driver's Plug and Play and power event callback functions.
old-location: wdf\wdf_pnppower_event_callbacks.htm
old-project: wdf
ms.assetid: 2bfd677f-f2bd-49d7-b572-d7df4de0425c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_PNPPOWER_EVENT_CALLBACKS, WDF_PNPPOWER_EVENT_CALLBACKS, *PWDF_PNPPOWER_EVENT_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_PNPPOWER_EVENT_CALLBACKS
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_PNPPOWER_EVENT_CALLBACKS structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_PNPPOWER_EVENT_CALLBACKS</b> structure contains pointers to a driver's Plug and Play and power event callback functions. </p>


## -syntax

````
typedef struct _WDF_PNPPOWER_EVENT_CALLBACKS {
  ULONG                                           Size;
  PFN_WDF_DEVICE_D0_ENTRY                         EvtDeviceD0Entry;
  PFN_WDF_DEVICE_D0_ENTRY_POST_INTERRUPTS_ENABLED EvtDeviceD0EntryPostInterruptsEnabled;
  PFN_WDF_DEVICE_D0_EXIT                          EvtDeviceD0Exit;
  PFN_WDF_DEVICE_D0_EXIT_PRE_INTERRUPTS_DISABLED  EvtDeviceD0ExitPreInterruptsDisabled;
  PFN_WDF_DEVICE_PREPARE_HARDWARE                 EvtDevicePrepareHardware;
  PFN_WDF_DEVICE_RELEASE_HARDWARE                 EvtDeviceReleaseHardware;
  PFN_WDF_DEVICE_SELF_MANAGED_IO_CLEANUP          EvtDeviceSelfManagedIoCleanup;
  PFN_WDF_DEVICE_SELF_MANAGED_IO_FLUSH            EvtDeviceSelfManagedIoFlush;
  PFN_WDF_DEVICE_SELF_MANAGED_IO_INIT             EvtDeviceSelfManagedIoInit;
  PFN_WDF_DEVICE_SELF_MANAGED_IO_SUSPEND          EvtDeviceSelfManagedIoSuspend;
  PFN_WDF_DEVICE_SELF_MANAGED_IO_RESTART          EvtDeviceSelfManagedIoRestart;
  PFN_WDF_DEVICE_SURPRISE_REMOVAL                 EvtDeviceSurpriseRemoval;
  PFN_WDF_DEVICE_QUERY_REMOVE                     EvtDeviceQueryRemove;
  PFN_WDF_DEVICE_QUERY_STOP                       EvtDeviceQueryStop;
  PFN_WDF_DEVICE_USAGE_NOTIFICATION               EvtDeviceUsageNotification;
  PFN_WDF_DEVICE_RELATIONS_QUERY                  EvtDeviceRelationsQuery;
  PFN_WDF_DEVICE_USAGE_NOTIFICATION_EX            EvtDeviceUsageNotificationEx;
} WDF_PNPPOWER_EVENT_CALLBACKS, *PWDF_PNPPOWER_EVENT_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>EvtDeviceD0Entry</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceD0EntryPostInterruptsEnabled</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry-post-interrupts-enabled.md">EvtDeviceD0EntryPostInterruptsEnabled</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceD0Exit</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceD0ExitPreInterruptsDisabled</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit-pre-interrupts-disabled.md">EvtDeviceD0ExitPreInterruptsDisabled</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDevicePrepareHardware</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceReleaseHardware</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoCleanup</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-cleanup.md">EvtDeviceSelfManagedIoCleanup</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoFlush</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-flush.md">EvtDeviceSelfManagedIoFlush</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoInit</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-init.md">EvtDeviceSelfManagedIoInit</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoSuspend</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-suspend.md">EvtDeviceSelfManagedIoSuspend</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoRestart</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-restart.md">EvtDeviceSelfManagedIoRestart</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSurpriseRemoval</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-surprise-removal.md">EvtDeviceSurpriseRemoval</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceQueryRemove</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-query-remove.md">EvtDeviceQueryRemove</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceQueryStop</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-query-stop.md">EvtDeviceQueryStop</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceUsageNotification</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-usage-notification.md">EvtDeviceUsageNotification</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceRelationsQuery</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-relations-query.md">EvtDeviceRelationsQuery</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceUsageNotificationEx</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-usage-notification-ex.md">EvtDeviceUsageNotificationEx</a> event callback function, or <b>NULL</b>. The <b>EvtDeviceUsageNotificationEx</b> member is available in version 1.11 and later versions of KMDF.
A driver can register either <b>EvtDeviceRelationsQuery</b> or <b>EvtDeviceUsageNotificationEx</b>, but not both.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_PNPPOWER_EVENT_CALLBACKS</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546135">WdfDeviceInitSetPnpPowerEventCallbacks</a> method.</p>

<p>Your driver should initialize its WDF_PNPPOWER_EVENT_CALLBACKS structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552418">WDF_PNPPOWER_EVENT_CALLBACKS_INIT</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552424">WDF_POWER_POLICY_EVENT_CALLBACKS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_PNPPOWER_EVENT_CALLBACKS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
