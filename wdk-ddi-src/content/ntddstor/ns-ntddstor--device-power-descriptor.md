---
UID: NS.ntddstor._DEVICE_POWER_DESCRIPTOR
title: DEVICE_POWER_DESCRIPTOR
author: windows-driver-content
description: Used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY control code to describes the power capabilities of a storage device.
old-location: storage\device_power_descriptor.htm
ms.assetid: A5925EE4-768C-421A-9813-015513751A91
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_POWER_DESCRIPTOR
req.alt-loc: ntddstor.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: DEVICE_POWER_DESCRIPTOR, DEVICE_POWER_DESCRIPTOR, *PDEVICE_POWER_DESCRIPTOR
req.iface: 
---

# DEVICE_POWER_DESCRIPTOR structure



## -description
<p>Used in conjunction with the 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> control code 
   to describes the power capabilities of a storage device.</p>


## -syntax

````
typedef struct _DEVICE_POWER_DESCRIPTOR {
  ULONG   Version;
  ULONG   Size;
  BOOLEAN DeviceAttentionSupported;
  BOOLEAN AsynchronousNotificationSupported;
  BOOLEAN IdlePowerManagementEnabled;
  BOOLEAN D3ColdEnabled;
  BOOLEAN D3ColdSupported;
  BOOLEAN NoVerifyDuringIdlePower;
  UCHAR   Reserved[2];
  ULONG   IdleTimeoutInMS;
} DEVICE_POWER_DESCRIPTOR, *PDEVICE_POWER_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Contains the size of this structure, in bytes. The value of this member will change as members are added to 
      the structure.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the total size of the data returned, in bytes. This may include data that follows this 
      structure.</p>
</dd>

### -field <b>DeviceAttentionSupported</b>

<dd>
<p><b>True</b> if device attention is supported. Otherwise, <b>False</b>.</p>
</dd>

### -field <b>AsynchronousNotificationSupported</b>

<dd>
<p><b>True</b> if the device supports asynchronous notifications, delivered via 
      <b>IOCTL_STORAGE_EVENT_NOTIFICATION</b>. Otherwise, <b>False</b></p>
</dd>

### -field <b>IdlePowerManagementEnabled</b>

<dd>
<p><b>True</b> if the device has been registered for runtime idle power management. Otherwise, <b>False</b></p>
</dd>

### -field <b>D3ColdEnabled</b>

<dd>
<p><b>True</b> if the device will be powered off when put into the D3 power state. Otherwise, <b>False</b></p>
</dd>

### -field <b>D3ColdSupported</b>

<dd>
<p><b>True</b> if the platform supports <b>D3ColdEnabled</b> for this device. Otherwise, 
      <b>False</b>.</p>
</dd>

### -field <b>NoVerifyDuringIdlePower</b>

<dd>
<p><b>True</b> if the device requires no verification during idle power transitions. Otherwise, <b>False</b></p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>IdleTimeoutInMS</b>

<dd>
<p>The idle timeout value in milliseconds. This member is ignored unless 
      <b>IdlePowerManagementEnabled</b> is true.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20DEVICE_POWER_DESCRIPTOR structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
