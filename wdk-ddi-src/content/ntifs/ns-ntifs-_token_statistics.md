---
UID: NS.NTIFS._TOKEN_STATISTICS
title: _TOKEN_STATISTICS
author: windows-driver-content
description: TOKEN_STATISTICS contains information about an access token. A driver can retrieve this information by calling SeQueryInformationToken or ZwQueryInformationToken.
old-location: ifsk\token_statistics.htm
old-project: ifsk
ms.assetid: a7f651c0-fcd5-4271-9452-b6ac41cd33cc
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _TOKEN_STATISTICS, *PTOKEN_STATISTICS, PTOKEN_STATISTICS, TOKEN_STATISTICS
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
---

# _TOKEN_STATISTICS structure



## -description
TOKEN_STATISTICS contains information about an access token. A driver can retrieve this information by calling <a href="ifsk.sequeryinformationtoken">SeQueryInformationToken</a> or <a href="kernel.zwqueryinformationtoken">ZwQueryInformationToken</a>. 



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

### -field TokenId

Specifies a locally unique identifier (<a href="ifsk.luid">LUID</a>) that identifies this instance of the token object. 


### -field AuthenticationId

Specifies an LUID assigned to the session this token represents. There can be many tokens representing a single logon session. 


### -field ExpirationTime

Specifies the time at which this token expires. Expiration times for access tokens are not currently supported. 


### -field TokenType

Specifies a <a href="ifsk.token_type">TOKEN_TYPE</a> enumerated type indicating whether the token is a primary or impersonation token. 


### -field ImpersonationLevel

Specifies a <a href="ifsk.security_impersonation_level">SECURITY_IMPERSONATION_LEVEL</a> enumerated type indicating the impersonation level of the token. This member is valid only if the <b>TokenType</b> is TokenImpersonation. 


### -field DynamicCharged

Specifies the amount, in bytes, of memory allocated for storing a default access-control list (DACL) and primary group identifier. 


### -field DynamicAvailable

Specifies the portion of the memory allocated for storing a DACL and primary group identifier that is not already in use. This value is returned as a count of free bytes. 


### -field GroupCount

Specifies the number of supplemental group security identifiers (<a href="ifsk.sid">SID</a>) included in the token. 


### -field PrivilegeCount

Specifies the number of privileges included in the token. 


### -field ModifiedId

Specifies an LUID that changes each time the token is modified. An application can use this value as a test of whether a security context has changed since it was last used. 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="ifsk.acl">ACL</a>
</dt>
<dt>
<a href="ifsk.luid">LUID</a>
</dt>
<dt>
<a href="ifsk.security_impersonation_level">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="ifsk.sequeryinformationtoken">SeQueryInformationToken</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
<dt>
<a href="ifsk.token_information_class">TOKEN_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="ifsk.token_type">TOKEN_TYPE</a>
</dt>
<dt>
<a href="kernel.zwqueryinformationtoken">ZwQueryInformationToken</a>
</dt>
<dt>
<a href="kernel.zwsetinformationtoken">ZwSetInformationToken</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20TOKEN_STATISTICS structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

