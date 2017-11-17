---
UID: NI.ntifs.IOCTL_REDIR_QUERY_PATH
title: IOCTL_REDIR_QUERY_PATH
author: windows-driver-content
description: The IOCTL_REDIR_QUERY_PATH control code is sent by the multiple UNC provider (MUP) to network redirectors to determine which provider can handle a specific UNC path in a name-based operation, typically an IRP_MJ_CREATE request.
old-location: ifsk\ioctl_redir_query_path.htm
ms.assetid: 876453a7-922e-4ab7-a609-64d31e60ce88
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_REDIR_QUERY_PATH
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
ms.keywords: ZwWaitForSingleObject
req.iface: 
---

# IOCTL_REDIR_QUERY_PATH IOCTL



## -description
<p>The <b>IOCTL_REDIR_QUERY_PATH</b> control code is sent by the multiple UNC provider (MUP) to network redirectors to determine which provider can handle a specific UNC path in a name-based operation, typically an IRP_MJ_CREATE request. This request is referred to as "prefix resolution."</p>
<p>MUP is a kernel-mode component responsible for channeling all remote file system accesses that use a UNC name to a network redirector (the UNC provider) capable of handling the remote file system requests. MUP is involved when a UNC path is used as illustrated by the following example that could be executed from a command line:</p>


## -syntax

````
notepad \\server\public\readme.txt
````


## -ioctlparameters

### -input-buffer
<p><b>IrpSp-&gt;Parameters.DeviceIoControl.Type3InputBuffer</b> is set to a <b>QUERY_PATH_REQUEST</b> data structure that contains the request. </p>

<p><b>PathNameLength</b></p>

<p>The length, in bytes, of the Unicode string contained in the <b>FilePathName</b> member.</p>

<p><b>SecurityContext</b></p>

<p>A pointer to the security context.</p>

<p><b>FilePathName</b></p>

<p>A non-NULL terminated Unicode string of the form \&lt;server&gt;\&lt;share&gt;\&lt;path&gt;. The length of the string, in bytes, is specified by the <b>PathNameLength</b> member.</p>

<p> </p>

### -input-buffer-length

<text></text>

### -output-buffer
<p><b>IRP-&gt;UserBuffer</b> is set to a <b>QUERY_PATH_REQUEST</b> data structure that contains the response.</p>

<p><b>LengthAccepted</b></p>

<p>The length, in bytes, of the prefix claimed by the provider from the Unicode string path that is specified in the <b>FilePathName</b> member of the <b>QUERY_PATH_REQUEST</b> structure.</p>

<p> </p>

<p><b>IRP-&gt;UserBuffer</b> is set to a <b>QUERY_PATH_REQUEST</b> data structure that contains the response.</p>

<p><b>LengthAccepted</b></p>

<p>The length, in bytes, of the prefix claimed by the provider from the Unicode string path that is specified in the <b>FilePathName</b> member of the <b>QUERY_PATH_REQUEST</b> structure.</p>

<p> </p>

### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The <b>Status</b> member is set to STATUS_SUCCESS on success if the \\server\share prefix name is recognized or to an appropriate NTSTATUS value, such as one of the following:  </p>

<p></p>

<p> The network path cannot be located. The machine name (\\server, for example) is not valid or the network redirector cannot resolve the machine name (using whatever name resolution mechanisms are available). </p>

<p>The specified share name cannot be found on the remote server. The machine name (\\server, for example) is valid, but specified share name cannot be found on the remote server.</p>

<p>There were insufficient resources available to allocate memory for buffers.</p>

<p>An IOCTL_REDIR_QUERY_PATH request should only come from MUP, and the <b>RequestorMode</b> member of the IRP structure should always be <b>KernelMode</b>. This error code is returned if the <b>RequestorMode</b> of the calling thread was not <b>KernelMode</b>. </p>

<p>The <b>PathNameLength</b> member in the <b>QUERY_PATH_REQUEST</b> structure exceeds the maximum allowable length, UNICODE_STRING_MAX_BYTES, for a Unicode string. </p>

