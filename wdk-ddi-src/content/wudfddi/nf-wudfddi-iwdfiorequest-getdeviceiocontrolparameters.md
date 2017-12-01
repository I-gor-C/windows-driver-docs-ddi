---
UID: NF.wudfddi.IWDFIoRequest.GetDeviceIoControlParameters
title: IWDFIoRequest::GetDeviceIoControlParameters
author: windows-driver-content
description: The GetDeviceIoControlParameters method retrieves the request parameters for a device I/O control-type request.
old-location: wdf\iwdfiorequest_getdeviceiocontrolparameters.htm
old-project: wdf
ms.assetid: 96de6f7a-da1d-44a6-b1f7-44859312a662
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFIoRequest, GetDeviceIoControlParameters, IWDFIoRequest::GetDeviceIoControlParameters
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
req.alt-api: IWDFIoRequest.GetDeviceIoControlParameters
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

# IWDFIoRequest::GetDeviceIoControlParameters method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetDeviceIoControlParameters</b> method retrieves the request parameters for a device I/O control-type request.</p>


## -syntax

````
void  GetDeviceIoControlParameters(
  [out] ULONG  *pControlCode,
  [out] SIZE_T *pInBufferSize,
  [out] SIZE_T *pOutBufferSize
);
````


## -parameters
<dl>

### -param <i>pControlCode</i> [out]

<dd>
<p>A pointer to a variable that receives the control code that identifies the specific operation to be performed.</p>
<p>This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require the information. </p>
</dd>

### -param <i>pInBufferSize</i> [out]

<dd>
<p>A pointer to a variable that receives the size, in bytes, of the input data buffer for the request. To retrieve the input data buffer, the driver calls the <a href="wdf.iwdfiorequest_getinputmemory">IWDFIoRequest::GetInputMemory</a> method.</p>
<p>This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require the information. </p>
</dd>

### -param <i>pOutBufferSize</i> [out]

<dd>
<p>A pointer to a variable that receives the size, in bytes, of the output data buffer for the request. To retrieve the output data buffer, the driver calls the <a href="wdf.iwdfiorequest_getoutputmemory">IWDFIoRequest::GetOutputMemory</a> method.</p>
<p>This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require the information. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The call to <b>GetDeviceIoControlParameters</b> fails if the request type is not a device I/O control type.</p>

<p>Although the driver can optionally specify <b>NULL</b> for each of the <i>pControlCode</i>, <i>pInBufferSize</i>, and <i>pOutBufferSize</i> parameters, the driver must specify at least one non-<b>NULL</b> parameter for <b>GetDeviceIoControlParameters</b> to execute successfully.</p>

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
<a href="..\wudfddi\nn-wudfddi-iwdfiorequest.md">IWDFIoRequest</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_getinputmemory">IWDFIoRequest::GetInputMemory</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_getoutputmemory">IWDFIoRequest::GetOutputMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest::GetDeviceIoControlParameters method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
