---
UID: NS.ntifs._TOKEN_GROUPS_AND_PRIVILEGES
title: TOKEN_GROUPS_AND_PRIVILEGES
author: windows-driver-content
description: TOKEN_GROUPS_AND_PRIVILEGES contains information about the group security identifiers (SIDs) and privileges in an access token.
old-location: ifsk\token_groups_and_privileges.htm
old-project: ifsk
ms.assetid: 27d4793d-bdb4-46c5-b6e4-a2136e899adc
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: TOKEN_GROUPS_AND_PRIVILEGES, TOKEN_GROUPS_AND_PRIVILEGES, *PTOKEN_GROUPS_AND_PRIVILEGES
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
req.alt-api: TOKEN_GROUPS_AND_PRIVILEGES
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

# TOKEN_GROUPS_AND_PRIVILEGES structure



## -description
<p>TOKEN_GROUPS_AND_PRIVILEGES contains information about the group security identifiers (SIDs) and privileges in an access token.</p>


## -syntax

````
typedef struct _TOKEN_GROUPS_AND_PRIVILEGES {
  ULONG                SidCount;
  ULONG                SidLength;
  PSID_AND_ATTRIBUTES  Sids;
  ULONG                RestrictedSidCount;
  ULONG                RestrictedSidLength;
  PSID_AND_ATTRIBUTES  RestrictedSids;
  ULONG                PrivilegeCount;
  ULONG                PrivilegeLength;
  PLUID_AND_ATTRIBUTES Privileges;
  LUID                 AuthenticationId;
} TOKEN_GROUPS_AND_PRIVILEGES, *PTOKEN_GROUPS_AND_PRIVILEGES;
````


## -struct-fields
<dl>

### -field SidCount

<dd>
<p>Specifies the number of SIDs in the access token. </p>
</dd>

### -field SidLength

<dd>
<p>Specifies the length, in bytes, required to hold all of the user SIDs and the account SID for the group. </p>
</dd>

### -field Sids

<dd>
<p>A pointer to SID_AND_ATTRIBUTES structures that contain a set of SIDs and corresponding attributes. </p>
</dd>

### -field RestrictedSidCount

<dd>
<p>Specifies the number of the restricted SIDs included in the access token. </p>
</dd>

### -field RestrictedSidLength

<dd>
<p>Specifies the length, in bytes, required to hold all of the restricted SIDs. </p>
</dd>

### -field RestrictedSids

<dd>
<p>A pointer to <a href="..\ntifs\ns-ntifs--sid-and-attributes.md">SID_AND_ATTRIBUTES</a> structures that contain a set of restricted SIDs and corresponding attributes. </p>
</dd>

### -field PrivilegeCount

<dd>
<p>Specifies the number of privileges included in the access token. </p>
</dd>

### -field PrivilegeLength

<dd>
<p>Specifies the length, in bytes, needed to hold all of the privileges. </p>
</dd>

### -field Privileges

<dd>
<p>A pointer to <a href="..\wdm\ns-wdm--luid-and-attributes.md">LUID_AND_ATTRIBUTES</a> structures that contain a set of privileges. </p>
</dd>

### -field AuthenticationId

<dd>
<p>The locally unique identifier (LUID) of the authenticator of the token. </p>
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
<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--luid-and-attributes.md">LUID_AND_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wudfddi\ne-wudfddi--security-impersonation-level.md">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-sefiltertoken.md">SeFilterToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-sequeryinformationtoken.md">SeQueryInformationToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-setokenisrestricted.md">SeTokenIsRestricted</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--sid-and-attributes.md">SID_AND_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-default-dacl.md">TOKEN_DEFAULT_DACL</a>
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
<dt>
<a href="..\ntifs\nf-ntifs-zwqueryinformationtoken.md">ZwQueryInformationToken</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwsetinformationtoken.md">ZwSetInformationToken</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20TOKEN_GROUPS_AND_PRIVILEGES structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
