---
UID: NS.storport.PPRI_RESERVATION_DESCRIPTOR
title: PPRI_RESERVATION_DESCRIPTOR
author: windows-driver-content
description: The PRI_RESERVATION_DESCRIPTOR structure is used to construct the PRI_RESERVATION_LIST structure that is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS.
old-location: storage\pri_reservation_descriptor.htm
old-project: storage
ms.assetid: f03506f6-404e-4635-a9ad-f2f36164ff2f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PPRI_RESERVATION_DESCRIPTOR, PRI_RESERVATION_DESCRIPTOR, *PPRI_RESERVATION_DESCRIPTOR
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
req.alt-api: PRI_RESERVATION_DESCRIPTOR
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

# PPRI_RESERVATION_DESCRIPTOR structure



## -description
<p>The PRI_RESERVATION_DESCRIPTOR structure is used to construct the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563921">PRI_RESERVATION_LIST</a> structure that is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS.</p>


## -syntax

````
typedef struct {
  UCHAR ReservationKey[8];
  UCHAR ScopeSpecificAddress[4];
  UCHAR Reserved;
  UCHAR Type  :4;
  UCHAR Scope  :4;
  UCHAR Obsolete[2];
} PRI_RESERVATION_DESCRIPTOR, *PPRI_RESERVATION_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>ReservationKey</b>

<dd>
<p>The reservation key under which the persistent reservation is held.</p>
</dd>

### -field <b>ScopeSpecificAddress</b>

<dd>
<p>The ScopeSpecificAddress field contains the element address, that has zeros placed in the most significant bits to fit the field.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Must be zero.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>The type of the persistent reservation as present in the Persistent Reserve Out command that created the persistent reservation.</p>
</dd>

### -field <b>Scope</b>

<dd>
<p>The scope of the persistent reservation as present in the Persistent Reserve Out command that created the persistent reservation.</p>
</dd>

### -field <b>Obsolete</b>

<dd>
<p>Reserved. Must be zero.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560582">IOCTL_STORAGE_PERSISTENT_RESERVE_IN</a> request is used to obtain information about persistent reservations and reservation keys that are active within a device server.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560582">IOCTL_STORAGE_PERSISTENT_RESERVE_IN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563921">PRI_RESERVATION_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20PRI_RESERVATION_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
