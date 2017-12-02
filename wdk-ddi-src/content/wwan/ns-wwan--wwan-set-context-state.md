---
UID: NS.wwan._WWAN_SET_CONTEXT_STATE
title: WWAN_SET_CONTEXT_STATE
author: windows-driver-content
description: The WWAN_SET_CONTEXT_STATE structure represents the command to set the Packet Data Protocol (PDP) context state of the MB device.
old-location: netvista\wwan_set_context_state.htm
old-project: netvista
ms.assetid: f1ed31af-97a7-472e-b834-577470950335
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WWAN_SET_CONTEXT_STATE, WWAN_SET_CONTEXT_STATE, *PWWAN_SET_CONTEXT_STATE
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
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_SET_CONTEXT_STATE structure



## -description
<p>The WWAN_SET_CONTEXT_STATE structure represents the command to set the Packet Data Protocol (PDP)
  context state of the MB device.</p>


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
<dl>

### -field ConnectionId

<dd>
<p>MB Service specifies this member to uniquely identify the PDP Context and its corresponding state.
     </p>
<p>The MB Service uses the value in this member to uniquely identify the current active context across
     MB network adapters.</p>
<p>The miniport driver must use the value in this member when completing 
     <i>set</i> requests. The MB Service uses the value in this member in subsequent 
     <i>query</i> requests as well as disconnect requests to the miniport driver.</p>
</dd>

### -field ActivationCommand

<dd>
<p>Activate or deactivate a PDP context that is referenced in the 
     <b>ConnectionId</b> member. The following table shows the possible values a miniport driver can specify.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WwanActivationCommandActivate</p>
</td>
<td>
<p>Activate PDP context referred to by 
        <b>ConnectionId</b> .</p>
</td>
</tr>
<tr>
<td>
<p>WwanActivationCommandDeactivate</p>
</td>
<td>
<p>Deactivate a currently activated PDP context referred by 
        <b>ConnectionId</b> .</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field AccessString

<dd>
<p>A NULL-terminated string to access the network. For GSM-based networks, this would be an Access
     Point Name (APN) string such as "data.thephone-company.com". For CDMA-based networks, this might be a
     special dial code such as "#777" or a Network Access Identifier (NAI) such as
     "foo@thephone-company.com". This member can be <b>NULL</b>.
     </p>
<p>The size of the string should not exceed 100 bytes.</p>
</dd>

### -field UserName

<dd>
<p>A NULL-terminated string that represents the username to authenticate. This member can be
     <b>NULL</b>.</p>
</dd>

### -field Password

<dd>
<p>A NULL-terminated string that represents the username's password. This member can be <b>NULL</b>.</p>
</dd>

### -field Compression

<dd>
<p>A value from the WWAN_COMPRESSION enumeration that specifies whether compression should be used in
     the data connection for header and data. This member applies only to GSM-based devices. The MB Service
     sets this member to 
     <b>WwanCompressionNone</b> for CDMA-based devices.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WwanCompressionNone</p>
</td>
<td>
<p>No compression is applied.</p>
</td>
</tr>
<tr>
<td>
<p>WwanCompressionEnable</p>
</td>
<td>
<p>Enable header and data compression.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field AuthType

<dd>
<p>A value from the WWAN_AUTH_PROTOCOL enumeration that specifies the authentication type to use for
     the PDP activation. This member applies only to GSM-based devices. The MB Service sets this member to 
     <b>WwanAuthProtocolNone</b> for CDMA-based devices.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WwanAuthProtocolNone</p>
</td>
<td>
<p>No authentication protocol.</p>
</td>
</tr>
<tr>
<td>
<p>WwanAuthProtocolPap</p>
</td>
<td>
<p>Unencrypted password authentication.</p>
</td>
</tr>
<tr>
<td>
<p>WwanAuthProtocolChap</p>
</td>
<td>
<p>Use the Challenge Handshake Authentication Protocol (CHAP).</p>
</td>
</tr>
<tr>
<td>
<p>WwanAuthProtocolMsChapV2</p>
</td>
<td>
<p>Use the Microsoft Challenge Handshake Authentication Protocol (CHAP) v2.0.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field IPType

<dd>
<p>A value from the WWAN_IP_TYPE enumeration that specifies the type of IP.</p>
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
<p>Available in Windows 8 and later versions of Windows.</p>
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
<a href="..\wwan\ne-wwan--wwan-activation-command.md">WWAN_ACTIVATION_COMMAND</a>
</dt>
<dt>
<a href="..\wwan\ne-wwan--wwan-compression.md">WWAN_COMPRESSION</a>
</dt>
<dt>
<a href="..\wwan\ne-wwan--wwan-auth-protocol.md">WWAN_AUTH_PROTOCOL</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-set-context-state.md">NDIS_WWAN_SET_CONTEXT_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SET_CONTEXT_STATE structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
