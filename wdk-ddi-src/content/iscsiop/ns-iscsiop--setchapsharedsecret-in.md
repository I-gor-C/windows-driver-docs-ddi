---
UID: NS.iscsiop._SetCHAPSharedSecret_IN
title: SetCHAPSharedSecret_IN
author: windows-driver-content
description: The SetCHAPSharedSecret_IN structure holds the input data for the SetCHAPSharedSecret method.
old-location: storage\setchapsharedsecret_in.htm
old-project: storage
ms.assetid: d352785b-982f-4469-bee8-6274c0ce1cd6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SetCHAPSharedSecret_IN, SetCHAPSharedSecret_IN, *PSetCHAPSharedSecret_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetCHAPSharedSecret_IN
req.alt-loc: iscsiop.h
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
---

# SetCHAPSharedSecret_IN structure



## -description
<p>The SetCHAPSharedSecret_IN structure holds the input data for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565585">SetCHAPSharedSecret</a> method.</p>


## -syntax

````
typedef struct _SetCHAPSharedSecret_IN {
  ULONG SharedSecretSize;
  UCHAR SharedSecret[1];
} SetCHAPSharedSecret_IN, *PSetCHAPSharedSecret_IN;
````


## -struct-fields
<dl>

### -field <b>SharedSecretSize</b>

<dd>
<p>The size, in bytes, of the shared secret.</p>
</dd>

### -field <b>SharedSecret</b>

<dd>
<p>A variable-length array that contains the shared secret.</p>
</dd>
</dl>

## -remarks
<p>You must implement this method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsiop.h (include Iscsiop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565585">SetCHAPSharedSecret</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565600">SetCHAPSharedSecret_OUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SetCHAPSharedSecret_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
