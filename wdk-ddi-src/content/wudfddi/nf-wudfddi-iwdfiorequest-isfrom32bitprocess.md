---
UID: NF.wudfddi.IWDFIoRequest.IsFrom32BitProcess
title: IWDFIoRequest::IsFrom32BitProcess
author: windows-driver-content
description: The IsFrom32BitProcess method determines whether a request originated from a 32-bit process.
old-location: wdf\iwdfiorequest_isfrom32bitprocess.htm
old-project: wdf
ms.assetid: 80e43bd7-9ab9-46b0-a7f3-08c3577be4bc
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFIoRequest, IsFrom32BitProcess, IWDFIoRequest::IsFrom32BitProcess
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
req.alt-api: IWDFIoRequest.IsFrom32BitProcess
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
req.iface: IWDFIoRequest
req.product: Windows 10 or later.
---

# IWDFIoRequest::IsFrom32BitProcess method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IsFrom32BitProcess</b> method determines whether a request originated from a 32-bit process.</p>


## -syntax

````
BOOL  IsFrom32BitProcess();
````


## -parameters


## -returns
<p><b>IsFrom32BitProcess</b> returns a BOOL value that indicates whether the request originated from a 32-bit process. <b>TRUE</b> indicates the request originated from a 32-bit process. <b>FALSE</b> indicates the request did not originate from a 32-bit process.</p>

<p><b>IsFrom32BitProcess</b> returns a BOOL value that indicates whether the request originated from a 32-bit process. <b>TRUE</b> indicates the request originated from a 32-bit process. <b>FALSE</b> indicates the request did not originate from a 32-bit process.</p>

<p><b>IsFrom32BitProcess</b> returns a BOOL value that indicates whether the request originated from a 32-bit process. <b>TRUE</b> indicates the request originated from a 32-bit process. <b>FALSE</b> indicates the request did not originate from a 32-bit process.</p>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest::IsFrom32BitProcess method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
