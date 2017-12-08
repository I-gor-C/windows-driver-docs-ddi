---
UID: NS.PEPFX._PEP_ACPI_UNREGISTER_DEVICE
title: _PEP_ACPI_UNREGISTER_DEVICE
author: windows-driver-content
description: The PEP_ACPI_UNREGISTER_DEVICE structure contains information about a device that has been unregistered from ACPI services.
old-location: kernel\pep_acpi_unregister_device.htm
old-project: kernel
ms.assetid: AA9D9AB3-B799-4D21-A418-D29360BBE605
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _PEP_ACPI_UNREGISTER_DEVICE, PEP_ACPI_UNREGISTER_DEVICE, *PPEP_ACPI_UNREGISTER_DEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_ACPI_UNREGISTER_DEVICE
req.alt-loc: pepfx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# _PEP_ACPI_UNREGISTER_DEVICE structure



## -description
The <b>PEP_ACPI_UNREGISTER_DEVICE</b> structure contains information about a device that has been unregistered from ACPI services.


## -syntax

````
typedef struct _PEP_ACPI_UNREGISTER_DEVICE {
  PEPHANDLE DeviceHandle;
  ULONG     InputFlags;
} PEP_ACPI_UNREGISTER_DEVICE, *PPEP_ACPI_UNREGISTER_DEVICE;
````


## -struct-fields

### -field DeviceHandle

[in] A PEPHANDLE value that identifies the device's registration for ACPI services. The platform extension plug-in (PEP) supplied this handle in response to a previous <a href="kernel.pep_notify_acpi_register_device">PEP_NOTIFY_ACPI_REGISTER_DEVICE</a> notification.

### -field InputFlags

[in] A set of input flags. No flags are currently defined for this member, which is always set to PEP_ACPI_UNREGISTER_DEVICE_INPUT_FLAG_NONE (0x0).

## -remarks
This structure is used by the <a href="kernel.pep_notify_acpi_unregister_device">PEP_NOTIFY_ACPI_UNREGISTER_DEVICE</a> notification. The <b>DeviceHandle</b> and <b>InputFlags</b> members contain input values that are supplied by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> when this notification is sent.

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported starting with Windows 10.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_notify_acpi_register_device">PEP_NOTIFY_ACPI_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="kernel.pep_notify_acpi_unregister_device">PEP_NOTIFY_ACPI_UNREGISTER_DEVICE</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_UNREGISTER_DEVICE structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
