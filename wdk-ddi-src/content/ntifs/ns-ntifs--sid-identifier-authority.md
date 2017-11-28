---
UID: NS.ntifs._SID_IDENTIFIER_AUTHORITY
title: SID_IDENTIFIER_AUTHORITY
author: windows-driver-content
description: The SID_IDENTIFIER_AUTHORITY structure represents the top-level authority of a security identifier (SID).
old-location: ifsk\sid_identifier_authority.htm
old-project: ifsk
ms.assetid: 66d8b02d-fbab-4ff7-8f47-858b9f143171
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SID_IDENTIFIER_AUTHORITY, SID_IDENTIFIER_AUTHORITY, *PSID_IDENTIFIER_AUTHORITY
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
req.alt-api: SID_IDENTIFIER_AUTHORITY
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

# SID_IDENTIFIER_AUTHORITY structure



## -description
<p>The SID_IDENTIFIER_AUTHORITY structure represents the top-level authority of a security identifier (SID). </p>


## -syntax

````
typedef struct _SID_IDENTIFIER_AUTHORITY {
  UCHAR Value[6];
} SID_IDENTIFIER_AUTHORITY, *PSID_IDENTIFIER_AUTHORITY;
````


## -struct-fields
<dl>

### -field <b>Value</b>

<dd>
<p>An array of six bytes specifying a SID's top-level authority. </p>
</dd>
</dl>

## -remarks
<p>The identifier authority value identifies the agency that issued the SID. The following identifier authorities are predefined. </p>

<p>SECURITY_NULL_SID_AUTHORITY</p>

<p>0</p>

<p>SECURITY_WORLD_SID_AUTHORITY</p>

<p>1</p>

<p>SECURITY_LOCAL_SID_AUTHORITY</p>

<p>2</p>

<p>SECURITY_CREATOR_SID_AUTHORITY</p>

<p>3</p>

<p>SECURITY_NON_UNIQUE_AUTHORITY</p>

<p>4</p>

<p>SECURITY_NT_AUTHORITY</p>

<p>5</p>

<p> </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552998">RtlInitializeSid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556740">SID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SID_IDENTIFIER_AUTHORITY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
