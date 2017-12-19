---
UID: NF.ntifs.SeQuerySubjectContextToken
title: SeQuerySubjectContextToken macro
author: windows-driver-content
description: The SeQuerySubjectContextToken macro retrieves the access token for a security subject context.
old-location: ifsk\sequerysubjectcontexttoken.htm
old-project: ifsk
ms.assetid: af326cb1-446a-49b7-a381-472deb9ecc82
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: SeQuerySubjectContextToken
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SeQuerySubjectContextToken
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
req.irql: PASSIVE_LEVEL
---

# SeQuerySubjectContextToken macro



## -description
The <b>SeQuerySubjectContextToken</b> macro retrieves the access token for a security subject context.



## -syntax

````
PACCESS_TOKEN SeQuerySubjectContextToken(
  _In_ PSECURITY_SUBJECT_CONTEXT SubjectContext
);
````


## -parameters

### -param SubjectContext [in]

Pointer to the subject context to query.


## -remarks
The access token pointer returned by <b>SeQuerySubjectContextToken</b> can be passed to <b>SeQueryInformationToken</b>. 

<b>SeQuerySubjectContextToken</b> does not affect the lock status or access token of the subject context.

For more information about security and access control, see the documentation on these topics in the Microsoft Windows SDK.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
This routine is available on Microsoft Windows 2000 and later. 

</td>
</tr>
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
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.psdereferenceimpersonationtoken">PsDereferenceImpersonationToken</a>
</dt>
<dt>
<a href="ifsk.psdereferenceprimarytoken">PsDereferencePrimaryToken</a>
</dt>
<dt>
<a href="ifsk.security_subject_context">SECURITY_SUBJECT_CONTEXT</a>
</dt>
<dt>
<a href="ifsk.sequeryauthenticationidtoken">SeQueryAuthenticationIdToken</a>
</dt>
<dt>
<a href="ifsk.sequeryinformationtoken">SeQueryInformationToken</a>
</dt>
<dt>
<a href="ifsk.setokenisadmin">SeTokenIsAdmin</a>
</dt>
<dt>
<a href="ifsk.setokenisrestricted">SeTokenIsRestricted</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SeQuerySubjectContextToken function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

