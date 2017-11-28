---
UID: NS.hidport._HID_MINIDRIVER_REGISTRATION
title: HID_MINIDRIVER_REGISTRATION
author: windows-driver-content
description: The HID_MINIDRIVER_REGISTRATION structure contains registration information that a HID minidriver passes to the HID Client Drivers when the minidriver registers with the class driver.
old-location: hid\hid_minidriver_registration.htm
old-project: hid
ms.assetid: 75c0f546-1a58-45e8-a3eb-3075f07c426b
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HID_MINIDRIVER_REGISTRATION, HID_MINIDRIVER_REGISTRATION, *PHID_MINIDRIVER_REGISTRATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidport.h
req.include-header: Hidport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HID_MINIDRIVER_REGISTRATION
req.alt-loc: hidport.h
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
req.iface: 
---

# HID_MINIDRIVER_REGISTRATION structure



## -description
<p>The HID_MINIDRIVER_REGISTRATION structure contains registration information that a HID minidriver passes to the <a href="NULL">HID Client Drivers</a> when the minidriver registers with the class driver.</p>


## -syntax

````
typedef struct _HID_MINIDRIVER_REGISTRATION {
  ULONG           Revision;
  PDRIVER_OBJECT  DriverObject;
  PUNICODE_STRING RegistryPath;
  ULONG           DeviceExtensionSize;
  BOOLEAN         DevicesArePolled;
  UCHAR           Reserved[3];
} HID_MINIDRIVER_REGISTRATION, *PHID_MINIDRIVER_REGISTRATION;
````


## -struct-fields
<dl>

### -field <b>Revision</b>

<dd>
<p>Specifies the HID version that this minidriver supports.</p>
</dd>

### -field <b>DriverObject</b>

<dd>
<p>Pointer to the minidriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>.</p>
</dd>

### -field <b>RegistryPath</b>

<dd>
<p>Pointer to the minidriver's registry path.</p>
</dd>

### -field <b>DeviceExtensionSize</b>

<dd>
<p>Specifies the length, in bytes, that the minidriver requests for a device extension.</p>
</dd>

### -field <b>DevicesArePolled</b>

<dd>
<p>Specifies that the devices on the bus that this minidriver supports must be polled in order to obtain data from the device.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for internal system use.</p>
</dd>
</dl>

## -remarks
<p>When a HID minidriver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff539835">HidRegisterMinidriver</a>, it uses this structure to pass information to the HID class driver. The minidriver must must zero-initialize this structure before setting members. A minidriver sets the members <b>DriverObject</b> and <b>RegistryPath</b> to the driver object and registry path parameters that are passed to the minidriver as system-supplied parameters to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. <b>Revision</b> should be set to HID_REVISION.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidport.h (include Hidport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539835">HidRegisterMinidriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HID_MINIDRIVER_REGISTRATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
