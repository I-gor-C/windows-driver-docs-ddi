---
UID: NS.ndiswwan._NDIS_WWAN_NETWORK_IDLE_HINT
title: NDIS_WWAN_NETWORK_IDLE_HINT
author: windows-driver-content
description: The NDIS_WWAN_NETWORK_IDLE_HINT structure contains a hint for the network interface regarding whether data is expected to be active or idle on the interface.
old-location: netvista\ndis_wwan_network_idle_hint.htm
old-project: netvista
ms.assetid: 81CA12B7-A7AD-494A-B79A-3EF4A50CB848
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_WWAN_NETWORK_IDLE_HINT, NDIS_WWAN_NETWORK_IDLE_HINT, *PNDIS_WWAN_NETWORK_IDLE_HINT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_NETWORK_IDLE_HINT
req.alt-loc: ndiswwan.h
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

# NDIS_WWAN_NETWORK_IDLE_HINT structure



## -description
<p>The NDIS_WWAN_NETWORK_IDLE_HINT structure contains a hint for the network interface regarding whether data is expected to be active or idle on the interface.</p>


## -syntax

````
typedef struct _NDIS_WWAN_NETWORK_IDLE_HINT {
  NDIS_OBJECT_HEADER     Header;
  WWAN_NETWORK_IDLE_HINT IdleHint;
} NDIS_WWAN_NETWORK_IDLE_HINT, *PNDIS_WWAN_NETWORK_IDLE_HINT;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The type, revision, and size of the NDIS_WWAN_NETWORK_IDLE_HINT structure. This member is
     formatted as an 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values:</p>
<p></p>
<table>
<tr>
<th>Member</th>
<th>Setting</th>
</tr>
<tr>
<td><b>Type</b></td>
<td>NDIS_OBJECT_TYPE_DEFAULT</td>
</tr>
<tr>
<td><b>Revision</b></td>
<td>NDIS_WWAN_NETWORK_IDLE_HINT_REVISION_1</td>
</tr>
<tr>
<td><b>Size</b></td>
<td>SIZEOF_NDIS_WWAN_NETWORK_IDLE_HINT_1</td>
</tr>
</table>
<p> </p>
</dd>

### -field IdleHint

<dd>
<p>A formatted <a href="..\wwan\ns-wwan--wwan-network-idle-hint.md">WWAN_NETWORK_IDLE_HINT</a> object that contains the network idle hint.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 10 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn931089">OID_WWAN_NETWORK_IDLE_HINT</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-network-idle-hint.md">WWAN_NETWORK_IDLE_HINT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_NETWORK_IDLE_HINT structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
