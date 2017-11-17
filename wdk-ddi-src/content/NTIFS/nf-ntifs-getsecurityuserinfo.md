---
UID: NF.ntifs.GetSecurityUserInfo
title: GetSecurityUserInfo
author: windows-driver-content
description: The GetSecurityUserInfo function retrieves information about a logon session.
old-location: ifsk\getsecurityuserinfo.htm
ms.assetid: 2f26ff14-dd2c-4e80-aea5-38a7dd16d904
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetSecurityUserInfo
req.alt-loc: ksecdd.lib,ksecdd.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ksecdd.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: GetSecurityUserInfo
req.iface: 
---

# GetSecurityUserInfo function



## -description
<p>The <b>GetSecurityUserInfo</b> function retrieves information about a logon <a href="http://go.microsoft.com/fwlink/p/?linkid=121237">session</a>.</p>


## -syntax

````
NTSTATUS GetSecurityUserInfo(
  _In_opt_ PLUID             LogonId,
  _In_     ULONG             Flags,
  _Out_    PSecurityUserData *UserInformation
);
````


## -parameters
<dl>

### -param <i>LogonId</i> [in, optional]

<dd>
<p>An optional pointer to an <a href="http://go.microsoft.com/fwlink/p/?linkid=121236">LUID</a> containing the logon session for which information is to be retrieved. If <i>LogonId</i> is <b>NULL</b>, information for the logon session of the calling thread is returned.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>This parameter is currently not used.</p>
</dd>

### -param <i>UserInformation</i> [out]

<dd>
<p>A pointer to a location which contains a pointer to a <a href="http://go.microsoft.com/fwlink/p/?linkid=121238">SecurityUserData</a> structure. If the function call succeeds, the user information is returned in this structure. The caller is responsible for freeing this buffer by calling the <a href="http://go.microsoft.com/fwlink/p/?linkid=121239">LsaFreeReturnBuffer</a> function.</p>
</dd>
</dl>

## -returns
<p><b>GetSecurityUserInfo</b> returns an appropriate NTSTATUS value, such as one of the following.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The SecurityUserData structure, indirectly pointed to by <i>UserInformation</i>, contains the requested user information.</p><dl>
<dt><b>STATUS_NO_SUCH_LOGON_SESSION</b></dt>
</dl><p>Indicates that the specified logon session does not exist.</p>

<p> </p>

## -remarks
<p>This function obtains information about a logon <a href="http://go.microsoft.com/fwlink/p/?linkid=121237">session</a> via  the <a href="http://go.microsoft.com/fwlink/p/?linkid=121238">SecurityUserData</a>  structure.</p>

<p>This function obtains information about a logon <a href="http://go.microsoft.com/fwlink/p/?linkid=121237">session</a> via  the <a href="http://go.microsoft.com/fwlink/p/?linkid=121238">SecurityUserData</a>  structure.</p>

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
<p>Available in Microsoft Windows 2000 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=121239">LsaFreeReturnBuffer</a></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549736">MapSecurityError</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20GetSecurityUserInfo function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
