---
UID: NF.wiamindr_lh.IWiaMiniDrvCallBack.MiniDrvCallback
title: IWiaMiniDrvCallBack::MiniDrvCallback
author: windows-driver-content
description: The IWiaMiniDrvCallBack::MiniDrvCallback method provides a callback method for WIA minidrivers to use during a callback data transfer.
old-location: image\iwiaminidrvcallback_minidrvcallback.htm
old-project: image
ms.assetid: 7d1c0d8a-65db-47fd-ad6a-a83c7ed3acd9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaMiniDrvCallBack, MiniDrvCallback, IWiaMiniDrvCallBack::MiniDrvCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaMiniDrvCallBack.MiniDrvCallback
req.alt-loc: wiamindr_lh.h
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
req.iface: IWiaMiniDrvCallBack
req.product: Windows 10 or later.
---

# IWiaMiniDrvCallBack::MiniDrvCallback method



## -description
<p>The <b>IWiaMiniDrvCallBack::MiniDrvCallback</b> method provides a callback method for WIA minidrivers to use during a callback data transfer.</p>


## -syntax

````
HRESULT MiniDrvCallback(
  [in] LONG                      lReason,
  [in] LONG                      lStatus,
  [in] LONG                      lPercentComplete,
  [in] LONG                      lOffset,
  [in] LONG                      lLength,
  [in] PMINIDRV_TRANSFER_CONTEXT pTranCtx,
  [in] LONG                      lReserved
);
````


## -parameters
<dl>

### -param <i>lReason</i> [in]

<dd>
<p>Specifies a constant value that designates a callback status message. This value is used to determine the purpose of the callback, and can be one of the following values:</p>
<table>
<tr>
<th>Message</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>IT_MSG_DATA</p>
</td>
<td>
<p>Indicates that the transfer buffer contains a block of data.</p>
</td>
</tr>
<tr>
<td>
<p>IT_MSG_DATA_HEADER</p>
</td>
<td>
<p>Received before any data transfers. Indicates that the transfer buffer points to a WIA_DATA_CALLBACK_HEADER structure (defined in the Microsoft Windows SDK documentation) that defines elements of the data transfer.</p>
</td>
</tr>
<tr>
<td>
<p>IT_MSG_DEVICE_STATUS</p>
</td>
<td>
<p>Callback contains only status information about the device.</p>
</td>
</tr>
<tr>
<td>
<p>IT_MSG_FILE_PREVIEW_DATA</p>
</td>
<td>
<p>Indicates preview data is being transferred to the application.</p>
</td>
</tr>
<tr>
<td>
<p>IT_MSG_FILE_PREVIEW_DATA_HEADER</p>
</td>
<td>
<p>Indicates a header is being transferred to the application, prior to the preview data being transferred.</p>
</td>
</tr>
<tr>
<td>
<p>IT_MSG_NEW_PAGE</p>
</td>
<td>
<p>Indicates that the data transfer of a page is complete, and a new page is being sent.</p>
</td>
</tr>
<tr>
<td>
<p>IT_MSG_STATUS</p>
</td>
<td>
<p>Callback contains only status information about the transfer.</p>
</td>
</tr>
<tr>
<td>
<p>IT_MSG_TERMINATION</p>
</td>
<td>
<p>Indicates that the data transfer is complete.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>lStatus</i> [in]

<dd>
<p>Specifies the status of the transfer. This parameter is a bitwise OR of the following values:</p>
<table>
<tr>
<th>Status</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>IT_STATUS_TRANSFER_FROM_DEVICE</p>
</td>
<td>
<p>Transferring data from device.</p>
</td>
</tr>
<tr>
<td>
<p>IT_STATUS_PROCESSING_DATA</p>
</td>
<td>
<p>Device and/or minidriver are processing the data.</p>
</td>
</tr>
<tr>
<td>
<p>IT_STATUS_TRANSFER_TO_CLIENT</p>
</td>
<td>
<p>Transferring data from the minidriver to the WIA service.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>lPercentComplete</i> [in]

<dd>
<p>Specifies the current percentage of data transferred.</p>
</dd>

### -param <i>lOffset</i> [in]

<dd>
<p>Specifies the current offset (in bytes) into the transfer buffer from the beginning of the buffer.</p>
</dd>

### -param <i>lLength</i> [in]

<dd>
<p>Specifies the number of bytes contained in the transfer.</p>
</dd>

### -param <i>pTranCtx</i> [in]

<dd>
<p>Points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545250">MINIDRV_TRANSFER_CONTEXT</a> structure containing the data transfer values.</p>
</dd>

### -param <i>lReserved</i> [in]

<dd>
<p>Reserved. Set to zero.</p>
</dd>
</dl>

## -returns
<p>If the method succeeds, it returns S_OK. If the callback is canceled by the client application, the method returns S_FALSE. If the method fails, it returns a standard COM error code.</p>

## -remarks
<p>The percent complete values are sent directly from the driver. The WIA service does not adjust the values.</p>

<p>IT_MSG_FILE_PREVIEW_DATA_HEADER  is for out-of-band-data. This allows the application doing a file transfer to display the banded data. This is useful for scroll-fed scanners that have an unknown length and no preview scan. The information reported in this message should be treated the same as IT_MSG_DATA_HEADER. If a driver supports this message, it can supply preview data during its file transfer. </p>

<p>The percent complete values are sent directly from the driver. The WIA service does not adjust the values.</p>

<p>IT_MSG_FILE_PREVIEW_DATA_HEADER  is for out-of-band-data. This allows the application doing a file transfer to display the banded data. This is useful for scroll-fed scanners that have an unknown length and no preview scan. The information reported in this message should be treated the same as IT_MSG_DATA_HEADER. If a driver supports this message, it can supply preview data during its file transfer. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545250">MINIDRV_TRANSFER_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaMiniDrvCallBack::MiniDrvCallback method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
