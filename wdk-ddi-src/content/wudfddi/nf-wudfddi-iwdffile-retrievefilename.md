---
UID: NF.wudfddi.IWDFFile.RetrieveFileName
title: IWDFFile::RetrieveFileName
author: windows-driver-content
description: The RetrieveFileName method retrieves the full name of the file that is associated with the underlying kernel-mode device.
old-location: wdf\iwdffile_retrievefilename.htm
old-project: wdf
ms.assetid: 7858f3ba-e02a-4115-bf30-12e3a6a75965
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFFile, RetrieveFileName, IWDFFile::RetrieveFileName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFFile.RetrieveFileName
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
req.iface: IWDFFile
req.product: Windows 10 or later.
---

# IWDFFile::RetrieveFileName method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>RetrieveFileName</b> method retrieves the full name of the file that is associated with the underlying kernel-mode device.</p>


## -syntax

````
HRESULT RetrieveFileName(
  [out]     PWSTR pFileName,
  [in, out] DWORD *pdwFileNameLengthInChars
);
````


## -parameters
<dl>

### -param <i>pFileName</i> [out]

<dd>
<p>A pointer to a caller-supplied buffer that receives a <b>NULL</b>-terminated string that represents the full name of the file that is associated with the underlying kernel-mode device, if the supplied pointer is non-<b>NULL</b> and <b>RetrieveFileName</b> is successful. </p>
</dd>

### -param <i>pdwFileNameLengthInChars</i> [in, out]

<dd>
<p>A pointer to a caller-supplied variable that receives the size, in characters, of the full file name that <i>pFileName</i> points to. If the buffer at <i>pFileName</i> is non-<b>NULL</b>, the framework returns the size, in characters, of the file name string.</p>
<p>On input, the driver sets this variable to the size, in characters, of the buffer that <i>pFileName</i> points to. If the driver supplies <b>NULL</b> for <i>pFileName</i> and zero for the variable that <i>pdwFileNameLengthInChars</i> points to, the framework sets the variable to the size, in characters, that the file name string requires.</p>
</dd>
</dl>

## -returns
<p><b>RetrieveFileName</b> returns S_OK for the following scenarios:</p>

<p>
<ul>
<li>
<p>The buffer that the <i>pFileName</i> parameter points to was non-<b>NULL</b> and large enough to hold the name string, including the <b>NULL</b> character, and the framework successfully copied the string into the supplied buffer and set the variable that is pointed to by the <i>pdwFileNameLengthInChars</i> parameter to the number of characters in the string.</p>
</li>
<li>
<p>The buffer at <i>pFileName</i> was <b>NULL</b>, the driver preset the variable at <i>pdwFileNameLengthInChars</i> to 0, and the framework set the variable at <i>pdwFileNameLengthInChars</i> to the number of characters that are required for the string. 
</p>
</li>
</ul><b>RetrieveFileName</b> returns HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER) to indicate that the supplied buffer is non-<b>NULL</b> and did not contain enough space to hold the file name. The framework sets the variable at <i>pdwFileNameLengthInChars</i> to the number of characters that are required for the string.

</p>

<p>The buffer that the <i>pFileName</i> parameter points to was non-<b>NULL</b> and large enough to hold the name string, including the <b>NULL</b> character, and the framework successfully copied the string into the supplied buffer and set the variable that is pointed to by the <i>pdwFileNameLengthInChars</i> parameter to the number of characters in the string.</p>

<p>The buffer at <i>pFileName</i> was <b>NULL</b>, the driver preset the variable at <i>pdwFileNameLengthInChars</i> to 0, and the framework set the variable at <i>pdwFileNameLengthInChars</i> to the number of characters that are required for the string. 
</p>

<p><b>RetrieveFileName</b> might also return other HRESULT values.</p>

## -remarks
<p>Your driver might call <b>RetrieveFileName</b> from its <a href="wdf.iqueuecallbackcreate_oncreatefile">IQueueCallbackCreate::OnCreateFile</a> callback function.  For more information, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF Drivers</a>.</p>

<p>The following code example shows how to retrieve the name of a file.</p>

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
<p>1.5</p>
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
<a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFFile::RetrieveFileName method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
