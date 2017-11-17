---
UID: NS.ntddndis._NDIS_PORT_STATE
title: NDIS_PORT_STATE
author: windows-driver-content
description: The NDIS_PORT_STATE structure specifies the port state information for an NDIS port.
old-location: netvista\ndis_port_state.htm
ms.assetid: 57d76d1e-4276-4dbd-b651-2bba6de898b2
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: NDIS_PORT_STATE, NDIS_PORT_STATE, *PNDIS_PORT_STATE
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

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_PORT_STATE structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_ DEFAULT, the 
     <b>Revision</b> member to NDIS_PORT_STATE_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_PORT_STATE_REVISION_1.</p>
</dd>

### -field <b>MediaConnectState</b>

<dd>
<p>The media connection state of the port. This state is the same information that the 
     <a href="netvista.oid_gen_media_connect_status_ex">
     OID_GEN_MEDIA_CONNECT_STATUS_EX</a> OID returns.</p>
</dd>

### -field <b>XmitLinkSpeed</b>

<dd>
<p>The transmit link speed of the port, in bits per second. A value of -1 in this member indicates
     that the transmit link speed is unknown.</p>
</dd>

### -field <b>RcvLinkSpeed</b>

<dd>
<p>The receive link speed of the port, in bits per second. A value of -1 in this member indicates
     that the receive link speed is unknown.</p>
</dd>

### -field <b>Direction</b>

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568742">NET_IF_DIRECTION_TYPE</a> NDIS network
     interface direction type.</p>
</dd>

### -field <b>SendControlState</b>

<dd>
<p>The current control state of the port for send operations. This member must contain one of the
     following values:
     </p>
<p></p>
<dl>

### -field <a id="NdisPortControlStateUnknown"></a><a id="ndisportcontrolstateunknown"></a><a id="NDISPORTCONTROLSTATEUNKNOWN"></a><b>NdisPortControlStateUnknown</b>

<dd>
<p>The port's control state for send operations is unknown.</p>
</dd>

### -field <a id="NdisPortControlStateControlled"></a><a id="ndisportcontrolstatecontrolled"></a><a id="NDISPORTCONTROLSTATECONTROLLED"></a><b>NdisPortControlStateControlled</b>

<dd>
<p>The port is in a controlled state for send operations. That is, the port requires
       authorization.</p>
</dd>

### -field <a id="NdisPortControlStateUncontrolled"></a><a id="ndisportcontrolstateuncontrolled"></a><a id="NDISPORTCONTROLSTATEUNCONTROLLED"></a><b>NdisPortControlStateUncontrolled</b>

<dd>
<p>The port is in an uncontrolled state for send operations. That is, the port does not require
       authorization.</p>
</dd>
</dl>
</dd>

### -field <b>RcvControlState</b>

<dd>
<p>The current control state of the port for receive operations. This member must contain one of the
     following values:
     </p>
<p></p>
<dl>

### -field <a id="NdisPortControlStateUnknown"></a><a id="ndisportcontrolstateunknown"></a><a id="NDISPORTCONTROLSTATEUNKNOWN"></a><b>NdisPortControlStateUnknown</b>

<dd>
<p>The port's control state for receive operations is unknown.</p>
</dd>

### -field <a id="NdisPortControlStateControlled"></a><a id="ndisportcontrolstatecontrolled"></a><a id="NDISPORTCONTROLSTATECONTROLLED"></a><b>NdisPortControlStateControlled</b>

<dd>
<p>The port is in a controlled state for receive operations. That is, the port requires
       authorization.</p>
</dd>

### -field <a id="NdisPortControlStateUncontrolled"></a><a id="ndisportcontrolstateuncontrolled"></a><a id="NDISPORTCONTROLSTATEUNCONTROLLED"></a><b>NdisPortControlStateUncontrolled</b>

<dd>
<p>The port is in an uncontrolled state for receive operations. That is, the port does not require
       authorization.</p>
</dd>
</dl>
</dd>

### -field <b>SendAuthorizationState</b>

<dd>
<p>The current authorization state of the port for send operations. Ignore this member if the 
     <b>SendControlState</b> member is set to 
     <b>NdisPortControlStateUncontrolled</b>.
     </p>
<p><b>SendAuthorizationState</b> must contain one of the following values:</p>
<p></p>
<dl>

### -field <a id="NdisPortAuthorizationUnknown"></a><a id="ndisportauthorizationunknown"></a><a id="NDISPORTAUTHORIZATIONUNKNOWN"></a><b>NdisPortAuthorizationUnknown</b>

<dd>
<p>The port's authorization state for send operations is unknown.</p>
</dd>

### -field <a id="NdisPortAuthorized"></a><a id="ndisportauthorized"></a><a id="NDISPORTAUTHORIZED"></a><b>NdisPortAuthorized</b>

<dd>
<p>The port is authorized for send operations.</p>
</dd>

### -field <a id="NdisPortUnauthorized"></a><a id="ndisportunauthorized"></a><a id="NDISPORTUNAUTHORIZED"></a><b>NdisPortUnauthorized</b>

<dd>
<p>The port is not authorized for send operations.</p>
</dd>

### -field <a id="NdisPortReauthorizing"></a><a id="ndisportreauthorizing"></a><a id="NDISPORTREAUTHORIZING"></a><b>NdisPortReauthorizing</b>

<dd>
<p>The port is re-authorizing for send operations.</p>
</dd>
</dl>
</dd>

### -field <b>RcvAuthorizationState</b>

<dd>
<p>The current authorization state of the port for receive operations. Ignore this member if the 
     <b>RcvControlState</b> member is set to 
     <b>NdisPortControlStateUncontrolled</b>.
     </p>
<p><b>RcvAuthorizationState</b> must contain one of the following values:</p>
<p></p>
<dl>

### -field <a id="NdisPortAuthorizationUnknown"></a><a id="ndisportauthorizationunknown"></a><a id="NDISPORTAUTHORIZATIONUNKNOWN"></a><b>NdisPortAuthorizationUnknown</b>

<dd>
<p>The port's authorization state for receive operations is unknown.</p>
</dd>

### -field <a id="NdisPortAuthorized"></a><a id="ndisportauthorized"></a><a id="NDISPORTAUTHORIZED"></a><b>NdisPortAuthorized</b>

<dd>
<p>The port is authorized for receive operations.</p>
</dd>

### -field <a id="NdisPortUnauthorized"></a><a id="ndisportunauthorized"></a><a id="NDISPORTUNAUTHORIZED"></a><b>NdisPortUnauthorized</b>

<dd>
<p>The port is not authorized for receive operations.</p>
</dd>

### -field <a id="NdisPortReauthorizing"></a><a id="ndisportreauthorizing"></a><a id="NDISPORTREAUTHORIZING"></a><b>NdisPortReauthorizing</b>

<dd>
<p>The port is re-authorizing for receive operations.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567415">NDIS_STATUS_PORT_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568742">NET_IF_DIRECTION_TYPE</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PORT_STATE structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
