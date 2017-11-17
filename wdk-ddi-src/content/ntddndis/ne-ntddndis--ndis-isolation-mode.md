---
UID: NE.ntddndis._NDIS_ISOLATION_MODE
title: NDIS_ISOLATION_MODE
author: windows-driver-content
description: The NDIS_ISOLATION_MODE enumeration defines the network isolation modes that can be specified for a VM network adapter.
old-location: netvista\ndis_isolation_mode.htm
ms.assetid: DA4765CD-808C-438A-9CA6-5ADC27A70EC8
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.40 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_ISOLATION_MODE
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
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
req.iface: 
---

# NDIS_ISOLATION_MODE enumeration



## -description
<p>The <b>NDIS_ISOLATION_MODE</b> enumeration defines the network isolation modes that can be specified for a VM network adapter.</p>


## -syntax

````
typedef enum _NDIS_ISOLATION_MODE { 
  NdisIsolationModeNone                   = 0,
  NdisIsolationModeNativeVirtualSubnet    = 1,
  NdisIsolationModeExternalVirtualSubnet  = 2,
  NdisIsolationModeVlan                   = 3
} NDIS_ISOLATION_MODE;
````


## -enum-fields
<dl>

### -field <a id="NdisIsolationModeNone"></a><a id="ndisisolationmodenone"></a><a id="NDISISOLATIONMODENONE"></a><b>NdisIsolationModeNone</b>

<dd>
<p>Network isolation is not supported.</p>
</dd>

### -field <a id="NdisIsolationModeNativeVirtualSubnet"></a><a id="ndisisolationmodenativevirtualsubnet"></a><a id="NDISISOLATIONMODENATIVEVIRTUALSUBNET"></a><b>NdisIsolationModeNativeVirtualSubnet</b>

<dd>
<p>Native <b>VirtualSubnetId</b>-based isolation provided by Hyper-V Network Virtualization.</p>
</dd>

### -field <a id="NdisIsolationModeExternalVirtualSubnet"></a><a id="ndisisolationmodeexternalvirtualsubnet"></a><a id="NDISISOLATIONMODEEXTERNALVIRTUALSUBNET"></a><b>NdisIsolationModeExternalVirtualSubnet</b>

<dd>
<p>External <b>VirtualSubnetId</b>-based isolation provided by a Hyper-V Extensible Switch extension.</p>
</dd>

### -field <a id="NdisIsolationModeVlan"></a><a id="ndisisolationmodevlan"></a><a id="NDISISOLATIONMODEVLAN"></a><b>NdisIsolationModeVlan</b>

<dd>
<p>Virtual local area network (VLAN)-based isolation.</p>
</dd>
</dl>

## -remarks
<p><b>NDIS_ISOLATION_MODE</b> enumeration values are used in the <b>IsolationMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn383687">NDIS_SWITCH_PORT_PROPERTY_ISOLATION</a> structures.</p>

<p><b>NDIS_ISOLATION_MODE</b> enumeration values are used in the <b>IsolationMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn383687">NDIS_SWITCH_PORT_PROPERTY_ISOLATION</a> structures.</p>

<p><b>NDIS_ISOLATION_MODE</b> enumeration values are used in the <b>IsolationMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn383687">NDIS_SWITCH_PORT_PROPERTY_ISOLATION</a> structures.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.40 and later.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383687">NDIS_SWITCH_PORT_PROPERTY_ISOLATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_ISOLATION_MODE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
