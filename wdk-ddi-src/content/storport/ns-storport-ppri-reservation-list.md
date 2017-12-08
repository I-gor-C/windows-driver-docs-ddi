---
UID: NS.storport.PPRI_RESERVATION_LIST
title: PPRI_RESERVATION_LIST
author: windows-driver-content
description: The PRI_RESERVATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS.
old-location: storage\pri_reservation_list.htm
old-project: storage
ms.assetid: 5756e907-008a-49c3-b1cd-947cb0ce1bd4
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PPRI_RESERVATION_LIST, PRI_RESERVATION_LIST, *PPRI_RESERVATION_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PRI_RESERVATION_LIST
req.alt-loc: storport.h
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

# PPRI_RESERVATION_LIST structure



## -description
<p>The PRI_RESERVATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS.</p>


## -syntax

````
typedef struct {
  UCHAR                      Generation[4];
  UCHAR                      AdditionalLength[4];
  PRI_RESERVATION_DESCRIPTOR Reservations[];
} PRI_RESERVATION_LIST, *PPRI_RESERVATION_LIST;
````


## -struct-fields
<dl>

### -field Generation

<dd>
<p>The Generation field contains a 32-bit counter that is maintained by the device server, which is incremented every time a Persistent Reserve Out command requests a REGISTER, REGISTER AND IGNORE</p>
<p>EXISTING KEY, CLEAR, PREEMPT, or PREEMPT AND ABORT service action.</p>
</dd>

### -field AdditionalLength

<dd>
<p>The AdditionalLength field contains a count of the number of bytes in the reservation descriptors.</p>
</dd>

### -field Reservations

<dd>
<p>An array of reservation descriptors.</p>
</dd>
</dl>

## -remarks
<p>The <a href="..\ntddstor\ni-ntddstor-ioctl-storage-persistent-reserve-in.md">IOCTL_STORAGE_PERSISTENT_RESERVE_IN</a> request is used to obtain information about persistent reservations and reservation keys that are active within a device server.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddstor\ni-ntddstor-ioctl-storage-persistent-reserve-in.md">IOCTL_STORAGE_PERSISTENT_RESERVE_IN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20PRI_RESERVATION_LIST structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
