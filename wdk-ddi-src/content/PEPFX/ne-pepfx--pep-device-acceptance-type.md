---
UID: NE.pepfx._PEP_DEVICE_ACCEPTANCE_TYPE
title: PEP_DEVICE_ACCEPTANCE_TYPE
author: windows-driver-content
description: The PEP_DEVICE_ACCEPTANCE_TYPE enumeration indicates whether a PEP accepts ownership of a device.
old-location: kernel\pep_device_acceptance_type.htm
ms.assetid: 72D0BEC2-F5D5-4045-AD63-F263993817B0
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: kernel
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
req.irql: PASSIVE_LEVEL
ms.keywords: VPCI_PNP_ID, VPCI_PNP_ID, *PVPCI_PNP_ID
req.iface: 
---

# PEP_DEVICE_ACCEPTANCE_TYPE enumeration



## -description
<p>The <b>PEP_DEVICE_ACCEPTANCE_TYPE</b> enumeration indicates whether a PEP accepts ownership of a device.</p>


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
<dl>

### -field <a id="PepDeviceNotAccepted"></a><a id="pepdevicenotaccepted"></a><a id="PEPDEVICENOTACCEPTED"></a><b>PepDeviceNotAccepted</b>

<dd>
<p>The PEP does not claim ownership of this device.</p>
</dd>

### -field <a id="PepDeviceAcceptedReserved"></a><a id="pepdeviceacceptedreserved"></a><a id="PEPDEVICEACCEPTEDRESERVED"></a><b>PepDeviceAcceptedReserved</b>

<dd>
<p>The PEP claims ownership of the device on behalf of the default PEP. The default PEP is implemented by the Windows kernel to manage devices for which hardware-specific PEPs are not available.</p>
</dd>

### -field <a id="PepDeviceAccepted"></a><a id="pepdeviceaccepted"></a><a id="PEPDEVICEACCEPTED"></a><b>PepDeviceAccepted</b>

<dd>
<p>The PEP claims ownership of this device.</p>
</dd>

### -field <a id="PepDeviceAcceptedMax"></a><a id="pepdeviceacceptedmax"></a><a id="PEPDEVICEACCEPTEDMAX"></a><b>PepDeviceAcceptedMax</b>

<dd>
<p>Reserved for use by operating system.</p>
</dd>
</dl>

## -remarks
<p>This enumeration is used by <b>DeviceAccepted</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186851">PEP_REGISTER_DEVICE_V2</a> structure to indicate whether a PEP accepts ownership of a device.</p>

<p>This enumeration is used by <b>DeviceAccepted</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186851">PEP_REGISTER_DEVICE_V2</a> structure to indicate whether a PEP accepts ownership of a device.</p>

<p>This enumeration is used by <b>DeviceAccepted</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186851">PEP_REGISTER_DEVICE_V2</a> structure to indicate whether a PEP accepts ownership of a device.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186851">PEP_REGISTER_DEVICE_V2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_DEVICE_ACCEPTANCE_TYPE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
