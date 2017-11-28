---
UID: NF.storduid.CompareStorageDuids
title: CompareStorageDuids
author: windows-driver-content
description: The CompareStorageDuids routine compares two device unique identifiers (DUIDs) and reports whether they match or not.
old-location: storage\comparestorageduids.htm
old-project: storage
ms.assetid: bf66a04d-0892-4813-9615-845054526125
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: CompareStorageDuids
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storduid.h
req.include-header: Storduid.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CompareStorageDuids
req.alt-loc: storduid.h
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

# CompareStorageDuids function



## -description
<p>The <b>CompareStorageDuids</b> routine compares two device unique identifiers (DUIDs) and reports whether they match or not.</p>


## -syntax

````
__inline DUID_MATCH_STATUS CompareStorageDuids(
  _In_ PSTORAGE_DEVICE_UNIQUE_IDENTIFIER Duid1,
  _In_ PSTORAGE_DEVICE_UNIQUE_IDENTIFIER Duid2
);
````


## -parameters
<dl>

### -param <i>Duid1</i> [in]

<dd>
<p>A pointer to a DUID to compare with the DUID that <i>Duid2</i> points to.</p>
</dd>

### -param <i>Duid2</i> [in]

<dd>
<p>A pointer to a DUID to compare with the DUID that <i>Duid1</i> points to.</p>
</dd>
</dl>

## -returns
<p><b>CompareStorageDuids</b> returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552760">DUID_MATCH_STATUS</a> value that indicates whether the two DUIDs matched or not, if the operation succeeds. Otherwise, this routine returns a DUID_MATCH_STATUS value that indicates the error status.</p>

## -remarks


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
<dt>Storduid.h (include Storduid.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552760">DUID_MATCH_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CompareStorageDuids routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
