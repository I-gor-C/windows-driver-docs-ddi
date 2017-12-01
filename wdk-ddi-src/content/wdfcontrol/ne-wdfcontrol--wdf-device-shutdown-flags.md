---
UID: NE.wdfcontrol._WDF_DEVICE_SHUTDOWN_FLAGS
title: WDF_DEVICE_SHUTDOWN_FLAGS
author: windows-driver-content
description: The WDF_DEVICE_SHUTDOWN_FLAGS enumeration defines flags that identify types of shutdown notifications that a driver can receive.
old-location: wdf\wdf_device_shutdown_flags.htm
old-project: wdf
ms.assetid: e394f8de-7257-4baa-9057-bd4bad34212d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_TASK_SEND_OPTIONS, WDF_TASK_SEND_OPTIONS, *PWDF_TASK_SEND_OPTIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfcontrol.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_DEVICE_SHUTDOWN_FLAGS
req.alt-loc: wdfcontrol.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_SHUTDOWN_FLAGS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_DEVICE_SHUTDOWN_FLAGS</b> enumeration defines flags that identify types of shutdown notifications that a driver can receive.</p>


## -syntax

````
typedef enum _WDF_DEVICE_SHUTDOWN_FLAGS { 
  WdfDeviceShutdown            = 0x01,
  WdfDeviceLastChanceShutdown  = 0x02
} WDF_DEVICE_SHUTDOWN_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WdfDeviceShutdown"></a><a id="wdfdeviceshutdown"></a><a id="WDFDEVICESHUTDOWN"></a><b>WdfDeviceShutdown</b>

<dd>
<p>The driver is notified when the system is losing its power, but before file systems are flushed.</p>
</dd>

### -field <a id="WdfDeviceLastChanceShutdown"></a><a id="wdfdevicelastchanceshutdown"></a><a id="WDFDEVICELASTCHANCESHUTDOWN"></a><b>WdfDeviceLastChanceShutdown</b>

<dd>
<p>The driver is notified when the system is losing its power, and after all file systems have been flushed.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_DEVICE_SHUTDOWN_FLAGS</b> enumeration is used as an input parameter to <a href="..\wdfcontrol\nf-wdfcontrol-wdfcontroldeviceinitsetshutdownnotification.md">WdfControlDeviceInitSetShutdownNotification</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcontrol.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfcontrol\nf-wdfcontrol-wdfcontroldeviceinitsetshutdownnotification.md">WdfControlDeviceInitSetShutdownNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_SHUTDOWN_FLAGS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
