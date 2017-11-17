---
UID: NF.wudfddi.IWDFRemoteTarget.Reopen
title: IWDFRemoteTarget::Reopen
author: windows-driver-content
description: The Reopen method reopens a remote I/O target after it has been temporarily closed.
old-location: wdf\iwdfremotetarget_reopen.htm
ms.assetid: 904904e7-ca59-4dcb-92db-8c7f6a9cbff7
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFRemoteTarget.Reopen
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
ms.keywords: IWDFRemoteTarget, Reopen, IWDFRemoteTarget::Reopen
req.iface: IWDFRemoteTarget
req.product: Windows 10 or later.
---

# IWDFRemoteTarget::Reopen method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>Reopen</b> method reopens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> after it has been temporarily closed.</p>


## -syntax

````
HRESULT Reopen();
````


## -parameters


## -returns
<p><b>Reopen</b> returns S_OK if the operation succeeds. Otherwise, the method might return the following value:</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The framework's attempt to allocate memory failed. </p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains.

</p>

<p>The framework's <a href="wdf.using_umdf_verifier">verifier</a> reports an error if the framework cannot open the file.</p>

<p><b>Reopen</b> returns S_OK if the operation succeeds. Otherwise, the method might return the following value:</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The framework's attempt to allocate memory failed. </p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains.

</p>

<p>The framework's <a href="wdf.using_umdf_verifier">verifier</a> reports an error if the framework cannot open the file.</p>

<p><b>Reopen</b> returns S_OK if the operation succeeds. Otherwise, the method might return the following value:</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The framework's attempt to allocate memory failed. </p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains.

</p>

<p>The framework's <a href="wdf.using_umdf_verifier">verifier</a> reports an error if the framework cannot open the file.</p>

## -remarks
<p>Typically, a driver calls <b>Reopen</b> from within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556899">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a> callback function, but <b>Reopen</b> can instead be called after <b>OnRemoteTargetRemoveCanceled</b> returns. </p>

<p>Reopen uses the file or interface name that the driver previously specified to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560273">IWDFRemoteTarget::OpenFileByName</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff560276">IWDFRemoteTarget::OpenRemoteInterface</a>. If you want to change the file or interface that the driver is using, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560253">IWDFRemoteTarget::Close</a>, and then it can call <b>OpenFileByName</b> or <b>OpenRemoteInterface</b> instead of <b>Reopen</b>.</p>

<p>For more information about <b>Reopen</b> and how to use remote I/O targets in UMDF-based drivers, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>.</p>

<p>The following code example shows an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556899">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a> callback function that calls <b>Reopen</b>.</p>

<p>Typically, a driver calls <b>Reopen</b> from within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556899">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a> callback function, but <b>Reopen</b> can instead be called after <b>OnRemoteTargetRemoveCanceled</b> returns. </p>

<p>Reopen uses the file or interface name that the driver previously specified to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560273">IWDFRemoteTarget::OpenFileByName</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff560276">IWDFRemoteTarget::OpenRemoteInterface</a>. If you want to change the file or interface that the driver is using, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560253">IWDFRemoteTarget::Close</a>, and then it can call <b>OpenFileByName</b> or <b>OpenRemoteInterface</b> instead of <b>Reopen</b>.</p>

<p>For more information about <b>Reopen</b> and how to use remote I/O targets in UMDF-based drivers, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>.</p>

<p>The following code example shows an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556899">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a> callback function that calls <b>Reopen</b>.</p>

<p>Typically, a driver calls <b>Reopen</b> from within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556899">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a> callback function, but <b>Reopen</b> can instead be called after <b>OnRemoteTargetRemoveCanceled</b> returns. </p>

<p>Reopen uses the file or interface name that the driver previously specified to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560273">IWDFRemoteTarget::OpenFileByName</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff560276">IWDFRemoteTarget::OpenRemoteInterface</a>. If you want to change the file or interface that the driver is using, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560253">IWDFRemoteTarget::Close</a>, and then it can call <b>OpenFileByName</b> or <b>OpenRemoteInterface</b> instead of <b>Reopen</b>.</p>

<p>For more information about <b>Reopen</b> and how to use remote I/O targets in UMDF-based drivers, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>.</p>

<p>The following code example shows an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556899">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a> callback function that calls <b>Reopen</b>.</p>

<p>Typically, a driver calls <b>Reopen</b> from within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556899">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a> callback function, but <b>Reopen</b> can instead be called after <b>OnRemoteTargetRemoveCanceled</b> returns. </p>

<p>Reopen uses the file or interface name that the driver previously specified to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560273">IWDFRemoteTarget::OpenFileByName</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff560276">IWDFRemoteTarget::OpenRemoteInterface</a>. If you want to change the file or interface that the driver is using, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560253">IWDFRemoteTarget::Close</a>, and then it can call <b>OpenFileByName</b> or <b>OpenRemoteInterface</b> instead of <b>Reopen</b>.</p>

<p>For more information about <b>Reopen</b> and how to use remote I/O targets in UMDF-based drivers, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>.</p>

<p>The following code example shows an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556899">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a> callback function that calls <b>Reopen</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560253">IWDFRemoteTarget::Close</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFRemoteTarget::Reopen method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
