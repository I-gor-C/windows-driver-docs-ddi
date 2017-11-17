---
UID: NS.ntddcdvd._AACS_BINDING_NONCE
title: AACS_BINDING_NONCE
author: windows-driver-content
description: The AACS_BINDING_NONCE structure contains the binding nonce.
old-location: storage\aacs_binding_nonce.htm
ms.assetid: 8bbefe34-9653-4868-894f-a77c1fc9939f
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AACS_BINDING_NONCE
req.alt-loc: ntddcdvd.h
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
ms.keywords: AACS_BINDING_NONCE, AACS_BINDING_NONCE, *PAACS_BINDING_NONCE
req.iface: 
---

# AACS_BINDING_NONCE structure



## -description
<p>The AACS_BINDING_NONCE structure contains the binding nonce.</p>


## -syntax

````
typedef struct _AACS_BINDING_NONCE {
  UCHAR BindingNonce[16];
  UCHAR MAC[16];
} AACS_BINDING_NONCE, *PAACS_BINDING_NONCE;
````


## -struct-fields
<dl>

### -field <b>BindingNonce</b>

<dd>
<p>The binding nonce for the requested logical block address(es) (LBAs).</p>
</dd>

### -field <b>MAC</b>

<dd>
<p>A message authentication code (MAC) that clients can use to verify that the binding nonce is for the current Advanced Access Content System (AACS) Authentication sequence.</p>
</dd>
</dl>

## -remarks
<p>Clients retrieve the binding nonce with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559262">IOCTL_AACS_READ_BINDING_NONCE</a> request or an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559248">IOCTL_AACS_GENERATE_BINDING_NONCE</a> request.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddcdvd.h (include Ntddcdvd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559248">IOCTL_AACS_GENERATE_BINDING_NONCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559262">IOCTL_AACS_READ_BINDING_NONCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20AACS_BINDING_NONCE structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
