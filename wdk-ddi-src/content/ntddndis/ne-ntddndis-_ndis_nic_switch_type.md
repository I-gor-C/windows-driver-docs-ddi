---
UID: NE.ntddndis._NDIS_NIC_SWITCH_TYPE
title: _NDIS_NIC_SWITCH_TYPE
author: windows-driver-content
description: The NDIS_NIC_SWITCH_TYPE enumeration specifies the type of the NIC switch on a network adapter.
old-location: netvista\ndis_nic_switch_type.htm
old-project: NetVista
ms.assetid: F990F166-D9DA-43F5-95D3-86B9B11FACF1
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _NDIS_NIC_SWITCH_TYPE, NDIS_NIC_SWITCH_TYPE, PNDIS_NIC_SWITCH_TYPE, *PNDIS_NIC_SWITCH_TYPE
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
req.alt-api: NDIS_NIC_SWITCH_TYPE
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
---

# _NDIS_NIC_SWITCH_TYPE enumeration



## -description
The <b>NDIS_NIC_SWITCH_TYPE</b> enumeration specifies the type of the NIC switch on a network adapter.





## -syntax

````
typedef enum _NDIS_NIC_SWITCH_TYPE { 
  NdisNicSwitchTypeUnspecified  = 0,
  NdisNicSwitchTypeExternal     = 1,
  NdisNicSwitchTypeMax          = 2
} NDIS_NIC_SWITCH_TYPE, *PNDIS_NIC_SWITCH_TYPE;
````


## -enum-fields

### -field NdisNicSwitchTypeUnspecified

The NIC switch type is not specified.


### -field NdisNicSwitchTypeExternal

This value specifies an external switch. The single root I/O virtualization (SR-IOV) virtual ports (VPorts) connected to this type of switch, including the default VPort, can access the external network through the physical port on the network adapter.


### -field NdisNicSwitchTypeMax

The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.




## -remarks
The <b>SwitchType</b> member of the <a href="netvista.ndis_nic_switch_parameters">NDIS_NIC_SWITCH_PARAMETERS</a> and <a href="netvista.ndis_nic_switch_info">NDIS_NIC_SWITCH_INFO</a> structures is an <b>NDIS_NIC_SWITCH_TYPE</b> enumeration data type. 



For more information about the NIC switch, see <a href="netvista.sr-iov_architecture">SR-IOV Architecture</a>.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.30 and later.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<dt><b></b></dt>
<dt>
<a href="netvista.ndis_nic_switch_info">NDIS_NIC_SWITCH_INFO</a>
</dt>
<dt>
<a href="netvista.ndis_nic_switch_parameters">NDIS_NIC_SWITCH_PARAMETERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NDIS_NIC_SWITCH_TYPE enumeration%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

