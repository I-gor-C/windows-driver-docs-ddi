---
UID: NF.wudfddi.IWDFRemoteTarget.OpenFileByName
title: IWDFRemoteTarget::OpenFileByName
author: windows-driver-content
description: The OpenFileByName method opens a remote I/O target that is a file.
old-location: wdf\iwdfremotetarget_openfilebyname.htm
old-project: wdf
ms.assetid: 7f0cef78-3edc-434b-af70-39694776e8a7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFRemoteTarget, OpenFileByName, IWDFRemoteTarget::OpenFileByName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFRemoteTarget.OpenFileByName
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFRemoteTarget
req.product: Windows 10 or later.
---

# IWDFRemoteTarget::OpenFileByName method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OpenFileByName</b> method opens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is a file.</p>


## -syntax

````
HRESULT OpenFileByName(
  [in]           PCWSTR                      pszFileName,
  [in]           DWORD                       DesiredAccess,
  [in, optional] PUMDF_IO_TARGET_OPEN_PARAMS pOpenParams
);
````


## -parameters
<dl>

### -param <i>pszFileName</i> [in]

<dd>
<p>A pointer to a caller-supplied, <b>null</b>-terminated string that represents the name of the file to open. For more information about this member, see the <i>FileName</i> parameter of <a href="http://go.microsoft.com/fwlink/p/?linkid=152795">CreateFile</a> in the Windows SDK.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>A bitmask that specifies the caller's desired access to the file. For more information about this member, see the <i>dwDesiredAccess</i> parameter of <a href="http://go.microsoft.com/fwlink/p/?linkid=152795">CreateFile</a> in the Windows SDK.</p>
</dd>

### -param <i>pOpenParams</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff561275">UMDF_IO_TARGET_OPEN_PARAMS</a> structure that contains additional parameters. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>OpenFileByName</b> returns S_OK if the operation succeeds. Otherwise, the method might return the following value:</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The framework's attempt to allocate memory failed. </p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains.

</p>

<p>The framework's <a href="wdf.using_umdf_verifier">verifier</a> reports an error if the framework cannot open the file.</p>

## -remarks
<p>Your driver can use <b>OpenFileByName</b> to open a file, if the driver stack to which your driver belongs does not support the file's device. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff558930">IWDFFileHandleTargetFactory::CreateFileHandleTarget</a> to open a file, if the driver stack to which your driver belongs does support the file's device.</p>

<p>The specified file must be accessible by the account that loaded the UMDF-based driver, which is typically the Local Service account. However, if the driver uses <a href="wdf.handling_client_impersonation">impersonation</a> when it calls <b>OpenFileByName</b>, the file must be accessible by the impersonated account.</p>

<p>Do not call <b>OpenFileByName</b> to open a remote target to a control device object. Instead, open the control device directly by calling <a href="http://go.microsoft.com/fwlink/p/?linkid=152795">CreateFile</a>.</p>

<p>For more information about the <b>OpenFileByName</b> method and remote I/O targets, see <a href="wdf.general_i_o_targets_in_umdf">General I/O Targets in UMDF</a>.</p>

<p>The following code example creates a remote target object and opens an existing file with read-only access.</p>

<p>Your driver can use <b>OpenFileByName</b> to open a file, if the driver stack to which your driver belongs does not support the file's device. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff558930">IWDFFileHandleTargetFactory::CreateFileHandleTarget</a> to open a file, if the driver stack to which your driver belongs does support the file's device.</p>

<p>The specified file must be accessible by the account that loaded the UMDF-based driver, which is typically the Local Service account. However, if the driver uses <a href="wdf.handling_client_impersonation">impersonation</a> when it calls <b>OpenFileByName</b>, the file must be accessible by the impersonated account.</p>

<p>Do not call <b>OpenFileByName</b> to open a remote target to a control device object. Instead, open the control device directly by calling <a href="http://go.microsoft.com/fwlink/p/?linkid=152795">CreateFile</a>.</p>

<p>For more information about the <b>OpenFileByName</b> method and remote I/O targets, see <a href="wdf.general_i_o_targets_in_umdf">General I/O Targets in UMDF</a>.</p>

<p>The following code example creates a remote target object and opens an existing file with read-only access.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560247">IWDFRemoteTarget</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556928">IWDFDevice2::CreateRemoteTarget</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560276">IWDFRemoteTarget::OpenRemoteInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFRemoteTarget::OpenFileByName method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
