---
UID: NF.wiamindr_lh.IWiaDrvItem.DumpItemData
title: IWiaDrvItem::DumpItemData
author: windows-driver-content
description: The IWiaDrvItem::DumpItemData method dumps private data associated with an IWiaDrvItem item into an allocated private buffer.
old-location: image\iwiadrvitem_dumpitemdata.htm
old-project: image
ms.assetid: e17da654-60a7-4942-99f9-f55df87a1ca3
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaDrvItem, DumpItemData, IWiaDrvItem::DumpItemData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaDrvItem.DumpItemData
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
req.iface: IWiaDrvItem
req.product: Windows 10 or later.
---

# IWiaDrvItem::DumpItemData method



## -description
<p>The <b>IWiaDrvItem::DumpItemData</b> method dumps private data associated with an <b>IWiaDrvItem</b> item into an allocated private buffer.</p>


## -syntax

````
HRESULT DumpItemData(
  [out, optional] BSTR *bstrDrvItemData
);
````


## -parameters
<dl>

### -param <i>bstrDrvItemData</i> [out, optional]

<dd>
<p>Points to an allocated buffer that will receive the <b>IWiaDrvItem</b> data. </p>
</dd>
</dl>

## -returns
<p>If the method succeeds, it returns S_OK. If the method fails the buffer allocation, it returns E_OUTOFMEMORY. If the method fails for another reason, it returns a standard COM error code.</p>

## -remarks
<p>This method is provided for Microsoft internal debugging only. It will return E_NOTIMPL on the release operating system. </p>

<p>This method is provided for Microsoft internal debugging only. It will return E_NOTIMPL on the release operating system. </p>

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
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
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