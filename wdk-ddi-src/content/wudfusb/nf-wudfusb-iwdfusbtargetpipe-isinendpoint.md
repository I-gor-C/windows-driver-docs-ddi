---
UID: NF.wudfusb.IWDFUsbTargetPipe.IsInEndPoint
title: IWDFUsbTargetPipe::IsInEndPoint
author: windows-driver-content
description: The IsInEndPoint method determines whether a USB pipe (endpoint) is an IN pipe.
old-location: wdf\iwdfusbtargetpipe_isinendpoint.htm
old-project: wdf
ms.assetid: c1cba1fa-3952-4f2f-829f-2f5983349df8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFUsbTargetPipe, IsInEndPoint, IWDFUsbTargetPipe::IsInEndPoint
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbTargetPipe.IsInEndPoint
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
req.irql: 
req.iface: IWDFUsbTargetPipe
req.product: Windows 10 or later.
---

# IWDFUsbTargetPipe::IsInEndPoint method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IsInEndPoint</b> method determines whether a USB pipe (endpoint) is an IN pipe.</p>


## -syntax

````
BOOL  IsInEndPoint();
````


## -parameters


## -returns
<p><b>IsInEndPoint</b> returns a BOOL value that indicates whether the USB pipe is an IN pipe. <b>TRUE</b> indicates the pipe is an IN pipe. <b>FALSE</b> indicates the pipe is not an IN pipe.</p>

<p><b>IsInEndPoint</b> returns a BOOL value that indicates whether the USB pipe is an IN pipe. <b>TRUE</b> indicates the pipe is an IN pipe. <b>FALSE</b> indicates the pipe is not an IN pipe.</p>

<p><b>IsInEndPoint</b> returns a BOOL value that indicates whether the USB pipe is an IN pipe. <b>TRUE</b> indicates the pipe is an IN pipe. <b>FALSE</b> indicates the pipe is not an IN pipe.</p>

## -remarks
<p>If the USB pipe is an IN pipe, a UMDF driver can call the <a href="wdf.iwdfiotarget_formatrequestforread">IWDFIoTarget::FormatRequestForRead</a> method to format a read request. The framework can then send the request to the USB pipe.</p>

<p>For a code example of how to use the <b>IsInEndPoint</b> method, see <a href="wdf.iwdfusbinterface_getnumendpoints">IWDFUsbInterface::GetNumEndPoints</a>.</p>

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
<dt>Wudfusb.h (include Wudfusb.h)</dt>
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
<a href="..\wudfusb\nn-wudfusb-iwdfusbtargetpipe.md">IWDFUsbTargetPipe</a>
</dt>
<dt>
<a href="wdf.iwdfiotarget_formatrequestforread">IWDFIoTarget::FormatRequestForRead</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbTargetPipe::IsInEndPoint method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
