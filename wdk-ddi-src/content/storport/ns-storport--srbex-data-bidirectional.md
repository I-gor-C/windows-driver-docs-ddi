---
UID: NS.storport._SRBEX_DATA_BIDIRECTIONAL
title: SRBEX_DATA_BIDIRECTIONAL
author: windows-driver-content
description: The SRBEX_DATA_BIDIRECTIONAL structure contains the extended SRB data for bi-directional transfer commands.
old-location: storage\srbex_data_bidirectional.htm
old-project: storage
ms.assetid: B61247DC-8AC3-4A96-985B-A4CAC232555E
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SRBEX_DATA_BIDIRECTIONAL, SRBEX_DATA_BIDIRECTIONAL, *PSRBEX_DATA_BIDIRECTIONAL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Storport.h, Srb.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRBEX_DATA_BIDIRECTIONAL
req.alt-loc: Storport.h
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

# SRBEX_DATA_BIDIRECTIONAL structure



## -description
<p>The <b>SRBEX_DATA_BIDIRECTIONAL</b> structure contains the extended SRB data for bi-directional transfer commands.</p>


## -syntax

````
typedef struct _SRBEX_DATA_BIDIRECTIONAL {
  SRBEXDATATYPE       Type;
  ULONG               Length;
  ULONG               DataInTransferLength;
  ULONG               Reserved1;
  PVOID POINTER_ALIGN DataInBuffer;
} SRBEX_DATA_BIDIRECTIONAL, *PSRBEX_DATA_BIDIRECTIONAL;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>Data type indicator for the bidirectional extended SRB data structure. Set to <b>SrbExDataTypeBidirectional</b>.</p>
</dd>

### -field Length

<dd>
<p>Length of the data in this structure, in bytes, starting with the <b>DataInTransferLength</b> member. Set to SRBEX_DATA_BIDIRECTIONAL_LENGTH.</p>
</dd>

### -field DataInTransferLength

<dd>
<p>Length of the data present  in the <b>DataInBuffer</b> member.</p>
</dd>

### -field Reserved1

<dd>
<p>This member is reserved. Set to 0.</p>
</dd>

### -field DataInBuffer

<dd>
<p>A pointer to the buffer that contains the data sent from the device.</p>
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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h or Srb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\storport\ns-storport--storage-request-block.md">STORAGE_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SRBEX_DATA_BIDIRECTIONAL structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
