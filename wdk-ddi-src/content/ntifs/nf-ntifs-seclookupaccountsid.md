---
UID: NF.ntifs.SecLookupAccountSid
title: SecLookupAccountSid
author: windows-driver-content
description: SecLookupAccountSid accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.
old-location: ifsk\seclookupaccountsid.htm
old-project: ifsk
ms.assetid: 7237a041-46e0-4211-97c1-96d309ada602
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SecLookupAccountSid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This SecLookupAccountSid function is only available on Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SecLookupAccountSid
req.alt-loc: Ksecdd.lib,Ksecdd.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ksecdd.lib
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# SecLookupAccountSid function



## -description
<p><b>SecLookupAccountSid</b> accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.</p>


## -syntax

````
NTSTATUS SecLookupAccountSid(
  _In_      PSID            Sid,
  _Out_     PULONG          NameSize,
  _Inout_   PUNICODE_STRING NameBuffer,
  _Out_     PULONG          DomainSize,
  _Out_opt_ PUNICODE_STRING DomainBuffer,
  _Out_     PSID_NAME_USE   NameUse
);
````


## -parameters
<dl>

### -param <i>Sid</i> [in]

<dd>
<p>A pointer to the SID to look up. </p>
</dd>

### -param <i>NameSize</i> [out]

<dd>
<p>A pointer to a variable that specifies the size of the <i>NameBuffer</i>. On input, this value specifies the size in bytes of the input <i>NameBuffer</i>. If the function fails because the buffer is too small, this variable receives the required buffer size. On success, this variable contains the size of the returned <i>NameBuffer</i>.</p>
</dd>

### -param <i>NameBuffer</i> [in, out]

<dd>
<p>A pointer to the <i>NameBuffer</i>. </p>
</dd>

### -param <i>DomainSize</i> [out]

<dd>
<p>A pointer to an optional variable that specifies the size of the <i>ReferencedDomain</i> parameter. On input, this value specifies the size of the <i>ReferencedDomain</i> buffer. If the function fails because the buffer is too small, this variable receives the required buffer size. If the <i>ReferencedDomain</i> parameter is <b>NULL</b>, this parameter must be zero.</p>
</dd>

### -param <i>DomainBuffer</i> [out, optional]

<dd>
<p>A pointer to an optional variable to the buffer that receives the name of the domain as a Unicode string where the account name is found. For computers that are not joined to a domain, this buffer receives the computer name. If this parameter is <b>NULL</b>, the function returns the required buffer size in the <i>DomainSize</i> variable. </p>
<p>On Windows Server 2003, the domain name returned for most accounts in the security database of the local computer is the name of the domain for which the server is a domain controller.</p>
<p>On Windows XP, the domain name returned for most accounts in the security database of the local computer is the name of the computer as of the last start of the system (backslashes are excluded). If the name of the computer changes, the old name continues to be returned as the domain name until the system is restarted.</p>
</dd>

### -param <i>NameUse</i> [out]

<dd>
<p>A pointer to a SID_NAME_USE enumerated type that indicates the type of the account when the function returns. </p>
</dd>
</dl>

## -returns
<p><b>SecLookupAccountSid</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: </p><dl>
<dt><b>SEC_E_INTERNAL_ERROR</b></dt>
</dl><p>An internal error occurred while trying to connect to the Local System Authority (LSA) or the local procedure call (LPC) to the security provider failed. </p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The process ID associated with the currently executing thread does not match the current process ID. </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer size for the <i>NameBuffer</i> or the <i>ReferencedDomain</i> parameter was too small.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The length of the <i>Name</i> parameter exceeded the length allowed in a message to the Local System Authority (LSA). </p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>It was not possible to allocate sufficient memory for a temporary internal buffer used by this function.</p><dl>
<dt><b>STATUS_NONE_MAPPED</b></dt>
</dl><p>The <i>Sid</i> parameter could not be found. </p><dl>
<dt><b>STATUS_PROCESS_IS_TERMINATING</b></dt>
</dl><p>This process has terminated so it is not possible to establish a local procedure call (LPC) connection.</p>

<p> </p>

## -remarks
<p><b>SecLookupAccountSid</b> attempts to find a name for the specified SID by first checking a list of well-known SIDs. If the supplied SID does not correspond to a well-known SID, the function checks built-in and administratively defined local accounts. Next, the function checks the primary domain. Security identifiers not recognized by the primary domain are checked against the trusted domains that correspond to their SID prefixes.</p>

<p>If the function cannot find an account name for the SID, <b>SecLookupAccountSid</b> fails. This can occur if a network time-out prevents the function from finding the name. It also occurs for SIDs that have no corresponding account name, such as a logon SID that identifies a logon session.</p>

<p>In addition to looking up SIDs for local accounts, local domain accounts, and explicitly trusted domain accounts, <b>SecLookupAccountSid</b> can look up SIDs for any account in any domain in the forest, including SIDs that appear only in the SIDhistory field of an account in the forest. The SIDhistory field stores former SIDs of an account that has been moved from another domain. To look up a SID, <b>SecLookupAccountSid</b> queries the global catalog of the forest. </p>

<p><b>SecLookupAccountSid</b> is equivalent to the Win32 <b>LookupAccountSid</b> function. </p>

<p><b>SecLookupAccountSid</b> is exported by the ksecdd driver, which implements this function by using user-mode helper services. Accordingly, the use of this function within file systems must obey the usual rules for communication with user-mode services. <b>SecLookupAccountSid</b> cannot be used during paging file I/O. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This SecLookupAccountSid function is only available on Windows XP and later.</p>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ksecdd.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-seclookupaccountname.md">SecLookupAccountName</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-seclookupwellknownsid.md">SecLookupWellKnownSid</a>
</dt>
<dt>
<a href="ifsk.sid">SID</a>
</dt>
<dt>
<a href="..\ntifs\ne-ntifs--sid-name-use.md">SID_NAME_USE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SecLookupAccountSid function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
