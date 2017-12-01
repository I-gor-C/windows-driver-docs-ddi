---
UID: NF.wudfddi.IWDFIoRequest2.GetCreateParametersEx
title: IWDFIoRequest2::GetCreateParametersEx
author: windows-driver-content
description: The GetCreateParametersEx method retrieves file creation parameters that are associated with a file that is being created or opened.
old-location: wdf\iwdfiorequest2_getcreateparametersex.htm
old-project: wdf
ms.assetid: bc34d86b-fa0e-419e-9342-61df12a8e484
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFIoRequest2, GetCreateParametersEx, IWDFIoRequest2::GetCreateParametersEx
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
req.alt-api: IWDFIoRequest2.GetCreateParametersEx
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
req.iface: IWDFIoRequest2
req.product: Windows 10 or later.
---

# IWDFIoRequest2::GetCreateParametersEx method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetCreateParametersEx</b> method retrieves file creation parameters that are associated with a file that is being created or opened.</p>


## -syntax

````
void GetCreateParametersEx(
  [out, optional] ULONG       *pOptions,
  [out, optional] USHORT      *pFileAttributes,
  [out, optional] USHORT      *pShareAccess,
  [out, optional] ACCESS_MASK *pDesiredAccess
);
````


## -parameters
<dl>

### -param <i>pOptions</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives bit flags that indicate file creation options. These FILE_XXXX-named bit flags are defined in Wdm.h. </p>
<p>The low 24 bits of the variable indicate options to apply when creating or opening the file. For more information about these bits, see the description of the <i>CreateOptions</i> parameter of the kernel-mode <a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a> function. </p>
<p>The high eight bits of the variable indicate actions to perform if the file does or does not already exist. For more information about these bits, see the description of the <i>CreateDisposition</i> parameter of <b>ZwCreateFile</b>. </p>
<p>This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param <i>pFileAttributes</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives bit flags that indicate file attributes. These FILE_ATTRIBUTE_XXXX-named bit flags are defined in Wdm.h. For more information about these bit flags, see the description of the <i>FileAttributes</i> parameter of <b>ZwCreateFile</b>.</p>
<p>This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param <i>pShareAccess</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives bit flags that indicate file sharing options. These FILE_SHARE_XXXX-named bit flags are defined in Wdm.h. For more information about these bit flags, see the description of the <i>ShareAccess</i> parameter of <a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a>.</p>
<p>This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param <i>pDesiredAccess</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> structure that specifies the requested access to the file. For more information about this parameter, see the <i>DesiredAccess</i> parameter of <b>ZwCreateFile</b>. </p>
<p>This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>After the framework calls a driver's <a href="wdf.iqueuecallbackcreate_oncreatefile">IQueueCallbackCreate::OnCreateFile</a> callback function, the driver can call the <a href="wdf.iwdfiorequest_getcreateparameters">IWDFIoRequest::GetCreateParameters</a> method or the <b>IWDFIoRequest2::GetCreateParametersEx</b> method to obtain the file's creation parameters. </p>

<p>For more information, see <a href="wdf.obtaining_parameters_for_i_o_requests">Obtaining Parameters for I/O Requests</a>.</p>

<p>The following code example shows how an <a href="wdf.iqueuecallbackcreate_oncreatefile">IQueueCallbackCreate::OnCreateFile</a> callback function can obtain the <a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a> interface and then call <b>GetCreateParametersEx</b>.</p>

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
<a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a>
</dt>
<dt>
<a href="wdf.iqueuecallbackcreate_oncreatefile">IQueueCallbackCreate::OnCreateFile</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_getcreateparameters">IWDFIoRequest::GetCreateParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest2::GetCreateParametersEx method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
