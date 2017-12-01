---
UID: NE.wiautil.SKIP_AMOUNT
title: SKIP_AMOUNT
author: windows-driver-content
description: The SKIP_AMOUNT enumeration is used to indicate whether the file and informational headers of an image should be skipped over.
old-location: image\skip_amount.htm
old-project: image
ms.assetid: 4e21b3e9-0383-4464-b87e-beea88123124
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: TWAIN_CAPABILITY, TWAIN_CAPABILITY, *PTWAIN_CAPABILITY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wiautil.h
req.include-header: Wiautil.h, Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SKIP_AMOUNT
req.alt-loc: wiautil.h
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

# SKIP_AMOUNT enumeration



## -description
<p>The SKIP_AMOUNT enumeration is used to indicate whether the file and informational headers of an image should be skipped over.</p>


## -syntax

````
typedef enum  { 
  SKIP_OFF      = 0,
  SKIP_FILEHDR  = 1,
  SKIP_BOTHHDR  = 2
} SKIP_AMOUNT;
````


## -enum-fields
<dl>

### -field <a id="SKIP_OFF"></a><a id="skip_off"></a><b>SKIP_OFF</b>

<dd>
<p>Do not skip over either header.</p>
</dd>

### -field <a id="SKIP_FILEHDR"></a><a id="skip_filehdr"></a><b>SKIP_FILEHDR</b>

<dd>
<p>Skip over the file header.</p>
</dd>

### -field <a id="SKIP_BOTHHDR"></a><a id="skip_bothhdr"></a><b>SKIP_BOTHHDR</b>

<dd>
<p>Skip over both the file and info headers.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h or Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.cwiauformatconverter_converttobmp">CWiauFormatConverter::ConvertToBmp</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20SKIP_AMOUNT enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