<p>If the prefix resolution operation failed due to invalid or incorrect credentials, the provider should return the exact error code that the remote server returns; these error codes must not be translated to STATUS_BAD_NETWORK_NAME or STATUS_BAD_NETWORK_PATH. Error codes like STATUS_LOGON_FAILURE and  STATUS_ACCESS_DENIED serve as a feedback mechanism to the user that indicate the requirement to use appropriate credentials. These error codes are also used in certain cases to prompt the user automatically for credentials. Without these error codes, the user might assume that the machine is not accessible. </p>

<p>If the network redirector is unable to resolve a prefix, it must return an NTSTATUS code that closely matches the intended semantics from the above list of recommended NTSTATUS codes. A network redirector must not return the actual encountered error (STATUS_CONNECTION_REFUSED, for example) directly to MUP if the NTSTATUS code is not from the above list. </p>

<p>The <b>Status</b> member is set to STATUS_SUCCESS on success if the \\server\share prefix name is recognized or to an appropriate NTSTATUS value, such as one of the following:  </p>

<p></p>

<p> The network path cannot be located. The machine name (\\server, for example) is not valid or the network redirector cannot resolve the machine name (using whatever name resolution mechanisms are available). </p>

<p>The specified share name cannot be found on the remote server. The machine name (\\server, for example) is valid, but specified share name cannot be found on the remote server.</p>

<p>There were insufficient resources available to allocate memory for buffers.</p>

<p>An IOCTL_REDIR_QUERY_PATH request should only come from MUP, and the <b>RequestorMode</b> member of the IRP structure should always be <b>KernelMode</b>. This error code is returned if the <b>RequestorMode</b> of the calling thread was not <b>KernelMode</b>. </p>

<p>The <b>PathNameLength</b> member in the <b>QUERY_PATH_REQUEST</b> structure exceeds the maximum allowable length, UNICODE_STRING_MAX_BYTES, for a Unicode string. </p>

<p>If the prefix resolution operation failed due to invalid or incorrect credentials, the provider should return the exact error code that the remote server returns; these error codes must not be translated to STATUS_BAD_NETWORK_NAME or STATUS_BAD_NETWORK_PATH. Error codes like STATUS_LOGON_FAILURE and  STATUS_ACCESS_DENIED serve as a feedback mechanism to the user that indicate the requirement to use appropriate credentials. These error codes are also used in certain cases to prompt the user automatically for credentials. Without these error codes, the user might assume that the machine is not accessible. </p>

<p>If the network redirector is unable to resolve a prefix, it must return an NTSTATUS code that closely matches the intended semantics from the above list of recommended NTSTATUS codes. A network redirector must not return the actual encountered error (STATUS_CONNECTION_REFUSED, for example) directly to MUP if the NTSTATUS code is not from the above list. </p>

<p>The <b>Status</b> member is set to STATUS_SUCCESS on success if the \\server\share prefix name is recognized or to an appropriate NTSTATUS value, such as one of the following:  </p>

<p></p>

<p> The network path cannot be located. The machine name (\\server, for example) is not valid or the network redirector cannot resolve the machine name (using whatever name resolution mechanisms are available). </p>

<p>The specified share name cannot be found on the remote server. The machine name (\\server, for example) is valid, but specified share name cannot be found on the remote server.</p>

<p>There were insufficient resources available to allocate memory for buffers.</p>

<p>An IOCTL_REDIR_QUERY_PATH request should only come from MUP, and the <b>RequestorMode</b> member of the IRP structure should always be <b>KernelMode</b>. This error code is returned if the <b>RequestorMode</b> of the calling thread was not <b>KernelMode</b>. </p>

<p>The <b>PathNameLength</b> member in the <b>QUERY_PATH_REQUEST</b> structure exceeds the maximum allowable length, UNICODE_STRING_MAX_BYTES, for a Unicode string. </p>

