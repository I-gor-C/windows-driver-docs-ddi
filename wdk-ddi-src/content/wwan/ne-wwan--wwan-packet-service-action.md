---
UID: NE.wwan._WWAN_PACKET_SERVICE_ACTION
title: WWAN_PACKET_SERVICE_ACTION
author: windows-driver-content
description: The WWAN_PACKET_SERVICE_ACTION enumeration lists different packet service actions.
old-location: netvista\wwan_packet_service_action.htm
old-project: netvista
ms.assetid: 976e0d67-a03c-4545-b165-4b48062c03b7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_PACKET_SERVICE_ACTION
req.alt-loc: wwan.h
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

# WWAN_PACKET_SERVICE_ACTION enumeration



## -description
<p>The WWAN_PACKET_SERVICE_ACTION enumeration lists different packet service actions.</p>


## -syntax

````
typedef enum _WWAN_PACKET_SERVICE_ACTION { 
  WwanPacketServiceActionAttach  = 0,
  WwanPacketServiceActionDetach
} WWAN_PACKET_SERVICE_ACTION, *PWWAN_PACKET_SERVICE_ACTION;
````


## -enum-fields
<dl>

### -field <a id="WwanPacketServiceActionAttach"></a><a id="wwanpacketserviceactionattach"></a><a id="WWANPACKETSERVICEACTIONATTACH"></a><b>WwanPacketServiceActionAttach</b>

<dd>
<p>Packet-attach to the registered provider.</p>
</dd>

### -field <a id="WwanPacketServiceActionDetach"></a><a id="wwanpacketserviceactiondetach"></a><a id="WWANPACKETSERVICEACTIONDETACH"></a><b>WwanPacketServiceActionDetach</b>

<dd>
<p>Packet-detach from the registered provider.</p>
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
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-set-packet-service.md">NDIS_WWAN_SET_PACKET_SERVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PACKET_SERVICE_ACTION enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
