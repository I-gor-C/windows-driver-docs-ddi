---
UID: NF.wiamindr_lh.IWiaDrvItem.GetItemFlags
title: IWiaDrvItem::GetItemFlags
author: windows-driver-content
description: The IWiaDrvItem::GetItemFlags method gets the item flags of the current IWiaDrvItem item.
old-location: image\iwiadrvitem_getitemflags.htm
old-project: image
ms.assetid: 47358d69-ef45-4cac-8187-72c354912c4e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaDrvItem, GetItemFlags, IWiaDrvItem::GetItemFlags
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
req.alt-api: IWiaDrvItem.GetItemFlags
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

# IWiaDrvItem::GetItemFlags method



## -description
<p>The <b>IWiaDrvItem::GetItemFlags</b> method gets the item flags of the current <b>IWiaDrvItem</b> item.</p>


## -syntax

````
HRESULT GetItemFlags(
  [out] LONG *plFlags
);
````


## -parameters
<dl>

### -param <i>plFlags</i> [out]

<dd>
<p>Points to a memory location that will receive the item flags.</p>
</dd>
</dl>

## -returns
<p>If the method succeeds, it places the item flag values in the location pointed to by <i>plFlags</i> and returns S_OK. If the pointer <i>plFlags</i> is invalid, the method returns E_INVALIDARG. If the method fails for another reason, it returns a standard COM error code.</p>

## -remarks
<p>The method places the current <b>IWiaDrvItem</b> item's flag values in the location pointed to by <i>pIFlags</i>. The item's flag values were set when the item was created by the driver services library function <a href="..\wiamdef\nf-wiamdef-wiascreatedrvitem.md">wiasCreateDrvItem</a>.</p>

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

## -see-also
<dl>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiascreatedrvitem.md">wiasCreateDrvItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaDrvItem::GetItemFlags method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