<p>If the prefix resolution operation failed due to invalid or incorrect credentials, the provider should return the exact error code that the remote server returns; these error codes must not be translated to STATUS_BAD_NETWORK_NAME or STATUS_BAD_NETWORK_PATH. Error codes like STATUS_LOGON_FAILURE and  STATUS_ACCESS_DENIED serve as a feedback mechanism to the user that indicate the requirement to use appropriate credentials. These error codes are also used in certain cases to prompt the user automatically for credentials. Without these error codes, the user might assume that the machine is not accessible. </p>

<p>If the network redirector is unable to resolve a prefix, it must return an NTSTATUS code that closely matches the intended semantics from the above list of recommended NTSTATUS codes. A network redirector must not return the actual encountered error (STATUS_CONNECTION_REFUSED, for example) directly to MUP if the NTSTATUS code is not from the above list. </p>

## -remarks
<p>Network redirectors should only honor kernel-mode senders of this IOCTL, by verifying that the <b>RequestorMode</b> member of the IRP structure is <b>KernelMode</b>. </p>

<p>Note that IOCTL_REDIR_QUERY_PATH is a METHOD_NEITHER IOCTL. This means that the input and output buffers might not be at the same address. A common mistake by UNC providers is to assume that the input buffer and the output buffer are the same and to use the input buffer pointer to provide the response.</p>

<p>When a UNC provider receives an IOCTL_REDIR_QUERY_PATH request, it has to determine whether it can handle the UNC path specified in the <b>FilePathName</b> member of the <b>QUERY_PATH_REQUEST</b> structure. If so, it has to update the <b>LengthAccepted</b> member of the <b>QUERY_PATH_RESPONSE</b> structure with the length, in bytes, of the prefix it has claimed and complete the IRP with STATUS_SUCCESS. If the provider cannot handle the UNC path specified, it must fail the IOCTL_REDIR_QUERY_PATH request with an appropriate NTSTATUS error code and must not update the <b>LengthAccepted</b> member of the <b>QUERY_PATH_RESPONSE</b> structure. Providers must not modify any of the other members or the <b>FilePathName</b> string under any condition. </p>

<p>The length of the prefix claimed by the provider depends on an individual UNC provider. Most providers claim the \\&lt;servername&gt;\&lt;sharename &gt; part of a path of the form \\&lt;servername&gt;\&lt;sharename&gt;\&lt;path&gt;. For example, if a provider claimed \\server\public given a path \\server\public\dir1\dir2, all name-based operations for the prefix \\server\public (\server\public\file1, for example) will be routed to that provider automatically without any prefix resolution because the prefix is already in the prefix cache. However, a path with the prefix \server\marketing\presentation will go through prefix resolution.</p>

<p>If a network redirector claims a server name (\\server, for example),all requests for shares on this server will go to this network redirector. This behavior is only acceptable if there is no possibility of another share on the same server being accessed by a different network redirector. For example, a network redirector that claims \\server of a UNC path will prevent access by other network redirectors to other shares on this server (WebDAV access to \\server\web, for example). </p>

<p>For more information, see the following sections in the Design Guide:</p><dl>
<dd>
<p>
<a href="ifsk.support_for_unc_naming_and_mup">Support for UNC Naming and MUP</a>
</p>
</dd>
<dd>
<p>
<a href="ifsk.mup_changes_in_microsoft_windows_vista">MUP Changes in Microsoft Windows Vista</a>
</p>
</dd>
</dl><p>
<a href="ifsk.support_for_unc_naming_and_mup">Support for UNC Naming and MUP</a>
</p>

<p>
<a href="ifsk.mup_changes_in_microsoft_windows_vista">MUP Changes in Microsoft Windows Vista</a>
</p>

<p>Network redirectors should only honor kernel-mode senders of this IOCTL, by verifying that the <b>RequestorMode</b> member of the IRP structure is <b>KernelMode</b>. </p>

<p>Note that IOCTL_REDIR_QUERY_PATH is a METHOD_NEITHER IOCTL. This means that the input and output buffers might not be at the same address. A common mistake by UNC providers is to assume that the input buffer and the output buffer are the same and to use the input buffer pointer to provide the response.</p>

