---
UID: NE.pepfx._PEP_DEVICE_ACCEPTANCE_TYPE
title: _PEP_DEVICE_ACCEPTANCE_TYPE
author: windows-driver-content
description: The PEP_DEVICE_ACCEPTANCE_TYPE enumeration indicates whether a PEP accepts ownership of a device.
old-location: kernel\pep_device_acceptance_type.htm
old-project: kernel
ms.assetid: 72D0BEC2-F5D5-4045-AD63-F263993817B0
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _PEP_DEVICE_ACCEPTANCE_TYPE, PEP_DEVICE_ACCEPTANCE_TYPE, *PPEP_DEVICE_ACCEPTANCE_TYPE, PPEP_DEVICE_ACCEPTANCE_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_DEVICE_ACCEPTANCE_TYPE
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
req.irql: See Remarks.
---

# _PEP_DEVICE_ACCEPTANCE_TYPE enumeration



## -description
The <b>PEP_DEVICE_ACCEPTANCE_TYPE</b> enumeration indicates whether a PEP accepts ownership of a device.



## -syntax

````
typedef enum _PEP_DEVICE_ACCEPTANCE_TYPE { 
  PepDeviceNotAccepted       = 0,
  PepDeviceAcceptedReserved,
  PepDeviceAccepted,
  PepDeviceAcceptedMax
} PEP_DEVICE_ACCEPTANCE_TYPE;
````


## -enum-fields

### -field PepDeviceNotAccepted

The PEP does not claim ownership of this device.


### -field PepDeviceAcceptedReserved

The PEP claims ownership of the device on behalf of the default PEP. The default PEP is implemented by the Windows kernel to manage devices for which hardware-specific PEPs are not available.


### -field PepDeviceAccepted

The PEP claims ownership of this device.


### -field PepDeviceAcceptedMax

Reserved for use by operating system.


## -remarks
This enumeration is used by <b>DeviceAccepted</b> member of the <a href="kernel.pep_register_device_v2">PEP_REGISTER_DEVICE_V2</a> structure to indicate whether a PEP accepts ownership of a device.


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
<a href="kernel.pep_register_device_v2">PEP_REGISTER_DEVICE_V2</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_DEVICE_ACCEPTANCE_TYPE enumeration%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

