---
UID: NF.wia_lh.IWiaTransferCallback.TransferCallback
title: IWiaTransferCallback::TransferCallback
author: windows-driver-content
description: The IWiaTransferCallback::TransferCallback method is implemented by an image processing filter. It is called by the WIA service as a result of an application calling IWiaTransfer::Download or the preview component's IWiaPreview::GetNewPreview.
old-location: image\iwiatransfercallback_transfercallback.htm
old-project: image
ms.assetid: dc6c2057-9617-4c69-ac79-2a8f910a1ee2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaTransferCallback, TransferCallback, IWiaTransferCallback::TransferCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wia_lh.h
req.include-header: Wia.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaTransferCallback.TransferCallback
req.alt-loc: wia_lh.h
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
req.iface: IWiaTransferCallback
req.product: Windows 10 or later.
---

# IWiaTransferCallback::TransferCallback method



## -description
<p>The <b>IWiaTransferCallback::TransferCallback</b> method is implemented by an image processing filter. It is called by the WIA service as a result of an application calling <b>IWiaTransfer::Download</b> or the preview component's <b>IWiaPreview::GetNewPreview</b>.</p>


## -syntax

````
HRESULT TransferCallback(
  [in] LONG              lFlags,
  [in] WiaTransferParams *WiaTransferParams
);
````


## -parameters
<dl>

### -param <i>lFlags</i> [in]

<dd>
<p>Currently unused. Should be set to zero.</p>
</dd>

### -param <i>WiaTransferParams</i> [in]

<dd>
<p>Specifies a pointer to a WiaTransferParams structure. This structure is defined in the Microsoft Windows SDK documentation.</p>
</dd>
</dl>

## -returns
<p>Returns S_OK if successful, or a standard COM error value otherwise. </p>

## -remarks
<p>An image processing filter's implementation of <b>IWiaTransferCallback::TransferCallback</b> method is called during image acquisition, when the WIA mini-driver asks for the destination stream from the client and when the mini-driver sends progress messages back to the application. </p>

<p>An image processing filter's <b>IWiaTransferCallback::TransferCallback</b> method must delegate to the application callback's <b>IWiaTransferCallback::TransferCallback</b> method. In many cases the image processing filter's <b>IWiaTransferCallback::TransferCallback</b> implementation will also have to modify the <i>ulBytesWrittenToCurrentStream</i> and possibly also the <i>lPercentComplete</i> values in the WiaTransferParams structure. <i>ulBytesWrittenToCurrentStream</i> must be modified if the image processing filter has to buffer image data between calls to its Write method before it writes the data to the application provided stream. This would, for example, be needed if deskewing and/or rotation if is being performed. If no rotation or deskewing is needed the filter should preferably work on bands of data. <i>lPercentComplete</i> does not necessarily need to be modified, however, since this parameter indicates the percentage of total transfer time. This member can for example be used by a progress bar in an application. Note that the image processing filter should not modify the lMessage member of the structure. <b>IWiaTransferCallback::TransferCallback</b> also should not "swallow" any messages it receives even if it performs buffering, rather it should modify the <i>ulBytesWrittenToCurrentStream</i> member.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wia_lh.h (include Wia.h)</dt>
</dl>
</td>
</tr>
</table>