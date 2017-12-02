---
UID: NS.windot11._DOT11_INCOMING_ASSOC_STARTED_PARAMETERS
title: DOT11_INCOMING_ASSOC_STARTED_PARAMETERS
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_incoming_assoc_started_parameters.htm
old-project: netvista
ms.assetid: 8bf8d69a-0c47-48c1-83f5-d436a3ab8323
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_INCOMING_ASSOC_STARTED_PARAMETERS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_INCOMING_ASSOC_STARTED_PARAMETERS
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

# DOT11_INCOMING_ASSOC_STARTED_PARAMETERS structure



## -description

## -syntax

````
typedef struct _DOT11_INCOMING_ASSOC_STARTED_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  DOT11_MAC_ADDRESS  PeerMacAddr;
} DOT11_INCOMING_ASSOC_STARTED_PARAMETERS, *PDOT11_INCOMING_ASSOC_STARTED_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The type, revision, and size of the DOT11_INCOMING_ASSOC_STARTED_PARAMETERS structure. This member
     is formatted as an 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values:</p>
<p></p>
<table>
<tr>
<th>Term</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<p><a id="Type"></a><a id="type"></a><a id="TYPE"></a>Type</p>
</td>
<td width="60%">
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="Revision"></a><a id="revision"></a><a id="REVISION"></a>Revision</p>
</td>
<td width="60%">
<p>This member must be set to DOT11_INCOMING_ASSOC_STARTED_PARAMETERS_REVISION_1.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="Size"></a><a id="size"></a><a id="SIZE"></a>Size</p>
</td>
<td width="60%">
<p>This member must be set to 
       <b>sizeof</b>(DOT11_INCOMING_ASSOC_STARTED_PARAMETERS).</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field PeerMacAddr

<dd>
<p>The media access control (MAC) address of the peer station that sent an 802.11 authentication
     request.</p>
</dd>
</dl>

## -remarks
<p>The Native 802.11 miniport driver includes a DOT11_INCOMING_ASSOC_STARTED_PARAMETERS structure when
    the driver makes an 
    <a href="netvista.ndis_status_dot11_incoming_assoc_started">
    NDIS_STATUS_DOT11_INCOMING_ASSOC_STARTED</a> status indication.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating
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
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_incoming_assoc_started">
   NDIS_STATUS_DOT11_INCOMING_ASSOC_STARTED</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_INCOMING_ASSOC_STARTED_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
