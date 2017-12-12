---
UID: NS.NTIFS._TOKEN_GROUPS_AND_PRIVILEGES
title: _TOKEN_GROUPS_AND_PRIVILEGES
author: windows-driver-content
description: TOKEN_GROUPS_AND_PRIVILEGES contains information about the group security identifiers (SIDs) and privileges in an access token.
old-location: ifsk\token_groups_and_privileges.htm
old-project: ifsk
ms.assetid: 27d4793d-bdb4-46c5-b6e4-a2136e899adc
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _TOKEN_GROUPS_AND_PRIVILEGES, *PTOKEN_GROUPS_AND_PRIVILEGES, TOKEN_GROUPS_AND_PRIVILEGES
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
---

# _TOKEN_GROUPS_AND_PRIVILEGES structure



## -description
TOKEN_GROUPS_AND_PRIVILEGES contains information about the group security identifiers (SIDs) and privileges in an access token.



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

### -field SidCount

Specifies the number of SIDs in the access token. 


### -field SidLength

Specifies the length, in bytes, required to hold all of the user SIDs and the account SID for the group. 


### -field Sids

A pointer to SID_AND_ATTRIBUTES structures that contain a set of SIDs and corresponding attributes. 


### -field RestrictedSidCount

Specifies the number of the restricted SIDs included in the access token. 


### -field RestrictedSidLength

Specifies the length, in bytes, required to hold all of the restricted SIDs. 


### -field RestrictedSids

A pointer to <a href="ifsk.sid_and_attributes">SID_AND_ATTRIBUTES</a> structures that contain a set of restricted SIDs and corresponding attributes. 


### -field PrivilegeCount

Specifies the number of privileges included in the access token. 


### -field PrivilegeLength

Specifies the length, in bytes, needed to hold all of the privileges. 


### -field Privileges

A pointer to <a href="ifsk.luid_and_attributes">LUID_AND_ATTRIBUTES</a> structures that contain a set of privileges. 


### -field AuthenticationId

The locally unique identifier (LUID) of the authenticator of the token. 


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
<a href="ifsk.luid_and_attributes">LUID_AND_ATTRIBUTES</a>
</dt>
<dt>
<a href="ifsk.security_impersonation_level">SECURITY_IMPERSONATION_LEVEL</a>
</dt>
<dt>
<a href="ifsk.sefiltertoken">SeFilterToken</a>
</dt>
<dt>
<a href="ifsk.sequeryinformationtoken">SeQueryInformationToken</a>
</dt>
<dt>
<a href="ifsk.setokenisrestricted">SeTokenIsRestricted</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
<dt>
<a href="ifsk.sid_and_attributes">SID_AND_ATTRIBUTES</a>
</dt>
<dt>
<a href="ifsk.token_default_dacl">TOKEN_DEFAULT_DACL</a>
</dt>
<dt>
<a href="ifsk.token_information_class">TOKEN_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="ifsk.token_owner">TOKEN_OWNER</a>
</dt>
<dt>
<a href="ifsk.token_primary_group">TOKEN_PRIMARY_GROUP</a>
</dt>
<dt>
<a href="ifsk.token_privileges">TOKEN_PRIVILEGES</a>
</dt>
<dt>
<a href="ifsk.token_source">TOKEN_SOURCE</a>
</dt>
<dt>
<a href="ifsk.token_statistics">TOKEN_STATISTICS</a>
</dt>
<dt>
<a href="ifsk.token_type">TOKEN_TYPE</a>
</dt>
<dt>
<a href="ifsk.token_user">TOKEN_USER</a>
</dt>
<dt>
<a href="kernel.zwqueryinformationtoken">ZwQueryInformationToken</a>
</dt>
<dt>
<a href="kernel.zwsetinformationtoken">ZwSetInformationToken</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20TOKEN_GROUPS_AND_PRIVILEGES structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

