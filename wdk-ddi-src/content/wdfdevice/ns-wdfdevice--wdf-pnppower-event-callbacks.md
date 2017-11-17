---
UID: NS.wdfdevice._WDF_PNPPOWER_EVENT_CALLBACKS
title: WDF_PNPPOWER_EVENT_CALLBACKS
author: windows-driver-content
description: The WDF_PNPPOWER_EVENT_CALLBACKS structure contains pointers to a driver's Plug and Play and power event callback functions.
old-location: wdf\wdf_pnppower_event_callbacks.htm
ms.assetid: 2bfd677f-f2bd-49d7-b572-d7df4de0425c
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
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
ms.keywords: WDF_PNPPOWER_EVENT_CALLBACKS, WDF_PNPPOWER_EVENT_CALLBACKS, *PWDF_PNPPOWER_EVENT_CALLBACKS
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
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/0cfabb0f-2d5e-4445-8683-d2916de5b549">EvtDeviceD0Entry</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceD0EntryPostInterruptsEnabled</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/38d74ce1-9d9d-4da5-a2b3-579048850b28">EvtDeviceD0EntryPostInterruptsEnabled</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceD0Exit</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/bc3af732-f9ab-43a4-bc6f-7fa0b4c05a66">EvtDeviceD0Exit</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceD0ExitPreInterruptsDisabled</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/8f57c3b3-2dcf-44a3-a3c2-c9585bdfa253">EvtDeviceD0ExitPreInterruptsDisabled</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDevicePrepareHardware</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/a3d4a983-8a75-44be-bd72-8673d89f9f87">EvtDevicePrepareHardware</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceReleaseHardware</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/b4c17e57-688c-4c76-892c-5c8abbf83f20">EvtDeviceReleaseHardware</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoCleanup</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/639ff3fd-ce38-417e-8fc4-a03ad259a5c8">EvtDeviceSelfManagedIoCleanup</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoFlush</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/ad4ace83-c6c1-4b5f-b998-f46f3e721165">EvtDeviceSelfManagedIoFlush</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoInit</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/9dbc66db-ea94-4e6a-9618-00999a9dd641">EvtDeviceSelfManagedIoInit</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoSuspend</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/85a569ea-eb14-4453-9591-fc44afbd3a59">EvtDeviceSelfManagedIoSuspend</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSelfManagedIoRestart</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/13d7fbc6-6f93-4ef9-abd4-f2adc4e8e23a">EvtDeviceSelfManagedIoRestart</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSurpriseRemoval</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/0fa0eb7e-7fbb-4838-b1d7-ef5a9d5024d4">EvtDeviceSurpriseRemoval</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceQueryRemove</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/59e6a8bc-e2f9-4d26-92b0-8f8944e1aa88">EvtDeviceQueryRemove</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceQueryStop</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/4f2ed29a-fed0-4286-81db-7a4c8a15a7dd">EvtDeviceQueryStop</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceUsageNotification</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/b6b7dd80-fd91-4194-8288-4d703983a798">EvtDeviceUsageNotification</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceRelationsQuery</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/3a156696-1dd5-4383-a0cc-8d07ec92bdbf">EvtDeviceRelationsQuery</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceUsageNotificationEx</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/A5C3E247-4883-4BFE-B36A-45AA989F36C9">EvtDeviceUsageNotificationEx</a> event callback function, or <b>NULL</b>. The <b>EvtDeviceUsageNotificationEx</b> member is available in version 1.11 and later versions of KMDF.
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_PNPPOWER_EVENT_CALLBACKS structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
