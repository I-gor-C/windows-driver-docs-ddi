---
UID: NE.wdm._POWER_STATE_TYPE
title: POWER_STATE_TYPE
author: windows-driver-content
description: The POWER_STATE_TYPE enumeration type indicates that a power state value is a system power state or a device power state.
old-location: kernel\power_state_type.htm
old-project: kernel
ms.assetid: d0e97474-4119-4359-a9f9-644c82df7fab
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POWER_STATE_TYPE
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# POWER_STATE_TYPE enumeration



## -description
<p>The <b>POWER_STATE_TYPE</b> enumeration type indicates that a power state value is a system power state or a device power state.</p>


## -syntax

````
typedef enum _POWER_STATE_TYPE { 
  SystemPowerState  = 0,
  DevicePowerState  = 1
} POWER_STATE_TYPE, *PPOWER_STATE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="SystemPowerState"></a><a id="systempowerstate"></a><a id="SYSTEMPOWERSTATE"></a><b>SystemPowerState</b>

<dd>
<p>Indicates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564565">SYSTEM_POWER_STATE</a> value.</p>
</dd>

### -field <a id="DevicePowerState"></a><a id="devicepowerstate"></a><a id="DEVICEPOWERSTATE"></a><b>DevicePowerState</b>

<dd>
<p>Indicates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a> value.</p>
</dd>
</dl>

## -remarks
<p>The <b>POWER_STATE_TYPE</b> enumeration type is used in conjunction with a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff559842">POWER_STATE</a> to indicate that the power state value is a system power state value or a device power state value. For an example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559765">PoSetPowerState</a>.</p>

<p>The <b>POWER_STATE_TYPE</b> enumeration type is used in conjunction with a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff559842">POWER_STATE</a> to indicate that the power state value is a system power state value or a device power state value. For an example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559765">PoSetPowerState</a>.</p>

<p>The <b>POWER_STATE_TYPE</b> enumeration type is used in conjunction with a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff559842">POWER_STATE</a> to indicate that the power state value is a system power state value or a device power state value. For an example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559765">PoSetPowerState</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559842">POWER_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559765">PoSetPowerState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564565">SYSTEM_POWER_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20POWER_STATE_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
