---
UID: NF.wudfddi.IWDFIoRequest.FormatUsingCurrentType
title: IWDFIoRequest::FormatUsingCurrentType method
author: windows-driver-content
description: The FormatUsingCurrentType method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver.
old-location: wdf\iwdfiorequest_formatusingcurrenttype.htm
old-project: wdf
ms.assetid: 4cbf6d29-bccd-4629-b282-eb5314f9b4f4
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFIoRequest, IWDFIoRequest::FormatUsingCurrentType, FormatUsingCurrentType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFIoRequest.FormatUsingCurrentType
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
req.product: Windows 10 or later.
---

# IWDFIoRequest::FormatUsingCurrentType method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>FormatUsingCurrentType</b> method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver.



## -syntax

````
void  FormatUsingCurrentType();
````


## -parameters


## -returns
None

None

None


## -remarks
When a driver receives an I/O request, the driver might forward the request to the local I/O target, unmodified. To forward the unmodified request, the driver must:

Call <b>FormatUsingCurrentType</b> to format the request so that the framework can pass the request to the driver's local I/O target.

Call the <a href="wdf.iwdfiorequest_send">IWDFIoRequest::Send</a> method to send the request to the I/O target.

For a code example of how to use the <b>FormatUsingCurrentType</b> method, see <a href="wdf.iwdfiorequest_send">IWDFIoRequest::Send</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
<a href="..\wudfddi\nn-wudfddi-iwdfiorequest.md">IWDFIoRequest</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_send">IWDFIoRequest::Send</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest::FormatUsingCurrentType method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

