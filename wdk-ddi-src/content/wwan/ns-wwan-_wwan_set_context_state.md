---
UID: NS.WWAN._WWAN_SET_CONTEXT_STATE
title: _WWAN_SET_CONTEXT_STATE
author: windows-driver-content
description: The WWAN_SET_CONTEXT_STATE structure represents the command to set the Packet Data Protocol (PDP) context state of the MB device.
old-location: netvista\wwan_set_context_state.htm
old-project: netvista
ms.assetid: f1ed31af-97a7-472e-b834-577470950335
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _WWAN_SET_CONTEXT_STATE, *PWWAN_SET_CONTEXT_STATE, WWAN_SET_CONTEXT_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_SET_CONTEXT_STATE
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
req.product: Windows 10 or later.
---

# _WWAN_SET_CONTEXT_STATE structure



## -description
The WWAN_SET_CONTEXT_STATE structure represents the command to set the Packet Data Protocol (PDP)
  context state of the MB device.


## -syntax

````
typedef struct _WWAN_SET_CONTEXT_STATE {
  ULONG                   ConnectionId;
  WWAN_ACTIVATION_COMMAND ActivationCommand;
  WCHAR                   AccessString[WWAN_ACCESSSTRING_LEN];
  WCHAR                   UserName[WWAN_USERNAME_LEN];
  WCHAR                   Password[WWAN_PASSWORD_LEN];
  WWAN_COMPRESSION        Compression;
  WWAN_AUTH_PROTOCOL      AuthType;
  WWAN_IP_TYPE            IPType;
} WWAN_SET_CONTEXT_STATE, *PWWAN_SET_CONTEXT_STATE;
````


## -struct-fields

### -field ConnectionId

MB Service specifies this member to uniquely identify the PDP Context and its corresponding state.
     
The MB Service uses the value in this member to uniquely identify the current active context across
     MB network adapters.
The miniport driver must use the value in this member when completing 
     <i>set</i> requests. The MB Service uses the value in this member in subsequent 
     <i>query</i> requests as well as disconnect requests to the miniport driver.

### -field ActivationCommand

Activate or deactivate a PDP context that is referenced in the 
     <b>ConnectionId</b> member. The following table shows the possible values a miniport driver can specify.
     
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
WwanActivationCommandActivate
</td>
<td>
Activate PDP context referred to by 
        <b>ConnectionId</b> .
</td>
</tr>
<tr>
<td>
WwanActivationCommandDeactivate
</td>
<td>
Deactivate a currently activated PDP context referred by 
        <b>ConnectionId</b> .
</td>
</tr>
</table>
 

### -field AccessString

A NULL-terminated string to access the network. For GSM-based networks, this would be an Access
     Point Name (APN) string such as "data.thephone-company.com". For CDMA-based networks, this might be a
     special dial code such as "#777" or a Network Access Identifier (NAI) such as
     "foo@thephone-company.com". This member can be <b>NULL</b>.
     
The size of the string should not exceed 100 bytes.

### -field UserName

A NULL-terminated string that represents the username to authenticate. This member can be
     <b>NULL</b>.

### -field Password

A NULL-terminated string that represents the username's password. This member can be <b>NULL</b>.

### -field Compression

A value from the WWAN_COMPRESSION enumeration that specifies whether compression should be used in
     the data connection for header and data. This member applies only to GSM-based devices. The MB Service
     sets this member to 
     <b>WwanCompressionNone</b> for CDMA-based devices.
     
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
WwanCompressionNone
</td>
<td>
No compression is applied.
</td>
</tr>
<tr>
<td>
WwanCompressionEnable
</td>
<td>
Enable header and data compression.
</td>
</tr>
</table>
 

### -field AuthType

A value from the WWAN_AUTH_PROTOCOL enumeration that specifies the authentication type to use for
     the PDP activation. This member applies only to GSM-based devices. The MB Service sets this member to 
     <b>WwanAuthProtocolNone</b> for CDMA-based devices.
     
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
WwanAuthProtocolNone
</td>
<td>
No authentication protocol.
</td>
</tr>
<tr>
<td>
WwanAuthProtocolPap
</td>
<td>
Unencrypted password authentication.
</td>
</tr>
<tr>
<td>
WwanAuthProtocolChap
</td>
<td>
Use the Challenge Handshake Authentication Protocol (CHAP).
</td>
</tr>
<tr>
<td>
WwanAuthProtocolMsChapV2
</td>
<td>
Use the Microsoft Challenge Handshake Authentication Protocol (CHAP) v2.0.
</td>
</tr>
</table>
 

### -field IPType

A value from the WWAN_IP_TYPE enumeration that specifies the type of IP.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows 8 and later versions of Windows.
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="netvista.wwan_activation_command">WWAN_ACTIVATION_COMMAND</a>
</dt>
<dt>
<a href="netvista.wwan_compression">WWAN_COMPRESSION</a>
</dt>
<dt>
<a href="netvista.wwan_auth_protocol">WWAN_AUTH_PROTOCOL</a>
</dt>
<dt>
<a href="netvista.ndis_wwan_set_context_state">NDIS_WWAN_SET_CONTEXT_STATE</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SET_CONTEXT_STATE structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
