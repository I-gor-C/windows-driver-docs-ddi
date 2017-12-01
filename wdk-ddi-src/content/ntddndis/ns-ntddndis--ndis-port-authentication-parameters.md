---
UID: NS.ntddndis._NDIS_PORT_AUTHENTICATION_PARAMETERS
title: NDIS_PORT_AUTHENTICATION_PARAMETERS
author: windows-driver-content
description: The NDIS_PORT_AUTHENTICATION_PARAMETERS structure specifies the state parameters for an NDIS port.
old-location: netvista\ndis_port_authentication_parameters.htm
old-project: netvista
ms.assetid: 7c411d9e-1064-4278-9870-0546891d4743
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PORT_AUTHENTICATION_PARAMETERS, NDIS_PORT_AUTHENTICATION_PARAMETERS, *PNDIS_PORT_AUTHENTICATION_PARAMETERS
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
req.alt-api: NDIS_PORT_AUTHENTICATION_PARAMETERS
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

# NDIS_PORT_AUTHENTICATION_PARAMETERS structure



## -description
<p>The NDIS_PORT_AUTHENTICATION_PARAMETERS structure specifies the state parameters for an NDIS
  port.</p>


## -syntax

````
typedef struct _NDIS_PORT_AUTHENTICATION_PARAMETERS {
  NDIS_OBJECT_HEADER            Header;
  NDIS_PORT_CONTROLL_STATE      SendControlState;
  NDIS_PORT_CONTROLL_STATE      RcvControlState;
  NDIS_PORT_AUTHORIZATION_STATE SendAuthorizationState;
  NDIS_PORT_AUTHORIZATION_STATE RcvAuthorizationState;
} NDIS_PORT_AUTHENTICATION_PARAMETERS, *PNDIS_PORT_AUTHENTICATION_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_PORT_AUTHENTICATION_PARAMETERS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_PORT_AUTHENTICATION_PARAMETERS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_PORT_AUTHENTICATION_PARAMETERS_REVISION_1.</p>
</dd>

### -field <b>SendControlState</b>

<dd>
<p>The control state of the port that the miniport adapter should use for send operations. This
     member must contain one of the following values:
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
<p>The control state of the port that the miniport adapter should use for receive operations. This
     member must contain one of the following values:
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
<p>The authorization state of the port that the miniport adapter should use for send operations.
     Ignore this member if the 
     <b>SendControlState</b> member is set to 
     <b>NdisPortControlStateUncontrolled</b>.
     </p>
<p>This member must contain one of the following values:</p>
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
<p>The authorization state of the port that the miniport adapter should use for receive operations.
     Ignore this member if the 
     <b>RcvControlState</b> member is set to 
     <b>NdisPortControlStateUncontrolled</b>.
     </p>
<p>This member must contain one of the following values:</p>
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
<p>The NDIS_PORT_AUTHENTICATION_PARAMETERS structure is used in 
    <a href="netvista.oid_gen_port_authentication_parameters">
    OID_GEN_PORT_AUTHENTICATION_PARAMETERS</a> OID requests to specify the current authentication state of
    an NDIS port.</p>

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
<a href="netvista.oid_gen_port_authentication_parameters">
   OID_GEN_PORT_AUTHENTICATION_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PORT_AUTHENTICATION_PARAMETERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
