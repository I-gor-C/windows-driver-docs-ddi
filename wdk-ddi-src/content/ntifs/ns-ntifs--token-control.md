---
UID: NS.ntifs._TOKEN_CONTROL
title: TOKEN_CONTROL
author: windows-driver-content
description: The TOKEN_CONTROL structure contains information that identifies an access token.
old-location: ifsk\token_control.htm
old-project: ifsk
ms.assetid: 3e0d41f4-4918-4768-a341-25d27f0a8af0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: TOKEN_CONTROL, TOKEN_CONTROL, *PTOKEN_CONTROL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TOKEN_CONTROL
req.alt-loc: ntifs.h
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
---

# TOKEN_CONTROL structure



## -description
<p>The TOKEN_CONTROL structure contains information that identifies an access token.</p>


## -syntax

````
typedef struct _TOKEN_CONTROL {
  LUID         TokenId;
  LUID         AuthenticationId;
  LUID         ModifiedId;
  TOKEN_SOURCE TokenSource;
} TOKEN_CONTROL, *PTOKEN_CONTROL;
````


## -struct-fields
<dl>

### -field TokenId

<dd>
<p>Specifies a locally unique identifier (LUID) identifying this instance of the token object. </p>
</dd>

### -field AuthenticationId

<dd>
<p>Specifies an LUID assigned to the session this token represents. There can be many tokens representing a single logon session. </p>
</dd>

### -field ModifiedId

<dd>
<p>Specifies an LUID that changes each time the token is modified. An application can use this value as a test of whether a security context has changed since it was last used. </p>
</dd>

### -field TokenSource

<dd>
<p>Specifies a <a href="..\ntifs\ns-ntifs--token-source.md">TOKEN_SOURCE</a> structure identifying the source that issued the token. This information is used in audit logging. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.luid">LUID</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--luid-and-attributes.md">LUID_AND_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-default-dacl.md">TOKEN_DEFAULT_DACL</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-groups.md">TOKEN_GROUPS</a>
</dt>
<dt>
<a href="..\ntifs\ne-ntifs--token-information-class.md">TOKEN_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-owner.md">TOKEN_OWNER</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-primary-group.md">TOKEN_PRIMARY_GROUP</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-privileges.md">TOKEN_PRIVILEGES</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-source.md">TOKEN_SOURCE</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-statistics.md">TOKEN_STATISTICS</a>
</dt>
<dt>
<a href="..\ntifs\ne-ntifs--token-type.md">TOKEN_TYPE</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-user.md">TOKEN_USER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20TOKEN_CONTROL structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
