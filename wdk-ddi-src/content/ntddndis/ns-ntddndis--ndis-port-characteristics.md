---
UID: NS.ntddndis._NDIS_PORT_CHARACTERISTICS
title: NDIS_PORT_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_PORT_CHARACTERISTICS structure specifies the characteristics of an NDIS port. For more information about NDIS ports, see NDIS Ports.
old-location: netvista\ndis_port_characteristics.htm
old-project: netvista
ms.assetid: fd602dd6-c216-413a-a4da-292739774937
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PORT_CHARACTERISTICS, NDIS_PORT_CHARACTERISTICS, *PNDIS_PORT_CHARACTERISTICS
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
req.alt-api: NDIS_PORT_CHARACTERISTICS
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

# NDIS_PORT_CHARACTERISTICS structure



## -description
<p>The <b>NDIS_PORT_CHARACTERISTICS</b> structure specifies the characteristics of an NDIS port. For more information about NDIS ports, see <a href="NULL">NDIS Ports</a>.</p>


## -syntax

````
typedef struct _NDIS_PORT_CHARACTERISTICS {
  NDIS_OBJECT_HEADER            Header;
  NDIS_PORT_NUMBER              PortNumber;
  ULONG                         Flags;
  NDIS_PORT_TYPE                Type;
  NDIS_MEDIA_CONNECT_STATE      MediaConnectState;
  ULONG64                       XmitLinkSpeed;
  ULONG64                       RcvLinkSpeed;
  NET_IF_DIRECTION_TYPE         Direction;
  NDIS_PORT_CONTROLL_STATE      SendControlState;
  NDIS_PORT_CONTROLL_STATE      RcvControlState;
  NDIS_PORT_AUTHORIZATION_STATE SendAuthorizationState;
  NDIS_PORT_AUTHORIZATION_STATE RcvAuthorizationState;
} NDIS_PORT_CHARACTERISTICS, *PNDIS_PORT_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_PORT_CHARACTERISTICS</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_PORT_CHARACTERISTICS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_PORT_CHARACTERISTICS_REVISION_1.</p>
</dd>

### -field <b>PortNumber</b>

<dd>
<p>The number of the NDIS port that is associated with this <b>NDIS_PORT_CHARACTERISTICS</b> structure. The 
     <b>PortNumber</b> value is an NDIS_PORT_NUMBER value, which has a ULONG data type and is valid from zero
     through 0xffffff, where zero is reserved for the default port.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR combination of the port characteristics flags, or zero if no flags are set. There is
     currently one flag.
     </p>
<p>If the NDIS_PORT_CHAR_USE_DEFAULT_AUTH_SETTINGS flag is set, NDIS ignores authentication state
     settings and uses the default authentication state instead. A miniport driver can use this flag to
     request that NDIS use the default authentication state settings for the ports that it allocates and
     activates. If the miniport driver controls the default port, when the miniport driver activates the
     default port, the driver can set NDIS_PORT_CHAR_USE_DEFAULT_AUTH_SETTINGS to activate the default port
     with the default authentication state settings.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>The type of NDIS port. For more information, see <a href="NULL">Types of NDIS Ports</a>. This type can be one of the following values:
     </p>
<p></p>
<dl>

### -field <a id="NdisPortTypeUndefined"></a><a id="ndisporttypeundefined"></a><a id="NDISPORTTYPEUNDEFINED"></a><b>NdisPortTypeUndefined</b>

<dd>
<p>The default port type.</p>
</dd>

### -field <a id="NdisPortTypeBridge"></a><a id="ndisporttypebridge"></a><a id="NDISPORTTYPEBRIDGE"></a><b>NdisPortTypeBridge</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="NdisPortTypeRasConnection"></a><a id="ndisporttyperasconnection"></a><a id="NDISPORTTYPERASCONNECTION"></a><b>NdisPortTypeRasConnection</b>

<dd>
<p>A Remote Access Service (RAS) connection.</p>
</dd>

