---
UID: NS.smclib._SMARTCARD_REQUEST
title: SMARTCARD_REQUEST
author: windows-driver-content
description: Describes the request buffer that contains data to send to the card.
old-location: smartcrd\smartcard_request.htm
old-project: smartcrd
ms.assetid: B5FF5B24-12E6-424A-B09A-4B0572621088
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SMARTCARD_REQUEST, SMARTCARD_REQUEST, *PSMARTCARD_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: smclib.h
req.include-header: Smclib.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SMARTCARD_REQUEST
req.alt-loc: Smclib.h
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
req.iface: 
req.product: Windows 10 or later.
---

# SMARTCARD_REQUEST structure



## -description
<p>Describes the request buffer that contains data to send to the card. </p>


## -syntax

````
typedef struct _SMARTCARD_REPLY {
  PUCHAR 	Buffer;
  ULONG  BufferSize;
  ULONG  BufferLength;
} SMARTCARD_REQUEST, *PSMARTCARD_REQUEST;
````


## -struct-fields
<dl>

### -field 	Buffer

<dd>
<p>Pointer to a buffer that  contains data to send.</p>
</dd>

### -field BufferSize

<dd>
<p>Size of the buffer pointed to by <i>Buffer</i>.</p>
</dd>

### -field BufferLength

<dd>
<p>Number of bytes required for this command.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Smclib.h (include Smclib.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn946593">SmcCxGetSmartcardRequestBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [smartcrd\smartcrd]:%20SMARTCARD_REQUEST structure%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
