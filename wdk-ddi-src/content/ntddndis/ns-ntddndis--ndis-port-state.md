---
UID: NS.ntddndis._NDIS_PORT_STATE
title: NDIS_PORT_STATE
author: windows-driver-content
description: The NDIS_PORT_STATE structure specifies the port state information for an NDIS port.
old-location: netvista\ndis_port_state.htm
old-project: netvista
ms.assetid: 57d76d1e-4276-4dbd-b651-2bba6de898b2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_PORT_STATE, NDIS_PORT_STATE, *PNDIS_PORT_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PORT_STATE
req.alt-loc: ntddndis.h
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

# NDIS_PORT_STATE structure



## -description
<p>The NDIS_PORT_STATE structure specifies the port state information for an NDIS port.</p>


## -syntax

````
typedef struct _NDIS_PORT_STATE {
  NDIS_OBJECT_HEADER            Header;
  NDIS_MEDIA_CONNECT_STATE      MediaConnectState;
  ULONG64                       XmitLinkSpeed;
  ULONG64                       RcvLinkSpeed;
  NET_IF_DIRECTION_TYPE         Direction;
  NDIS_PORT_CONTROLL_STATE      SendControlState;
  NDIS_PORT_CONTROLL_STATE      RcvControlState;
  NDIS_PORT_AUTHORIZATION_STATE SendAuthorizationState;
  NDIS_PORT_AUTHORIZATION_STATE RcvAuthorizationState;
  ULONG                         Flags;
} NDIS_PORT_STATE, *PNDIS_PORT_STATE;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_PORT_STATE structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_ DEFAULT, the 
     <b>Revision</b> member to NDIS_PORT_STATE_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_PORT_STATE_REVISION_1.</p>
</dd>

### -field MediaConnectState

<dd>
<p>The media connection state of the port. This state is the same information that the 
     <a href="netvista.oid_gen_media_connect_status_ex">
     OID_GEN_MEDIA_CONNECT_STATUS_EX</a> OID returns.</p>
</dd>

### -field XmitLinkSpeed

<dd>
<p>The transmit link speed of the port, in bits per second. A value of -1 in this member indicates
     that the transmit link speed is unknown.</p>
</dd>

### -field RcvLinkSpeed

<dd>
<p>The receive link speed of the port, in bits per second. A value of -1 in this member indicates
     that the receive link speed is unknown.</p>
</dd>

### -field Direction

<dd>
<p>A 
     <a href="netvista.net_if_direction_type">NET_IF_DIRECTION_TYPE</a> NDIS network
     interface direction type.</p>
</dd>

### -field SendControlState

<dd>
<p>The current control state of the port for send operations. This member must contain one of the
     following values:
     </p>
<p></p>
<dl>

### -field NdisPortControlStateUnknown

<dd>
<p>The port's control state for send operations is unknown.</p>
</dd>

### -field NdisPortControlStateControlled

<dd>
<p>The port is in a controlled state for send operations. That is, the port requires
       authorization.</p>
</dd>

### -field NdisPortControlStateUncontrolled

<dd>
<p>The port is in an uncontrolled state for send operations. That is, the port does not require
       authorization.</p>
</dd>
</dl>
</dd>

### -field RcvControlState

<dd>
<p>The current control state of the port for receive operations. This member must contain one of the
     following values:
     </p>
<p></p>
<dl>

### -field NdisPortControlStateUnknown

<dd>
<p>The port's control state for receive operations is unknown.</p>
</dd>

### -field NdisPortControlStateControlled

<dd>
<p>The port is in a controlled state for receive operations. That is, the port requires
       authorization.</p>
</dd>

### -field NdisPortControlStateUncontrolled

<dd>
<p>The port is in an uncontrolled state for receive operations. That is, the port does not require
       authorization.</p>
</dd>
</dl>
</dd>

### -field SendAuthorizationState

<dd>
<p>The current authorization state of the port for send operations. Ignore this member if the 
     <b>SendControlState</b> member is set to 
     <b>NdisPortControlStateUncontrolled</b>.
     </p>
<p><b>SendAuthorizationState</b> must contain one of the following values:</p>
<p></p>
<dl>

### -field NdisPortAuthorizationUnknown

<dd>
<p>The port's authorization state for send operations is unknown.</p>
</dd>

### -field NdisPortAuthorized

<dd>
<p>The port is authorized for send operations.</p>
</dd>

### -field NdisPortUnauthorized

<dd>
<p>The port is not authorized for send operations.</p>
</dd>

### -field NdisPortReauthorizing

<dd>
<p>The port is re-authorizing for send operations.</p>
</dd>
</dl>
</dd>

### -field RcvAuthorizationState

<dd>
<p>The current authorization state of the port for receive operations. Ignore this member if the 
     <b>RcvControlState</b> member is set to 
     <b>NdisPortControlStateUncontrolled</b>.
     </p>
<p><b>RcvAuthorizationState</b> must contain one of the following values:</p>
<p></p>
<dl>

### -field NdisPortAuthorizationUnknown

<dd>
<p>The port's authorization state for receive operations is unknown.</p>
</dd>

### -field NdisPortAuthorized

<dd>
<p>The port is authorized for receive operations.</p>
</dd>

### -field NdisPortUnauthorized

<dd>
<p>The port is not authorized for receive operations.</p>
</dd>

### -field NdisPortReauthorizing

<dd>
<p>The port is re-authorizing for receive operations.</p>
</dd>
</dl>
</dd>

### -field Flags

<dd>
<p>Reserved for NDIS.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_PORT_STATE structure is used in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff567415">NDIS_STATUS_PORT_STATE</a> status
    indication to indicate a change in the state of a port and is used in response to an 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569624">OID_GEN_PORT_STATE</a> OID query.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
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
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567415">NDIS_STATUS_PORT_STATE</a>
</dt>
<dt>
<a href="netvista.net_if_direction_type">NET_IF_DIRECTION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569605">OID_GEN_MEDIA_CONNECT_STATUS_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569624">OID_GEN_PORT_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PORT_STATE structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
