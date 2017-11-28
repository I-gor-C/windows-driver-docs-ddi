---
UID: NS.wiamindr_lh._WIAS_ENDORSER_VALUE
title: WIAS_ENDORSER_VALUE
author: windows-driver-content
description: The WIAS_ENDORSER_VALUE structure stores token/value pairs for endorser strings.
old-location: image\wias_endorser_value.htm
old-project: image
ms.assetid: 54395899-c35d-4251-9e9d-ec2128b28c67
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WIAS_ENDORSER_VALUE, WIAS_ENDORSER_VALUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WIAS_ENDORSER_VALUE
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
req.iface: IWiaMiniDrvTransferCallback
req.product: Windows 10 or later.
---

# WIAS_ENDORSER_VALUE structure



## -description
<p>The WIAS_ENDORSER_VALUE structure stores token/value pairs for endorser strings.</p>


## -syntax

````
typedef struct _WIAS_ENDORSER_VALUE {
  LPWSTR wszTokenName;
  LPWSTR wszValue;
} WIAS_ENDORSER_VALUE, *PWIAS_ENDORSER_VALUE;
````


## -struct-fields
<dl>

### -field <b>wszTokenName</b>

<dd>
<p>Specifies a string value that represents the token name. Endorser token names begin and end with the $ character (for example, L"$MY_TOKEN_NAME$").</p>
</dd>

### -field <b>wszValue</b>

<dd>
<p>Specifies the value with which to replace the token.</p>
</dd>
</dl>

## -remarks
<p>This structure is used indirectly by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549282">wiasParseEndorserString</a> function. One of the parameters of this function is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff549556">WIAS_ENDORSER_INFO</a> structure, which has a WIAS_ENDORSER_VALUE structure as one of its members.</p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549282">wiasParseEndorserString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549556">WIAS_ENDORSER_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20WIAS_ENDORSER_VALUE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
