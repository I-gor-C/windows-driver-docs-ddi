---
UID: NS.wwan._WWAN_CONTEXT
title: WWAN_CONTEXT
author: windows-driver-content
description: The WWAN_CONTEXT structure represents a provisioned context that is supported by the MB device.
old-location: netvista\wwan_context.htm
old-project: netvista
ms.assetid: 81687237-7b24-439f-b706-e0bf95b4de68
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WWAN_CONTEXT, WWAN_CONTEXT, *PWWAN_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_CONTEXT
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

# WWAN_CONTEXT structure



## -description
<p>The WWAN_CONTEXT structure represents a provisioned context that is supported by the MB
  device.</p>


## -syntax

````
typedef struct _WWAN_CONTEXT {
  ULONG              ContextId;
  WWAN_CONTEXT_TYPE  ContextType;
  WCHAR              AccessString[WWAN_ACCESSSTRING_LEN];
  WCHAR              UserName[WWAN_USERNAME_LEN];
  WCHAR              Password[WWAN_PASSWORD_LEN];
  WWAN_COMPRESSION   Compression;
  WWAN_AUTH_PROTOCOL AuthType;
} WWAN_CONTEXT, *PWWAN_CONTEXT;
````


## -struct-fields
<dl>

### -field ContextId

<dd>
<p>A unique ID for this context.
     </p>
<p>For 
     <i>set</i> OID_WWAN_PROVISIONED_CONTEXT requests, the MB Service can set the value to
     WWAN_CONTEXT_ID_APPEND. If this value is used, the miniport driver should decide the index for storing
     the context information. WWAN_CONTEXT_ID_APPEND should never be returned in response to 
     <i>query</i> OID_WWAN_PROVISIONED_CONTEXT requests.</p>
</dd>

### -field ContextType

<dd>
<p>Specifies the type of context being represented, for example, Internet connectivity, VPN (a
     connection to a corporate network), or Voice-over-IP (VOIP). Miniport drivers should specify 
     <b>WwanContextTypeNone</b> for empty or unprovisioned contexts.</p>
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
<p>The username to use for authentication. This member can be <b>NULL</b>.</p>
</dd>

### -field Password

<dd>
<p>The password to use for authentication. This member can be <b>NULL</b>.</p>
</dd>

### -field Compression

<dd>
<p>Specifies the compression to be used in the data connection for header and data. This member
     applies only to GSM-based devices. The MB Service sets this member to 
     <b>WwanCompressionNone</b> for CDMA-based devices.</p>
</dd>

### -field AuthType

<dd>
<p>Authentication type to use for the PDP activation.</p>
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
<a href="..\wwan\ne-wwan--wwan-context-type.md">WWAN_CONTEXT_TYPE</a>
</dt>
<dt>
<a href="..\wwan\ne-wwan--wwan-compression.md">WWAN_COMPRESSION</a>
</dt>
<dt>
<a href="..\wwan\ne-wwan--wwan-auth-protocol.md">WWAN_AUTH_PROTOCOL</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-set-provisioned-context.md">
   NDIS_WWAN_SET_PROVISIONED_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_CONTEXT structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