### -field <a id="NdisPortType8021xSupplicant"></a><a id="ndisporttype8021xsupplicant"></a><a id="NDISPORTTYPE8021XSUPPLICANT"></a><b>NdisPortType8021xSupplicant</b>

<dd>
<p>A remote wireless station that is associated with an access point on this host computer.</p>
</dd>

### -field <a id="NdisPortTypeNdisImPlatform"></a><a id="ndisporttypendisimplatform"></a><a id="NDISPORTTYPENDISIMPLATFORM"></a><b>NdisPortTypeNdisImPlatform</b>

<dd>
<p>Reserved for system use.</p>
<div class="alert"><b>Note</b>  This value is supported only in NDIS 6.30 and later.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>MediaConnectState</b>

<dd>
<p>The media connection state of the port. This state is the same information that the 
     <a href="netvista.oid_gen_media_connect_status_ex">
     OID_GEN_MEDIA_CONNECT_STATUS_EX</a> OID returns.</p>
</dd>

### -field <b>XmitLinkSpeed</b>

<dd>
<p>The transmit link speed of the port in bits per second. A value of -1 in this member indicates
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
     <a href="netvista.net_if_direction_type">NET_IF_DIRECTION_TYPE</a> NDIS network
     interface direction type.</p>
</dd>

### -field <b>SendControlState</b>

<dd>
<p>The control state of the port for send operations. This member must contain one of the following
     values:
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
<p>The control state of the port for receive operations. This member must contain one of the
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
<p>The port is in a controlled state for receive operations (that is, the port requires
       authorization), and the value in the 
       <b>SendAuthorizationState</b> member determines the authentication state.</p>
</dd>

### -field <a id="NdisPortControlStateUncontrolled"></a><a id="ndisportcontrolstateuncontrolled"></a><a id="NDISPORTCONTROLSTATEUNCONTROLLED"></a><b>NdisPortControlStateUncontrolled</b>

<dd>
<p>The port is in an uncontrolled state for receive operations. Therefore, authentication does not
       apply to this port.</p>
</dd>
</dl>
</dd>

### -field <b>SendAuthorizationState</b>

<dd>
<p>The authorization state of the port for send operations. Ignore this member if the 
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
<p>The authorization state of the port for receive operations. Ignore this member if the 
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
</dl>

## -remarks
<p>The <b>NDIS_PORT_CHARACTERISTICS</b> structure specifies the characteristics of an NDIS port. This structure
    appears in a list of port characteristics that are provided in the 
    <a href="..\ntddndis\ns-ntddndis--ndis-port-array.md">NDIS_PORT_ARRAY</a> structure that is used with
    the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569583">OID_GEN_ENUMERATE_PORTS</a> OID.</p>

<p>To allocate an NDIS port, a driver initializes an <b>NDIS_PORT_CHARACTERISTICS</b> structure and passes it to
    the 
    <a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a> function. When 
    <b>NdisMAllocatePort</b> successfully returns, NDIS sets the 
    <b>PortNumber</b> member of <b>NDIS_PORT_CHARACTERISTICS</b> to the port number that NDIS assigned to the
    port.</p>

<p>NDIS uses a linked list of ports in port activation Plug and Play (PnP) events. NDIS uses the 
    <a href="..\ntddndis\ns-ntddndis--ndis-port.md">NDIS_PORT</a> structure to create a linked list of
    ports, and each <b>NDIS_PORT</b> structure contains an <b>NDIS_PORT_CHARACTERISTICS</b> structure.</p>

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
<a href="..\ntddndis\ns-ntddndis--ndis-port.md">NDIS_PORT</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-port-array.md">NDIS_PORT_ARRAY</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a>
</dt>
<dt>
<a href="netvista.net_if_direction_type">NET_IF_DIRECTION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569583">OID_GEN_ENUMERATE_PORTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569605">OID_GEN_MEDIA_CONNECT_STATUS_EX</a>
</dt>
<dt>
<a href="NULL">NDIS Ports</a>
</dt>
<dt>
<a href="NULL">Types of NDIS Ports</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PORT_CHARACTERISTICS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
