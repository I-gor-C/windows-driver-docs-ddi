---
UID: NS.windot11._DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS
title: DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS
author: windows-driver-content
description: The request parameters for a provision discovery request are specified in a DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS structure. This structure is sent with an OID_DOT11_WFD_SEND_PROVISION_DISCOVERY_REQUEST request to the miniport.
old-location: netvista\dot11_send_provision_discovery_request_parameters.htm
old-project: netvista
ms.assetid: 1F764A80-71FC-445A-AADE-09660D1C250B
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with   Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS
req.alt-loc: Windot11.h
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

# DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS structure



## -description

## -syntax

````
typedef struct _DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS {
  NDIS_OBJECT_HEADER         Header;
  DOT11_DIALOG_TOKEN         DialogToken;
  DOT11_MAC_ADDRESS          PeerDeviceAddress;
  ULONG                      uSendTimeout;
  DOT11_WFD_GROUP_CAPABILITY GroupCapability;
  DOT11_WFD_GROUP_ID         GroupID;
  BOOLEAN                    bUseGroupID;
  ULONG                      uIEsOffset;
  ULONG                      uIEsLength;
} DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS, *PDOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS</b> structure. The required settings for the members of <b>Header</b> are the following.</p>
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
<td>DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS_REVISION_1</td>
</tr>
<tr>
<td><b>Size</b></td>
<td>DOT11_SIZEOF_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS_REVISION_1</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DialogToken</b>

<dd>
<p>The dialog token to send  in the provision discovery request packet.</p>
</dd>

### -field <b>PeerDeviceAddress</b>

<dd>
<p>The destination address of the WFD device receiving the provision discovery packet.</p>
</dd>

### -field <b>uSendTimeout</b>

<dd>
<p>The maximum time, in milliseconds, allowed to send the provision discovery request. If the time-out expires before the miniport has successfully transmitted the provision discovery response, it should indicate the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439783">NDIS_STATUS_DOT11_WFD_PROVISION_DISCOVERY_REQUEST_SEND_COMPLETE</a> with a failure status.</p>
</dd>

### -field <b>GroupCapability</b>

<dd>
<p>The capability values that are included in the Group Capability bitmask of the Peer-to-Peer (P2P) Capability Information Element (IE) in  a provision discovery request.</p>
</dd>

### -field <b>GroupID</b>

<dd>
<p>The group identifier to include in the provision discovery request.</p>
</dd>

### -field <b>bUseGroupID</b>

<dd>
<p>If TRUE, the value in <b>GroupID</b> should be included in the provision discovery request.</p>
</dd>

### -field <b>uIEsOffset</b>

<dd>
<p>The offset, in bytes,  of the array of additional information elements (IEs) the Wi-Fi Direct (WFD) port must add to the provision discovery request packet. This offset is from the start of the buffer that contains this structure.</p>
</dd>

### -field <b>uIEsLength</b>

<dd>
<p>The length, in bytes, of the array of IEs provided at <b>uIEsOffset</b>.</p>
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
<p>Supported starting with   Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406556">DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439783">NDIS_STATUS_DOT11_WFD_PROVISION_DISCOVERY_REQUEST_SEND_COMPLETE</a>
</dt>
<dt>
<a href="netvista._oid_dot11_wfd_send_provision_discovery_request">OID_DOT11_WFD_SEND_PROVISION_DISCOVERY_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_SEND_PROVISION_DISCOVERY_REQUEST_PARAMETERS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
