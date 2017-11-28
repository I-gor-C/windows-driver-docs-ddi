---
UID: NF.wudfddi.IWDFIoRequest.GetWriteParameters
title: IWDFIoRequest::GetWriteParameters
author: windows-driver-content
description: The GetWriteParameters method retrieves the request parameters for a write-type request.
old-location: wdf\iwdfiorequest_getwriteparameters.htm
old-project: wdf
ms.assetid: 0627b278-2fd5-4185-8ec9-8b306c6d85a8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFIoRequest, GetWriteParameters, IWDFIoRequest::GetWriteParameters
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
req.alt-api: IWDFIoRequest.GetWriteParameters
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

# IWDFIoRequest::GetWriteParameters method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetWriteParameters</b> method retrieves the request parameters for a write-type request.</p>


## -syntax

````
void  GetWriteParameters(
  [out] SIZE_T   *pSizeInBytes,
  [out] LONGLONG *pllOffset,
  [out] ULONG    *pulKey
);
````


## -parameters
<dl>

### -param <i>pSizeInBytes</i> [out]

<dd>
<p>A pointer to a variable that receives the size, in bytes, to write. To retrieve the data for writing, the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559100">IWDFIoRequest::GetInputMemory</a> method.</p>
<p>This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require the information. </p>
</dd>

### -param <i>pllOffset</i> [out]

<dd>
<p>A pointer to a variable that receives the offset, in bytes, to begin writing to the device or the file on the device. If the device does not support absolute write addresses, <i>pllOffset</i> can be ignored. For more information, see the following Remarks section.</p>
<p>Client applications specify this value in the <b>Offset</b> and <b>OffsetHigh</b> members of the OVERLAPPED structure. A pointer to OVERLAPPED is passed in the Microsoft Win32 <b>WriteFile</b> or <b>WriteFileEx</b> function. </p>
<p>This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require the information. </p>
</dd>

### -param <i>pulKey</i> [out]

<dd>
<p>A pointer to a variable that receives a key that the driver can use to sort the I/O request in a way that the driver determines. </p>
<p>This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require the information. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A call to <b>GetWriteParameters</b> fails if the request type is not a write type.</p>

<p>For devices that support addressing (for example, a disk device), the value that the <i>pllOffset</i> parameter points to is typically the byte offset into the device. For devices that do not support addressing (for example, a serial port), the driver can ignore the value at <i>pllOffset</i>. </p>

<p>A call to <b>GetWriteParameters</b> fails if the request type is not a write type.</p>

<p>For devices that support addressing (for example, a disk device), the value that the <i>pllOffset</i> parameter points to is typically the byte offset into the device. For devices that do not support addressing (for example, a serial port), the driver can ignore the value at <i>pllOffset</i>. </p>

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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559100">IWDFIoRequest::GetInputMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest::GetWriteParameters method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
