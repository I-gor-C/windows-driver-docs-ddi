---
UID: NE.wdm._SECURITY_IMPERSONATION_LEVEL
title: SECURITY_IMPERSONATION_LEVEL
author: windows-driver-content
description: The SECURITY_IMPERSONATION_LEVEL enumeration type contains values that specify security impersonation levels. Security impersonation levels govern the degree to which a server process can act on behalf of a client process.
old-location: ifsk\security_impersonation_level.htm
ms.assetid: 6033b33f-74cd-4034-baff-a931b7add370
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: ifsk
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURITY_IMPERSONATION_LEVEL
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
req.iface: 
req.product: Windows 10 or later.
---

# SECURITY_IMPERSONATION_LEVEL enumeration



## -description
<p>The <b>SECURITY_IMPERSONATION_LEVEL</b> enumeration type contains values that specify security impersonation levels. Security impersonation levels govern the degree to which a server process can act on behalf of a client process. </p>


## -syntax

````
typedef enum _SECURITY_IMPERSONATION_LEVEL { 
  SecurityAnonymous,
  SecurityIdentification,
  SecurityImpersonation,
  SecurityDelegation
} SECURITY_IMPERSONATION_LEVEL, *PSECURITY_IMPERSONATION_LEVEL;
````


## -enum-fields
<dl>

### -field <a id="SecurityAnonymous"></a><a id="securityanonymous"></a><a id="SECURITYANONYMOUS"></a><b>SecurityAnonymous</b>

<dd>
<p>The server process cannot obtain identification information about the client and it cannot impersonate the client. It is defined with no value given, and thus, by ANSI C rules, defaults to a value of zero. </p>
</dd>

### -field <a id="SecurityIdentification"></a><a id="securityidentification"></a><a id="SECURITYIDENTIFICATION"></a><b>SecurityIdentification</b>

<dd>
<p>The server process can obtain information about the client, such as security identifiers and privileges, but it cannot impersonate the client. This is useful for servers that export their own objects -- for example, database products that export tables and views. Using the retrieved client-security information, the server can make access-validation decisions without being able to utilize other services using the client's security context. </p>
</dd>

### -field <a id="SecurityImpersonation"></a><a id="securityimpersonation"></a><a id="SECURITYIMPERSONATION"></a><b>SecurityImpersonation</b>

<dd>
<p>The server process can impersonate the client's security context on its local system. The server cannot impersonate the client on remote systems. </p>
</dd>

### -field <a id="SecurityDelegation"></a><a id="securitydelegation"></a><a id="SECURITYDELEGATION"></a><b>SecurityDelegation</b>

<dd>
<p>The server process can impersonate the client's security context on remote systems. </p>
<p> This impersonation level is supported starting with Windows 2000.</p>
</dd>
</dl>

## -remarks
<p>Impersonation is the ability of a process to take on the security attributes of another process.</p>

<p>Impersonation is the ability of a process to take on the security attributes of another process.</p>

<p>Impersonation is the ability of a process to take on the security attributes of another process.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557080">LUID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549716">LUID_AND_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551860">PRIVILEGE_SET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551907">PsImpersonateClient</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551929">PsReferenceImpersonationToken</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563674">SeAccessCheck</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563714">SECURITY_SUBJECT_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556690">SeQueryInformationToken</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556742">SID_AND_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567055">ZwQueryInformationToken</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SECURITY_IMPERSONATION_LEVEL enumeration%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
