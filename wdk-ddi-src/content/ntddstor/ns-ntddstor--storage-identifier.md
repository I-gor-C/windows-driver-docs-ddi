---
UID: NS.ntddstor._STORAGE_IDENTIFIER
title: STORAGE_IDENTIFIER
author: windows-driver-content
description: The STORAGE_IDENTIFIER structure represents a SCSI identification descriptor.
old-location: storage\storage_identifier.htm
ms.assetid: f2b0610a-dffa-48fb-bc5a-355fa9f05770
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_IDENTIFIER
req.alt-loc: ntddstor.h
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
ms.keywords: STORAGE_IDENTIFIER, STORAGE_IDENTIFIER, *PSTORAGE_IDENTIFIER
req.iface: 
---

# STORAGE_IDENTIFIER structure



## -description
<p>The STORAGE_IDENTIFIER structure represents a SCSI identification descriptor.</p>


## -syntax

````
typedef struct _STORAGE_IDENTIFIER {
  STORAGE_IDENTIFIER_CODE_SET CodeSet;
  STORAGE_IDENTIFIER_TYPE     Type;
  USHORT                      IdentifierSize;
  USHORT                      NextOffset;
  STORAGE_ASSOCIATION_TYPE    Association;
  UCHAR                       Identifier[1];
} STORAGE_IDENTIFIER, *PSTORAGE_IDENTIFIER;
````


## -struct-fields
<dl>

### -field <b>CodeSet</b>

<dd>
<p>Specifies the code set used by a SCSI identification descriptor to identify a logical unit.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>Contains an enumerator value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff566990">STORAGE_IDENTIFIER_TYPE</a> that indicates the identifier type.</p>
</dd>

### -field <b>IdentifierSize</b>

<dd>
<p>Specifies the size in bytes of the identifier.</p>
</dd>

### -field <b>NextOffset</b>

<dd>
<p>Specifies the offset in bytes from the current descriptor to the next descriptor.</p>
</dd>

### -field <b>Association</b>

<dd>
<p>Contains an enumerator value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff566349">STORAGE_ASSOCIATION_TYPE</a> that indicates whether the descriptor identifies a device or a port.</p>
</dd>

### -field <b>Identifier</b>

<dd>
<p>Contains the identifier associated with this descriptor.</p>
</dd>
</dl>

## -remarks
<p>Every device identification page (page code 0x83) of SCSI vital product data contains a series of identification descriptors. The STORAGE_IDENTIFIER structure represents a SCSI identification descriptor.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566349">STORAGE_ASSOCIATION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566990">STORAGE_IDENTIFIER_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20STORAGE_IDENTIFIER structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
