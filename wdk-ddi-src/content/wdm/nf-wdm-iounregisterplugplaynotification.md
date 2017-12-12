---
UID: NF.wdm.IoUnregisterPlugPlayNotification
title: IoUnregisterPlugPlayNotification function
author: windows-driver-content
description: This routine is obsolete in Windows 7 and later versions of Windows. For more information, see the following Remarks section.The IoUnregisterPlugPlayNotification routine removes the registration of a driver's callback routine for a PnP event.
old-location: kernel\iounregisterplugplaynotification.htm
old-project: kernel
ms.assetid: 55eca513-030c-47f8-9ce9-ab36183cbaf2
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: IoUnregisterPlugPlayNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoUnregisterPlugPlayNotification
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# IoUnregisterPlugPlayNotification function



## -description
This routine is <u>obsolete</u> in Windows 7 and later versions of Windows. For more information, see the following Remarks section.

The <b>IoUnregisterPlugPlayNotification</b> routine removes the registration of a driver's callback routine for a PnP event.



## -syntax

````
NTSTATUS IoUnregisterPlugPlayNotification(
  _In_ PVOID NotificationEntry
);
````


## -parameters

### -param NotificationEntry [in]

Pointer to an opaque value representing the registration to be removed. The value was returned by a previous call to <a href="kernel.ioregisterplugplaynotification">IoRegisterPlugPlayNotification</a>.


## -returns
<b>IoUnregisterPlugPlayNotification</b> always returns STATUS_SUCCESS if <i>NotificationEntry </i>is valid.


## -remarks
In Windows 7 and later versions of Windows, this function is obsolete and is provided only to support existing drivers. Use the <a href="kernel.iounregisterplugplaynotificationex">IoUnregisterPlugPlayNotificationEx</a> routine instead.

<b>IoUnregisterPlugPlayNotification</b> removes one PnP notification registration; that is, the registration of one driver callback routine for one PnP event category.

Drivers should unregister a notification first, then free any related context buffer.

A driver cannot be unloaded until it removes all of its PnP notification registrations because there is a reference on its driver object for each active registration.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioregisterplugplaynotification">IoRegisterPlugPlayNotification</a>
</dt>
<dt>
<a href="kernel.iounregisterplugplaynotificationex">IoUnregisterPlugPlayNotificationEx</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoUnregisterPlugPlayNotification routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

