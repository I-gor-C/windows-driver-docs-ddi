---
UID: NS.ks.PKSCLOCK_CREATE
title: PKSCLOCK_CREATE
author: windows-driver-content
description: The KSCLOCK_CREATE structure is used in clock create parameters for the KsCreateClock function.
old-location: stream\ksclock_create.htm
old-project: stream
ms.assetid: 72986a01-de40-4b8f-9dfc-d26f4999e66b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSCLOCK_CREATE, KSCLOCK_CREATE, *PKSCLOCK_CREATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCLOCK_CREATE
req.alt-loc: ks.h
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

# PKSCLOCK_CREATE structure



## -description
<p>The KSCLOCK_CREATE structure is used in clock create parameters for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561637">KsCreateClock</a> function.</p>


## -syntax

````
typedef struct {
  ULONG CreateFlags;
} KSCLOCK_CREATE, *PKSCLOCK_CREATE;
````


## -struct-fields
<dl>

### -field <b>CreateFlags</b>

<dd>
<p>Currently consists of a flags item, which must be set to zero.</p>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561637">KsCreateClock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSCLOCK_CREATE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
