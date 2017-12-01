---
UID: NE.ntddndis._NDIS_SWITCH_NIC_STATE
title: NDIS_SWITCH_NIC_STATE
author: windows-driver-content
description: The NDIS_SWITCH_NIC_STATE enumeration specifies the current state of the Hyper-V extensible switch network adapter.
old-location: netvista\ndis_switch_nic_state.htm
old-project: netvista
ms.assetid: 06FFECB3-0883-41CA-9BD3-A6A1D95D5F8C
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_NIC_STATE
req.alt-loc: Ntddndis.h
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
req.iface: 
---

# NDIS_SWITCH_NIC_STATE enumeration



## -description
<p>The <b>NDIS_SWITCH_NIC_STATE</b> enumeration specifies the current state of the Hyper-V extensible switch network adapter. </p>


## -syntax

````
typedef enum _NDIS_SWITCH_NIC_STATE { 
  NdisSwitchNicStateUnknown       = 0,
  NdisSwitchNicStateCreated       = 1,
  NdisSwitchNicStateConnected     = 2,
  NdisSwitchNicStateDisconnected  = 3,
  NdisSwitchNicStateDeleted       = 4
} NDIS_SWITCH_NIC_STATE;
````


## -enum-fields
<dl>

### -field <a id="NdisSwitchNicStateUnknown"></a><a id="ndisswitchnicstateunknown"></a><a id="NDISSWITCHNICSTATEUNKNOWN"></a><b>NdisSwitchNicStateUnknown</b>

<dd>
<p>       This value specifies an undefined NIC state. This value is unused. </p>
</dd>

### -field <a id="NdisSwitchNicStateCreated"></a><a id="ndisswitchnicstatecreated"></a><a id="NDISSWITCHNICSTATECREATED"></a><b>NdisSwitchNicStateCreated</b>

<dd>
<p>This value specifies that the NIC is in the created state. </p>
</dd>

### -field <a id="NdisSwitchNicStateConnected"></a><a id="ndisswitchnicstateconnected"></a><a id="NDISSWITCHNICSTATECONNECTED"></a><b>NdisSwitchNicStateConnected</b>

<dd>
<p>This value specifies that the NIC is connected.</p>
</dd>

### -field <a id="NdisSwitchNicStateDisconnected"></a><a id="ndisswitchnicstatedisconnected"></a><a id="NDISSWITCHNICSTATEDISCONNECTED"></a><b>NdisSwitchNicStateDisconnected</b>

<dd>
<p>This value specifies that the NIC is disconnected.</p>
</dd>

### -field <a id="NdisSwitchNicStateDeleted"></a><a id="ndisswitchnicstatedeleted"></a><a id="NDISSWITCHNICSTATEDELETED"></a><b>NdisSwitchNicStateDeleted</b>

<dd>
<p>This value specifies that the NIC is deleted.</p>
</dd>
</dl>

## -remarks
<p>The <b>NicState</b>  member of the <a href="..\ntddndis\ns-ntddndis--ndis-switch-nic-parameters.md">NDIS_SWITCH_NIC_PARAMETERS</a> structure is an <b>NDIS_SWITCH_NIC_STATE</b> enumeration data type. 
</p>

<p>For more information about extensible switch port states, see <a href="NULL">Overview of Hyper-V Extensible Switch Network Adapters</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-switch-nic-parameters.md">NDIS_SWITCH_NIC_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_NIC_STATE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
