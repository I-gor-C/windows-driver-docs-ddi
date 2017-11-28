---
UID: NS.wdm._DEVICE_INTERFACE_CHANGE_NOTIFICATION
title: DEVICE_INTERFACE_CHANGE_NOTIFICATION
author: windows-driver-content
description: The DEVICE_INTERFACE_CHANGE_NOTIFICATION structure describes a device interface that has been enabled (arrived) or disabled (removed).
old-location: kernel\device_interface_change_notification.htm
old-project: kernel
ms.assetid: 3b5d67c0-eb3f-4ac1-9f85-f9c673314458
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: DEVICE_INTERFACE_CHANGE_NOTIFICATION, DEVICE_INTERFACE_CHANGE_NOTIFICATION, *PDEVICE_INTERFACE_CHANGE_NOTIFICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_INTERFACE_CHANGE_NOTIFICATION
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# DEVICE_INTERFACE_CHANGE_NOTIFICATION structure



## -description
<p>The <b>DEVICE_INTERFACE_CHANGE_NOTIFICATION</b> structure describes a device interface that has been enabled (arrived) or disabled (removed). The PnP manager sends this structure to a driver that registered a callback routine for notification of <b>EventCategoryDeviceInterfaceChange</b> events.</p>


## -syntax

````
typedef struct _DEVICE_INTERFACE_CHANGE_NOTIFICATION {
  USHORT          Version;
  USHORT          Size;
  GUID            Event;
  GUID            InterfaceClassGuid;
  PUNICODE_STRING SymbolicLinkName;
} DEVICE_INTERFACE_CHANGE_NOTIFICATION, *PDEVICE_INTERFACE_CHANGE_NOTIFICATION;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Specifies the version of the data structure, currently 1. </p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the size of the structure, in bytes, including the size of the standard first three members plus the event-specific data. </p>
</dd>

### -field <b>Event</b>

<dd>
<p>Specifies a GUID identifying the event:  GUID_DEVICE_INTERFACE_ARRIVAL or GUID_DEVICE_INTERFACE_REMOVAL. The GUIDs are defined in Wdmguid.h. </p>
</dd>

### -field <b>InterfaceClassGuid</b>

<dd>
<p>Specifies the class of the device interface that has just been enabled or disabled.</p>
</dd>

### -field <b>SymbolicLinkName</b>

<dd>
<p>Pointer to a Unicode string that contains the name of the symbolic link for the device interface. </p>
</dd>
</dl>

## -remarks
<p>This structure is allocated from paged memory.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547073">HWPROFILE_CHANGE_NOTIFICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549526">IoRegisterPlugPlayNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558805">PLUGPLAY_NOTIFICATION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564601">TARGET_DEVICE_REMOVAL_NOTIFICATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DEVICE_INTERFACE_CHANGE_NOTIFICATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
