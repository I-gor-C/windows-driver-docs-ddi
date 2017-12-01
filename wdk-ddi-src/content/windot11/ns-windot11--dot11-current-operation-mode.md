---
UID: NS.windot11._DOT11_CURRENT_OPERATION_MODE
title: DOT11_CURRENT_OPERATION_MODE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_current_operation_mode.htm
old-project: netvista
ms.assetid: 085ee8f4-7e96-416a-a59f-f35c8ad0dbf4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11_CURRENT_OPERATION_MODE, DOT11_CURRENT_OPERATION_MODE, *PDOT11_CURRENT_OPERATION_MODE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_CURRENT_OPERATION_MODE
req.alt-loc: windot11.h
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
req.product: Windows 10 or later.
---

# DOT11_CURRENT_OPERATION_MODE structure



## -description

## -syntax

````
typedef struct _DOT11_CURRENT_OPERATION_MODE {
  ULONG uReserved;
  ULONG uCurrentOpMode;
} DOT11_CURRENT_OPERATION_MODE, *PDOT11_CURRENT_OPERATION_MODE;
````


## -struct-fields
<dl>

### -field <b>uReserved</b>

<dd>
<p>This member is reserved. The miniport driver must not modify the value of this member.</p>
</dd>

### -field <b>uCurrentOpMode</b>

<dd>
<p>A bitmask of the miniport driver's current operation modes. This bitmask is defined through the
      following:</p>
<p></p>
<dl>

### -field <a id="DOT11_OPERATION_MODE_EXTENSIBLE_AP"></a><a id="dot11_operation_mode_extensible_ap"></a>DOT11_OPERATION_MODE_EXTENSIBLE_AP

<dd>
<p>Specifies that the miniport driver supports the Extensible Access Point (ExtAP) operation
         mode.</p>
<p>This value is available starting with Windows 7.</p>
</dd>

### -field <a id="DOT11_OPERATION_MODE_EXTENSIBLE_STATION"></a><a id="dot11_operation_mode_extensible_station"></a>DOT11_OPERATION_MODE_EXTENSIBLE_STATION

<dd>
<p>Specifies that the miniport driver supports the Extensible Station (ExtSTA) operation
        mode.</p>
</dd>

### -field <a id="DOT11_OPERATION_MODE_NETWORK_MONITOR"></a><a id="dot11_operation_mode_network_monitor"></a>DOT11_OPERATION_MODE_NETWORK_MONITOR

<dd>
<p>Specifies that the miniport driver supports the Network Monitor (NetMon) operation mode.</p>
</dd>

### -field <a id="DOT11_OPERATION_MODE_WFD_DEVICE"></a><a id="dot11_operation_mode_wfd_device"></a>DOT11_OPERATION_MODE_WFD_DEVICE

<dd>
<p>Specifies that the miniport driver supports the Wi-Fi Direct Device operation mode. This mode is available starting in Windows 8.</p>
</dd>

### -field <a id="DOT11_OPERATION_MODE_WFD_GROUP_OWNER"></a><a id="dot11_operation_mode_wfd_group_owner"></a>DOT11_OPERATION_MODE_WFD_GROUP_OWNER

<dd>
<p>Specifies that the miniport driver supports the Wi-Fi Direct Group Owner operation mode.This mode is available starting in Windows 8.</p>
</dd>

### -field <a id="DOT11_OPERATION_MODE_WFD_CLIENT"></a><a id="dot11_operation_mode_wfd_client"></a>DOT11_OPERATION_MODE_WFD_CLIENT

<dd>
<p>Specifies that the miniport driver supports the Wi-Fi Direct Client operation mode. This mode is available starting in Windows 8.</p>
</dd>
</dl>
<p>For more information about operation modes, see 
      <a href="netvista.native_802_11_operation_modes">Native 802.11 Operation
      Modes</a>.</p>
</dd>
</dl>

## -remarks
<p>The miniport driver must specify only one operation mode in the 
    <b>uCurrentOpMode</b> member.</p>

<p>For more information about Native 802.11 operation modes, see 
    <a href="netvista.native_802_11_operation_modes">Native 802.11 Operation
    Modes</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wlclient\ns-wlclient--dot11-adapter.md">DOT11_ADAPTER</a>
</dt>
<dt>
<a href="netvista.oid_dot11_current_operation_mode">
   OID_DOT11_CURRENT_OPERATION_MODE</a>
</dt>
<dt>
<a href="NULL">Native 802.11 Operation Modes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_CURRENT_OPERATION_MODE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
