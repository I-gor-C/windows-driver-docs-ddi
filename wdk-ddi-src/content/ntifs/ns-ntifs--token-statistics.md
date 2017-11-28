---
UID: NS.ntifs._TOKEN_STATISTICS
title: TOKEN_STATISTICS
author: windows-driver-content
description: TOKEN_STATISTICS contains information about an access token. A driver can retrieve this information by calling SeQueryInformationToken or ZwQueryInformationToken.
old-location: ifsk\token_statistics.htm
old-project: ifsk
ms.assetid: a7f651c0-fcd5-4271-9452-b6ac41cd33cc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: TOKEN_STATISTICS, TOKEN_STATISTICS, *PTOKEN_STATISTICS
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
req.alt-api: TOKEN_STATISTICS
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

# TOKEN_STATISTICS structure



## -description
<p>TOKEN_STATISTICS contains information about an access token. A driver can retrieve this information by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff556690">SeQueryInformationToken</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff567055">ZwQueryInformationToken</a>. </p>


## -syntax

````
typedef struct _TOKEN_STATISTICS {
  LUID                         TokenId;
  LUID                         AuthenticationId;
  LARGE_INTEGER                ExpirationTime;
  TOKEN_TYPE                   TokenType;
  SECURITY_IMPERSONATION_LEVEL ImpersonationLevel;
  ULONG                        DynamicCharged;
  ULONG                        DynamicAvailable;
  ULONG                        GroupCount;
  ULONG                        PrivilegeCount;
  LUID                         ModifiedId;
} TOKEN_STATISTICS, *PTOKEN_STATISTICS;
````


## -struct-fields
<dl>

### -field <b>TokenId</b>

<dd>
<p>Specifies a locally unique identifier (<a href="https://msdn.microsoft.com/library/windows/hardware/ff557080">LUID</a>) that identifies this instance of the token object. </p>
</dd>

### -field <b>AuthenticationId</b>

<dd>
<p>Specifies an LUID assigned to the session this token represents. There can be many tokens representing a single logon session. </p>
</dd>

### -field <b>ExpirationTime</b>

<dd>
<p>Specifies the time at which this token expires. Expiration times for access tokens are not currently supported. </p>
</dd>

### -field <b>TokenType</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556851">TOKEN_TYPE</a> enumerated type indicating whether the token is a primary or impersonation token. </p>
</dd>

### -field <b>ImpersonationLevel</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556631">SECURITY_IMPERSONATION_LEVEL</a> enumerated type indicating the impersonation level of the token. This member is valid only if the <b>TokenType</b> is TokenImpersonation. </p>
</dd>

### -field <b>DynamicCharged</b>

<dd>
<p>Specifies the amount, in bytes, of memory allocated for storing a default access-control list (DACL) and primary group identifier. </p>
</dd>

### -field <b>DynamicAvailable</b>

<dd>
<p>Specifies the portion of the memory allocated for storing a DACL and primary group identifier that is not already in use. This value is returned as a count of free bytes. </p>
</dd>

### -field <b>GroupCount</b>

<dd>
<p>Specifies the number of supplemental group security identifiers (<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>) included in the token. </p>
</dd>

### -field <b>PrivilegeCount</b>

<dd>
<p>Specifies the number of privileges included in the token. </p>
</dd>

### -field <b>ModifiedId</b>

<dd>
<p>Specifies an LUID that changes each time the token is modified. An application can use this value as a test of whether a security context has changed since it was last used. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557080">LUID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556631">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556690">SeQueryInformationToken</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556838">TOKEN_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556851">TOKEN_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567055">ZwQueryInformationToken</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567102">ZwSetInformationToken</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20TOKEN_STATISTICS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