<p>When a UNC provider receives an IOCTL_REDIR_QUERY_PATH request, it has to determine whether it can handle the UNC path specified in the <b>FilePathName</b> member of the <b>QUERY_PATH_REQUEST</b> structure. If so, it has to update the <b>LengthAccepted</b> member of the <b>QUERY_PATH_RESPONSE</b> structure with the length, in bytes, of the prefix it has claimed and complete the IRP with STATUS_SUCCESS. If the provider cannot handle the UNC path specified, it must fail the IOCTL_REDIR_QUERY_PATH request with an appropriate NTSTATUS error code and must not update the <b>LengthAccepted</b> member of the <b>QUERY_PATH_RESPONSE</b> structure. Providers must not modify any of the other members or the <b>FilePathName</b> string under any condition. </p>

<p>The length of the prefix claimed by the provider depends on an individual UNC provider. Most providers claim the \\&lt;servername&gt;\&lt;sharename &gt; part of a path of the form \\&lt;servername&gt;\&lt;sharename&gt;\&lt;path&gt;. For example, if a provider claimed \\server\public given a path \\server\public\dir1\dir2, all name-based operations for the prefix \\server\public (\server\public\file1, for example) will be routed to that provider automatically without any prefix resolution because the prefix is already in the prefix cache. However, a path with the prefix \server\marketing\presentation will go through prefix resolution.</p>

<p>If a network redirector claims a server name (\\server, for example),all requests for shares on this server will go to this network redirector. This behavior is only acceptable if there is no possibility of another share on the same server being accessed by a different network redirector. For example, a network redirector that claims \\server of a UNC path will prevent access by other network redirectors to other shares on this server (WebDAV access to \\server\web, for example). </p>

<p>For more information, see the following sections in the Design Guide:</p><dl>
<dd>
<p>
<a href="ifsk.support_for_unc_naming_and_mup">Support for UNC Naming and MUP</a>
</p>
</dd>
<dd>
<p>
<a href="ifsk.mup_changes_in_microsoft_windows_vista">MUP Changes in Microsoft Windows Vista</a>
</p>
</dd>
</dl><p>
<a href="ifsk.support_for_unc_naming_and_mup">Support for UNC Naming and MUP</a>
</p>

<p>
<a href="ifsk.mup_changes_in_microsoft_windows_vista">MUP Changes in Microsoft Windows Vista</a>
</p>

<p>Network redirectors should only honor kernel-mode senders of this IOCTL, by verifying that the <b>RequestorMode</b> member of the IRP structure is <b>KernelMode</b>. </p>

<p>Note that IOCTL_REDIR_QUERY_PATH is a METHOD_NEITHER IOCTL. This means that the input and output buffers might not be at the same address. A common mistake by UNC providers is to assume that the input buffer and the output buffer are the same and to use the input buffer pointer to provide the response.</p>

<p>When a UNC provider receives an IOCTL_REDIR_QUERY_PATH request, it has to determine whether it can handle the UNC path specified in the <b>FilePathName</b> member of the <b>QUERY_PATH_REQUEST</b> structure. If so, it has to update the <b>LengthAccepted</b> member of the <b>QUERY_PATH_RESPONSE</b> structure with the length, in bytes, of the prefix it has claimed and complete the IRP with STATUS_SUCCESS. If the provider cannot handle the UNC path specified, it must fail the IOCTL_REDIR_QUERY_PATH request with an appropriate NTSTATUS error code and must not update the <b>LengthAccepted</b> member of the <b>QUERY_PATH_RESPONSE</b> structure. Providers must not modify any of the other members or the <b>FilePathName</b> string under any condition. </p>

<p>The length of the prefix claimed by the provider depends on an individual UNC provider. Most providers claim the \\&lt;servername&gt;\&lt;sharename &gt; part of a path of the form \\&lt;servername&gt;\&lt;sharename&gt;\&lt;path&gt;. For example, if a provider claimed \\server\public given a path \\server\public\dir1\dir2, all name-based operations for the prefix \\server\public (\server\public\file1, for example) will be routed to that provider automatically without any prefix resolution because the prefix is already in the prefix cache. However, a path with the prefix \server\marketing\presentation will go through prefix resolution.</p>

