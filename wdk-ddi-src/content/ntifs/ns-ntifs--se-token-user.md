---
UID: NS.ntifs._SE_TOKEN_USER
title: SE_TOKEN_USER
author: windows-driver-content
description: The SE_TOKEN_USER structure holds the maximum-sized valid user SID that can be returned by SeQueryInformationToken, GetTokenInformation, or ZwQueryInformationToken with the TokenUser information class. This structure is suitable for stack allocation.
old-location: ifsk\se_token_user.htm
old-project: ifsk
ms.assetid: 3B870461-0C5D-46DF-A850-EB796AE5A4CB
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SE_TOKEN_USER, SE_TOKEN_USER, PSE_TOKEN_USER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SE_TOKEN_USER
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

# SE_TOKEN_USER structure



## -description
<p>The <b>SE_TOKEN_USER</b> structure holds the maximum-sized valid user SID that can be returned by <a href="..\ntifs\nf-ntifs-sequeryinformationtoken.md">SeQueryInformationToken</a>, <a href="security.gettokeninformation">GetTokenInformation</a>, or <a href="..\ntifs\nf-ntifs-zwqueryinformationtoken.md">ZwQueryInformationToken</a> with the TokenUser information class. This structure is suitable for stack allocation.</p>


## -syntax

````
typedef struct _SE_TOKEN_USER {
  union {
    TOKEN_USER         TokenUser;
    SID_AND_ATTRIBUTES User;
  };
  union {
    SID   Sid;
    UCHAR Buffer[SECURITY_MAX_SID_SIZE];
  };
} SE_TOKEN_USER, *PSE_TOKEN_USER;
````


## -struct-fields
<dl>

### -field TokenUser

<dd>
<p>Specifies a <b>TOKEN_USER</b> structure representing the user associated with an access token.</p>
</dd>

### -field User

<dd>
<p>Specifies an <b>SID_AND_ATTRIBUTES</b> structure representing the user associated with the access token.</p>
</dd>

### -field Sid

<dd>
<p>Specifies a <b>Security Identifier (SID)</b> structure used to uniquely identify users or groups</p>
</dd>

### -field Buffer

<dd>
<p>Specifies an array of SECURITY_MAX_SID_SIZE for allocating enough memory for the largest possible SID size.</p>
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
<dt>Ntifs.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556742">SID_AND_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--token-user.md">TOKEN_USER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SE_TOKEN_USER structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
