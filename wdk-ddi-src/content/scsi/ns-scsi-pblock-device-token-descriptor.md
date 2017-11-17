---
UID: NS.scsi.PBLOCK_DEVICE_TOKEN_DESCRIPTOR
title: PBLOCK_DEVICE_TOKEN_DESCRIPTOR
author: windows-driver-content
description: BLOCK_DEVICE_TOKEN_DESCRIPTOR contains the token returned from a the POPULATE TOKEN command for an offload read data operation.
old-location: storage\block_device_token_descriptor.htm
ms.assetid: AD4E4EF6-F033-4226-9DC6-A6E55E965B4C
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: scsi.h
req.include-header: Scsi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BLOCK_DEVICE_TOKEN_DESCRIPTOR
req.alt-loc: scsi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: PBLOCK_DEVICE_TOKEN_DESCRIPTOR, BLOCK_DEVICE_TOKEN_DESCRIPTOR, *PBLOCK_DEVICE_TOKEN_DESCRIPTOR
req.iface: 
req.product: Windows 10 or later.
---

# PBLOCK_DEVICE_TOKEN_DESCRIPTOR structure



## -description
<p><b>BLOCK_DEVICE_TOKEN_DESCRIPTOR</b> contains the token returned from a the POPULATE TOKEN command for an offload read data operation. The token information is included as part of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh967732">RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER</a> structure.</p>


## -syntax

````
typedef struct _BLOCK_DEVICE_TOKEN_DESCRIPTOR {
  UCHAR TokenIdentifier[2];
  UCHAR Token[BLOCK_DEVICE_TOKEN_SIZE];
} BLOCK_DEVICE_TOKEN_DESCRIPTOR, *PBLOCK_DEVICE_TOKEN_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>TokenIdentifier</b>

<dd>
<p>An identifier value assigned by the copy provider to provide uniqueness to <b>Token</b> while the value of <b>Token</b> is valid. This member is reserved for system use and must not be modified.</p>
</dd>

### -field <b>Token</b>

<dd>
<p>A data value defining a token as a point-in-time representation of data (ROD) for an offload read data operation. <b>Token</b> is an opaque value and must be used unmodified in offload write data operations.</p>
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
<dt>Scsi.h (include Scsi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh967732">RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20BLOCK_DEVICE_TOKEN_DESCRIPTOR structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
