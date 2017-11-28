---
UID: NF.wiamindr_lh.IWiaMiniDrvTransferCallback.GetNextStream
title: IWiaMiniDrvTransferCallback::GetNextStream
author: windows-driver-content
description: Called by the WIA mini-driver to obtain a stream for the current data transfer (download or upload).
old-location: image\iwiaminidrvtransfercallback_getnextstream.htm
old-project: image
ms.assetid: FF33471A-692B-4568-BF37-1870DEC367D0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaMiniDrvTransferCallback, GetNextStream, IWiaMiniDrvTransferCallback::GetNextStream
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamindr_lh.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaMiniDrvTransferCallback.GetNextStream
req.alt-loc: Wiamindr_lh.h
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
req.iface: IWiaMiniDrvTransferCallback
req.product: Windows 10 or later.
---

# IWiaMiniDrvTransferCallback::GetNextStream method



## -description
<p>Called by the WIA mini-driver to obtain a stream for the current data transfer (download or upload).</p>


## -syntax

````
HRESULT GetNextStream(
  [in]  LONG    lFlags,
  [in]  BSTR    bstrItemName,
  [in]  BSTR    bstrFullItemName,
  [out] IStream **ppIStream
);
````


## -parameters
<dl>

### -param <i>lFlags</i> [in]

<dd>
<p>Represents flag bits. This parameter is unused and should always be set to zero (0) by the caller.</p>
</dd>

### -param <i>bstrItemName</i> [in]

<dd>
<p>The name of the item that will perform the data transfer. For more information, see  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551590">WIA_IPA_ITEM_NAME</a>.</p>
</dd>

### -param <i>bstrFullItemName</i> [in]

<dd>
<p>The full name of the item that will perform the data transfer. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551561">WIA_IPA_FULL_ITEM_NAME</a>.</p>
</dd>

### -param <i>ppIStream</i> [out]

<dd>
<p>A pointer to an <b>IStream</b> object.</p>
</dd>
</dl>

## -returns
<p>This method returns S_OK when the call is successful. Otherwise it returns an appropriate HRESULT error code.</p>

## -remarks
<p>When the client requests to skip the data transfer, the <b>GetNextStream</b> method returns WIA_STATUS_SKIP_ITEM. The WIA mini-driver must skip the current image transfer and continue with the next image transfer, if any. For example, for a download transfer, finish scanning the current image and then discard the image data.</p>

<p>When the current transfer sequence is cancelled, the <b>GetNextStream</b> method returns S_FALSE.</p>

<p>When the client requests to skip the data transfer, the <b>GetNextStream</b> method returns WIA_STATUS_SKIP_ITEM. The WIA mini-driver must skip the current image transfer and continue with the next image transfer, if any. For example, for a download transfer, finish scanning the current image and then discard the image data.</p>

<p>When the current transfer sequence is cancelled, the <b>GetNextStream</b> method returns S_FALSE.</p>

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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">Cancellation of Data Transfers in Windows Vista</a>
</dt>
<dt>
<a href="NULL">Data Transfer Between Legacy Application and Windows Vista Driver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj151550">IWiaMiniDrvTransferCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551561">WIA_IPA_FULL_ITEM_NAME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551590">WIA_IPA_ITEM_NAME</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaMiniDrvTransferCallback::GetNextStream method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