<p>If a network redirector claims a server name (\\server, for example),all requests for shares on this server will go to this network redirector. This behavior is only acceptable if there is no possibility of another share on the same server being accessed by a different network redirector. For example, a network redirector that claims \\server of a UNC path will prevent access by other network redirectors to other shares on this server (WebDAV access to \\server\web, for example). </p>

<p>For more information, see the following sections in the Design Guide:</p><dl>
<dd>
<p>
<a href="ifsk.support_for_unc_naming_and_mup">Support for UNC Naming and MUP</a>
</p>
</dd>
<dd>
<p>
<a href="ifsk.mup_changes_in_microsoft_windows_vista">MUP Changes in Microsoft Windows Vista</a>
</p>
</dd>
</dl><p>
<a href="ifsk.support_for_unc_naming_and_mup">Support for UNC Naming and MUP</a>
</p>

<p>
<a href="ifsk.mup_changes_in_microsoft_windows_vista">MUP Changes in Microsoft Windows Vista</a>
</p>

<p>Network redirectors should only honor kernel-mode senders of this IOCTL, by verifying that the <b>RequestorMode</b> member of the IRP structure is <b>KernelMode</b>. </p>

<p>Note that IOCTL_REDIR_QUERY_PATH is a METHOD_NEITHER IOCTL. This means that the input and output buffers might not be at the same address. A common mistake by UNC providers is to assume that the input buffer and the output buffer are the same and to use the input buffer pointer to provide the response.</p>

<p>When a UNC provider receives an IOCTL_REDIR_QUERY_PATH request, it has to determine whether it can handle the UNC path specified in the <b>FilePathName</b> member of the <b>QUERY_PATH_REQUEST</b> structure. If so, it has to update the <b>LengthAccepted</b> member of the <b>QUERY_PATH_RESPONSE</b> structure with the length, in bytes, of the prefix it has claimed and complete the IRP with STATUS_SUCCESS. If the provider cannot handle the UNC path specified, it must fail the IOCTL_REDIR_QUERY_PATH request with an appropriate NTSTATUS error code and must not update the <b>LengthAccepted</b> member of the <b>QUERY_PATH_RESPONSE</b> structure. Providers must not modify any of the other members or the <b>FilePathName</b> string under any condition. </p>

<p>The length of the prefix claimed by the provider depends on an individual UNC provider. Most providers claim the \\&lt;servername&gt;\&lt;sharename &gt; part of a path of the form \\&lt;servername&gt;\&lt;sharename&gt;\&lt;path&gt;. For example, if a provider claimed \\server\public given a path \\server\public\dir1\dir2, all name-based operations for the prefix \\server\public (\server\public\file1, for example) will be routed to that provider automatically without any prefix resolution because the prefix is already in the prefix cache. However, a path with the prefix \server\marketing\presentation will go through prefix resolution.</p>

<p>If a network redirector claims a server name (\\server, for example),all requests for shares on this server will go to this network redirector. This behavior is only acceptable if there is no possibility of another share on the same server being accessed by a different network redirector. For example, a network redirector that claims \\server of a UNC path will prevent access by other network redirectors to other shares on this server (WebDAV access to \\server\web, for example). </p>

<p>For more information, see the following sections in the Design Guide:</p><dl>
<dd>
<p>
<a href="ifsk.support_for_unc_naming_and_mup">Support for UNC Naming and MUP</a>
</p>
</dd>
<dd>
<p>
<a href="ifsk.mup_changes_in_microsoft_windows_vista">MUP Changes in Microsoft Windows Vista</a>
</p>
</dd>
</dl><p>
<a href="ifsk.support_for_unc_naming_and_mup">Support for UNC Naming and MUP</a>
</p>

<p>
<a href="ifsk.mup_changes_in_microsoft_windows_vista">MUP Changes in Microsoft Windows Vista</a>
</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545865">FsRtlDeregisterUncProvider</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547184">FsRtlRegisterUncProviderEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548320">IOCTL_REDIR_QUERY_PATH_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IOCTL_REDIR_QUERY_PATH control code%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
