---
UID: NS.PEPFX._PEP_ABANDON_DEVICE
title: _PEP_ABANDON_DEVICE
author: windows-driver-content
description: The PEP_ABANDON_DEVICE structure identifies a device that has been abandoned and will no longer be used by the operating system.
old-location: kernel\pep_abandon_device.htm
old-project: kernel
ms.assetid: 15F54054-F20B-43A6-8BCD-3A1C47433B12
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _PEP_ABANDON_DEVICE, PEP_ABANDON_DEVICE, *PPEP_ABANDON_DEVICE
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
req.alt-api: PEP_ABANDON_DEVICE
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

# _PEP_ABANDON_DEVICE structure



## -description
The <b>PEP_ABANDON_DEVICE</b> structure identifies a device that has been abandoned and will no longer be used by the operating system.


## -syntax

````
typedef struct _PEP_ABANDON_DEVICE {
  PCUNICODE_STRING DeviceId;
  BOOLEAN          DeviceAccepted;
} PEP_ABANDON_DEVICE, *PPEP_ABANDON_DEVICE;
````


## -struct-fields

### -field DeviceId

[in] A string that uniquely identifies the device. This member is a pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains a <a href="devinst.device_identification_strings">device identification string</a>.

### -field DeviceAccepted

[out] Whether the PEP claims ownership of the device. The PEP sets this member to TRUE to claim ownership of the device, or to FALSE to indicate that it does not own the device.

## -remarks
This structure is used by the <a href="kernel.pep_dpm_abandon_device">PEP_DPM_ABANDON_DEVICE</a> notification. The <b>DeviceId</b> member of the structure contains an input value that is supplied by the Windows <a href="https://msdn.microsoft.com/9F2D8ACD-44D5-46E0-9FC7-1B38B99450FF">power management framework</a> (PoFx). The <b>DeviceAccepted</b> member contains an output value that the PEP writes to the structure in response to this notification.

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
<a href="kernel.pep_dpm_abandon_device">PEP_DPM_ABANDON_DEVICE</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ABANDON_DEVICE structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>