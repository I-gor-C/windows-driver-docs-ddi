---
UID: NS.ntddcdvd._AACS_READ_BINDING_NONCE
title: AACS_READ_BINDING_NONCE
author: windows-driver-content
description: The AACS_READ_BINDING_NONCE structure is a wrapper for the Authentication Grant Identifier (AGID) and logical block address (LBA)/length pair that are required to read a nonce.
old-location: storage\aacs_read_binding_nonce.htm
ms.assetid: 5d017896-bb83-4ea3-9d28-b774213f86e9
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
req.alt-api: AACS_READ_BINDING_NONCE
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
ms.keywords: AACS_READ_BINDING_NONCE, AACS_READ_BINDING_NONCE, *PAACS_READ_BINDING_NONCE
req.iface: 
---

# AACS_READ_BINDING_NONCE structure



## -description
<p>The AACS_READ_BINDING_NONCE structure is a wrapper for the Authentication Grant Identifier (AGID) and logical block address (LBA)/length pair that are required to read a nonce.</p>


## -syntax

````
typedef struct _AACS_READ_BINDING_NONCE {
  DVD_SESSION_ID SessionId;
  ULONG          NumberOfSectors;
  ULONGLONG      StartLba;
  union {
    HANDLE    Handle;
    ULONGLONG ForceStructureLengthToMatch64bit;
  };
} AACS_READ_BINDING_NONCE, *PAACS_READ_BINDING_NONCE;
````


## -struct-fields
<dl>

### -field <b>SessionId</b>

<dd>
<p>A value of type DVD_SESSION_ID that specifies an AGID. The client obtains this value by a successful call to IOCTL_AACS_START_SESSION.</p>
</dd>

### -field <b>NumberOfSectors</b>

<dd>
<p>The number of sectors in the area for which the binding nonce is retrieved. To request the nonce for a file, the caller of IOCTL_AACS_READ_BINDING_NONCE must set this member to MAXULONGLONG.</p>
</dd>

### -field <b>StartLba</b>

<dd>
<p>The starting logical block address of the area for which the binding nonce is retrieved. To request the nonce for a file, the caller of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559248">IOCTL_AACS_GENERATE_BINDING_NONCE</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff559262">IOCTL_AACS_READ_BINDING_NONCE</a> must set this member to MAXULONGLONG.</p>
</dd>

### -field <b>Handle</b>

<dd>
<p>The file handle. Callers of IOCTL_AACS_READ_BINDING_NONCE that use file system support can set this member to a file handle. If the caller does not use file system support, this member must have a value of INVALID_HANDLE_VALUE.</p>
</dd>

### -field <b>ForceStructureLengthToMatch64bit</b>

<dd></dd>
</dl>

## -remarks
<p>Clients retrieve the binding nonce with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559248">IOCTL_AACS_GENERATE_BINDING_NONCE</a> request or an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559262">IOCTL_AACS_READ_BINDING_NONCE</a> request.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550106">AACS_BINDING_NONCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559248">IOCTL_AACS_GENERATE_BINDING_NONCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559262">IOCTL_AACS_READ_BINDING_NONCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20AACS_READ_BINDING_NONCE structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
