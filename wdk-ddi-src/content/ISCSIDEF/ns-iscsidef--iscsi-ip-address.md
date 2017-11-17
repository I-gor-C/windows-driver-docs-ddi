---
UID: NS.iscsidef._ISCSI_IP_Address
title: ISCSI_IP_Address
author: windows-driver-content
description: The ISCSI_IP_Address structure defines an IP address.
old-location: storage\iscsi_ip_address.htm
ms.assetid: ec4c2add-33e0-4e3d-8f19-892cca4720a7
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsidef.h
req.include-header: Iscsidef.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISCSI_IP_Address
req.alt-loc: iscsidef.h
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
ms.keywords: ISCSI_IP_Address, ISCSI_IP_Address, *PISCSI_IP_Address
req.iface: 
---

# ISCSI_IP_Address structure



## -description
<p>The ISCSI_IP_Address structure defines an IP address.</p>


## -syntax

````
typedef struct _ISCSI_IP_Address {
  ULONG Type;
  ULONG IpV4Address;
  UCHAR IpV6Address[16];
  ULONG IpV6FlowInfo;
  ULONG IpV6ScopeId;
  WCHAR TextAddress[256 + 1];
} ISCSI_IP_Address, *PISCSI_IP_Address;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561482">ISCSIIPADDRESSTYPE</a> value that indicates the type of IP address. </p>
</dd>

### -field <b>IpV4Address</b>

<dd>
<p>If <b>Type</b> = <b>ISCSI_IP_ADDRESS_IPV4</b>, the binary version 4 IP address. Otherwise, <b>IpV4Address</b> is not defined.</p>
</dd>

### -field <b>IpV6Address</b>

<dd>
<p>If <b>Type</b> = <b>ISCSI_IP_ADDRESS_IPV6</b>, the binary version 6 IP address. Otherwise, <b>IpV6Address</b> is not defined.</p>
</dd>

### -field <b>IpV6FlowInfo</b>

<dd>
<p>If <b>Type</b> = <b>ISCSI_IP_ADDRESS_IPV6</b>, the flow information for this IP address, as defined in version 6 of the IP protocol. Otherwise, <b>IpV6FlowInfo</b> is not defined.</p>
</dd>

### -field <b>IpV6ScopeId</b>

<dd>
<p>If <b>Type</b> = <b>ISCSI_IP_ADDRESS_IPV6</b>, the scope ID of this IP address, as defined in version 6 of the IP protocol,. Otherwise, <b>IpV6ScopeId</b> is not defined.</p>
</dd>

### -field <b>TextAddress</b>

<dd>
<p>If <b>Type</b> = <b>ISCSI_IP_ADDRESS_TEXT</b>, the DNS or dotted decimal text address. Otherwise, <b>TextAddress</b> is not defined.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsidef.h (include Iscsidef.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561536">ISCSI_IP_Address</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561482">ISCSIIPADDRESSTYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20ISCSI_IP_Address structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
